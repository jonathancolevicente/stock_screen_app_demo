import streamlit as st
import yfinance as yf

st.title("Stock Overview App")

ticker = st.text_input("Enter a stock ticker (example: AAPL)")

if st.button("Load Data"):
    if ticker == "":
        st.write("Please enter a ticker.")
    else:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            # Company name
            name = info.get("longName", ticker.upper())
            st.subheader(name)

            # ---- Basic Info ----
            st.write("### Basic Info")
            st.write("**Current Price:**", info.get("currentPrice", "N/A"))
            st.write("**Previous Close:**", info.get("previousClose", "N/A"))
            st.write("**52-Week High:**", info.get("fiftyTwoWeekHigh", "N/A"))
            st.write("**52-Week Low:**", info.get("fiftyTwoWeekLow", "N/A"))
            st.write("**Market Cap:**", info.get("marketCap", "N/A"))
            st.write("**Float Shares:**", info.get("floatShares", "N/A"))
            st.write("**Average Volume:**", info.get("averageVolume", "N/A"))

            # ---- Valuation Multiples ----
            st.write("### Valuation Multiples")
            st.write("**P/E Ratio:**", info.get("trailingPE", "N/A"))
            st.write("**Forward P/E:**", info.get("forwardPE", "N/A"))
            st.write("**Price/Sales:**", info.get("priceToSalesTrailing12Months", "N/A"))
            st.write("**Price/Book:**", info.get("priceToBook", "N/A"))
            st.write("**EV/EBITDA:**", info.get("enterpriseToEbitda", "N/A"))
            st.write("**EV/Revenue:**", info.get("enterpriseToRevenue", "N/A"))

            # ---- Company Description ----
            st.write("### Company Description")
            description = info.get("longBusinessSummary", "No description available.")
            st.write(description)

            # ---- Chart ----
            st.write("### 1-Year Price Chart")
            hist = stock.history(period="1y")
            st.line_chart(hist["Close"])

        except Exception as e:
            st.write("Error loading data.")
            st.write(e)
