import streamlit as st
import pandas as pd
import yfinance
from yahoo_fin.stock_info import get_data
import datetime
from datetime import date
from yahoo_fin import stock_info

today = date.today()

# Set up the Streamlit app
st.title("Ticker checker 📈")
st.caption("This app allows you to check data about a ticker.")

# Get OpenAI API key from user
ticker = st.text_input("ticker", type="default")
line_color = st.color_picker("Pick A Color for the second stock", "#0ff980")
start_date = st.date_input("start date", datetime.date(2000, 1, 1))
end_date = st.date_input("end date", today)

if ticker:

    ticker_ticker = yfinance.Ticker(ticker)
    ticker_data = ticker_ticker.info
    a = pd.DataFrame(ticker_ticker.dividends)

    data_ticker1 = get_data(ticker, start_date = start_date, end_date = end_date, index_as_date = True, interval = "1d")
    price = stock_info.get_live_price(ticker).round(2)
    st.write("actual price:", price)
    
    
    

# show meta information about the history (requires history() to be called first)
    tab1, tab2, tab3 = st.tabs(["📈 Chart", "🗃 Data", "Business Presentation"])

    tab1.subheader("Chart")

    tab2.subheader("A tab with the data")
    tab2.write(ticker + " sector is : " + ticker_data["sector"])
    tab2.write(ticker + " total Market Cap is : " + str(ticker_data["marketCap"]) + " " + ticker_data["currency"])
    if a.empty :
        tab2.write(ticker + " dividend yield is : 0")
    else : 
        tab2.write(ticker + " dividend yield is : " + str(a.iat[-1,0]) + " %")
    
    tab3.write(ticker_data["longBusinessSummary"])

    genre = tab1.radio(
    "What's your favorite movie genre",
    ["Open Price", "Close Price"])


    if genre == "Close Price":
        price_close = data_ticker1["close"]
        tab1.line_chart(price_close, color = line_color)
    else :
        price_open =  data_ticker1["open"]
        tab1.line_chart(price_open, color = line_color)
