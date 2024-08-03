from fastapi import FastAPI

app = FastAPI()

data = [{"id": "1", "name":"kukumber", "balance":"120"},
        {"id": "2", "name":"pidor", "balance":"512"},
        {"id": "3", "name":"huesos", "balance":"654"}]

@app.get("/users/{user_id}")
def get_user_id(user_id: str):
    get_id = [user for user in data  if user.get("id") == user_id]
    return {"id":get_id}

    