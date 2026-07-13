from memory.database import engine

try:
    with engine.connect() as conn:
        print("Db connected successfully!")
except Exception as e:
    print("Connection Failed!")
    print(e)