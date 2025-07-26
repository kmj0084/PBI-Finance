# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:49:23 2024

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Quarterly Financial Metrics for Actively Traded S&P 500 Stocks
"""
import yfinance as yf
import pandas as pd
from datetime import datetime

def get_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    sp500_df = table[0]
    tickers = sp500_df['Symbol'].tolist()
    return tickers

def fetch_top_500_stocks(tickers):
    stock_data = {}
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            # Fetch recent data to get volume
            data = stock.history(period='1mo')  # Last month of data to estimate active volume
            if not data.empty:
                stock_data[ticker] = data['Volume'].mean()  # Average volume over the last month
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
    
    # Sort by volume and select top 500 most actively traded stocks
    top_500 = sorted(stock_data, key=stock_data.get, reverse=True)[:500]
    return top_500

def fetch_quarterly_financial_metrics(tickers):
    metrics_list = []
    
    # Date range from Jan 1, 2022 to yesterday
    start_date = pd.Timestamp('2022-01-01')
    end_date = pd.Timestamp.now() - pd.DateOffset(days=1)

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            income_statement = stock.quarterly_financials
            balance_sheet = stock.quarterly_balance_sheet
            cash_flow = stock.quarterly_cashflow

            # Fetch additional metrics
            info = stock.info  # General stock information

            for date in income_statement.columns:
                if start_date <= date <= end_date:
                    metrics = {
                        'Ticker': ticker,
                        'Date': date,
                        'Net Income': income_statement.loc['Net Income'][date],
                        'Total Assets': balance_sheet.loc['Total Assets'][date],
                        'Total Liabilities': balance_sheet.loc['Total Liabilities Net Minority Interest'][date],
                        'Operating Cash Flow': cash_flow.loc['Operating Cash Flow'][date],
                        'Free Cash Flow': cash_flow.loc['Free Cash Flow'][date],
                        'P/E Ratio': info.get('forwardPE', 'N/A'),
                        'Operating Margins': info.get('operatingMargins', 'N/A'),
                        'EBITDA Margins': info.get('ebitdaMargins', 'N/A'),
                        'Quick Ratio': info.get('quickRatio', 'N/A'),
                        'Current Ratio': info.get('currentRatio', 'N/A'),
                        'Revenue Growth': info.get('revenueGrowth', 'N/A'),
                        'Earnings Growth': info.get('earningsGrowth', 'N/A'),
                        'Return on Equity': info.get('returnOnEquity', 'N/A'),
                        'Return on Assets': info.get('returnOnAssets', 'N/A'),
                        'Revenue per Share': info.get('revenuePerShare', 'N/A'),
                        'Debt to Equity': info.get('debtToEquity', 'N/A'),
                        'Total Revenue': info.get('totalRevenue', 'N/A'),
                        'Total Debt': info.get('totalDebt', 'N/A'),
                        'Long Business Summary': info.get('longBusinessSummary', 'N/A'),
                        'Overall Risk': info.get('overallRisk', 'N/A'),
                        'Dividend Rate': info.get('dividendRate', 'N/A'),
                        'Five-Year Avg Dividend Yield': info.get('fiveYearAvgDividendYield', 'N/A'),
                        '52-Week High': info.get('fiftyTwoWeekHigh', 'N/A'),
                        '50-Day Average': info.get('fiftyDayAverage', 'N/A'),
                        '52-Week Low': info.get('fiftyTwoWeekLow', 'N/A'),
                        'PEG Ratio': info.get('pegRatio', 'N/A'),
                        'Trailing PEG Ratio': info.get('trailingPegRatio', 'N/A'),
                        'Trailing P/E': info.get('trailingPE', 'N/A'),
                        'Forward P/E': info.get('forwardPE', 'N/A'), 
                        'Industry': info.get('industry', 'N/A'),
                        'Sector': info.get('sector', 'N/A')
                    }
                    metrics_list.append(metrics)
        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    metrics_df = pd.DataFrame(metrics_list)
    return metrics_df

# Fetch S&P 500 tickers
tickers = get_sp500_tickers()

# Get the top 500 most actively traded stocks
top_500_tickers = fetch_top_500_stocks(tickers)

# Fetch quarterly financial metrics for the top 500
quarterly_financial_metrics_df = fetch_quarterly_financial_metrics(top_500_tickers)

# Save to CSV
quarterly_financial_metrics_df.to_csv('quarterly_financial_metrics_top_500.csv', index=False)

print("Quarterly financial metrics fetched for the top 500 most actively traded S&P 500 stocks and saved to 'quarterly_financial_metrics_top_500.csv'")
