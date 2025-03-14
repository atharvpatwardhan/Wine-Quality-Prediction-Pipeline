from src.wine_quality_pipline.config.configuration import ConfigurationManager
from src.wine_quality_pipline.components.data_ingestion import DataIngestion    
from src.wine_quality_pipline import logger



STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    

    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        data_ingestion_pipeline=DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
