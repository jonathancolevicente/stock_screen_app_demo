import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock App", page_icon="📈")

st.title("Stock Overview App")

# sidebar page selector
from streamlit_option_menu import option_menu

with st.sidebar:
    page = option_menu(
        "Navigation",
        ["Company Overview", "Financials", "Chart"],
        icons=["building", "bar-chart", "graph-up"],  # optional
        menu_icon="cast",
        default_index=0
    )

# store ticker across pages
if "ticker" not in st.session_state:
    st.session_state["ticker"] = ""

ticker = st.text_input(
    "Enter a stock ticker (example: AAPL)",
    value=st.session_state["ticker"]
)

st.session_state["ticker"] = ticker  # update ticker

if not ticker:
    st.write("Enter a ticker above to load data.")
else:
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # Page 1: Overview

    if page == "Company Overview":
        st.header("Company Overview")

        name = info.get("longName", ticker.upper())
        st.subheader(name)

        description = info.get("longBusinessSummary", "No description available.")
        st.write(description)

    #   Page 2: Financials

    elif page == "Financials":
        st.header("Financials & Multiples")

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

    # Page 3: Chart

    elif page == "Chart":
        st.write("### 1-Year Price Chart")
        hist = stock.history(period="1y")
        st.line_chart(hist["Close"])
