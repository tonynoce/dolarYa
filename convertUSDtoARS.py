import json
import time
import requests

# currency
currency = "ARS"

# get url
url = f"""https://api.yadio.io/exrates/{currency}"""
response = requests.get(url)
data = response.json()

# get precio
USDtoARS = data["ARS"]["USD"]


def convertUSDtoARS(monto):
    cotizacion = monto / USDtoARS
    return cotizacion
