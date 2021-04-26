import requests
import pandas as pd
import json

response = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
    params={'symbol': 'VXX', 'expiration': '2019-05-17', 'greeks': 'true'},
    headers={'Authorization': 'Bearer <DOoic2w9mNAX0GUA9hL4vuMRqHzd>', 'Accept': 'application/json'}
)
print(response)
