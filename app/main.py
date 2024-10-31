from fastapi import FastAPI
import os
from .src.database import database, create_db
from app.src.database import database, create_db, database_url
from app.src.routers.buyers import router as buyers_router
from .src.routers.buyers import router as buyers_router
from .src.routers.sellers import router as sellers_router
from .src.routers.sales import router as sales_router
from .src.routers.auth import router as auth_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
# Include routers
app.include_router(auth_router, tags=["User Registration & Login"])
app.include_router(sellers_router)
app.include_router(buyers_router)
app.include_router(sales_router)