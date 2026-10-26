# House Price Prediction

A Flask web application that predicts an estimated house price using the included trained scikit-learn model.

## Run locally (Mac)

1. Install Python 3.11 or 3.12.
2. Open Terminal and move into this project folder.
3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Install packages:

   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:

   ```bash
   python app.py
   ```
6. Open http://127.0.0.1:8000

## Deploy to Render

1. Upload this folder to a GitHub repository (do not upload `.venv`).
2. In Render, choose **New + → Blueprint** and connect the repository.
3. Render reads `render.yaml`, installs requirements, and starts Gunicorn.
   Alternatively, create a **Web Service** with build command `pip install -r requirements.txt`
   and start command `gunicorn app:app`.
4. Deploy and open the public URL.

The model is loaded using an absolute path, the app listens on `0.0.0.0` and uses the hosting platform's `PORT` variable when run directly. The prediction form sends its values to Flask; it does not generate a random price in the browser.

## Files

- `app.py` — Flask routes and prediction logic
- `model/house_price_model.pkl` — trained model
- `templates/index.html` — page
- `static/` — CSS and JavaScript
- `data/train.csv` and `train_model.py` — optional data/model retraining files
