"""
schemas package

This package contains all Pydantic schema definitions used by the application.
Schemas (also known as DTOs or serializers) define the structure and validation
of data exchanged through the API.

Each model in `app/models` typically has a matching schema module here.

Example usage:
    from app.schemas import UserCreate, UserResponse

When adding a new schema:
1. Create a new file (e.g. `invoice.py`) inside this folder.
2. Define your Pydantic models there.
3. Import them below to make them available at the package level.
"""

from .user import UserBase, UserCreate, UserResponse

__all__ = [
    "UserBase",
    "UserCreate",
    "UserResponse",
]