python# =============================================================
# Exchange Rate ETL Pipeline
# Author: Harshpreet Kour
# Description: Simulates an ETL process to create a normalized
#              Exchange Rate dimension table for multi-currency
#              revenue reporting in Power BI.
# =============================================================

import pandas as pd
from io import StringIO

# ----------------------------
# Raw exchange rate data
# Base currency: USD
# ----------------------------
data = """Exchange ID;ExchangeRate;Exchange Currency
1;1.00;USD
2;0.75;GBP
3;0.85;EUR
4;3.67;AED
5;1.30;AUD"""

# ----------------------------
# Load & transform
# ----------------------------
Exchange_Data = pd.read_csv(StringIO(data), sep=';')

# Note: This script is run inside Power BI Desktop using the
# Python script connector, which ingests Exchange_Data directly
# as a Power BI table — no CSV export required.