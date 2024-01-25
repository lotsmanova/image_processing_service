from pydantic import BaseModel
from typing import List, Optional


class StepBase(BaseModel):
    """Схема шагов паплайна"""

    title: str
    step_parameters: str

    class Config:
        from_attributes = True


class StepRead(StepBase):
    """Схема шагов паплайна"""

    step_id: Optional[int]


class PipelineRead(BaseModel):
    """Схема паплайна"""

    id: int
    title: str
    steps: List[StepRead]

    class Config:
        from_attributes = True


class PipelineAdd(BaseModel):
    """Схема паплайна"""

    title: str
    steps: List[StepBase]

    class Config:
        from_attributes = True
