from src.wine_quality_pipline.config.configuration import ConfigurationManager
from src.wine_quality_pipline.components.model_trainer import ModelTrainer
from src.wine_quality_pipline import logger


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_training_config)
        model_trainer.train()


