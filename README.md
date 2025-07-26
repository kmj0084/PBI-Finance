# PBI-Finance
Interactive dashboard with public financial data. 

# 📊 Stories of Data: Power BI + Python Dashboard Project

This is a data storytelling dashboard built in Power BI and powered by a Python-based data pipeline. It simulates an investor-facing portfolio report with clean visuals, dynamic filters, and narrative structure. Python was used to generate and update the dataset via automated scripts.

---

## 🚀 Project Overview

- 🎯 **Goal:** Present stock portfolio insights through interactive data storytelling
- ⚙️ **Tech:** Power BI (visualization), Python (data prep), CSV (source data)
- 🧠 **Focus:** Executive dashboards, custom metrics, layout UX

---

## 📂 Project Structure

```
stories-of-data/
├── storiesOfData.pbix                 # Main Power BI dashboard
├── daily_stock_data_top_100.csv      # Cleaned dataset used in dashboard
├── daily_stock.py                    # Script to ingest stock data
├── daily_stock_new.py                # Enhanced stock metrics
├── metrics_new.py                    # Additional KPI calculations
├── images/
│   ├── page1_overview.png
│   ├── page2_investor_snapshot.png
│   ├── page3_geo_map.png
│   ├── page4_story_narrative.png
│   └── page5_conclusions.png
└── README.md
```

---

## 🖥️ Dashboard Walkthrough

| Page | Description |
|------|-------------|
| ![Overview](Overview.png) | **Executive Overview** – KPIs, total portfolio stats |
| ![Investor Snapshot](edita_snap.png) | **Sector View** – General Sectors - Equities |
| ![Portfolio Tracking](Port_watchlist.png) | **Personal Portfolio** – Slide-style tracker in the report |

---

## 🐍 Python Data Pipeline

The dataset was generated and refreshed using:

- `metrics_new.py`: Adds calculated KPIs (e.g., volatility, growth)
- `daily_stock_new.py`: Pipeline for batch processing multiple tickers
- Output is saved to `daily_stock_data_top_100.csv` and fed into Power BI

> You can run these Python scripts with minimal setup. If you'd like a `requirements.txt` file, let me know.

---

## 📥 Getting Started

> To explore the dashboard:

1. Clone or download the repo
2. Open `storiesOfData.pbix` in Power BI Desktop
3. Use navigation buttons and filters to explore the report

---

## 📌 Notes

- Sample data used for demonstration only
- PBIX file can be adapted for any stock or KPI-based portfolio

