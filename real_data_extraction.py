import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# 1. SETUP CONNECTION (Your fixed version)
USER = 'root'
PASSWORD = urllib.parse.quote_plus('@Aakash277') 
HOST = 'localhost'
PORT = '3306'
DATABASE = 'full_stack_data_analysis_project'

conn_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(conn_string)

# 2. LOAD REAL DATA
try:
    # This replaces our manual 'data' dictionary
    df = pd.read_csv('raw_data.csv') 
    
    # TUTOR TIP: Always check your data before pushing it!
    print("Columns found:", df.columns)
    print("First 5 rows:\n", df.head())

    # 3. PUSH TO SQL
    df.to_sql('cleaned_sales_data', con=engine, if_exists='replace', index=False)
    print("\n✅ Success! The CSV is now a SQL Table.")

except FileNotFoundError:
    print("❌ Error: I couldn't find 'raw_data.csv' in your folder!")
except Exception as e:
    print(f"❌ Something went wrong: {e}")