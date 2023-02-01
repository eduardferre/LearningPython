from fastapi import FastAPI
from routers import users, products
from fastapi.staticfiles import StaticFiles

# Documentation with Swagger: http://localhost:8000/docs
# Documentation with Redocly: http://localhost:8000/redoc

app = FastAPI() # uvicorn main:app --reload

# Routers
app.include_router(users.router)
app.include_router(products.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/url")
async def root():
    return { "url_github": "https://github.com/eduardferre" }