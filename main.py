from fastapi import FastAPI
from classes import *

app = FastAPI()

@app.get("/users/{user_id}", response_model = User_Response)
def get_user_info(user_id: int):
    user = next((user for user in users_data if user.get('client_id') == user_id), None)
    transaction = next((trade for trade in reversed(trades_data) if trade.get('client_id') == user_id), None)
    title = next((title for title in reversed(user_titles_data) if title.get('client_id') == user_id), None)
    return {"user": user,"title": title, "transaction": transaction}

"""
@app.get("/users/{user_id}", response_model = List[Data])
def get_last_trades(user_id: int, need_parametr: str = 'last_trades', offset: int = 1):
    get_trade = [user for user in trades_data if user.get('client_id') == user_id]
    return get_trade[0:offset]
"""
@app.post("/users_info/{user_id}")
def info(trades: List[Data]):
    trades_data.extend(trades)
    return {"trades": trades_data}

@app.post("/users_info/{user_id}")
def info(titles: List[Title]):
    user_titles_data.extend(titles)
    return {"titles": user_titles_data}