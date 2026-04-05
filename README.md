# 🏭 Manufacturing Analytics Pipeline

An end-to-end manufacturing analytics pipeline that predicts machine failures using real sensor data — built with MySQL, Python, and Power BI.

---

## 📌 Project Overview

This project simulates a real-world manufacturing environment where machine sensor data is collected, analyzed, and used to predict equipment failures before they happen — reducing unplanned downtime and saving operational costs.

---

## 🎯 Key Results

- Built a complete data pipeline from raw CSV to MySQL to Python to Power BI
- Trained a Random Forest model with 99.9% accuracy
- Achieved a ROC AUC Score of 0.98 on test data
- Identified 331 machines at risk of failure out of 10,000
- Built an interactive Power BI dashboard for operations monitoring

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| MySQL | Data storage and querying |
| Python Pandas and NumPy | Data cleaning and analysis |
| Seaborn and Matplotlib | Data visualization |
| Scikit-learn | Machine learning Random Forest |
| SQLAlchemy and PyMySQL | Python MySQL connection |
| Joblib | Model saving and loading |
| Power BI | Interactive dashboard |

---

## 📁 Project Structure

manufacturing-analytics/
├── data/                   # Raw dataset CSV
├── sql/                    # SQL scripts and schema
├── notebooks/              # Jupyter notebooks
│   ├── eda_analysis.ipynb  # Exploratory Data Analysis
│   └── failure_model.ipynb # ML model training
├── pipeline/               # Python ETL scripts
│   ├── load_data.py        # Load CSV into MySQL
│   └── pipeline.py         # Run predictions pipeline
├── models/                 # Saved ML model
├── dashboard/              # Power BI dashboard file
├── .env.example            # Environment variables template
└── README.md

---

## 📊 Dashboard

The Power BI dashboard includes:
- Total machines, failures and machines at risk KPIs
- Failure distribution by machine type
- Tool wear vs failures trend
- Average failure probability by machine type

---

## 🚀 How to Run

1. Clone the repository
git clone https://github.com/sid10079/manufacturing-analytics.git

2. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn sqlalchemy pymysql joblib python-dotenv jupyter

3. Set up environment variables
Copy .env.example to .env and fill in your MySQL credentials

4. Load data into MySQL
python pipeline/load_data.py

5. Run the predictions pipeline
python pipeline/pipeline.py

6. Open the Jupyter notebooks for EDA and modeling
jupyter notebook

---

## 📂 Dataset

AI4I 2020 Predictive Maintenance Dataset
- Source: UCI Machine Learning Repository
- 10,000 rows of machine sensor readings
- Features: Air temperature, Process temperature, Rotational speed, Torque, Tool wear
- Target: Machine failure binary classification

---

## 💡 Key Insights

- L type machines have the highest failure rate at 69.32%
- High torque combined with high tool wear are the strongest predictors of failure
- Machines with tool wear above 200 minutes show significantly higher failure rates
- Only 3.39% failure rate in the dataset handled using class balancing

---

## 👤 Author

Sidhanth S
GitHub: https://github.com/sid10079

---

## 📄 License

This project is open source and available under the MIT License.
