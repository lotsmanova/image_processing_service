from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.src.database import get_async_session
from app.src.pipeline.schemas import PipelineRead, PipelineAdd
from app.src.pipeline.crud import pipeline_crud

router = APIRouter(
    prefix="/pipelines",
    tags=["Pipeline"]
)


@router.post("", response_model=PipelineRead)
async def add_pipeline(pipeline: PipelineAdd, session: AsyncSession = Depends(get_async_session)) -> PipelineRead:
    pipeline_db = await pipeline_crud.add_pipeline(session, pipeline)
    return pipeline_db


@router.get("", response_model=list[PipelineRead])
async def get_pipelines(
        skip: Annotated[int, Query(ge=0)] = 0,
        limit: Annotated[int, Query(ge=0)] = 10,
        session: AsyncSession = Depends(get_async_session)) -> list[PipelineRead]:
    pipelines = await pipeline_crud.get_pipelines(session, skip, limit)
    return pipelines


@router.patch("/{id}", response_model=PipelineRead)
async def edit_pipeline(id: int, pipeline: PipelineAdd,
                        session: AsyncSession = Depends(get_async_session)) -> PipelineRead:
    db_pipeline = await pipeline_crud.update_pipeline(session, id, pipeline)

    if db_pipeline is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pipeline not found"
        )
    return db_pipeline


@router.get("/{id}", response_model=PipelineRead)
async def get_one_pipeline(id: int, session: AsyncSession = Depends(get_async_session)) -> PipelineRead:
    pipeline = await pipeline_crud.get_pipeline(session, id)
    if pipeline is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pipeline not found"
        )
    return pipeline


@router.delete("/{id}", response_model=PipelineRead)
async def delete_pipeline(id: int, session: AsyncSession = Depends(get_async_session)) -> PipelineRead:
    pipeline = await pipeline_crud.delete_pipeline(session, id)
    if pipeline is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pipelines not found"
        )
    return pipeline
