import ccxt
import pandas as pd
import numpy as np
import asyncio
import time  # додано імпорт time
from telegram import Bot

# Налаштування Telegram бота
telegram_token = '6527124998:AAFtg0GXAZcowoqZM3yUeMKHPS9W4slD4vI'
chat_id = '810065989'
bot = Bot(token=telegram_token)

async def send_message(bot, chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

async def main():
    await send_message(bot, chat_id, "Test python trading bot v1.0")

    # Підключення до біржі Bybit для отримання ринкових даних (без ключів API)
    exchange = ccxt.bybit()

    symbol = 'BTC/USDT'
    timeframe = '15m'

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

    async def send_telegram_message(message):
        await bot.send_message(chat_id=chat_id, text=message)

    # Основний цикл торгівлі
    while True:
        try:
            df = fetch_ohlcv(symbol, timeframe)
            df['rsi'] = calculate_rsi(df)
            df['sma_50'] = calculate_sma(df, 50)
            df['sma_200'] = calculate_sma(df, 200)

            # Виведення поточного значення RSI
            rsi_value = df['rsi'].iloc[-1]
            await send_telegram_message(f"Current RSI: {rsi_value:.2f} at {df.index[-1]}")

            # Проста стратегія на основі RSI та SMA
            # Логіка покупки: RSI < 30 та SMA(50) > SMA(200)
            if rsi_value < 30 and df['sma_50'].iloc[-1] > df['sma_200'].iloc[-1]:
                message = f"Buy signal: RSI < 30 and SMA(50) > SMA(200) at {df.index[-1]}"
                await send_telegram_message(message)
                print(message)

            # Логіка продажу: RSI > 70
            elif rsi_value > 70:
                message = f"Sell signal: RSI > 70 at {df.index[-1]}"
                await send_telegram_message(message)
                print(message)

            await asyncio.sleep(60)  # Затримка в 60 секунд перед наступним циклом
            
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(60)  # Затримка перед повторною спробою в разі помилки

if __name__ == '__main__':
    asyncio.run(main())
