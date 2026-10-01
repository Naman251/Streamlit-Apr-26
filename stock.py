import streamlit as st
import yfinance as yf
import datetime as dt

st.title("Stock Price Analyser")
st.subheader("This application helps you to analyse the stock price of the company")
# Create a Ticker object for Apple

col1,col2,col3=st.columns(3)

#symbol = yf.Ticker("AAPL")
with col1:
    symbol = st.text_input(
    "Enter the stock ticker",
    value="MSFT"
    )

ticker=yf.Ticker(symbol)
# Get historical market data for a specific period
#ticker_data = ticker.history(period="1y")


with col2:
    start_date=st.date_input(
    "Start Date",
    dt.date.today()-dt.timedelta(days=30)
    )

with col3:
    end_date=st.date_input(
    "End Date",
    dt.date.today()
    )


ticker_data=ticker.history(start=start_date,end=end_date)
col3,col4=st.columns(2)

with col3:
    st.write(ticker_data)

with col4:
    st.subheader("Price Movement")
    st.line_chart(ticker_data["Close"])

st.header("Volume Movement")
st.bar_chart(ticker_data['Volume'])

