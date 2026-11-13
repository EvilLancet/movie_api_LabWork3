from pydantic import BaseModel, Field, ConfigDict
from typing import List

# Cхема данных фильма для API
class MovieResponse(BaseModel):
    name: str = Field(..., min_length=1, description="Название фильма")
    plot: str = Field(..., min_length=1, description="Сюжет")
    genres: List[str] = Field(..., min_length=1, description="Жанры фильма")
    casts: List[str] = Field(..., min_length=1, description="Актерский состав")

# Cхема данных фильма для базы данных
class MovieDB(MovieResponse):
    id: int
    model_config = ConfigDict(from_attributes=True)