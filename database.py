from pymongo import MongoClient
from config import MONGO_URI
import time

client = MongoClient(MONGO_URI)
db = client['multitaskbot']

def is_banned(user_id):
    return db.banned.find_one({"_id": user_id}) is not None

def ban_user(user_id):
    db.banned.update_one({"_id": user_id}, {"$set": {}}, upsert=True)

def unban_user(user_id):
    db.banned.delete_one({"_id": user_id})

def add_user(user_id):
    db.users.update_one({"_id": user_id}, {"$set": {}}, upsert=True)

def count_users():
    return db.users.count_documents({})

def count_banned():
    return db.banned.count_documents({})

def activate_token(user_id):
    db.tokens.update_one({"_id": user_id}, {"$set": {"active": True, "expires": time.time() + 7200}}, upsert=True)

def is_token_active(user_id):
    user = db.tokens.find_one({"_id": user_id})
    return user and user.get("active", False)

def count_token_users():
    return db.tokens.count_documents({})

async def cleanup_expired_tokens():
    now = time.time()
    db.tokens.delete_many({"expires": {"$lt": now}})