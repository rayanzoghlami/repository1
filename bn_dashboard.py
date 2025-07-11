# -*- coding: utf-8 -*-
"""bn_dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C5LFJwTvc56PFBKr1ZM_UNa_5IbQLhMK
"""

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Page Title
st.set_page_config(page_title="BN.TO Stock Dashboard", layout="centered")


# Header
st.title("Brookfield Corporation (BN.TO) Stock Dashboard")

# Fetch data
ticker = yf.Ticker("BN.TO")
hist = ticker.history(period="1y")
info = ticker.info

# Plot TTM data
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(hist.index, hist['Close'], label="Closing Price", linewidth=2)
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.set_title("Past 12 Months of Closing Prices")
ax.set_xlabel("Date")
ax.set_ylabel("Price (CAD)")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Get and print key info
def format_dollars(value):
    if value is None:
        return "N/A"
    return "${:,.0f}".format(value)

def format_number(value):
    if value is None:
        return "N/A"
    return f"{value:.2f}"

st.subheader("Key Stats")
st.write({
    "Current Price": format_dollars(info.get("currentPrice")),
    "Market Cap": format_dollars(info.get("marketCap")),
    "PE Ratio (TTM)": format_number(info.get("trailingPE")),
    "Forward PE": format_number(info.get("forwardPE")),
    "EPS (TTM)": format_number(info.get("trailingEps")),
    "Dividend Yield": format_number(info.get("dividendYield")),
    "52 Week High": format_dollars(info.get("fiftyTwoWeekHigh")),
    "52 Week Low": format_dollars(info.get("fiftyTwoWeekLow")),
    "Currency": info.get("currency"),
})

