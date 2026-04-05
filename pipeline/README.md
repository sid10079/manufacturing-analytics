# Manufacturing Analytics Pipeline

End-to-end manufacturing analytics pipeline built with MySQL, Python, and Power BI.

## Project Overview
This project simulates a real-world manufacturing environment where machine sensor data is analyzed to predict equipment failures before they happen.

## Key Results
- Trained a Random Forest model with 99.9% accuracy
- Identified 331 machines at risk of failure  
- Built an interactive Power BI dashboard for operations monitoring

## Tech Stack
- **Database**: MySQL
- **Data Analysis**: Python (Pandas, NumPy, Seaborn, Matplotlib)
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Dashboard**: Power BI
- **Pipeline**: SQLAlchemy, Joblib

## Project Structure
manufacturing-analytics/
├── data/               # Raw dataset
├── sql/                # SQL scripts
├── notebooks/          # Jupyter notebooks for EDA and modeling
├── pipeline/           # Python ETL scripts
├── models/             # Saved ML model
└── dashboard/          # Power BI dashboard file

## How to Run
1. Clone the repository
2. Copy .env.example to .env and fill in your MySQL credentials
3. Install dependencies: pip install -r requirements.txt
4. Run data pipeline: python pipeline/load_data.py
5. Run predictions: python pipeline/pipeline.py

## Dataset
AI4I 2020 Predictive Maintenance Dataset from UCI Machine Learning Repository