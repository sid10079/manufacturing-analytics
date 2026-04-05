import pandas as pd
import joblib
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def run_pipeline():
    print("Running Manufacturing Analytics Pipeline...")
    
    # Connect to MySQL using env variables
    engine = create_engine(
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    
    # Load data
    df = pd.read_sql('SELECT * FROM machine_data', con=engine)
    print(f"Loaded {len(df)} rows from MySQL")
    
    # Prepare features
    df_model = df.drop(columns=['Product_ID', 'Type', 'Machine_failure', 'UDI'])
    
    # Load saved model
    model = joblib.load('../models/failure_model.pkl')
    
    # Make predictions
    df['Predicted_Failure'] = model.predict(df_model)
    df['Failure_Probability'] = model.predict_proba(df_model)[:, 1]
    
    # Save predictions back to MySQL
    df[['UDI', 'Predicted_Failure', 'Failure_Probability']].to_sql(
        'failure_predictions',
        con=engine,
        if_exists='replace',
        index=False
    )
    
    print(f"Predictions saved to MySQL!")
    print(f"Machines at risk: {df['Predicted_Failure'].sum()}")
    print("Pipeline complete!")

if __name__ == "__main__":
    run_pipeline()