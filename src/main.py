import base64
from typing import Dict, Union
import cv2
import numpy as np
from fastapi import FastAPI, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.pipeline.crud import pipeline_crud
from src.pipeline.routers import router as router_pipeline


app = FastAPI(
    title="Image Processing Service"
)

app.include_router(router_pipeline)


@app.post("/process_image", tags=["Process Image"], response_model=Union[Dict[str, str], str])
async def process_image(pipeline_id: int, image: UploadFile = File(...), session: AsyncSession = Depends(get_async_session)) -> \
dict[str, str] | str:
    try:
        # Получаем пайплайн из базы данных
        pipeline = await pipeline_crud.get_pipeline(session, pipeline_id)
        if not pipeline:
            raise ValueError(f"Pipeline with id {pipeline_id} does not exist.")

        # Загружаем изображение
        image_bytes = await image.read()

        # Проходим по всем шагам пайплайна
        for step in pipeline.steps:
            if step.title == 'convert_to_numpy':
                image_np = np.frombuffer(image_bytes, dtype=np.uint8)
            elif step.title == 'read_with_opencv':
                image_cv2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
            elif step.title == 'resize':
                resized_image = cv2.resize(image_cv2, (640, 640))
            elif step.title == 'normalize':
                normalized_image = cv2.normalize(resized_image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            elif step.title == 'encode_to_base64':
                _, encoded_image = cv2.imencode('.jpg', normalized_image)
                base64_image = base64.b64encode(encoded_image.tobytes()).decode('utf-8')
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await image.close()

    return base64_image
