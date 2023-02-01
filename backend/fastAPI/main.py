from fastapi import FastAPI

# Documentation with Swagger: http://localhost:8000/docs
# Documentation with Redocly: http://localhost:8000/redoc

app = FastAPI()

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/url")
async def root():
    return { "url_github": "https://github.com/eduardferre" }