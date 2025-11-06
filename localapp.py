from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainerConfig,ModelTrainer
import sys

if __name__ == "__main__":
    logging.info("Starting the ML Project Application")
    try:
        # Initialize and run data ingestion
        data_ingestion = DataIngestion()

        # initiate_data_ingestion requires a file_path argument in the signature.
        # The implementation currently reads the source via `read_sql_data()` so
        # an empty string is acceptable as a placeholder.
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion("")

        # Run data transformation and get transformed arrays
        data_transformation = DataTransformation()
        train_array, test_array, _ = data_transformation.initiate_data_transormation(train_data_path, test_data_path)
        
        # Model Training
        model_trainer = ModelTrainer()
        trained_model_score = model_trainer.initiate_model_trainer(train_array, test_array)
        logging.info(f"Model training completed. Score: {trained_model_score}")












        logging.info("ML Project Application Finished")

    except Exception as e:
        logging.info("Custom Exception occurred in app.py")
        raise CustomException(e, sys)
    
    