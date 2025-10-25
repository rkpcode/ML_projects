from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    logging.info("Starting the ML Project Application")
    # Add application logic here
    logging.info("ML Project Application Finished")

    try:
        data_ingestion = DataIngestion()
        # initiate_data_ingestion expects a file_path parameter in the signature; pass an empty string
        data_ingestion.initiate_data_ingestion("")

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)