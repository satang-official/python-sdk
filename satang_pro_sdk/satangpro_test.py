import unittest
import time
import os
from satangpro import Satangpro

class TestSatangpro(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        #simulate user that already done KYC 
        self.satang_api_key = os.getenv('SATANG_API_KEY')
        self.satang_secret_key = os.getenv('SATANG_API_SECRET')
        self.url = os.getenv('URL')
        self.sp = Satangpro(self.satang_api_key,self.satang_secret_key, self.url)
        self.sp.create_order(pair='usdt_thb',amount=1,price=30,side='buy')
        self.sp.create_order(pair='usdt_thb',amount=1,price=31,side='sell')

    def test_get_info(self):
        info = self.sp.get_info()
        self.assertEqual(200, info.status_code)
        self.assertTrue(len(info.json()['wallets'])>0)

    def test_get_order_buy(self):
        orders = self.sp.get_order(pair='usdt_thb',side='buy')
        self.assertEqual(200, orders.status_code)
        for o in orders.json():
            self.assertIsNotNone(o['price'])
            self.assertIsNotNone(o['amount'])

    def test_get_order_sell(self): 
        orders = self.sp.get_order(pair='usdt_thb',side='sell')
        self.assertEqual(200, orders.status_code)
        for o in orders.json():
            self.assertIsNotNone(o['price'])
            self.assertIsNotNone(o['amount'])

    def test_get_order_no_side(self):
        orders = self.sp.get_order(pair='usdt_thb')
        self.assertEqual(200, orders.status_code)
        for key,data in orders.json().items():
            if key == 'bid':
                for o in data:
                    self.assertIsNotNone(o['price'])
                    self.assertIsNotNone(o['amount'])
            if key == 'ask':
                for o in data:
                    self.assertIsNotNone(o['price'])
                    self.assertIsNotNone(o['amount'])

    def test_get_order_ticker(self):
        tickers = self.sp.get_order_ticker()
        self.assertEqual(200, tickers.status_code)
        self.assertIsNotNone(tickers.json()['USDT_THB'])

    def test_get_list_open_order(self):
        orders = self.sp.get_list_order(pair='usdt_thb',status='open')
        self.assertEqual(200, orders.status_code)
        self.assertTrue(len(orders.json()) > 0)
        self.assertIsNotNone(orders.json()[0]['id'])
        self.assertIsNotNone(orders.json()[0]['type'])
        self.assertIsNotNone(orders.json()[0]['price'])
        self.assertIsNotNone(orders.json()[0]['amount'])
        self.assertIsNotNone(orders.json()[0]['remaining_amount'])
        self.assertIsNotNone(orders.json()[0]['average_price'])
        self.assertIsNotNone(orders.json()[0]['side'])
        self.assertIsNotNone(orders.json()[0]['cost'])
        self.assertIsNotNone(orders.json()[0]['created_at'])
        self.assertIsNotNone(orders.json()[0]['status'])

    def test_get_list_close_order(self):
        orders = self.sp.get_list_order(pair='usdt_thb',status='close')
        self.assertEqual(200, orders.status_code)
        self.assertTrue(len(orders.json()) > 0)
        self.assertIsNotNone(orders.json()[0]['id'])
        self.assertIsNotNone(orders.json()[0]['type'])
        self.assertIsNotNone(orders.json()[0]['price'])
        self.assertIsNotNone(orders.json()[0]['amount'])
        self.assertIsNotNone(orders.json()[0]['remaining_amount'])
        self.assertIsNotNone(orders.json()[0]['average_price'])
        self.assertIsNotNone(orders.json()[0]['side'])
        self.assertIsNotNone(orders.json()[0]['cost'])
        self.assertIsNotNone(orders.json()[0]['created_at'])
        self.assertIsNotNone(orders.json()[0]['status'])

    def test_get_list_order(self):
        orders = self.sp.get_list_order(pair='usdt_thb')
        self.assertEqual(200, orders.status_code)
        self.assertTrue(len(orders.json()) > 0)
        self.assertIsNotNone(orders.json()[0]['id'])
        self.assertIsNotNone(orders.json()[0]['type'])
        self.assertIsNotNone(orders.json()[0]['price'])
        self.assertIsNotNone(orders.json()[0]['amount'])
        self.assertIsNotNone(orders.json()[0]['remaining_amount'])
        self.assertIsNotNone(orders.json()[0]['average_price'])
        self.assertIsNotNone(orders.json()[0]['side'])
        self.assertIsNotNone(orders.json()[0]['cost'])
        self.assertIsNotNone(orders.json()[0]['created_at'])
        self.assertIsNotNone(orders.json()[0]['status'])

    def test_get_list_order_specify(self):
        orders = self.sp.get_list_order(pair='usdt_thb',offset=5)
        self.assertEqual(200, orders.status_code)
        self.assertTrue(len(orders.json()) > 0)
        self.assertIsNotNone(orders.json()[0]['id'])
        self.assertIsNotNone(orders.json()[0]['type'])
        self.assertIsNotNone(orders.json()[0]['price'])
        self.assertIsNotNone(orders.json()[0]['amount'])
        self.assertIsNotNone(orders.json()[0]['remaining_amount'])
        self.assertIsNotNone(orders.json()[0]['average_price'])
        self.assertIsNotNone(orders.json()[0]['side'])
        self.assertIsNotNone(orders.json()[0]['cost'])
        self.assertIsNotNone(orders.json()[0]['created_at'])
        self.assertIsNotNone(orders.json()[0]['status'])

    def test_get_exchange_info(self):
        exchange_info = self.sp.get_exchange_info()
        self.assertGreater(len(exchange_info.json()), 1)
        self.assertEqual(200, exchange_info.status_code)   
        self.assertIsNotNone(exchange_info.json()['symbols'])  

    def test_get_order_depth(self):
        order_depth = self.sp.get_order_depth(pair='usdt_thb')
        self.assertEqual(200, order_depth.status_code)
        self.assertIsNotNone(order_depth.json()['lastUpdateId'])  
        self.assertIsNotNone(order_depth.json()['bids'])  
        self.assertIsNotNone(order_depth.json()['asks'])  

    def test_get_kline_candlestick_1h(self):
        kline_candlestick = self.sp.get_kline_candlestick(pair='usdt_thb')
        self.assertEqual(200, kline_candlestick.status_code)
        self.assertTrue(len(kline_candlestick.json())>0)

    def test_get_kline_candlestick_1h_specify(self):
        kline_candlestick = self.sp.get_kline_candlestick(pair='usdt_thb',interval='1h')
        self.assertEqual(200, kline_candlestick.status_code)
        self.assertTrue(len(kline_candlestick.json())>0)

    def test_get_kline_candlestick_3m(self):
        kline_candlestick = self.sp.get_kline_candlestick(pair='usdt_thb',interval='3m')
        self.assertEqual(200, kline_candlestick.status_code)
        self.assertTrue(len(kline_candlestick.json())>0)

    def test_get_kline_candlestick_3d(self):
        kline_candlestick = self.sp.get_kline_candlestick(pair='usdt_thb',interval='3d')
        self.assertEqual(200, kline_candlestick.status_code)
        self.assertTrue(len(kline_candlestick.json())>0)

    def test_get_kline_candlestick_1M(self):
        kline_candlestick = self.sp.get_kline_candlestick(pair='usdt_thb',interval='1M')
        self.assertEqual(200, kline_candlestick.status_code)
        self.assertTrue(len(kline_candlestick.json())>0)

    def test_get_24hr_ticker(self):
        ticker = self.sp.get_24hr_ticker()
        self.assertEqual(200, ticker.status_code)
        self.assertTrue(len(ticker.json())>0)

    def test_get_aggregate_trade(self):
        aggregate_trade = self.sp.get_aggregate_trade(pair='usdt_thb')
        self.assertEqual(200, aggregate_trade.status_code)
        self.assertTrue(len(aggregate_trade.json())>0)
        self.assertIsNotNone(aggregate_trade.json()[0]['a'])
        self.assertIsNotNone(aggregate_trade.json()[0]['p'])
        self.assertIsNotNone(aggregate_trade.json()[0]['q'])
        self.assertIsNotNone(aggregate_trade.json()[0]['f'])
        self.assertIsNotNone(aggregate_trade.json()[0]['l'])
        self.assertIsNotNone(aggregate_trade.json()[0]['T'])
        self.assertIsNotNone(aggregate_trade.json()[0]['m'])
        self.assertIsNotNone(aggregate_trade.json()[0]['M'])

    def test_generate_listen_key(self):
        listenkey = self.sp.generate_listen_key()
        self.assertEqual(200, listenkey.status_code)
        self.assertIsNotNone(listenkey.json()['listenKey'])
        self.assertGreater(len(listenkey.json()['listenKey']), 1)

    def test_keep_alive_listen_key(self):
        alive_listenkey = self.sp.generate_listen_key()
        self.assertEqual(200, alive_listenkey.status_code)
        self.assertIsNotNone(alive_listenkey.json()['listenKey'])
        self.assertGreater(len(alive_listenkey.json()['listenKey']), 1)

    def test_create_buy_order(self):
        order = self.sp.create_order(pair='usdt_thb',amount=2,price=30,side='buy')
        self.assertEqual(200, order.status_code)
        o = order.json()
        self.assertIsNotNone(o['id'])
        self.assertIsNotNone(o['type'])
        self.assertIsNotNone(o['side'])
        self.assertIsNotNone(o['pair'])
        self.assertIsNotNone(o['open_cost'])
        self.assertIsNotNone(o['average_price'])
        self.assertIsNotNone(o['value'])
        self.assertIsNotNone(o['cost'])
        self.assertIsNotNone(o['fee_percent'])
        self.assertIsNotNone(o['taker_fee_percent'])
        self.assertIsNotNone(o['vat_percent'])
        self.assertIsNotNone(o['time_in_force'])
        self.assertIsNotNone(o['status'])
        self.assertIsNotNone(o['user_id'])
        self.assertIsNotNone(o['created_at'])
        self.assertIsNotNone(o['created_by_ip'])
        self.assertIsNotNone(o['updated_at'])
        self.assertIsNotNone(o['price'])
        self.assertIsNotNone(o['amount'])
        self.assertIsNotNone(o['remain_amount'])

    def test_create_sell_order(self):
        order = self.sp.create_order(pair='usdt_thb',amount=2,price=30,side='sell')
        self.assertEqual(200, order.status_code)
        o = order.json()
        self.assertIsNotNone(o['id'])
        self.assertIsNotNone(o['type'])
        self.assertIsNotNone(o['side'])
        self.assertIsNotNone(o['pair'])
        self.assertIsNotNone(o['open_cost'])
        self.assertIsNotNone(o['average_price'])
        self.assertIsNotNone(o['value'])
        self.assertIsNotNone(o['cost'])
        self.assertIsNotNone(o['fee_percent'])
        self.assertIsNotNone(o['taker_fee_percent'])
        self.assertIsNotNone(o['vat_percent'])
        self.assertIsNotNone(o['time_in_force'])
        self.assertIsNotNone(o['status'])
        self.assertIsNotNone(o['user_id'])
        self.assertIsNotNone(o['created_at'])
        self.assertIsNotNone(o['created_by_ip'])
        self.assertIsNotNone(o['updated_at'])
        self.assertIsNotNone(o['price'])
        self.assertIsNotNone(o['amount'])
        self.assertIsNotNone(o['remain_amount'])

    def test_cancel_buy_order(self):
        buy_order = self.sp.create_order(pair='usdt_thb',amount=2,price=31,side='buy')
        self.assertEqual(200, buy_order.status_code)
        order_id = buy_order.json()['id']
        time.sleep(2)
        cancel_order = self.sp.cancel_order(pair='usdt_thb', order_id= order_id)
        self.assertEqual(202, cancel_order.status_code)

    def test_cancel_sell_order(self):
        sell_order = self.sp.create_order(pair='usdt_thb',amount=2,price=31,side='sell')
        self.assertEqual(200, sell_order.status_code)
        order_id = sell_order.json()['id']
        time.sleep(2)
        cancel_order = self.sp.cancel_order(pair='usdt_thb', order_id= order_id)
        self.assertEqual(202, cancel_order.status_code)

    def test_cancel_all_order_bypair(self):
        buy_order = self.sp.create_order(pair='usdt_thb',amount=2,price=31,side='buy')
        sell_order = self.sp.create_order(pair='usdt_thb',amount=2,price=31,side='sell')
        self.assertEqual(200, buy_order.status_code)
        self.assertEqual(200, sell_order.status_code)
        cancel_all = self.sp.cancel_all_order_bypair(pair='usdt_thb')
        time.sleep(2)
        self.assertEqual(200, cancel_all.status_code)
        self.assertEqual(len(self.sp.get_list_order(pair='usdt_thb',status='open').json()), 0)

    def test_thb_deposit_hist(self):
        thb_deposit = self.sp.thb_deposit_hist()
        self.assertEqual(200, thb_deposit.status_code)
        self.assertTrue(thb_deposit.json()['count'] > 1)
        self.assertIsNotNone(thb_deposit.json()['items'])

    def test_thb_withfrawal_hist(self):
        thb_withdrawal = self.sp.thb_withdrawal_hist()
        self.assertEqual(200, thb_withdrawal.status_code)
        self.assertTrue(thb_withdrawal.json()['count'] > 1)
        self.assertIsNotNone(thb_withdrawal.json()['items'])

    def test_crypto_deposit_hist(self):
        crypto_deposit = self.sp.crypto_deposit_hist()
        self.assertEqual(200, crypto_deposit.status_code)
        self.assertTrue(crypto_deposit.json()['count'] > 1)
        self.assertIsNotNone(crypto_deposit.json()['items'])

    def test_crypto_withfrawal_hist(self):
        crypto_withdrawal = self.sp.thb_withdrawal_hist()
        self.assertEqual(200, crypto_withdrawal.status_code)
        self.assertTrue(crypto_withdrawal.json()['count'] > 1)
        self.assertIsNotNone(crypto_withdrawal.json()['items'])

    def test_get_configs(self):
        configs = self.sp.get_configs()
        self.assertEqual(200, configs.status_code)
        self.assertTrue(len(configs.json()) > 1)
        self.assertIsNotNone(configs.json()['kyc'])
        self.assertIsNotNone(configs.json()['kyc_forms'])

    def test_scenario_1(self):
        #cancel all open order of selected pair
        self.sp.cancel_all_order_bypair('usdt_thb')
        #making sure that no open order of testing pair
        self.assertEqual(0, len(self.sp.get_list_order('usdt_thb',status='open').json()))
        self.sp.create_order('usdt_thb',amount=1,price=32,side='buy')
        #server response time is not fast enough need to sleep for right server response
        #for example create order and get list order in the same time, order will be created but server record is not update yet
        #so get list order function return an old open order record
        time.sleep(1)
        #check that create only 1 order
        self.assertEqual(len(self.sp.get_list_order('usdt_thb',status='open').json()), 1)
        #save order id
        id = self.sp.get_list_order('usdt_thb',status='open').json()[-1]['id']
        #cancle order
        self.sp.cancel_order(pair='usdt_thb',order_id= id)
        time.sleep(1)
        #check order id with lastest cancle order that match and no open order in record
        self.assertEqual(len(self.sp.get_list_order('usdt_thb',status='open').json()), 0)
        self.assertEqual(self.sp.get_list_order('usdt_thb',status='close').json()[0]['id'], id)

    def test_scenario_2(self):
        #cancle all open order
        self.sp.cancel_all_order_bypair('usdt_thb')
        #create 2 open order
        self.sp.create_order('usdt_thb',amount=1,price=33,side='buy')
        self.sp.create_order('usdt_thb',amount=1,price=34,side='buy')
        time.sleep(1)
        #check that in record have 2 open order that were created previously
        self.assertEqual(len(self.sp.get_list_order('usdt_thb',status='open').json()), 2)
        #cancle all order
        self.sp.cancel_all_order_bypair('usdt_thb')
        time.sleep(1)
        #check that no order is open
        self.assertEqual(len(self.sp.get_list_order('usdt_thb',status='open').json()), 0)
        
    def test_signature(self):
        #test signature for get order
        request_header = ''
        signature = self.sp.request_signature(request_header)
        expected_sig = f'9f2dd5c6e9437f54d9045700bf63091d457d1792a70fae7c7b6bd99df81fe25fd789874053d7356358641f8ed1351aea01ad0dec0041466c13f62e1cd26c041b'
        self.assertEqual(signature, expected_sig)

        #test signature for cancel order (usdt_thb)
        request_header = f'pair=usdt_thb'
        signature = self.sp.request_signature(request_header)
        expected_sig = f'2e068810c39a64db68ef57b63a5d9367270f1c687a6bc548b21adec2842339254fd5f93a723c9416b8b53ae383c9edb63c17d44a6c0c5e19ea219fed2d36bc3b'
        self.assertEqual(signature, expected_sig)

        #test signature for create buy order usdt_thb (assume nounce as 123, price as 30)
        #in postman still write nonce as nounce but API can work perfectly fine
        request_header = f'amount=1&nounce=123&pair=usdt_thb&price=30&side=buy&type=limit'
        signature = self.sp.request_signature(request_header)
        expected_sig = f'6283d93ec4b64a95d76082ae42338f4c5b4b10e3c6ae5f2f5806b016d08d949f35afb1a712a5752e9f223f52ec4aa2feee119ee63649c58fa63aa0defc171764'
        self.assertEqual(signature, expected_sig)


if __name__ == '__main__':
    unittest.main()
