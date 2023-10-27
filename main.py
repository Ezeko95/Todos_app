from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# Get all Todos
@app.get("/todos")
async def get_todos():
    return {"message": todos}

# Get a Todo 
@app.get("/todos/{id}")
async def get_todo_by_id(id: int):
    return {"message": todos[id]}

# Create a Todo
@app.post("/todos") 
async def create_todos(todo: str):
    todos.append(todo)
    return {"message": "Todo Created Successfully"}

# Update a Todo
@app.put("/todos/{id}")
async def update_todos(id: int, todo: str):
    todos[id] = todo
    return {"message": "Todo Updated Successfully"}
