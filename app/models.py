from sqlalchemy import Column, Integer, String, Boolean
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__="userpost"

    id=Column(Integer,primary_key=True,nullable= False)
    email=Column(String,nullable=False)
    title = Column(String, nullable=False)
    blog=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
