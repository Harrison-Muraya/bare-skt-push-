import requests
import base64
from datetime import datetime

from requests.auth import HTTPBasicAuth
import key



unformated_time = datetime.now()
formated_time = unformated_time.strftime("%Y%m%d%H%M%S")

data_to_encode = key.businessshortcode + key.lipa_na_mpesa_passkey + formated_time

encoded = base64.b64encode(data_to_encode.encode())
decoded_pass = encoded.decode("utf-8")

consumer_key = key.consumer_key
consumer_secret = key.comsumer_secret
api_URL = (
    "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
)

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))

json_responce = r.json()

my_access_token = json_responce["access_token"]


def lipa_na_mpeas():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": key.businessshortcode,
        "password": decoded_pass,
        "Timestamp": formated_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartA": key.phone_no,
        "PartB": key.businessshortcode,
        "PhoneNumber": key.phone_no,
        "CallBackaurl": "https://ip_address:port/callback",
        "AccountReference": " ",
        "TransactionDesc": "shool fee",
    }
    responce = requests.post(api_url, json=request, headers=headers)

license()