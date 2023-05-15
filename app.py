from db import Mongo

mongodb_host = "0.0.0.0"
mongodb_port = 27017
database_name = "Tasks"
collection_name = "user_tasks"

user_tasks = {
    "name": "User",
    "task_title": "Buy bread",
    "task_description": "Go to nearest shop",
    "task_status": "pending",
}

my_db = Mongo(
    host=mongodb_host, port=mongodb_port, db_name=database_name, coll=collection_name
)

def create_task(task: dict) -> str:
    creation = my_db.create_task(task)
    return creation

def find_task(querry: dict) -> list:
    found = my_db.find_task(query=querry)
    return found

def update_task(query: dict, update:dict) -> str:
    updated = my_db.update_task(query=query, update=update)
    return updated

def delete_task(querry: dict) -> str:
    deleted = my_db.delete_tasks(query=querry)
    return deleted
