from fastapi import FastAPI
from app.src.routers.sales import router as sales_router
from app.src.database import database, create_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Import & Include the buyers router regarding to your router files
app.include_router(sales_router)