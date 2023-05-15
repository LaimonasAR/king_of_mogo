from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List


user_tasks = {
    "name": "User",
    "task_title": "Buy bread",
    "task_description": "Go to nearest shop",
    "task_status": "pending",
}
