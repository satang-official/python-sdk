Welcome to satangpro
====================

Updated 15 Sep 2022

This is an official Python SDK for the Satangpro API

If you don’t have Satangpro account yet `click
here <https://satangcorp.com/exchange/en/register>`__

This python SDK is an easier tool for using Satangpro API

Source code
-----------

https://github.com/satang-official

Documentation
-------------

https://docs.satangcorp.com/

Satangpro Telegram
------------------

https://t.me/joinchat/N3FyBg8ckQB3e1giJ79MgA

Satangpro Facebook page
-----------------------

https://www.facebook.com/satangcorp

Satangpro support email
-----------------------

support@satangcorp.com

Features
--------

-  Call function and input specify parameters then finish! all done.
-  \ **19 Open API function**\  are ready for you!
-  No need to request signature for sending API request, this SDK will
   do it for you.
-  SDK do not cache any data given to it, feel free to use!
-  Shorten coding redundant authentication from documentation, only one
   line of code is needed.

Notice
------

-  Satangpro SDK will return \ **response object**\  so you need to
   specify Methods such as **response.json(), etc.**

Quick Start
-----------

`Register an account with
Satangpro <https://satangcorp.com/exchange/en/register>`__.

`Generate an API
Key <https://satangcorp.com/exchange/en/settings/api>`__ and assign
relevant permissions.

Installation
~~~~~~~~~~~~

::

   pip install satang-pro-sdk

Initial Step
~~~~~~~~~~~~

::

   from satangpro import Satangpro
   satang_api_key = 'live_12345.....'
   satang_api_secret = '7oDsUT.....'
   sp = Satangpro(satang_api_key,satang_api_secret)

Example (8 of 19 Functions)
---------------------------

List of Contents
~~~~~~~~~~~~~~~~

-  **get open order information of selected pair**

-  **get information of all pair best offer and bid order**

-  **get user listed order on satangpro exchange**

-  **get list of price and grouping amount**

-  **get list of kline & candlestick information of selected pair**

-  **create order**

-  **cancel order**

-  **cancel all open order**

Function 1
~~~~~~~~~~

**get open order information of selected pair**

   This function take 2 parameters such as **pair** and **side**

-  **pair** coin symbol such as ‘btc_thb’, ‘eth_thb, etc.’

-  **side** symbol such as ‘buy’, ‘sell’

..

   **side** does not have to specify, it take initial value as empty
   string

**# no specify side**

::

   btc_order = sp.get_order(pair = 'btc_thb')

..

   Resposne of **print(btc_order.json())**

::

   {
   'bid':[{'price': '12345', 'amount': '0.02', {'price': . . .}], 'ask':[{'price': '12346', 'amount': '0.01',}, {'price': . . .}] 
   }

**# specify**\ side*\* as ‘buy’ or ‘sell’\*\*

::

   btc_order = sp.get_order(pair='btc_thb', side='buy').json()

..

   Resposne of **print(btc_order.json())**

::

   [
   {'price':'12345', 'amount':'0.02'}, {price: . . . } 
   ]

Function 2
~~~~~~~~~~

**get information of all pair best offer and bid order**

   This function take none parameter

::

   best_order = sp.get_order_ticker()

..

   Response of **print(best_order.json())**

::

   {
   'BTC_THB': {
   'bid': {'price': '12345, 'amount': '0.02'}, 'ask': {'price': '12346', 'amount': '0.01'} },
   'USDT_THB': { . . .
   .
   }

Function 3
~~~~~~~~~~

**get user listed order on satangpro exchange**

   This function take 4 parameters

-  **pair** coin symbol such as ‘btc_thb’, ‘eth_thb, etc.’

-  **limit** specify subset data take as integer

-  **offset** specify start index of subset take as positive integer

-  **status** specify complete or incomplete order status take as
   ‘open’, ‘close’

**limit, offset and status** do not have to specify, they take initial
value as limit = 10, offset = 0 and status = empty string

**# only pair is specify**

::

   my_btc_list_order = sp.get_list_order(pair='btc_thb')

..

   Response of **print(my_btc_list_order.json())**

::

   [
   {'id': 23456, 'type': 'limit', 'price': '12345', 'amount': '0.02', 'remaining_amount': '0', 'average_price': '800000', 'side': 'buy', 'cost': '16042.2', 'created_at': '2022-07-10T12:33:49.505228Z', 'status': 'complete'}, {'id': 23457, . . .}, . . .
   ]

**# pair and limit = 1 are specify**

::

   my_btc_list_order = sp.get_list_order(pair='btc_thb', limit = 1)

..

   Response of **print(my_btc_list_order.json())**

::

   [
   {'id': 23456, 'type': 'limit', 'price': '12345', 'amount': '0.02', 'remaining_amount': '0', 'average_price': '800000', 'side': 'buy', 'cost': '16042.2', 'created_at': '2022-07-10T12:33:49.505228Z', 'status': 'complete'}, 
   ]

**# pair and offset = 1 are specify**

::

   # offsest take as index count from lastest to oldest
   my_btc_list_order = sp.get_list_order(pair='btc_thb', offset = 1)

..

   Response of **print(my_btc_list_order.json())**

::

   [
   {'id': 23457, 'type': 'limit', 'price': '12348', 'amount': '0.04', 'remaining_amount': '0', 'average_price': '900000', 'side': 'buy', 'cost': '16067.2', 'created_at': '2022-07-10T19:53:49.505228Z', 'status': 'complete'}, 
   ]

**# pair and status = ‘open’ are specify (Assume no open order)**

::

   # status refer to position of order
   my_btc_list_order = sp.get_list_order(pair='btc_thb', status = 'open')

..

   Response of **print(my_btc_list_order.json())**

::

   []

**# pair and status = ‘close’ are specify**

::

   # status refer to position of order
   my_btc_list_order = sp.get_list_order(pair='btc_thb', status = 'close')

..

   Response of **print(my_btc_list_order.json())**

::

   [
   {'id': 23456, 'type': 'limit', 'price': '12345', 'amount': '0.02', 'remaining_amount': '0', 'average_price': '800000', 'side': 'buy', 'cost': '16042.2', 'created_at': '2022-07-10T12:33:49.505228Z', 'status': 'complete'}, {'id': 23457, . . .}, . . .
   ]

Function 4
~~~~~~~~~~

**get list of price and grouping amount**

   This function take 1 parameter such as **pair**

-  **pair** coin symbol such as ‘btc_thb’, ‘eth_thb, etc.’

::

   all_btc_order = sp.get_order_depth(pair='btc_thb')

..

   Response of **print(all_btc_order.json())**

::

   {
   'lastUpdateId': 54321, 'bids': [ ['12345', '0.02'], . . .
   ], 'asks': [
   ['12346', '0.01'], . . .
   ]
   }

Function 5
~~~~~~~~~~

**get list of kline & candlestick information of selected pair**

   This function take 2 parameters such as **pair and interval**

-  **pair** coin symbol such as ‘btc_thb’, ‘eth_thb, etc.’

-  **interval** specify time limit of support information such as 1m,
   3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M

..

   *m* for minute, *h* for hour, *d* for day, *w* for week and *M* for
   month

   **interval** do not have to specify, it takes initial value as 1h

::

   kline_candlestick_btc = sp.get_kline_candlestick(pair='btc_thb')

..

   Response of **print(kline_candlestick_btc.json())**

::

   [
   [1660140000000, '800000', '800000', '800000', '800000', '0', 1660143599999, '0', 0, '0', '0', '0'], [1660143600000, '800000', '800000', '800000', '800000', '0', 1660147199999, '0', 0, '0', '0', '0'], . . .
   ]

Function 6
~~~~~~~~~~

**create order**

   this function take 4 parameters

-  **pair** coin symbol such as ‘btc_thb’, ‘eth_thb, etc.’

-  **amount** specify coin amount of selected pair

..

   if side = ‘sell’ based on **coin** in wallet, if side = ‘buy’ based
   on **THB** in wallet

-  **price** specify price in THB

..

   if specify price is more than or less than price limit **server**
   will return **error**

-  **side** specify position such as ‘buy’ or ‘sell’

::

   # create order function similar to how to call python function
   # want to buy usdt 3 coin at 42 baht 
   sp.create_order(pair='usdt_thb',amount=3,price=42,side='buy')

..

   Response of
   **print(sp.create_order(pair=‘usdt_thb’,amount=3,price=42,side=‘buy’).json())**

::

   # originally, this function do not return any output
   # for print order (not recommend because python send post request twice)

   {
   'id': 1234567, 'type': 'limit', 'side': 'buy', 'pair': 'usdt_thb', 'open_cost': '123456', 'average_price': '0', 'value': '0', 'cost': '0', 'fee_percent': '0.25', 'taker_fee_percent': '0.25', 'vat_percent': '7', 'time_in_force': 'GTC', 'status': 'processing', 'user_id': 123, 'created_at': '2022-08-31T10:21:23.347858Z', 'created_by_ip': '123.123.123.123', 'updated_at': '2022-08- 31T10:21:23.347858Z', 'price': '42', 'amount': '3', 'remain_amount': '3'
   }

Function 7
~~~~~~~~~~

**cancel order**

   this function take 2 parameters

-  **pair** coin symbol such as ‘btc_thb’, ‘eth_thb’

-  **order_id** specify order id

::

   # cancel order function similar to how to call python function
   # order_id can get through get_list_order(pair = 'selected_pair', status = 'open') function
   sp.cancel_order(pair='usdt_thb',order_id= 12345)

..

   Response of **print(sp.cancel_order(pair=‘usdt_thb’,order_id=
   12345).json())**

::

   # originally, this function do not return any output
   # for print order (not recommend because python send request twice that make order_id not valid because first order_id was cancel)

..

   Example of cancel order

::

   #create open order
   sp.create_order(pair='usdt_thb',amount=3,price=42,side='buy') 

   #check order id of created open order
   order_id = sp.get_list_order(pair='usdt_thb',offset=0,limit=1,status='open').json()[0]['id'] 

   #print to check order id
   print(f'order id = {order_id}') 

   #cancel order that was created
   sp.cancel_order(pair='usdt_thb',order_id=order_id) 

   #make sure server response to cancel request
   time.sleep(2)

   #check order id of created open order (should not be the same with previous order id)
   order_id = sp.get_list_order(pair='usdt_thb',offset=0,limit=1,status='open').json()[0]['id'] 

   #print to check order id
   print(f'order id = {order_id}') 

Function 8
~~~~~~~~~~

**cancel all open order**

   this function take 1 parameter

-  **pair** coin symbol such as ‘btc_thb’, ‘eth_thb, etc.’

::

   # cancel all order function similar to how to call python function
   sp.cancel_all_order(pair='usdt_thb')

..

   Response

::

   # originally, this function do not return any output
   # can check open order by get_list_order() API Function

Summary
=======

Python SDK for the Satangpro API have 19 function which classified into
2 class which are **Take parameters** and **None parameters**

\ **Take parameters (parameters)**\ 

**bold** parameters refer to **must specify**

non-bold = {initial value} of that parameters (Ex.
get_kline_candlestick() -> interval = ‘1h’ if not specify interval value
)

-  

   1. get_order (**pair**, side = ’’)

..

   return dictionary contain order information of specify pair

-  

   2. get_list_order (**pair**, limit = 10, offset = 0, status = ’’)

..

   return list contain all of user order information of specify pair

-  

   3. get_order_depth (**pair**)

..

   return list of price and grouping amount in that price

-  

   4. get_kline_candlestick (**pair**, interval = ‘1h’)

..

   return list of kline & candlestick information of specify pair

-  

   5. get_aggregate_trade (**pair**)

..

   return list of dictionary contain a = ‘trade_id’, p = ‘price in that
   trade’ and q = ‘amount of coin in that trade’

-  

   6. create_order (**pair, amount, price, side**)

..

   send buy or sell order of specify pair to Satangpro server

-  

   7. cancel_order (**pair, order_id**)

..

   send cancel order of selected order_id to Satangpro server

-  

   8. cancel_all_order_bypair (**pair**)

..

   cancel all open order in specify pair

-  

   9. thb_deposit_hist (limit = 10, offset = 0)

..

   return dict of personal information THB_deposit

-  

   10. thb_withdrawal_hist (limit = 10, offset = 0)

..

   return dict of personal information THB_withdrawal

-  

   11. crypto_deposit_hist (limit = 10, offset = 0)

..

   return dict of personal information crypto_deposit

-  

   12. crypto_withdrawal_hist (limit = 10, offset = 0)

..

   return dict of personal information crypto_withdrawal

\ **None parameters**\ 

-  

   1. get_info

..

   return dictionary contain all information of user account

-  

   2. get_order_ticker

..

   return dictionary contain all pair best offer and bid order

-  

   3. get_exchange_info

..

   return dictionary of exchange information such as timezone,
   coin_symbol, etc.

-  

   4. get_24hr_ticker

..

   return list of dictionary contain all pair best offer and bid order
   in 24-hour

-  

   5. generate_listen_key

..

   return listenkey as a token to connect with Satangpro Websocket,
   expire within 1 hour

-  

   6. keep_alive_listen_key

..

   return listenkey but keep it alive more than 1 hour

-  

   7. get_configs

..

   return configs of Satangpro system
