#!/usr/bin/python
# -*- coding: utf-8 -*-
# 用于访问OKCOIN 现货REST API
import Utilv3 as utils
# Spot

# 获取OKCOIN现货行情信息


def ticker(symbol):
    url = "/api/spot/v3/products/{0}/ticker".format(symbol)
    params = {}
    return utils.api_key_get(params, url)


# 下单
# 创建并执行订单
def send_order(symbol, side, amount, price=0, margin_trading=1):
    params = {"client_oid": "",
              "instrument_id": symbol,
              "side": side,
              "type": "limit",
              "size": amount,
              "price": price,
              "margin_trading": margin_trading}
    if margin_trading == 1:
        url = '/api/spot/v3/orders'
    else:
        url = '/api/margin/v3/orders'

    return utils.api_key_post(params, url)


# 撤销订单
def cancel_order(order_i,margin_trading=1):
    params = {}
    if margin_trading == 1:
        url = "/api/spot/v3/cancel_orders/{0}".format(order_id)
    else:
        url = "/api/margin/v3/cancel_orders/{0}".format(order_id)
    return utils.api_key_post(params, url)


# 批量撤销订单
def batchcancel(symbol, order_ids, margin_trading=1):
    params = {'instrument_id': symbol,
              'order-ids': order_ids
              }
    if margin_trading == 1:
        url = "/api/spot/v3/cancel_batch_orders"
    else:
        url = "/api/margin/v3/cancel_batch_orders"
    return utils.api_key_post(params, url)

# 查询某个订单


def order_info(order_id, margin_trading=1):
    params = {}
    if margin_trading == 1:
        url = "/api/spot/v3/orders/{0}".format(order_id)
    else:
        url = "/api/margin/v3/orders/{0}".format(order_id)
    return utils.api_key_get(params, url)


# 未完成订单

def openorder(size=100):
    params = {'limit': size}
    url = "/api/spot/v3/orders_pending"
    return utils.api_key_get(params, url)


def openorder_margin(size=100):
    params = {'limit': size}
    url = "/api/margin/v3/orders_pending"
    return utils.api_key_get(params, url)

# 获取所有币对信息


def get_instruments():
    params = {}
    url = '/api/spot/v3/products'
    return utils.api_key_get(params, url)


# Margin

# 杠杆配置信息
def get_margininfo(symbol):
    params = {}
    url = '/api/margin/v3/accounts/{0}/availability'.format(symbol)
    return utils.api_key_get(params, url)

# 借币


def get_margin(symbol, currency, amount):
    params = {"instrument_id": symbol,
              "currency": currency,
              "amount": amount}
    url = '/api/margin/v3/accounts/borrow'
    return utils.api_key_post(params, url)

# 还币


def repay_margin(borrow_id, symbol, currency, amount):
    params = {'borrow_id': borrow_id,
              "instrument_id": symbol,
              "currency": currency,
              "amount": amount}
    url = '/api/margin/v3/accounts/repayment'
    return utils.api_key_post(params, url)


# 资金划转


def transfer(currency, amount, fromid, toid, sub_account='', symbol=''):

    params = {'from': fromid,
              "to": toid,
              "currency": currency,
              "amount": amount}
    if sub_account:
        params['sub_account'] = sub_account
    if symbol:
        params['instrument_id'] = sub_account

    url = '/api/account/v3/transfer'
    return utils.api_key_post(params, url)


# 某账户借币记录


def get_borrowed(status, symbol, fromid='', toid='',limit=100):
    params = {'status': status}
    if fromid:
      params['fromid'] = fromid
    if fromid:
      params['toid'] = toid
    url = '/api/margin/v3/accounts/{0}/borrowed'.format(symbol)
    return utils.api_key_get(params, url)