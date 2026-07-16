# 🌡️ AQI Predictor

A simple machine learning project that predicts the **Air Quality Index (AQI)** from temperature using linear regression — built from scratch as a first hands-on ML project.

🔗 **Live App:** _add your Streamlit link here once deployed_

---

## 📌 Overview

This project explores the relationship between temperature and air quality using a single-feature linear regression model. It covers the full ML workflow: exploratory data analysis, model training, evaluation, and deployment as an interactive web app.

## 📊 Exploratory Data Analysis

A scatter plot of temperature vs. AQI showed a clear positive linear relationship — as temperature increases, AQI tends to increase as well.

## 🧠 Model

- **Algorithm:** Linear Regression (scikit-learn)
- **Feature:** Temperature (°C)
- **Target:** AQI

**Train/test split:** 80% train, 20% test (`random_state=42`)

**Learned parameters:**
- Coefficient (slope): `4.64297839`
- Intercept: `25.881965904035724`

**Formula:** `AQI = 4.643 × Temperature + 25.88`

## 📈 Results

| Metric | Train | Test |
|---|---|---|
| R² Score | 0.890 | 0.861 |
| MSE | — | 480.45 |

The model explains roughly **86%** of the variance in AQI on unseen test data, indicating a strong linear fit.

## 🖥️ App Features

The Streamlit app lets users:
- Adjust a temperature slider (0–50°C)
- Get an instant predicted AQI value
- See a color-coded air quality category (Good / Moderate / Unhealthy, etc.)
- View the model's coefficient and intercept in an expandable info section

## 🛠️ Tech Stack

- Python
- pandas, matplotlib
- scikit-learn
- joblib (model persistence)
- Streamlit (UI & deployment)

## 🚀 Run Locally

```bash
git clone https://github.com/saqijani-lab/aqi-predictor.git
cd aqi-predictor
pip install -r requirements.txt
streamlit run app.py
```

## ⚠️ Limitations

- Uses a single feature (temperature) — real AQI depends on many additional factors such as humidity, wind speed, and pollution sources.
- Predictions are approximate and intended for learning purposes, not real-world air quality monitoring.

## 📁 Project Structure

```
aqi-predictor/
├── app.py              # Streamlit app
├── aqi_model.pkl        # Trained linear regression model
├── requirements.txt      # Python dependencies
└── README.md
```

---

*This is my first end-to-end machine learning project, covering data exploration, model training, evaluation, and deployment.*
