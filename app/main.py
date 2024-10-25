from fastapi import FastAPI
from app.src.routers.buyers import router as buyers_router
from app.src.database import database, create_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_db()  # Create the database tables

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include the buyers router
app.include_router(buyers_router)
