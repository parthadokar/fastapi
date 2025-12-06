from fastapi import FastAPI, HTTPException,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class BookCreateModel(BaseModel):
    title : str
    author : str

@app.get('/')
async def read_root():
    return {"message":"ok"}

@app.get('/greet')
async def greet_name(name:Optional[str] = "user",age:int = 0) -> dict:
    return {"message":f"hello {name}","age":{age}}

@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return {
        "title" : book_data.title,
        "author" : book_data.author
    }

@app.get('/get_headers',status_code=200)
async def get_headers(accept:str = Header(None),content_type:str = Header(None),user_agent:str = Header(None),host:str = Header(None)):
    request_header = {}
    request_header["Accept"] = accept
    request_header["Content-type"] = content_type
    request_header["User-Agent"] = user_agent
    request_header["Host"] = host
    return request_header
