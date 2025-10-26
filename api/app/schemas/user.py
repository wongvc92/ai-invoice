"""
Pydantic schemas for User model.
These define the structure of incoming (request) and outgoing (response) data.

Validation
- Automatically checks incoming data (e.g. email must be valid)
 Separation of concerns
 -Keeps DB layer (SQLAlchemy) separate from API layer
 Security
- Prevents leaking internal fields (like passwords or admin flags)
 Serialization
- Converts SQLAlchemy objects → JSON automatically
 Type safety
- Works perfectly with Python typing + autocomplete


"""

from pydantic import BaseModel, EmailStr
from datetime import datetime

# Shared base fields (used by both Create/Response)
class UserBase(BaseModel):
    name: str
    email: EmailStr

# For user creation (client -> API)
class UserCreate(UserBase):
    password: str

# For responses (API -> client)
class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Enables returning SQLAlchemy objects directly