from pathlib import Path
import os

import joblib
import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "house_price_model.pkl"

app = Flask(__name__)

# Load the trained model using an absolute path so hosting working directories
# do not affect the app.
model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None, error=None)


@app.route("/predict", methods=["POST"])
def predict():
    feature_names = [
        "GrLivArea", "YearBuilt", "GarageCars",
        "TotalBsmtSF", "OverallQual", "OverallCond"
    ]
    try:
        values = {name: float(request.form[name]) for name in feature_names}
        if any(value < 0 for value in values.values()):
            raise ValueError("Please enter values of zero or greater.")
        if not 1 <= values["OverallQual"] <= 10:
            raise ValueError("Overall Quality must be between 1 and 10.")
        if not 1 <= values["OverallCond"] <= 10:
            raise ValueError("Overall Condition must be between 1 and 10.")
        input_data = pd.DataFrame([values], columns=feature_names)
        prediction = float(model.predict(input_data)[0])
        return render_template(
            "index.html", prediction=max(0, prediction), error=None
        )
    except (KeyError, TypeError, ValueError) as exc:
        message = str(exc) or "Please complete all fields with valid numbers."
        return render_template(
            "index.html", prediction=None, error=message
        ), 400
    except Exception:
        app.logger.exception("Prediction failed")
        return render_template(
            "index.html",
            prediction=None,
            error="The prediction could not be completed. Please check your inputs and try again."
        ), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=False)
