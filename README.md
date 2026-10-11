# Full Stack Data Analysis Project

## Overview

This project demonstrates a Python-based data extraction and processing workflow integrated with MySQL. It includes loading CSV and Excel datasets into relational database tables, processing tax compliance data, and retrieving currency exchange rates.

The repository also contains a Power BI dashboard for reporting and analysis.

**Technologies:** Python 3.11, MySQL, Pandas, Excel, CSV, REST API, Power BI

## 1. Project Components

### Data Extraction and Loading

The project includes the following Python scripts:

| Script | Description |
|---|---|
| `extraction.py` | Loads a Python DataFrame into MySQL as the `sales_data` table. |
| `real_data_extraction.py` | Reads raw CSV data and loads it into MySQL as the `cleaned_sales_data` table. |
| `compliance_engine.py` | Reads Excel and CSV files, retrieves currency exchange rates, and updates MySQL compliance tables. |

*Note: The paths and availability of the sales extraction scripts should be verified against the latest repository structure.*

## 2. MySQL Database Structure

### Database: `full_stack_data_analysis_project`

This database contains sales-related data.

| Table | Description |
|---|---|
| `sales_data` | Data loaded from a Python DataFrame using `extraction.py`. |
| `cleaned_sales_data` | Data loaded from the raw CSV source using `real_data_extraction.py`. |

### Database: `compliance_db`

This database contains compliance-related information loaded from Excel and CSV files.

| Source File | MySQL Table | Purpose |
|---|---|---|
| `company_details.xlsx` | `dim_entities` | Stores company/entity information. |
| `raw_tax_data.csv` | `fact_compliance` | Stores tax compliance data. |

## 3. Environment Setup

### Prerequisites

- Python 3.11
- MySQL Server
- Python dependencies listed in `requirements.txt`
- Required Excel and CSV input files

### Create a Virtual Environment

Open a terminal in the project's root directory.

```powershell
py -3.11 -m venv venv
```

### Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

Ensure that MySQL is running and that the required database connection configuration is available before executing the scripts.

## 4. Running the Compliance Engine

Navigate to the directory containing `compliance_engine.py`:

```powershell
cd Lookables
```

Execute the script:

```powershell
python compliance_engine.py
```

### Example Execution Output

The following output was captured during a successful local execution:

```text
checking currency rates....
USD to INR Rate: 94.4628
Reading Excel...
Reading CSV...
Uploading to MySQL...
Updating fact_compliance...
Updating dim_entities...
✅ Data successfully replaced in MySQL!
```

The USD-to-INR exchange rate shown above is an example from a previous execution and may differ in subsequent runs.

## 5. Compliance Data Workflow

The compliance engine follows this general processing sequence:

1. Retrieve the USD-to-INR currency exchange rate.
2. Read company details from the Excel source file.
3. Read tax compliance records from the CSV source file.
4. Connect to the MySQL database.
5. Upload and update the compliance-related tables:
   - `dim_entities`
   - `fact_compliance`
6. Display a confirmation message after successful execution.

## 6. Power BI Reporting

The repository includes a Power BI report:

**Strategic Tax Compliance & Revenue Oversight Dashboard**

The report is maintained as a `.pbix` file within the `Reports` directory.

The Power BI reporting component is part of the broader data analysis project.

## 7. Repository Notes

- Use Python 3.11 when creating the virtual environment.
- Keep the `venv/` directory excluded from Git using `.gitignore`.
- Do not commit database passwords, API keys, or other sensitive credentials.
- Ensure the required input datasets are available before running the compliance engine.
- Configure MySQL connectivity for the local environment.
- The project documentation will be expanded as development progresses.

---

## Project Status

**Under active development**

This is an initial project README. Additional technical documentation, architecture details, database schemas, setup instructions, and dashboard screenshots will be added in future updates.
