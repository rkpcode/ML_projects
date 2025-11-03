from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
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

        # Run data transformation
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path, test_data_path)

        logging.info("ML Project Application Finished")

    except Exception as e:
        logging.info("Custom Exception occurred in app.py")
        raise CustomException(e, sys)
    
    