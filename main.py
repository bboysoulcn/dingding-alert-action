import requests
import time
import hmac
import hashlib
import base64
import urllib.parse
import json
import sys


ding_secret = sys.argv[1]
dingding_base_url = sys.argv[2]
msg = sys.argv[3]
title = sys.argv[4]

def send_msg(title,msg,ding_secret,dingding_base_url):
    timestamp = str(round(time.time() * 1000))
    secret = ding_secret
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    body = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": msg
        },
        "at": {
            "isAtAll": "true"
        }
    }
    dingding_url = dingding_base_url + "&timestamp=" + timestamp + "&sign=" + sign
    res = requests.post(dingding_url, json.dumps(body), headers=headers)
    print(res.text)

send_msg(title,msg,ding_secret,dingding_base_url)
