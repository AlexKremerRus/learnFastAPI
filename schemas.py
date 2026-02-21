from pydantic import BaseModel

# 1. Базовый класс (общие поля)
class STaskBase(BaseModel):
    name: str
    description: str | None = None

# 2. Класс для создания (ничего не добавляет, просто копирует базу)
class STaskAdd1(STaskBase):
    pass

# 3. Класс для чтения (добавляет id)
class STask1(STaskBase):
    id: int

class SUser1(BaseModel):
    username: str
    email: str

class SProductBase(BaseModel):
    title: str
    price: int

class SProductCreate(SProductBase):
    pass

class SProductResponse(SProductBase):
    id:int


class SUserBase(BaseModel):
    username: str

class SUserCreate(SUserBase):
    password: str

class SUserRead(SUserBase):
    id: int

