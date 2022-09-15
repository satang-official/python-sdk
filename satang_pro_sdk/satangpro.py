'''
library that provide user to call Satang Pro API easier
'''

import hashlib
import hmac
import json
from get_unix_time import nonce
from all_request import get_request, post_requst, delete_request

class Satangpro:
    '''
    get all constant repeated value
    '''
    def __init__(self, satang_api_key='', satang_api_secret='',url='https://satangcorp.com/api'):
        self.satang_api_key = satang_api_key
        self.satang_api_secret = satang_api_secret
        self.url = url

    def secret_key_encode(self):
        return self.satang_api_secret.encode()

    def request_signature(self,body=''):
        signature = hmac.new(self.secret_key_encode(), msg=body.encode(), digestmod=hashlib.sha512).hexdigest()
        return signature

    def get_headers(self, signature):
        headers = {}
        headers['X-MBX-APIKey'] = self.satang_api_key
        headers['Signature'] = signature
        headers['Authorization'] = f"TDAX-API {self.satang_api_key}"
        headers['Content-Type'] = 'application/json'
        return headers
    '''
    work with API function
    '''
    def get_info(self):
        url = f'{self.url}/users/me' 
        headers = self.get_headers(self.request_signature())
        return get_request(url,headers=headers)

    def get_order(self, pair = '', side = ''):
        #side can be '' then you will get all sell and buy order
        #if side has value as 'buy' or 'sell' you will get only buy or sell order
        params = {'pair': pair}
        if side.lower() in ['buy', 'sell']:
            params['side'] = side.lower()
        headers = self.get_headers(self.request_signature())
        return get_request(f'{self.url}/orders/', params=params,headers = headers)
        
    def get_order_ticker(self):
        url = f'{self.url}/orderbook-tickers/'
        headers = self.get_headers(self.request_signature())
        return get_request(url,headers)

    def get_list_order(self,pair='',limit=10,offset=0,status=''):
        #limit offset status is optional
        params = {'pair':pair,'limit':limit,'offset':offset}
        headers = self.get_headers(self.request_signature())
        url_query = ['open','close']
        if status.lower() in url_query:
            params['status'] = status.lower()
        return get_request(f'{self.url}/orders/user', params=params,headers=headers)

    def get_exchange_info(self):
        url = f'{self.url}/v3/exchangeInfo' 
        headers = self.get_headers(self.request_signature())
        return get_request(url,headers) 

    def get_order_depth(self,pair=''):
        headers = self.get_headers(self.request_signature())
        params={'symbol':pair}
        return get_request(f'{self.url}/v3/depth',params=params,headers=headers)   

    def get_kline_candlestick(self,pair='',interval='1h'):
        #interval is optional between 1 and 2
        headers = self.get_headers(self.request_signature())
        params={'symbol':pair,'interval':interval}
        return get_request(f'{self.url}/v3/klines',params=params,headers=headers)           

    def get_24hr_ticker(self):
        url = f'{self.url}/v3/ticker/24hr'
        headers = self.get_headers(self.request_signature())
        return get_request(url,headers)    

    def get_aggregate_trade(self,pair=''):
        headers = self.get_headers(self.request_signature())
        params = {'symbol':pair}
        return get_request(f'{self.url}/v3/aggTrades',params=params,headers=headers)  

    def generate_listen_key(self):
        url = f'{self.url}/v3/userDataStream'
        headers = self.get_headers(self.request_signature())
        return post_requst(url,headers=headers)

    def keep_alive_listen_key(self):
        url = f'{self.url}/v3/userDataStream'
        payload = json.dumps({'listenKey': self.generate_listen_key().json()})
        headers = self.get_headers(self.request_signature())
        return post_requst(url,headers=headers,payload=payload)

    def create_order(self,pair='',amount='',price='',side=''):
        url = f'{self.url}/orders/'
        type = 'limit'
        unix_timestamp = nonce()
        payload = json.dumps({"amount":str(amount),"nonce":unix_timestamp,"pair":pair,"price":str(price),"side":side,"type":type})
        request_header = f'amount={amount}&nonce={unix_timestamp}&pair={pair}&price={price}&side={side}&type={type}'
        headers = self.get_headers(self.request_signature(request_header))
        return post_requst(url,headers=headers,payload=payload)

    def cancel_order(self,pair='',order_id=''):
        url = f'{self.url}/orders/{order_id}'
        payload = json.dumps({"pair":pair})
        request_header = f'pair={pair}' 
        headers = self.get_headers(self.request_signature(request_header))
        return delete_request(url,headers=headers,payload=payload)

    def cancel_all_order_bypair(self,pair=''):
        url = f'{self.url}/orders/all'
        payload = json.dumps({"pair":pair})
        request_header = f'pair={pair}'
        headers = self.get_headers(self.request_signature(request_header))
        return delete_request(url,headers=headers,payload=payload)

    def thb_deposit_hist(self,limit=10,offset=0):
        headers = self.get_headers(self.request_signature())
        params={'limit':limit,'offset':offset}
        return get_request(f'{self.url}/bank-account-deposits/',params=params,headers=headers)    

    def thb_withdrawal_hist(self,limit=10,offset=0):
        headers = self.get_headers(self.request_signature())
        params={'limit':limit,'offset':offset}
        return get_request(f'{self.url}/fiat-withdrawals/',params=params,headers=headers)   

    def crypto_deposit_hist(self,limit=10,offset=0):
        headers = self.get_headers(self.request_signature())
        params={'limit':limit,'offset':offset}
        return get_request(f'{self.url}/crypto-deposits/', params=params,headers=headers)   

    def crypto_withdrawal_hist(self,limit=10,offset=0):
        headers = self.get_headers(self.request_signature())
        params={'limit':limit,'offset':offset}
        return get_request(f'{self.url}/crypto-withdrawals/', params=params,headers=headers) 

    def get_configs(self):
        url = f'{self.url}/configs/'
        headers = self.get_headers(self.request_signature())
        return get_request(url,headers=headers)   













