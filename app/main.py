#from fastapi import FastAPI
#from app.src.routers import auth
from fastapi import FastAPI
from app.src.routers.auth import router as auth_router
from app.src.database import database, create_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup():
    await database.connect()
    await create_db()  # Create the database tables

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# app.include_router(api.router)
app.include_router(auth_router, tags=["Authentication & user registration"])
# app.include_router(buyers.router)
# app.include_router(users.router)
# app.include_router(cars.router)
# app.include_router(items.router)
# app.include_router(sales.router)
# app.include_router(sellers.router)
# app.include_router(stocks.router)