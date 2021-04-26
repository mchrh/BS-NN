import requests
import urllib
import pandas as pd
import json
import simplejson
from pprint import pprint

response = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
    params={'symbol': 'APPL', 'expiration': '2019-03-30', 'greeks': 'false'},
    headers={'Authorization': 'Bearer <DOoic2w9mNAX0GUA9hL4vuMRqHzd>', 'Accept': 'application/json'}
)

if 'json' in response.headers.get('Content-Type'):
    js = response.json()
else:
    print('Response content is not in JSON format.')
    js = 'spam'
