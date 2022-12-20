from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
from src.mylib.logic import search_wiki

app = FastAPI()

client = MongoClient('localhost', 27017)
db = client['wiki_db']
testCollection = db.test
# search_records = client['search_records']


@app.get('/')
async def root():
    return {'wikipedia search service , call /search/value endpoint to search in wikipedia'}


@app.get('/search/{value}')
async def search(value: str):
    """search in wikipedia for given value"""
    result = search_wiki(value, 1)

    # save value and result in database
    # record = {value: result}
    testCollection.insert_one({"test": 'test'})

    # try:
    #     testCollection.insertOne({"test": 'test'})
    # except:
    #     result += " failed to insert record to database   "
    #
    # return result


@app.get('/history')
def records():
    return db.list_collection_names()


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
