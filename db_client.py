from sqlalchemy.orm import Session
from models import Movie
from schemas import MovieResponse


# Получение всех фильмов из базы данных
def get_all_movies(db: Session):
    return db.query(Movie).all()

# Получение фильма по его идентификатору
def get_movie(movie_id: int, db: Session):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if movie is None:
        return None

    return movie

# Добавление нового фильма в базу данных
def add_movie(payload: MovieResponse, db: Session):
    new_movie = Movie(
        name=payload.name,
        plot=payload.plot,
        genres=payload.genres,
        casts=payload.casts
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie

# Удаление фильма из базы данных по его идентификатору
def delete_movie(movie_id: int, db: Session):
    movie = get_movie(movie_id, db)

    if movie is None:
        return False

    db.delete(movie)
    db.commit()

    return True

# Обновление информации о фильме в базе данных
def update_movie(movie_id: int, payload: MovieResponse, db: Session):
    movie = get_movie(movie_id, db)

    if movie is None:
        return None

    movie.name = payload.name
    movie.plot = payload.plot
    movie.genres = payload.genres
    movie.casts = payload.casts

    db.commit()
    db.refresh(movie)

    return movie