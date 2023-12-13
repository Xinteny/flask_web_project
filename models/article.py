from routes import db
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

class Article(db.Model):
    __tablename__ = 'article'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
