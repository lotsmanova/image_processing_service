from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.src.database import Base


class Result(Base):
    """Модель результата детекции"""

    __tablename__ = "detection_result"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    processed_image: Mapped[str] = mapped_column()
    is_detected: Mapped[bool] = mapped_column()
    top_left_x: Mapped[float] = mapped_column(nullable=True)
    top_left_y: Mapped[float] = mapped_column(nullable=True)
    width: Mapped[float] = mapped_column(nullable=True)
    height: Mapped[float] = mapped_column(nullable=True)
    confidence: Mapped[float] = mapped_column(nullable=True)
    label: Mapped[int] = mapped_column(nullable=True)
