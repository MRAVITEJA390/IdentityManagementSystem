from datetime import datetime
from models import Precedence
from pydantic import BaseModel


class ContactBase(BaseModel):
    phone_no: str | None = None
    email: str | None = None
    linked_id: int
    link_precedence: Precedence
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
