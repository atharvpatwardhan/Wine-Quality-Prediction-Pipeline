# 🍷 Wine Quality Prediction Pipeline

## 📌 Project Overview

This project is an end-to-end **Wine Quality Prediction Pipeline** that automates the entire machine learning workflow. The pipeline processes wine dataset features to predict the quality of wine based on wine properties.

## 🚀 Features

- **Automated ML Pipeline:** Includes data ingestion, validation, transformation, model training, evaluation, and prediction.
- **MLflow Integration:** Tracks model performance, metrics, and experiment logging.
- **Flask Web App:** Provides an interactive interface for users to input wine properties and get predictions.
- **Scalable & Modular Design:** Ensures ease of modification and extension for different datasets and models.

# ⚙️ Pipeline Stages

- **Data Ingestion:** Loads the wine dataset and handles missing values.
- **Data Validation:** Ensures the dataset meets required schema constraints.
- **Data Transformation:** Prepares features by scaling and encoding categorical variables.
- **Model Training:** Trains the model using algorithms like Random Forest, XGBoost, or others.
- **Model Evaluation:** Logs performance metrics using MLflow for tracking and comparison.
- **Model Prediction:** Deploys the trained model via a Flask web application.

# 📊 Model Performance

The model is evaluated using metrics such as:

- **Accuracy**
- **Mean Squared Error (MSE)**
- **R-squared Score (R²)**

Results and logs are stored in **MLflow** for easy tracking and comparison.

# 🌐 Web Application (Flask)

The Flask-based UI allows users to input wine features and get instant predictions on wine quality.

### **Run the Flask App**

```bash
python app.py
```

Use the route **/train** to train the model before predicting values through the ui.
