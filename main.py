from fastapi import FastAPI
from routes import router as routes_app

app = FastAPI()

app.include_router(routes_app)