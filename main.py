from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="Учебное приложение для курса по FastAPI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

@app.get("/get_test")
async def get_test():
    return {"message": "Hello get_test"}

users_db = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    for user in users_db:
        if user == user_id:
            return {"name": users_db[user]}
    return {"error": "User not found"}

@app.get("/users/{user_id}/tasks/{task_id}")
async def get_user_task(user_id, task_id):
    return {"user": user_id, "task": task_id}

@app.post("/create")
async def create():
    return {"status": "created"}


fake_tasks_db = [
    {"task_id": 1, "task_name": "Изучить Python"},
    {"task_id": 2, "task_name": "Подключить Базу Данных"},
    {"task_id": 3, "task_name": "Выучить FastAPI"},
    {"task_id": 4, "task_name": "Изучить FastAPI"},

]

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    for task in fake_tasks_db:
        if task["task_id"] == task_id:
            return {"task": task["task_name"]}
    return {}

@app.get("/hello/{name}")
async def hello_name(name:str):
    return {"message": f"Hello, {name}!"}

@app.get("/product/{product_id}")
async def read_product(product_id: int):
    return {"product_id": product_id}


@app.get("/flights/{from_code}/{to_code}")
async def read_flight(from_code: str, to_code: str):
    return {"from": from_code, "to": to_code}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file": file_path}


fake_tasks_db2 = [
    {"task_name": "Task 1"},
    {"task_name": "Task 2"},
    {"task_name": "Task 3"},
    {"task_name": "Task 4"},
    {"task_name": "Task 5"},
    {"task_name": "Task 6"},
    {"task_name": "Task 7"},
    {"task_name": "Task 8"},
    {"task_name": "Task 9"},
    {"task_name": "Task 10"},
]

@app.get("/tasks2")
async def get_tasks(limit: int = 10, offset: int = 0, keyword: str | None = None):
    if keyword:
        tasks = []

        for task in fake_tasks_db:
            if keyword.lower() in task["task_name"].lower():
                tasks.append(task)
    else:
        tasks = fake_tasks_db2

    return tasks[offset : offset + limit]

@app.get("/items2/")
async def read_items(q: str | None = None):
    if q:
        return {"message": f"Ищем товары по запросу: {q}"}
    return {"message": "Показываем все товары"}

@app.get("/items")
async def get_item(skip:int = 0, limit:int =10):
    return {"skip": skip, "limit": limit}

@app.get("/login")
async def login(username:str, password:str):
    return {"username": username, "password": password}


@app.get("/users1")
async def get_users(is_admin:bool = False):
    return {"is_admin": is_admin}


@app.get("/search")
async def search(query:str | None = None):
    if query:
        return {"msg": f"Searching for {query}"}
    return {"msg": "Showing all results"}

@app.get("/multiply")
async def multiply(value:int, multiplier: int = 2):
    return {"result": value * multiplier}


@app.get("/sum")
async def summa(a:int, b:int):
    return {"result": a+b}


