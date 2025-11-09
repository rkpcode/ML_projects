# ML Projects Repository

## Overview
This repository contains  end-to-end **Machine Learning project** developed using structured engineering practices. It covers the entire data science pipeline starting from data ingestion, exploratory data analysis (EDA), feature engineering, model building, experiment tracking, and model deployment using Flask.

The goal of these projects is to build production-ready ML systems with modularized and reusable components.

---

## Project Structure

```
├── .dvc/                    # DVC pipeline files for data versioning
├── .github/                 # GitHub workflows for CI/CD integration
├── artifacts/               # Saved models, logs, and intermediary files
├── catboost_info/           # CatBoost metadata directory
├── notebook/                # Jupyter notebooks for analysis and experiments
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src/                     # Core project source code (modules and pipelines)
├── templates/               # HTML templates for Flask web application
├── app.py                   # Entry point for running the Flask application
├── flask_app.py             # Alternate or test Flask app setup
├── Dockerfile               # Docker configuration for containerizing the app
├── requirements.txt         # List of Python dependencies
├── setup.py                 # Setup script for packaging and installation
├── .gitignore               # Ignored files for Git
├── .dvcignore               # Ignored files for DVC
└── README.md                # Project documentation (this file)
```

---

## Key Features
- **Data Ingestion**: Extracts raw data from SQL databases and stores it in a structured format.
- **Exploratory Data Analysis (EDA)**: Comprehensive visualization and statistical summary of the data.
- **Feature Engineering & Transformation**: Handles missing values, encoding, scaling, and feature selection.
- **Model Training**: Multiple models trained and compared (including CatBoost, XGBoost, etc.).
- **Experiment Tracking**: Integrated **MLflow** and **DagsHub** for experiment logging and model versioning.
- **Model Monitoring**: Tracks performance metrics and logs for continuous improvement.
- **Deployment**: Flask-based web application for live predictions using the trained model.
- **Containerization**: Dockerized for easy deployment and scalability.

---

## Tech Stack
**Programming Language:** Python 3.10+  
**Frameworks & Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, CatBoost, XGBoost, MLflow, Flask  
**Database:** MySQL  
**Version Control & Tracking:** Git, DVC, MLflow, DagsHub  
**Containerization:** Docker

---

## Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/rkpcode/ML_projects.git
cd ML_projects
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt/ pip install .
```

### 4. Run the Flask Application
```bash
python flask_app.py
```

Visit the app in your browser at: **http://127.0.0.1:5000/**

---

## Project Workflow

1. **Data Collection** → Data fetched from SQL database.  
2. **Data Ingestion** → Stored in local or DVC-managed directories.  
3. **EDA** → Performed using Jupyter notebooks in `/notebook/`.  
4. **Feature Engineering** → Feature transformations and preprocessing.  
5. **Model Training** → Automated training and model selection pipeline.  
6. **Model Tracking** → Monitored via MLflow and DagsHub.  
7. **Model Deployment** → Served through Flask-based prediction API.  
8. **Monitoring** → Model performance metrics logged and visualized.  

---

## Deployment (Docker)

To build and run the Docker container:

```bash
docker build -t ml_project_app .
docker run -p 5000:5000 ml_project_app
```

---

## Future Enhancements

- Integration with cloud services (AWS/GCP/Azure) for deployment.  
- Adding CI/CD pipeline for automated deployment.  
- Enhanced data drift and model monitoring system.  

---

## Author

**Rahul Kumar**  
Machine Learning Enthusiast | Data Science AI/ML Learner  
📧 [contactrkp21@gmail.com](mailto:contactrkp21@gmail.com)  
🌐 [GitHub Profile](https://github.com/rkpcode)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
