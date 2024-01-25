import random
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from model_machine_learning.src.detection_result.crud import result_crud
from app.src.database import get_async_session
from model_machine_learning.src.detection_result.routers import router as router_result

app = FastAPI(
    title="Model Machine Learning"
)


@app.post("/detect_car", tags=["Detected Car"])
async def detect_car(processed_image: str, session: AsyncSession = Depends(get_async_session)):
    # Обработка изображения, прогон через модель машинного обучения
    # Моделируем случайное возвращение координат или пустого ответа с шансом 50/50
    if random.random() < 0.5:
        response = {}  # Пустой ответ
    else:
        # Заготовленные координаты бокса автомобиля
        top_left_x = 100
        top_left_y = 100
        w = 200
        h = 100
        conf = 0.8
        label = 1
        response = {
            "bbox": [top_left_x, top_left_y, w, h, conf, label]
        }
    result_db = await result_crud.add_result(session, processed_image, response)

    return result_db

app.include_router(router_result)
