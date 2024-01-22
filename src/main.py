from fastapi import FastAPI
from src.pipeline.routers import router as router_pipeline


app = FastAPI(
    title="Image Processing Service"
)

app.include_router(router_pipeline)
