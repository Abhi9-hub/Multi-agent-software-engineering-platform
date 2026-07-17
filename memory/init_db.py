from memory.database import engine
from memory.models import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("Memory table created.")
