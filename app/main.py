from fastapi import FastAPI, Response, status, HTTPException,Depends

from fastapi.params import Body
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
import time
from . import models,schemas
from .database import engine, get_db
from typing import List
from .routers import userRoutes

models.Base.metadata.create_all(bind=engine)

app=FastAPI()
while True:

    try:
        conn=psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='vgadmin@123',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print('DataBase connected successful')
        break
    except Exception as error:
        print('Connection to Database Failed')
        print('error:',error)
        time.sleep(2)  

@app.get('/')
def start_app():
    return {"message":"hey everybody"}

app.include_router(userRoutes.router)





