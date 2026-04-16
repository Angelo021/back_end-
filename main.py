from fastapi import FastAPI
from app.routes import router
from app.database import client

app = FastAPI(
    title="Book CRUD API",
    description="API para gerenciar livros (CRUD completo)",
    version="1.0.0"
)

app.include_router(router)

@app.on_event("shutdown")
async def shutdown_event():
    client.close()

@app.get("/")
async def root():
    return {"message": "Book CRUD API - FastAPI + MongoDB", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
