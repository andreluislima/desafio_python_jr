from fastapi import FastAPI
from app.api.routes import api_router

app = FastAPI(title="Consultation API - Desafio")
app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000,
        log_level='info',
        reload=True
    )