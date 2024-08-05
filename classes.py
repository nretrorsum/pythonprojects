from pydantic import BaseModel
from typing import Union, List, Optional
from datetime import datetime
from enum import Enum
from data import user_titles_data, users_data, trades_data


class Data(BaseModel):
    client_id: Optional[int] 
    transaction_id: Optional[int] 
    trade_type: Optional[str] 
    ticker: Optional[str] 
    price: Optional[float] 
    volume: Optional[float] 

class TypeDegree(Enum):
    dungeon_master = "Dungeon master"

class Title(BaseModel):
    client_id: Optional[int]
    title: Optional[str]
    awarded_date: Optional[datetime]

class Degree(BaseModel):
    id: int
    type_degree: TypeDegree
    
class User(BaseModel):
    client_id: int 
    name: str 
    email: str 
    registration_date: datetime 
    degree: Optional[List[Degree]] = None #тут була помилка, оскільки було не заданим по замовчуванню стан None при обробці БД
    
class User_Response(BaseModel):
    user: User
    title: Optional[Title] = None
    transaction: Optional[Data] = None