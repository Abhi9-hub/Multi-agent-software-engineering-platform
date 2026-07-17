from memory.repository import MemoryRepository

repo = MemoryRepository()

repo.save(
    "language",
    "Python"
)

memory = repo.get("language")

print(memory.key)
print(memory.value)