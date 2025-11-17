
class BaseHandlerClass:
    def __init__(self, name):
        self.name = name

    def on_message(self, topic:str, message:str):
        print(f"Message received: {topic} -> {message}")
