from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import Union, List, Optional
from datetime import datetime

app = FastAPI()

trades_data = [
    {'client_id': 1, 'transaction_id': 101, 'trade_type': 'buy', 'ticker': 'BTC', 'price': 30000.0, 'volume': 0.5},
    {'client_id': 1, 'transaction_id': 102, 'trade_type': 'sell', 'ticker': 'ETH', 'price': 2000.0, 'volume': 1.0},
    {'client_id': 2, 'transaction_id': 103, 'trade_type': 'buy', 'ticker': 'ADA', 'price': 1.2, 'volume': 1000},
    {'client_id': 2, 'transaction_id': 104, 'trade_type': 'buy', 'ticker': 'BTC', 'price': 32000.0, 'volume': 0.1},
    {'client_id': 3, 'transaction_id': 105, 'trade_type': 'sell', 'ticker': 'BNB', 'price': 350.0, 'volume': 5},
    {'client_id': 3, 'transaction_id': 106, 'trade_type': 'buy', 'ticker': 'SOL', 'price': 35.0, 'volume': 50},
    {'client_id': 1, 'transaction_id': 107, 'trade_type': 'buy', 'ticker': 'DOT', 'price': 25.0, 'volume': 40},
    {'client_id': 2, 'transaction_id': 108, 'trade_type': 'sell', 'ticker': 'ETH', 'price': 2100.0, 'volume': 0.5},
    {'client_id': 3, 'transaction_id': 109, 'trade_type': 'buy', 'ticker': 'LINK', 'price': 18.0, 'volume': 150}
]

users_data = [
    {"client_id": 1, "name": "John Doe", "email": "john.doe@example.com", "registration_date": "2024-01-01"},
    {"client_id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "registration_date": "2024-01-02"},
    {"client_id": 3, "name": "Alice Johnson", "email": "alice.johnson@example.com", "registration_date": "2024-01-03"},
    {"client_id": 4, "name": "Bob Brown", "email": "bob.brown@example.com", "registration_date": "2024-01-04"},
    {"client_id": 5, "name": "Charlie Davis", "email": "charlie.davis@example.com", "registration_date": "2024-01-05", "degree": [{"id": 1, "type_degree": "Dungeon master"}]}
]

class Data(BaseModel):
    client_id: int
    transaction_id: int
    trade_type: str
    ticker: str
    price: float
    volume: float

class TypeDegree(Enum):
    dungeon_master = "Dungeon master"

class Degree(BaseModel):
    id: int
    type_degree: TypeDegree
    

class User(BaseModel):
    client_id: int | None = None
    name: str | None = None
    email: str | None = None
    registration_date: datetime | None = None
    degree: Optional[List[Degree]] = None #тут була помилка, оскільки було не заданим по замовчуванню стан None при обробці БД

@app.get("/users/{user_id}", response_model = List[User])
def get_user_info(user_id: int):
    get_id = [user for user in users_data if user.get('client_id') == user_id]
    return get_id

@app.post("/users_info/{user_id}")
def info(trades: List[Data]):
    trades_data.extend(trades)
    return {"trades": trades_data}

