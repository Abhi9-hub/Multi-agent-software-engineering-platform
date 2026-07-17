from memory.service import MemoryService

memory = MemoryService()

memory.remember(
    "user",
    "Build a calculator"
)

memory.remember(
    "assistant",
    "Calculator generated successfully"
)

history = memory.history()

for item in history:
    print(item.role, ":", item.content)