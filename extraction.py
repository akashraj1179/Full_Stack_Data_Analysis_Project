import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# 1. CREATE SAMPLE DATA (Since we are starting from scratch)
data = {
    'Transaction_ID': [101, 102, 103, 104, 105],
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Webcam'],
    'Price': [1200, 25, 300, 75, 110],
    'Date': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-04']
}

df = pd.DataFrame(data)

# 2. CONNECTION DETAILS (Update these!)
USER = 'root'
PASSWORD = urllib.parse.quote_plus('@Aakash277') # Put your actual MySQL password here
HOST = 'localhost'
PORT = '3306'
DATABASE = 'full_stack_data_analysis_project'

# 3. CREATE THE ENGINE
# The 'mysql+pymysql' tells SQLAlchemy to use the driver we installed
conn_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(conn_string)

# 4. PUSH TO MYSQL
try:
    # 'if_exists' will create the table for you if it doesn't exist!
    df.to_sql('sales_data', con=engine, if_exists='replace', index=False)
    print("✅ Success! Data has been pushed to MySQL.")
except Exception as e:
    print(f"❌ Error: {e}")
