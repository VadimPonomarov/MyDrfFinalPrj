from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    crated_at: datetime
    updated_at: datetime
