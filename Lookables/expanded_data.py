import pandas as pd
import random

# --- 1. Load your specific files ---
# We treat the Excel file as a real .xlsx and the tax file as a .csv
company_filename = 'company_details.xlsx'
tax_filename = 'raw_tax_data.csv'

# Read the Excel file (ensure openpyxl is installed)
df_companies = pd.read_excel(company_filename)
df_tax = pd.read_csv(tax_filename)

# --- 2. Create New Company Data ---
last_id = df_companies['Entity_ID'].max()
hqs = df_companies['Headquarters'].unique().tolist()
industries = df_companies['Industry'].unique().tolist()

new_companies = []
for i in range(1, 81): # Adding 80 more records
    new_id = last_id + i
    new_companies.append({
        "Entity_ID": new_id,
        "Company_Name": f"Corp_{new_id}",
        "Headquarters": random.choice(hqs),
        "Industry": random.choice(industries)
    })

df_companies_final = pd.concat([df_companies, pd.DataFrame(new_companies)], ignore_index=True)

# --- 3. Create Multi-Year Tax Records ---
years = [2021, 2022, 2023, 2024]
new_tax_records = []

for entity_id in df_companies_final['Entity_ID']:
    for year in years:
        if not ((df_tax['Entity_ID'] == entity_id) & (df_tax['Tax_Year'] == year)).any():
            revenue = random.randint(500000, 5000000)
            tax_rate = random.uniform(0.15, 0.28)
            tax_owed = int(revenue * tax_rate)
            
            new_tax_records.append({
                "Entity_ID": entity_id,
                "Tax_Year": year,
                "Total_Revenue": revenue,
                "Tax_Owed": tax_owed
            })

df_tax_final = pd.concat([df_tax, pd.DataFrame(new_tax_records)], ignore_index=True)

# --- 4. OVERWRITE the original files ---
# Save the Excel file back as .xlsx
df_companies_final.to_excel(company_filename, index=False)

# Save the Tax file back as .csv
df_tax_final.to_csv(tax_filename, index=False)

print("Process Complete.")
print(f"Overwrote {company_filename} (Excel) and {tax_filename} (CSV).") 