from pydantic import BaseModel, Field

class STask(BaseModel):
    # Обязательное поле с валидацией
    name: str = Field(..., min_length=2)

    # Необязательное поле (значение по умолчанию None)
    description: str | None = Field(None, max_length=500)

    # is_done: bool
    priority: int = Field(ge=1, le=10)

class STaskAnn(BaseModel):
    description: str | None = Field(
        default=None,
        title="Детали задачи",
        description="Здесь можно добавить **подробное** описание до 1000 знаков"
    )
    name: str = Field(min_length=2, max_length=100)
    is_done: bool = False  # Если не прислали, будет False
    tags: list[str] = []  # Список строк, по умолчанию пустой

class STaskAdd(BaseModel):
    name:str = Field(..., min_length=2, max_length=100, description="Название задачи")
    description: str | None = Field(None, max_length=300)
    priority: int = Field(ge=1, le=5, default=1)


class SUser(BaseModel):
    name: str = Field()
    age: int = Field()
    is_active: bool = Field(default=True)

class SProduct(BaseModel):
    title: str = Field(...)
    price: int = Field(...)
    description: str | None = Field(None)

class SFeedback(BaseModel):
    message: str = Field(...)
    rating: int = Field(..., ge=1, le=5)

class SRegistration(BaseModel):
    username: str = Field(..., min_length=5, max_length=20)
    bio: str = Field(default="", max_length=100)

