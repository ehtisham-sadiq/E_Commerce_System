from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.src.database import database, create_db
from app.src.routers import sellers, stocks
from app.src.routers.sellers import router as sellers_router
from app.src.routers.stocks import router as stocks_router

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
# Include the buyers router
app.include_router(stocks_router)