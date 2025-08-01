from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

# Define request body
class Item(BaseModel):
    name : str
    value: int

class Message(BaseModel):
    name : str

@app.get("/")
def read_root():
    return {"message": "Hello, API world!"}

@app.post("/process/")
def process_item(item:Item):
    return {"processed": item.name.upper(), "double_value": item.value*2}

@app.post("/greeting")
def prepare_welcome_message(message:Message):
    return "Hello "+ message.name.lower()


