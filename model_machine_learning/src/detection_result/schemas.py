from typing import Optional
from pydantic import BaseModel


class ResultAdd(BaseModel):
    """Схема результата детекции"""

    processed_image: str
    is_detected: bool
    top_left_x: Optional[float]
    top_left_y: Optional[float]
    width: Optional[float]
    height: Optional[float]
    confidence: Optional[float]
    label: Optional[int]

    class Config:
        from_attributes = True


class ResultRead(ResultAdd):
    id: Optional[int]

    class Config:
        from_attributes = True
