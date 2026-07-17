#SQLAlchemy ORM Models

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Memory(Base):
    __tablename__ = "memory"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), default="local")
    content= Column(Text)
    role = Column(String(50))
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )