#Memory Business Logic
from memory.repository import MemoryRepository

class MemoryService:
    def __init__(self):
        self.repository = MemoryRepository()

    def remember(self, role, content, session_id="local"):

        print(f"[Memory] {role}: {content}")

        return self.repository.save(
            role=role,
            content=content,
            session_id=session_id
        )

    def history(self, session_id="local", limit=20):

        return self.repository.history(
            session_id=session_id,
            limit=limit
        )