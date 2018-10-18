import account_api as account
import ett_api as ett
import futures_api as future
import lever_api as lever
import spot_api as spot


if __name__ == '__main__':

    api_key = ''
    seceret_key = ''
    passphrase = ''

    # account api test
    # param use_server_time's value is False if is True will use server timestamp
    accountAPI = account.AccountAPI(api_key, seceret_key, passphrase, True)
    result = accountAPI.get_currencies()
    #result = accountAPI.get_wallet()
    #result = accountAPI.get_currency('btc')
    #result = accountAPI.get_currency('btc')
    #result = accountAPI.get_coin_fee('btc')
    # system error...
    #result = accountAPI.get_coin_fee('btc')
    #result = accountAPI.get_coins_withdraw_record()
    #result = accountAPI.get_coin_withdraw_record('BTC')
    #result = accountAPI.get_ledger_record_v3()
    #result = accountAPI.get_top_up_address('BTC')
    #result = accountAPI.get_top_up_address('BTC')
    #result = accountAPI.get_top_up_records()
    #result = accountAPI.get_top_up_record('BTC')
    # spot api test
    #spotAPI = spot.SpotAPI(api_key, seceret_key, passphrase, True)
    #result = spotAPI.get_account_info()
    #result = spotAPI.get_coin_account_info('BTC')
    #result = spotAPI.get_coin_info()
    #result = spotAPI.get_depth('LTC-USDT')
    #result = spotAPI.get_ticker()
    #result = spotAPI.get_orders_list('all', 'Btc-usdT', limit=100)
    #result = spotAPI.get_ledger_record('BTC', limit=1)
    #result = spotAPI.get_specific_ticker('LTC-USDT')
    #result = spotAPI.get_deal_v3('LTC-USDT', 1, 3, 10)
    #result = spotAPI.get_kline('LTC-USDT', '2018-09-12T07:59:45.977Z', '2018-09-13T07:59:45.977Z', 60)

    # future api test
    #futureAPI = future.FutureAPI(api_key, seceret_key, passphrase, True)
    #position = futureAPI.get_position()
    #result = futureAPI.get_coin_account('btc')
    #result = futureAPI.get_leverage('btc')
    #result = futureAPI.set_leverage('BTC', leverage=10)
    #result = futureAPI.get_ledger('btc')
    #result = futureAPI.get_products()
    #result = futureAPI.get_depth('BTC-USD-181019', 1)
    #result = futureAPI.get_ticker()
    #result = futureAPI.get_specific_ticker('ETC-USD-181026')
    #result = futureAPI.get_trades('ETC-USD-181026', 1, 3, 10)
    #result = futureAPI.get_kline('ETC-USD-181026','2018-10-14T03:48:04.081Z', '2018-10-15T03:48:04.081Z')
    #result = futureAPI.get_index('EOS-USD-181019')
    #result = futureAPI.get_rate()
    #result = futureAPI.get_estimated_price('BTC-USD-181019')
    #result = futureAPI.get_holds('BTC-USD-181019')
    #result = futureAPI.get_limit('BTC-USD-181019')
    #result = futureAPI.get_liquidation('BTC-USD-181019')
    #result = futureAPI.get_mark_price('BTC-USD-181019')

    # level api test
    levelAPI = lever.LeverAPI(api_key, seceret_key, passphrase, True)
    #result = levelAPI.get_account_info()
    #result = lever.get_specific_account('btc-usdt')
    #result = levelAPI.get_ledger_record_v3('btc-usdt', '1', '4', '2')
    result3 = levelAPI.get_specific_account('btc-usdt')
    #result = levelAPI.get_specific_config_info('btc-usdt')
    # 分页错误
    #result = levelAPI.get_borrow_coin_v3(0, 1, 2, 1)

    # ett api test
    #ettAPI = ett.EttAPI(api_key, seceret_key, passphrase, True)
    #result = ettAPI.get_accounts()
    #result = ettAPI.get_account('usdt')
    #result = ettAPI.get_ledger('usdt')
    #result = ettAPI.get_constituents('ok06ett')
    #result = ettAPI.get_define_price('ok06ett')

    print(result)









