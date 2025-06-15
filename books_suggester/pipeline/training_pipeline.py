from books_suggester.components.stage_1_data_ingestion import DataIngestion
from books_suggester.components.stage_2_data_validation import DataValidation
from books_suggester.components.stage_3_data_transformation import DataTransformation
from books_suggester.components.stage_4_model_trainer import ModelTrainer


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_validation = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        self.data_transformation.initiate_data_transformation()
        self.model_trainer.initiate_model_trainer() 
        