from fastapi import FastAPI, HTTPException, Depends, Response
from sqlalchemy.orm import Session

from db import engine, get_db
from models import Base
from schemas import MovieResponse, MovieDB
from db_client import (
    get_all_movies,
    get_movie,
    add_movie,
    delete_movie,
    update_movie
)

app = FastAPI()

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)


# Получить список всех фильмов
@app.get("/", response_model=list[MovieDB])
async def get_all_movies_endpoint(db: Session = Depends(get_db)):
    return get_all_movies(db)


# Получить фильм по id
@app.get("/{movie_id}", response_model=MovieDB)
async def get_movie_endpoint(
    movie_id: int,
    db: Session = Depends(get_db)
):
    movie = get_movie(movie_id, db)

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie with given id not found"
        )

    return movie


# Добавить фильм
@app.post("/", status_code=201, response_model=MovieDB)
async def add_movie_endpoint(
    payload: MovieResponse,
    db: Session = Depends(get_db)
):
    return add_movie(payload, db)


# Удалить фильм по id
@app.delete("/{movie_id}", status_code=204)
async def delete_movie_endpoint(
    movie_id: int,
    db: Session = Depends(get_db)
):
    result = delete_movie(movie_id, db)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Movie with given id not found"
        )

    return Response(status_code=204)

# Обновить фильм по id
@app.put("/{movie_id}", response_model=MovieDB)
async def update_movie_endpoint(
    movie_id: int,
    payload: MovieResponse,
    db: Session = Depends(get_db)
):
    movie = update_movie(movie_id, payload, db)

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie with given id not found"
        )

    return movie