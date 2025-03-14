from src.wine_quality_pipline.config.configuration import ConfigurationManager
from src.wine_quality_pipline.components.model_evaluation import ModelEvaluation
from src.wine_quality_pipline import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
    



if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        data_validation_pipeline = ModelEvaluationPipeline()
        data_validation_pipeline.initiate_model_evaluation()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e