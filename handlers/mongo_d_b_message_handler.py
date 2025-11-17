from pymongo import MongoClient
from handlers.base_handler import BaseHandlerClass
import datetime
import json


class MongoDBHandler(BaseHandlerClass):
    def __init__(self, name, connection_uri='mongodb://localhost:27017/'):
        super().__init__(name)
        self.client = MongoClient(connection_uri)
        self.db = self.client['mqtt_messages']
        self.collection = self.db['messages']

    def on_message(self, topic: str, message: str):
        try:
            message_json = json.loads(message)
            # message_json['topic'] = topic
            self.collection.insert_one(message_json)
        except json.JSONDecodeError:
            print(f"Error storing message: {message}")
        #
        #document = {
        #    'topic': topic,
        #    'message': message
        #}
        #self.collection.insert_one(document)

