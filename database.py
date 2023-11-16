from sqlalchemy import create_engine
import databases
import os

DATABASE_URL = os.environ['DATABASE_URL']

database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)