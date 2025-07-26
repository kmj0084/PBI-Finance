import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_sp500_tickers():
    # Fetch S&P 500 tickers from Wikipedia
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url)
    sp500_df = table[0]
    tickers = sp500_df['Symbol'].tolist()
    return tickers

def fetch_top_100_stocks(tickers):
    # Fetch the top 500 most actively traded stocks based on average volume
    stock_data = {}
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period='1mo')  # Get one month of data for volume calculation
            if not data.empty:
                stock_data[ticker] = data['Volume'].mean()  # Average volume over the last month
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
    
    # Sort tickers by average volume and get the top 100
    top_100 = sorted(stock_data, key=stock_data.get, reverse=True)[:500]
    return top_100

def fetch_daily_stock_data(tickers):
    # Stock data for tickers from Jan 1, 2022 through previous day
    data_list = []
    start_date = '2022-01-01'
    end_date = datetime.now() - timedelta(days=1)
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            # Fetch historical data
            data = stock.history(start=start_date, end=end_date.strftime('%Y-%m-%d'))
            if not data.empty:
                data['Ticker'] = ticker  # Add a column for the ticker symbol
                data.reset_index(inplace=True)  # Reset index to include 'Date' as a column
                data_list.append(data)
        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    # Concatenate all data into one DataFrame
    all_data = pd.concat(data_list, ignore_index=True)
    return all_data

# Fetch S&P 500 tickers
tickers = get_sp500_tickers()

# Get the top 500 most actively traded stocks
top_100_tickers = fetch_top_100_stocks(tickers)

# Fetch daily stock data
daily_stock_data_df = fetch_daily_stock_data(top_100_tickers)

# Save to CSV
daily_stock_data_df.to_csv('daily_stock_data_top_100.csv', index=False)

print("Daily stock data for the top 500 most actively traded stocks saved to 'daily_stock_data_top_100.csv'")
