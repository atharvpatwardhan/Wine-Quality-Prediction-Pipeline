from src.wine_quality_pipline.config.configuration import ConfigurationManager
from src.wine_quality_pipline.components.data_validation import DataValidation
from src.wine_quality_pipline import logger

STAGE_NAME = "Data Logging Stage"


class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.initiate_data_validation()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e