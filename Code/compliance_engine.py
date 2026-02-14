import pandas as pd
import requests
from sqlalchemy import create_engine, text
import urllib.parse

# 1. Database Connection Setup
USER = 'root'
PASSWORD = urllib.parse.quote_plus('@Aakash277') 
HOST = 'localhost'
PORT = '3306'
DATABASE = 'compliance_db'

conn_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(conn_string)

try:
    # 2. Extract Data
    print("checking currency rates....")
    rates = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()['rates']
    usd_to_inr = rates.get('INR', 90.0)

    print("Reading Excel...")
    df_dim = pd.read_excel('company_details.xlsx')

    print("Reading CSV...")
    df_fact = pd.read_csv('raw_tax_data.csv')
    
    # 3. Transformation (Business Logic)
    # Rule: If Tax > 35% of Revenue, Flag for Audit
    # def audit_logic(row):
    #     tax_ratio = row['Tax_Owed'] / row['Total_Revenue']
    #     if tax_ratio > 0.35:
    #         return 'FLAGGED: HIGH RISK'
    #     return 'COMPLIANT'

    # df['Compliance_Status'] = df.apply(audit_logic, axis=1)

    full_df = pd.merge(df_fact, df_dim, on='Entity_ID')
    def process_compliance(row):
            rev_usd = row['Total_Revenue']/usd_to_inr if row['Headquarters'] == 'India' else  row['Total_Revenue'] 
    # Risk Assessment
            tax_ratio = row['Tax_Owed']/row['Total_Revenue']
            Status = 'HIGH RISK' if tax_ratio > 0.35 else 'COMPLIANT'
            return pd.Series([rev_usd, Status])
    # 4. Load Data to SQL
    # ... (After your merge and process_compliance function)

# 1. Apply the logic to get the calculated columns
    processed_cols = full_df.apply(process_compliance, axis=1)
    processed_cols.columns = ['Revenue_USD', 'Compliance_Status']

# 2. Define final_fact: Pick columns from full_df + the new ones
# Note: We are now including 'Tax_Year'
    final_fact = pd.concat([
    full_df[['Entity_ID', 'Tax_Year', 'Total_Revenue', 'Tax_Owed']], 
    processed_cols
    ], axis=1)

# 3. Rename columns to match the SQL table names exactly
    final_fact.columns = [
    'Entity_ID', 
    'Tax_Year', 
    'Revenue_Local', 
    'Tax_Owed_Local', 
    'Revenue_USD', 
    'Compliance_Status'
    ]

# 4. Load Data to SQL
    print("Uploading to MySQL...")
    
    with engine.connect() as conn:
        # Step A: Disable checks temporarily
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
        
        try:
            # Step B: SWAP THE ORDER
            # We replace the CHILD table first. 
            # This removes the constraint so the Parent can be replaced.
            print("Updating fact_compliance...")
            final_fact.to_sql('fact_compliance', con=conn, if_exists='replace', index=False)
            
            # Now we can safely replace the PARENT table
            print("Updating dim_entities...")
            df_dim.to_sql('dim_entities', con=conn, if_exists='replace', index=False)
            
            # Step C: Save changes
            conn.commit()
            print("✅ Data successfully replaced in MySQL!")
            
        finally:
            # Step D: Always turn checks back on
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
            conn.commit()
except Exception as e:
    print(f"❌ Error: {e}") 