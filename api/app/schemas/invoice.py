"""
Pydantic schemas for Invoice model.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class InvoiceBase(BaseModel):
    file_name: str
    vendor_name: Optional[str] = None
    total_cents: Optional[int] = None
    raw_ocr: Optional[Dict] = None

class InvoiceCreate(InvoiceBase):
    pass  # same as base for now, but you can add extra validation later

class InvoiceResponse(InvoiceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True