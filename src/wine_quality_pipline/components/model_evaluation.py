import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.wine_quality_pipline.utils.common import save_json
from src.wine_quality_pipline.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
import os

os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/atharvpatwardhan/Wine-Quality-Prediction-Pipeline.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="atharvpatwardhan"
os.environ['MLFLOW_TRACKING_PASSWORD']=""

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    

    def evaluate_metric(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        X_test = test_data.drop(self.config.target_column, axis=1)
        y_test = test_data[[self.config.target_column]]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_experiment("wine_quality_prediction")
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(X_test)

            (rmse, mae, r2) = self.evaluate_metric(y_test, predicted_qualities)

            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(data=scores, path = Path(self.config.metric_file_name))

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElatsticNetWineQualityPredictionModel")

            else:
                mlflow.sklearn.log_model(model, "model")
    