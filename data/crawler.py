import requests
import urllib
import pandas as pd
import json
import simplejson

response = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
    params={'symbol': 'APPL', 'expiration': '2019-03-30', 'greeks': 'false'},
    headers={'Authorization': 'Bearer <DOoic2w9mNAX0GUA9hL4vuMRqHzd>', 'Accept': 'application/json'}
).json()
<<<<<<< HEAD
=======

"""if 'json' in response.headers.get('Content-Type'):
    js = response.json()
else:
    print('Response content is not in JSON format.')
    js = 'spam'
"""
>>>>>>> 18be9d15af2bb12199d4453616b0f7955963cf8d
