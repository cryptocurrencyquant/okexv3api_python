#!/usr/bin/python
# -*- coding: utf-8 -*-
# 用于进行http请求，以及MD5加密，生成签名的工具类
import hmac
import base64
import requests
import json
import datetime
import time


ACCESS_KEY = ''
SECRET_KEY = ''
PASSPHRASE = ''

BASE_URL = 'https://www.okex.com'
CONTENT_TYPE = 'Content-Type'
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'


# signature
def signature(message, secretKey):
    mac = hmac.new(bytes(secretKey, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body



# set request header


def get_header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[CONTENT_TYPE] = APPLICATION_JSON
    header[OK_ACCESS_KEY] = api_key
    header[OK_ACCESS_SIGN] = sign
    header[OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[OK_ACCESS_PASSPHRASE] = passphrase
    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat()
    return t + "Z"

def _get_timestamp():
    url = BASE_URL + '/api/futures/v3/time'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['iso']
    else:
        return ""

def api_key_get(params, request_path):
    method = 'GET'
    timestamp = _get_timestamp()
    sign = signature(pre_hash(timestamp, method, request_path, ''), SECRET_KEY)
    header = get_header(ACCESS_KEY, sign, timestamp, PASSPHRASE)
    request_path = request_path + parse_params_to_str(params)
    url = BASE_URL + request_path
    # print(url)
    # print(header)
    response = requests.get(url, headers=header)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return
    except BaseException as e:
        print("httpPost failed, detail is:%s,%s" % (response.text, e))
        return


def api_key_post(params, request_path):
    method = 'POST'
    timestamp = _get_timestamp()
    body = json.dumps(params)
    sign = signature(pre_hash(timestamp, method, request_path, str(body)), SECRET_KEY)
    header = get_header(ACCESS_KEY, sign, timestamp, PASSPHRASE)
    url = BASE_URL + request_path
    response = requests.post(url, data=body, headers=header)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return
    except BaseException as e:
        print("httpPost failed, detail is:%s,%s" % (response.text, e))
        return
