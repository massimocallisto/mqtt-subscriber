from redis import Redis
from handlers.base_handler import BaseHandlerClass

class RedisHandler(BaseHandlerClass):
    def __init__(self, name, host='localhost', port=6379):
        super().__init__(name)
        self.redis_client = Redis(host=host, port=port, decode_responses=True)

    def on_message(self, topic: str, message: str):
        # Using topic as key and message as value
        self.redis_client.set(topic, message)
        # Optionally set expiration (e.g., 24 hours)
        self.redis_client.expire(topic, 86400)
        print(f"Stored in Redis - Key: {topic}, Value: {message}")