import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')

cluster = MongoClient(MONGODB_URI)
db = cluster["users"]


async def get_warning_count(username):
    collection = db[username].find()
    count = -1
    for user in collection:
        count = user["count"]
        break

    if count == -1:
        await create_user(username)
        return 0
    return count


async def get_timeout_count(username):
    collection = db[username].find()
    timeout_count = -1
    for user in collection:
        timeout_count = user["timeout_count"]
        break

    if timeout_count == -1:
        await create_user(username)
        return 0
    return timeout_count


async def create_user(username):
    collection = db[username]
    user_data = {"user": username, "count": 0, "timeout_count": 0}
    collection.insert_one(user_data)
    return


async def update_warning_count(username, warning, timeout):
    prev_count = await get_warning_count(username)
    prev_timeout_count = await get_timeout_count(username)

    if timeout == 1:
        prev_timeout_count = prev_timeout_count + 1

    collection = db[username]
    collection.delete_many({})
    new_user_data = {"user": username, "count": prev_count+warning, "timeout_count": prev_timeout_count}
    collection.insert_one(new_user_data)
    return
