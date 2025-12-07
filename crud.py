from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id : int
    title : str
    author : str
    publisher : str
    published_date : str
    page_count : int
    language: str

class BookUpdateModel(BaseModel):
    title : str
    publisher : str
    page_count : int
    language: str

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2020-07-15",
        "page_count": 792,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Effective Python",
        "author": "Brett Slatkin",
        "publisher": "Pearson",
        "published_date": "2019-05-10",
        "page_count": 480,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Python Crash Course",
               "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2021-11-02",
        "page_count": 544,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2020-02-18",
        "page_count": 592,
        "language": "English",
    },
]

@app.get('/books',response_model=List[Book])
async def get_all_books() -> dict:
    return books

@app.post('/books',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/book/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book does not exist")

@app.patch('/book/{book_id}')
async def update_book(book_id:int,book_update_data:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

@app.delete('/books/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_204_NOT_FOUND,detail="Book not found")
