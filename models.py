from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    plot: Mapped[str] = mapped_column(String, nullable=False)
    genres: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    casts: Mapped[list[str]] = mapped_column(JSON, nullable=False)