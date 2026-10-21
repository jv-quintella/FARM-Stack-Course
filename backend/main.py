from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed frontend origins. The protocol and port must match the frontend URL.
origins = ["https://localhost:300"]

# Configure CORS so the browser can make requests from the frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow credentials such as cookies.
    allow_methods=["*"],     # Allow all HTTP methods.
    allow_headers=["*"],     # Allow all request headers.
)

# Currently return 1 as a placeholder; 


@app.get("/api/todo")
async def get_todo():
    # Return all todos once the database is connected
    return 1


@app.get("/api/todo/{id}")
async def get_todo_by_id(id):
    # The id comes from the URL
    return 1


@app.post("/api/todo")
async def post_todo(todo):
    # Will receive the new todo and save it to the database.
    return 1


@app.put("/api/todo/{id}")
async def put_todo(id, data):
    # Use id to find the todo and data to update its fields.
    return 1


@app.delete("/api/todo/{id}")
async def delete_todo(id):
    # Find the todo by its id and remove it from the database.
    return 1