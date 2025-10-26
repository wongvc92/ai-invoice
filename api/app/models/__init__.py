"""
models package

This package contains all SQLAlchemy model definitions used by the application.
Each model is defined in its own module for clarity and scalability.

The imports below expose all model classes at the package level, so they can be
imported easily elsewhere in the codebase, for example:

    from app.models import User, Invoice

When adding a new model, simply:
1. Create a new file (e.g. `invoice.py`) inside this folder.
2. Define your SQLAlchemy model class inside it.
3. Import it here to make it available globally.

"""

from .user import User
from .invoice import Invoice
# from .receipt import Receipt
# from .transaction import Transaction

# Controls which names are exported when using "from app.models import *"
__all__ = ["User","Invoice"]