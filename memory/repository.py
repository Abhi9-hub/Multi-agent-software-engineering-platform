#Database CRUD operations

from memory.database import SessionLocal
from memory.models import Memory

class MemoryRepository:
    def save(self, role: str, content: str, session_id="local"):

        db = SessionLocal()

        try:

            memory = Memory(
                session_id=session_id,
                role=role,
                content=content
            )

            db.add(memory)
            db.commit()
            db.refresh(memory)

            return memory

        finally:
            db.close()

    def history(self, session_id="local", limit=20):
        db= SessionLocal()

        try:
            return(
                db.query(Memory)
                .filter(Memory.session_id == session_id)
                .order_by(Memory.id.desc())
                .limit(limit)
                .all()
            )
        finally:
            db.close()