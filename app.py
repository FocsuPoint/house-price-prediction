from flask import Flask, render_template, request
import joblib
import pandas as pd


# ==========================================
# Create Flask Application
# ==========================================

app = Flask(__name__)


# ==========================================
# Load Trained Machine Learning Model
# ==========================================

model = joblib.load("model/house_price_model.pkl")


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# House Price Prediction
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get values from HTML form

        gr_liv_area = float(request.form["GrLivArea"])
        year_built = float(request.form["YearBuilt"])
        garage_cars = float(request.form["GarageCars"])
        total_bsmt_sf = float(request.form["TotalBsmtSF"])
        overall_qual = float(request.form["OverallQual"])
        overall_cond = float(request.form["OverallCond"])


        # Create DataFrame

        input_data = pd.DataFrame([{
            "GrLivArea": gr_liv_area,
            "YearBuilt": year_built,
            "GarageCars": garage_cars,
            "TotalBsmtSF": total_bsmt_sf,
            "OverallQual": overall_qual,
            "OverallCond": overall_cond
        }])


        # Make prediction

        prediction = model.predict(input_data)[0]


        # Round prediction

        prediction = round(prediction, 2)


        # Return result to HTML

        return render_template(
            "index.html",
            prediction=prediction
        )


    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


# ==========================================
# Run Flask Application
# ==========================================















if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000
    )
