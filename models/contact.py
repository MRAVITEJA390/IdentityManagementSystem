import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime

from database import Base


class Precedence(enum.Enum):
    primary = 1
    secondary = 2


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    phone_no = Column(String, nullable=True)
    email = Column(String, nullable=True)
    linked_id = Column(Integer, nullable=True)
    link_precedence = Column(Enum(Precedence))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime, nullable=True)
