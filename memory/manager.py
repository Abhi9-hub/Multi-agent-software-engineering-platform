#Decides where to store the memory

from memory.service import MemoryService

class MemoryManger():
    def __init__(self):
        self.memory = MemoryService()
    
    def remember(self, key, value):
        return self.memory.remember(key, value)
    
    def recall(self, key):
        return self.memory.recall(key)

