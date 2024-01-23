from sqlalchemy import insert, ScalarResult, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from model_machine_learning.detection_result.models import Result
from model_machine_learning.detection_result.schemas import ResultAdd


class ResultCRUD:
    async def add_result(self, db: AsyncSession, processed_image: str, response: dict) -> Result:
        is_detected = "bbox" in response

        # Получение координат и метрик детекции (если есть)
        top_left_x = response["bbox"][0] if is_detected else None
        top_left_y = response["bbox"][1] if is_detected else None
        width = response["bbox"][2] if is_detected else None
        height = response["bbox"][3] if is_detected else None
        confidence = response["bbox"][4] if is_detected else None
        label = response["bbox"][5] if is_detected else None

        # Создание объекта результата детекции
        result = Result(
            processed_image=processed_image,
            is_detected=is_detected,
            top_left_x=top_left_x,
            top_left_y=top_left_y,
            width=width,
            height=height,
            confidence=confidence,
            label=label
        )
        db.add(result)
        try:
            await db.commit()
            return result
        except IntegrityError as e:
            await db.rollback()
            raise e

    async def get_results(self, db: AsyncSession, skip: int, limit: int) -> ScalarResult[Result]:
            results = await db.execute(
                select(Result).offset(skip).limit(limit)
            )
            # unique_pipelines = results.unique()
            return results.scalars()

    async def get_result(self, db: AsyncSession, result_id: int) -> Result:
        result = await db.execute(select(Result).where(Result.id == result_id))
        return result.scalars().first()



result_crud = ResultCRUD()
