# 🌍 Global Retail Business Intelligence Dashboard
`Power BI` `DAX` `Python` `ETL` `Star Schema` `Dimensional Modeling` `Multi-Currency`

## 📌 Project Overview
An end-to-end Business Intelligence solution built for a simulated global retail business operating across the **UK, USA, France, Australia, and UAE**. The project covers the full BI lifecycle — from raw data ingestion and currency normalization to dimensional modeling, DAX development, and executive dashboard delivery.

---

## 🎯 Business Problem
The business operated across multiple countries with sales recorded in local currencies, making it impossible to compare revenue performance globally. Management lacked a single source of truth for:
- Cross-country revenue and profit performance
- Product profitability vs. sales volume
- Customer loyalty trends by region
- Time-based variance (YTD, QoQ, YoY)

---

## 🛠 Tech Stack
| Layer | Tools Used |
|---|---|
| Data Ingestion & Currency ETL | Python (Pandas) |
| Data Modeling | Power BI, Star Schema, Dimensional Modeling |
| Calculations & KPIs | DAX (19 measures) |
| Reporting & Visualization | Power BI Desktop |
| Time Intelligence | DAX + Calendar Table |

---

## 🏗 Data Model (Star Schema)
The data model follows a **star schema** design with:
- **Fact Tables:** Sales, Sales in USD, Purchases
- **Dimension Tables:** Countries, Calendar, Exchange Rate

![Data Model](Global-Retail-Dashboard/Screenshots/Data_Model.png)

---

## 📂 Data Sources
| File | Description |
|---|---|
| `sales.xlsx` | Raw sales transactions |
| `purchases.xlsx` | Purchase records including dates and suppliers |
| `countries.xlsx` | Country dimension with region mapping |
| Exchange Rate | Created via Python script inside Power BI |

---

## 🐍 Python — Exchange Rate ETL
The Exchange Rate dimension table was created using a **Python script run directly inside Power BI Desktop** via the Python script data connector. This eliminated the need for an external file and kept the pipeline fully contained within the Power BI solution.
```python
import pandas as pd
from io import StringIO

data = """Exchange ID;ExchangeRate;Exchange Currency
1;1.00;USD
2;0.75;GBP
3;0.85;EUR
4;3.67;AED
5;1.30;AUD"""

Exchange_Data = pd.read_csv(StringIO(data), sep=';')
Exchange_Data
```

> See `/python/exchange_rate_etl.py` for the full documented script.

---

## 🔄 Sales in USD — DAX Calculated Table
To enable global revenue comparison, a **calculated table** was created in DAX using `ADDCOLUMNS` to extend the Sales fact table with USD-normalized revenue columns by joining Exchange Rate, Country, and Purchase date dimensions:
```dax
Sales_in_USD = 
ADDCOLUMNS(
    Sales,
    "Date", RELATED(Purchases[Purchase Date]),
    "Country Name", RELATED(Countries[Country]),
    "Exchange Rate", RELATED('Exchange_Data'[ExchangeRate]),
    "Exchange Currency", RELATED('Exchange_Data'[Exchange Currency]),
    "Gross Revenue USD", [Gross Revenue] * RELATED('Exchange_Data'[ExchangeRate]),
    "Net Revenue USD", [Net Revenue] * RELATED('Exchange_Data'[ExchangeRate]),
    "Total Tax USD", [Total Tax] * RELATED('Exchange_Data'[ExchangeRate]),
    "Profit USD", ([Net Revenue] - [Total Tax]) * RELATED('Exchange_Data'[ExchangeRate])
)
```
This ensures all revenue metrics are comparable in a single currency (USD) regardless of country of sale.

---

## 📐 DAX Measures (19)
Key measures developed:
- `YTD Profit` / `YTD Net Revenue` / `YTD Profit Margin`
- `YoY Revenue Growth %` / `Profit Growth Percentage`
- `Quarterly Profit` / `Quarterly Profit Margin`
- `Running Total Revenue` / `Top Country Revenue`
- `Total Gross Revenue USD` / `Total Net Revenue USD`
- `Median Sales` / `Total Loyalty Points`
- `Tax Per Product` / `Total Stock`

---

## 📊 Dashboard Pages

### Sales Overview
![Sales Dashboard](Global-Retail-Dashboard/Screenshots/Sales_Overview.png)

### Profit Overview
![Profit Dashboard](Global-Retail-Dashboard/Screenshots/Profit_Overview.png)

### Insights & Recommendation 
![Insights and Recommendations Dashboard](Global-Retail-Dashboard/Screenshots/Insights&Recommendations.png)

---

## 💡 Key Business Insights
- **UAE drives 43% of total revenue** — creating over-reliance risk; recommended diversification through targeted promotions in underperforming countries
- **UK holds highest loyalty points** but lags in revenue — opportunity for loyalty-to-purchase conversion programs and premium product bundles
- **Profit volatility in Sep–Oct** indicates seasonal demand patterns — recommended staggered, demand-forecasted promotions to smooth revenue
- **High-volume, low-revenue products** identified — pricing, bundling strategies, and margin adjustments recommended
- **Declining median sales trend** signals need for upselling, cross-selling, and minimum order incentives

---

## 📂 Repository Structure
```
├── GlobalRetail_BI_Dashboard.pbix   ← Power BI report file
├── python/
│   └── exchange_rate.py         ← Python ETL script
├── data/
│   ├── sales.xlsx                   ← Sales transactions
│   ├── purchases.xlsx               ← Purchase records
│   └── countries.xlsx               ← Country dimension
├── screenshots/                     ← Dashboard & model visuals
└── README.md
```

---

## 👩‍💻 Author
**Harshpreet Kour**
