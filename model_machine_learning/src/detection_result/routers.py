from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from model_machine_learning.src.detection_result.crud import result_crud
from model_machine_learning.src.detection_result.schemas import ResultRead
from app.src.database import get_async_session

router = APIRouter(
    prefix="/image_detection",
    tags=["Image"]
)


@router.get("", response_model=list[ResultRead])
async def get_results(
        skip: Annotated[int, Query(ge=0)] = 0,
        limit: Annotated[int, Query(ge=0)] = 10,
        session: AsyncSession = Depends(get_async_session)) -> list[ResultRead]:
    results = await result_crud.get_results(session, skip, limit)
    return results


@router.get("/{id}", response_model=ResultRead)
async def get_one_pipeline(id: int, session: AsyncSession = Depends(get_async_session)) -> ResultRead:
    result = await result_crud.get_result(session, id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Result detected not found"
        )
    return result
