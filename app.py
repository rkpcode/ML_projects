from src.mlproject.logger import logging
from src.mlproject.exception import CustomException


if __name__ == "__main__":
    logging.info("Starting the ML Project Application")
    # Add application logic here
    logging.info("ML Project Application Finished")

    try:
        a=1/0
    except Exception.info("Custom Exception")