from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

app = FastAPI()

# Allowed frontend origins. The protocol and port must match the frontend URL.
origins = ["http://localhost:3000"]

# Configure CORS so the browser can make requests from the frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow credentials such as cookies.
    allow_methods=["*"],     # Allow all HTTP methods.
    allow_headers=["*"],     # Allow all request headers.
)

# Database functions used by the routes below.
from database import (
    fetch_all_todos,
    fetch_one_todo,
    create_todo,
    update_todo,
    remove_todo,
)


@app.get("/api/todo")
async def get_todo():
    # Fetch and return all todos from the database.
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_id(title):
    # Search using the title from the URL. Return 404 if not found.
    response = await fetch_one_todo(title)
    if response:
        return response
    else:
        raise HTTPException(404, f"No TODO item with this title {title}")


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    # Convert the validated request to a dictionary and save it.
    response = await create_todo(todo.model_dump())
    if response:
        return response
    else:
        raise HTTPException(400, "Bad request")


@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, description: str):
    # Find by title and update the description.
    response = await update_todo(title, description)
    if response:
        return response
    else:
        raise HTTPException(404, f"No TODO item with this title {title}")


@app.delete("/api/todo/{title}")
async def delete_todo(title):
    # Delete the todo with the given title.
    response = await remove_todo(title)
    if response:
        return "Succesfully deleted TODO item"
    else:
        raise HTTPException(404, f"No TODO item with this title {title}")