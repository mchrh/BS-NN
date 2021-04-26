import requests
import urllib
import pandas as pd
import json
import simplejson
import PyTradier

import yfinance as yf 

urls=['VOO', 'MSFT', 'AAPL', 'GOOG']

for url in urls:
    tickerTag = yf.Ticker(url)
    tickerTag.actions.to_csv("tickertag{}.csv".format(url))