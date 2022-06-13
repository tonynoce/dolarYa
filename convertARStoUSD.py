import json
import time
import requests

# currency
currency = "USD"

# get url
url = f"""https://api.yadio.io/exrates/{currency}"""
response = requests.get(url)
data = response.json()

# get precio
ARStoUSD = data["USD"]["ARS"]


def convertARStoUSD(monto):
    cotizacion = monto / ARStoUSD
    return cotizacion
