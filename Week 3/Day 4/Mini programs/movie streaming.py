import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            logging.info(f"Creating new {cls.__name__} instance")
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class StreamingDB:
    def __init__(self, connection):
        self.connection = connection

db1 = StreamingDB("server1")
db2 = StreamingDB("server2")
print(db1 is db2)
