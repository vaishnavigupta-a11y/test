# from database import Base
# from sqlalchemy import Column,rows,boolean,integer,text,String,TIMESTAMP

# class Post(Base):
#       __tablename__="posts"
#       id= Column(integer,primary_key=True,nullable=False)
#       title=Column(String,nullable=False)
#       content=Column(String,nullable=False)
#       published=Column(String,nullable=True)
#     #   created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

# from sqlalchemy import Column, Integer, String
# from .database import Base

# # 1) Creating a page called "users" in notebook
# class User(Base):
#     __tablename__ = "users"

#     # 2) Add columns
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)

# from sqlalchemy import Column,row,Integer,String,lphanumeric
# from database import Base

# class user(Base):
#     __tablename__="userdetail"
#     username=Column(alphanumeric,nullable=False)
#     password=Column(alphanumeric,nullable=False)
#     rollnumber=Column(Integer,Primary_key=True,nullable=False)
# for main3
from sqlalchemy import Column,Integer,String
from database import Base

class User(Base):
    __tablename__="userdetails"
    username=Column(String,nullable=False)
    password=Column(String,nullable=False)
    rollnumber=Column(Integer,primary_key=True,nullable=False)
