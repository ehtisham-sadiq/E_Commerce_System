from fastapi import FastAPI
from app.src.database import database, create_db
from app.src.routers.sellers import router as sellers_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include routers
app.include_router(sellers_router)
