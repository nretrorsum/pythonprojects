import ccxt
import pandas as pd
import numpy as np
import time

# Підключення до біржі Binance
exchange = ccxt.bybit({
    'apiKey': '9yzoYRF6GeGGTNGcHj',
    'secret': 'EoP1hyWoQluFbq80hQnHEQVVeb4Iu0YV7XLU',
})

# Перевірка API-ключів
try:
    exchange.check_required_credentials()
    print("API keys are valid.")
except Exception as e:
    print(f"Error with API keys: {e}")
    exit()

symbol = 'BTC/USDT'
timeframe = '15m'

def fetch_balance():
    balance = exchange.fetch_balance()
    return balance['free']['USDT'], balance['free']['BTC']

def fetch_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def place_order(symbol, order_type, amount):
    if order_type == 'buy':
        order = exchange.create_market_buy_order(symbol, amount)
    elif order_type == 'sell':
        order = exchange.create_market_sell_order(symbol, amount)
    return order

def fetch_ohlcv(symbol, timeframe='1h', limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

def calculate_rsi(df, period=14):
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_sma(df, period):
    return df['close'].rolling(window=period).mean()

# Основний цикл торгівлі
while True:
    df = fetch_ohlcv(symbol, timeframe)
    df['rsi'] = calculate_rsi(df)
    df['sma_50'] = calculate_sma(df, 50)
    df['sma_200'] = calculate_sma(df, 200)

    # Проста стратегія на основі RSI та SMA
    usdt_balance, btc_balance = fetch_balance()

    # Логіка покупки: RSI < 30 та SMA(50) > SMA(200)
    if df['rsi'].iloc[-1] < 30 and df['sma_50'].iloc[-1] > df['sma_200'].iloc[-1] and usdt_balance > 100:
        price = fetch_price(symbol)
        amount = 100 / price  # Купуємо BTC на 100 USDT
        place_order(symbol, 'buy', amount)
        print(f"Bought {amount} BTC at {price} USDT")

    time.sleep(60)  # Затримка в 60 секунд

    # Логіка продажу: RSI > 70 та баланс BTC > 0.001
    usdt_balance, btc_balance = fetch_balance()
    if df['rsi'].iloc[-1] > 70 and btc_balance > 0.001:
        place_order(symbol, 'sell', btc_balance)
        print(f"Sold {btc_balance} BTC")

    time.sleep(60)  # Затримка в 60 секунд