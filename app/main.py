from fastapi import FastAPI
from app.src.database import database, create_db, database_url
from app.src.routers.buyers import router as buyers_router
import os

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include your routers here, as
app.include_router(buyers_router)

