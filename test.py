import yfinance as yf
import pandas as pd 

t = yf.Ticker("MSFT")

dati = t.history(period = "1Y")
dati.to_csv("AzioniMicrosoft.csv")

print(dati.head())

