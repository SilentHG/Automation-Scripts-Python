from binance.client import Client
import time
import datetime
from binance.enums import *

api_key = ""
api_secret = ""

percentage = 0.10 #FIX THIS

profit_calculator = []
profit_calculator.append(0)

doge = False
waves = False
ada = False
bnb = False
wavesbtc = True

client = Client(api_key, api_secret, {"verify": True, "timeout": 20})

# First we store 3 IDS
# Then every second, we check if those id come in historical tradees
# If ID there, then see ID had what "Buy" or "Sell" and also get "Qty" and "Rate"
# And based on "Buy" or "Sell" create opposite order.


if doge == True:
    open_orders = client.get_open_margin_orders(symbol='DOGEUSDT', requests_params={'timeout': 5})
    inner_list_doge = []
    actual_list_doge = []
    for open_order in open_orders:
        # NO USE OF INNER_LIST
        inner_list_doge.append(open_order["orderId"])
        inner_list_doge.append(open_order["side"])
        inner_list_doge.append(open_order["origQty"])
        inner_list_doge.append(open_order["price"])
        temp_orderId = inner_list_doge[0]
        temp_side = inner_list_doge[1]
        temp_origQty = inner_list_doge[2]
        temp_price = inner_list_doge[3]
        actual_list_doge.append([temp_orderId, temp_side, temp_origQty, temp_price])
        inner_list_doge.clear()

    time.sleep(5)

if waves == True:

    open_orders = client.get_open_margin_orders(symbol='WAVESUSDT', requests_params={'timeout': 5})
    inner_list_waves = []
    actual_list_waves = []
    for open_order in open_orders:
        # NO USE OF INNER_LIST
        inner_list_waves.append(open_order["orderId"])
        inner_list_waves.append(open_order["side"])
        inner_list_waves.append(open_order["origQty"])
        inner_list_waves.append(open_order["price"])
        temp_orderId = inner_list_waves[0]
        temp_side = inner_list_waves[1]
        temp_origQty = inner_list_waves[2]
        temp_price = inner_list_waves[3]
        actual_list_waves.append([temp_orderId, temp_side, temp_origQty, temp_price])
        inner_list_waves.clear()

    time.sleep(5)

if ada == True:

    open_orders = client.get_open_margin_orders(symbol='ADAUSDT', requests_params={'timeout': 5})
    inner_list_ada = []
    actual_list_ada = []
    for open_order in open_orders:
        # NO USE OF INNER_LIST
        inner_list_ada.append(open_order["orderId"])
        inner_list_ada.append(open_order["side"])
        inner_list_ada.append(open_order["origQty"])
        inner_list_ada.append(open_order["price"])
        temp_orderId = inner_list_ada[0]
        temp_side = inner_list_ada[1]
        temp_origQty = inner_list_ada[2]
        temp_price = inner_list_ada[3]
        actual_list_ada.append([temp_orderId, temp_side, temp_origQty, temp_price])
        inner_list_ada.clear()

    time.sleep(5)



if bnb == True:

    open_orders = client.get_open_margin_orders(symbol='BNBUSDT', requests_params={'timeout': 5})
    inner_list_bnb = []
    actual_list_bnb = []
    for open_order in open_orders:
        # NO USE OF INNER_LIST
        inner_list_bnb.append(open_order["orderId"])
        inner_list_bnb.append(open_order["side"])
        inner_list_bnb.append(open_order["origQty"])
        inner_list_bnb.append(open_order["price"])
        temp_orderId = inner_list_bnb[0]
        temp_side = inner_list_bnb[1]
        temp_origQty = inner_list_bnb[2]
        temp_price = inner_list_bnb[3]
        actual_list_bnb.append([temp_orderId, temp_side, temp_origQty, temp_price])
        inner_list_bnb.clear()

    time.sleep(5)

if wavesbtc == True:

    open_orders = client.get_open_margin_orders(symbol='WAVESBTC', requests_params={'timeout': 5})
    inner_list_wavesbtc = []
    actual_list_wavesbtc = []
    for open_order in open_orders:
        # NO USE OF INNER_LIST
        inner_list_wavesbtc.append(open_order["orderId"])
        inner_list_wavesbtc.append(open_order["side"])
        inner_list_wavesbtc.append(open_order["origQty"])
        inner_list_wavesbtc.append(open_order["price"])
        temp_orderId = inner_list_wavesbtc[0]
        temp_side = inner_list_wavesbtc[1]
        temp_origQty = inner_list_wavesbtc[2]
        temp_price = inner_list_wavesbtc[3]
        actual_list_wavesbtc.append([temp_orderId, temp_side, temp_origQty, temp_price])
        inner_list_wavesbtc.clear()


def doge_usdt(profit_calculator):
    time.sleep(10)
    client = Client(api_key, api_secret, {"verify": True, "timeout": 20})
    print("Getting Old Trades DOGE " + str(datetime.datetime.now()))
    orders_prev = client.get_all_margin_orders(symbol='DOGEUSDT', limit=100, requests_params={'timeout': 5})
    for prev_orders in orders_prev:
        for curr_order in actual_list_doge:
            if prev_orders["status"] == "FILLED" and prev_orders["orderId"] == curr_order[0]:
                if curr_order[1] == "BUY":
                    order_price = float(curr_order[3]) + float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='DOGEUSDT',
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " DOGE")  # FIX THIS
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_doge.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_doge.append([temp_orderId, temp_side, temp_origQty, temp_price])
                elif curr_order[1] == "SELL":
                    profit_calculator.append(profit_calculator[-1] + (float(curr_order[3])*float(curr_order[2])) * percentage) 


                    order_price = float(curr_order[3]) - float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='DOGEUSDT',
                        side=SIDE_BUY,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " DOGE")
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                        log.write(str(profit_calculator[-1])+"$ Profit Made Yet \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_doge.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_doge.append([temp_orderId, temp_side, temp_origQty, temp_price])


def waves_usdt(profit_calculator):
    time.sleep(10)
    client = Client(api_key, api_secret, {"verify": True, "timeout": 20})
    print("Getting Old Trades WAVES " + str(datetime.datetime.now()))
    orders_prev = client.get_all_margin_orders(symbol='WAVESUSDT', limit=100, requests_params={'timeout': 5})
    for prev_orders in orders_prev:
        for curr_order in actual_list_waves:
            if prev_orders["status"] == "FILLED" and prev_orders["orderId"] == curr_order[0]:
                if curr_order[1] == "BUY":
                    order_price = float(curr_order[3]) + float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='WAVESUSDT',
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " WAVES")
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_waves.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_waves.append([temp_orderId, temp_side, temp_origQty, temp_price])
                elif curr_order[1] == "SELL":
                    profit_calculator.append(profit_calculator[-1] + (float(curr_order[3])*float(curr_order[2])) * percentage)



                    order_price = float(curr_order[3]) - float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='WAVESUSDT',
                        side=SIDE_BUY,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " WAVES")
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                        log.write(str(profit_calculator[-1])+"$ Profit Made Yet \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_waves.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_waves.append([temp_orderId, temp_side, temp_origQty, temp_price])


def ada_usdt(profit_calculator):
    time.sleep(10)
    client = Client(api_key, api_secret, {"verify": True, "timeout": 20})
    print("Getting Old Trades ADA " + str(datetime.datetime.now()))
    orders_prev = client.get_all_margin_orders(symbol='ADAUSDT', limit=100, requests_params={'timeout': 5})
    for prev_orders in orders_prev:
        for curr_order in actual_list_ada:
            if prev_orders["status"] == "FILLED" and prev_orders["orderId"] == curr_order[0]:
                if curr_order[1] == "BUY":
                    order_price = float(curr_order[3]) + float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='ADAUSDT',
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + "ADA")
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_ada.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_ada.append([temp_orderId, temp_side, temp_origQty, temp_price])
                elif curr_order[1] == "SELL":
                    profit_calculator.append(profit_calculator[-1] + (float(curr_order[3])*float(curr_order[2])) * percentage)



                    order_price = float(curr_order[3]) - float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='ADAUSDT',
                        side=SIDE_BUY,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + "ADA")
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                        log.write(str(profit_calculator[-1])+"$ Profit Made Yet \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_ada.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_ada.append([temp_orderId, temp_side, temp_origQty, temp_price])


def bnb_usdt(profit_calculator):
    time.sleep(10)
    client = Client(api_key, api_secret, {"verify": True, "timeout": 20})
    print("Getting Old Trades BNB " + str(datetime.datetime.now()))
    orders_prev = client.get_all_margin_orders(symbol='BNBUSDT', limit=100, requests_params={'timeout': 5})
    for prev_orders in orders_prev:
        for curr_order in actual_list_bnb:
            if prev_orders["status"] == "FILLED" and prev_orders["orderId"] == curr_order[0]:
                if curr_order[1] == "BUY":
                    order_price = float(curr_order[3]) + float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='BNBUSDT',
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " BNB")  # FIX THIS
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_bnb.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_bnb.append([temp_orderId, temp_side, temp_origQty, temp_price])
                elif curr_order[1] == "SELL":
                    profit_calculator.append(profit_calculator[-1] + (float(curr_order[3])*float(curr_order[2])) * percentage)



                    order_price = float(curr_order[3]) - float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='BNBUSDT',
                        side=SIDE_BUY,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " BNB")
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                        log.write(str(profit_calculator[-1])+"$ Profit Made Yet \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_bnb.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_bnb.append([temp_orderId, temp_side, temp_origQty, temp_price])

def waves_btc(profit_calculator):
    time.sleep(10)
    client = Client(api_key, api_secret, {"verify": True, "timeout": 20})
    print("Getting Old Trades WAVESBTC " + str(datetime.datetime.now()))
    orders_prev = client.get_all_margin_orders(symbol='WAVESBTC', limit=100, requests_params={'timeout': 5})
    for prev_orders in orders_prev:
        for curr_order in actual_list_wavesbtc:
            if prev_orders["status"] == "FILLED" and prev_orders["orderId"] == curr_order[0]:
                if curr_order[1] == "BUY":
                    order_price = float(curr_order[3]) + float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='WAVESBTC',
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " WAVESBTC")  # FIX THIS
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_wavesbtc.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_wavesbtc.append([temp_orderId, temp_side, temp_origQty, temp_price])
                elif curr_order[1] == "SELL":
                    profit_calculator.append(profit_calculator[-1] + (float(curr_order[3])*float(curr_order[2])) * percentage)



                    order_price = float(curr_order[3]) - float(curr_order[3]) * percentage
                    order_price = format(order_price, '.4f')
                    order = client.create_margin_order(
                        symbol='WAVESBTC',
                        side=SIDE_BUY,
                        type=ORDER_TYPE_LIMIT,
                        timeInForce=TIME_IN_FORCE_GTC,
                        quantity=float(curr_order[2]),
                        sideEffectType="MARGIN_BUY",
                        price=str(order_price),
                        requests_params={'timeout': 5})
                    print_statement = str(order["side"]) + " at " + str(order["price"] + " WAVESBTC")
                    with open('logger.txt', 'a') as log:
                        log.write(print_statement + " " + str(datetime.datetime.now()) + " \n")
                        log.write(str(profit_calculator[-1])+"$ Profit Made Yet \n")
                    print(str(order["side"]) + " at " + str(order["price"]))
                    actual_list_wavesbtc.remove(curr_order)
                    temp_orderId = order["orderId"]
                    temp_side = order["side"]
                    temp_origQty = order["origQty"]
                    temp_price = order["price"]
                    actual_list_wavesbtc.append([temp_orderId, temp_side, temp_origQty, temp_price])


while True:
    try:
        
        if doge == True:

            doge_usdt(profit_calculator)
            time.sleep(5)

        if waves == True:

            waves_usdt(profit_calculator)
            time.sleep(5)

        if ada == True:

            ada_usdt(profit_calculator)
            time.sleep(5)

        if bnb == True:

            bnb_usdt(profit_calculator)
            time.sleep(5)

        if wavesbtc == True:
            waves_btc(profit_calculator)
            time.sleep(5)




    except Exception as e:
        print(str(e))
        with open('logger.txt', 'a') as log:
            log.write(str(e) + str(datetime.datetime.now()) + " \n")
        time.sleep(60)
