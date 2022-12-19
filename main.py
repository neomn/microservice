from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
from src.mylib.logic import search_wiki

app = FastAPI()
client = MongoClient('localhost', 27017)

# print(search_wiki())

@app.get('/')
async def root():
    return {'wikipedia search service , call /search/value endpoint to search in wikipedia'}


@app.get('/search/{value}')
async def search(value: str):
    """search in wikipedia for given value"""
    return search_wiki(value, 1)


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
