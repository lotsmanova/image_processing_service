from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.src.database import Base


class Pipelines(Base):
    """Модель паплайнов"""

    __tablename__ = "pipeline"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    title: Mapped[str] = mapped_column()

    steps = relationship("Steps", back_populates="pipeline")


class Steps(Base):
    """Модель шагов паплайна"""

    __tablename__ = "step"

    step_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    step_parameters: Mapped[str] = mapped_column()

    pipeline_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("pipeline.id"), nullable=True)
    pipeline = relationship("Pipelines", back_populates="steps")
