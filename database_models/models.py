from sqlalchemy import Boolean, Column, Integer, String
from database   import Base


class User(Base):
    __tablename__ = "users"

    ID          = Column(Integer, primary_key = True, index = True)
    Username    = Column(String(50), unique = True)


class Post(Base):
    __tablename__ = "posts"

    ID      = Column(Integer, primary_key = True, index = True)
    Title   = Column(String(50), unique = True)
    Content = Column(String(100), unique = True)
    User_ID = Column(Integer, unique = True)