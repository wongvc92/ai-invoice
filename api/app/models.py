from sqlalchemy import String, Integer, DateTime, JSON, func
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    file_name: Mapped[str] = mapped_column(String(255))
    vendor_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    total_cents: Mapped[int | None] = mapped_column(Integer, nullable=True)
    raw_ocr: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())