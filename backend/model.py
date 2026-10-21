from pydantic import BaseModel

# Define the data structure and validation rules for a todo item.
# Pydantic automatically validates if the incoming API data
class Todo(BaseModel):
    title: str
    description: str