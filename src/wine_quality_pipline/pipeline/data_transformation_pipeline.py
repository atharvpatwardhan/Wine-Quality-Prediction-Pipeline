from src.wine_quality_pipline.config.configuration import ConfigurationManager
from src.wine_quality_pipline.components.data_transformation import DataTransformation
from src.wine_quality_pipline import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        data_ingestion_pipeline=DataTransformationPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
