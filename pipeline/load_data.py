import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MySQL using env variables
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

# Load CSV
df = pd.read_csv(r'C:\Users\sidsa\OneDrive\Desktop\New folder\manufacturing-analytics\data\ai4i2020.csv')

# Clean column names
df.columns = df.columns.str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)

# Load into MySQL
df.to_sql('machine_data', con=engine, if_exists='replace', index=False)

print(f"Done! {len(df)} rows loaded into MySQL.")