from src.wine_quality_pipline import logger
from src.wine_quality_pipline.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wine_quality_pipline.pipeline.data_validation_pipeline import DataValidationPipeline
from src.wine_quality_pipline.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.wine_quality_pipline.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.wine_quality_pipline.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation_pipeline=DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    model_training_pipeline=ModelTrainingPipeline()
    model_training_pipeline.initiate_model_training()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e