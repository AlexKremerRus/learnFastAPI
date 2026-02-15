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

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

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
]

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    for task in fake_tasks_db:
        if task["task_id"] == task_id:
            return {"task": task["task_name"]}
    return {}