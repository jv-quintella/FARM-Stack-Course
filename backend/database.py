from model import Todo
# MongoDB driver for asynchronous database operations.
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    # Find the first todo with the given title.
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})

    # Read all documents and convert each one to a Todo model.
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    # Insert the todo into the collection.
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, description):
    # Find a todo by title and update only its description.
    await collection.update_one(
        {"title": title},
        {"$set": {"description": description}}
    )
    document = await collection.find_one("{title}:title")
    return document


async def remove_todo(title):
    # Delete the first todo matching the title.
    await collection.delete_one({"title":title})
    return True