from sqlalchemy import select
from sqlalchemy.engine import ScalarResult
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from app.src.pipeline.schemas import PipelineAdd
from app.src.pipeline.models import Pipelines, Steps


class PipelineCRUD:
    async def add_pipeline(self, db: AsyncSession, pipeline: PipelineAdd) -> Pipelines:
        db_pipeline = Pipelines(title=pipeline.title)
        db_pipeline.steps = [Steps(**step.dict()) for step in pipeline.steps]
        db.add(db_pipeline)
        try:
            await db.commit()
            return db_pipeline
        except IntegrityError as e:
            await db.rollback()
            raise e

    async def get_pipelines(self, db: AsyncSession, skip: int, limit: int) -> ScalarResult[Pipelines]:
        pipelines = await db.execute(
            select(Pipelines).options(joinedload(Pipelines.steps)).offset(skip).limit(limit)
        )
        unique_pipelines = pipelines.unique()
        return unique_pipelines.scalars()

    async def get_pipeline(self, db: AsyncSession, pipeline_id: int) -> Pipelines:
        pipeline = await db.execute(select(Pipelines).options(joinedload(Pipelines.steps)).where(Pipelines.id == pipeline_id))
        return pipeline.scalars().first()

    async def update_pipeline(
            self, db: AsyncSession, pipeline_id: int, pipeline_update: PipelineAdd
    ) -> Pipelines:

        db_pipeline = await self.get_pipeline(db, pipeline_id)
        db_pipeline.title = pipeline_update.title

        existing_steps = db_pipeline.steps

        # Update existing steps
        for i, step in enumerate(pipeline_update.steps):
            if i < len(existing_steps):
                existing_steps[i].title = step.title
                existing_steps[i].step_parameters = step.step_parameters
            else:
                # Add new steps
                existing_steps.append(Steps(**step.dict()))

        db_pipeline.steps = existing_steps

        try:
            await db.commit()
            return db_pipeline
        except IntegrityError as e:
            await db.rollback()
            raise e

    async def delete_pipeline(self, db: AsyncSession, pipeline_id: int) -> Pipelines:
        try:
            db_pipeline = await pipeline_crud.get_pipeline(db, pipeline_id)
            await db.delete(db_pipeline)
            await db.commit()
            return db_pipeline
        except IntegrityError as e:
            await db.rollback()
            raise e


pipeline_crud = PipelineCRUD()
