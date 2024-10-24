from fastapi import FastAPI
from routers import auth, api, buyers, cars, items, sales, sellers, users, stocks

app= FastAPI()

app.include_router(api.router)
app.include_router(auth.router)
app.include_router(buyers.router)
app.include_router(users.router)
app.include_router(cars.router)
app.include_router(items.router)
app.include_router(sales.router)
app.include_router(sellers.router)
app.include_router(stocks.router)