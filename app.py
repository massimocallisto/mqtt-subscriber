import datetime

import paho.mqtt.client as mqtt
import os

from handlers.base_handler import BaseHandlerClass
from handlers.cassandra_database_handler import CassandraHandler
from handlers.mongo_d_b_message_handler import MongoDBHandler
from handlers.neo4j_message_handler import Neo4jHandler
from handlers.redis_message_handler import RedisHandler

server_addr =os.getenv('SERVER_ADDR', "")
port = int(os.getenv('PORT', ""))
username = os.getenv('USERNAME', "")
password = os.getenv('PASSWORD', "")
topic = os.getenv('TOPIC', "")
handler_type = os.getenv('HANDLER', "console")

if topic is None:
    topic = "#"
if username == "-":
    username = None
if password == "-":
    password = None

print("Connecting to %s:%d with %s on topic %s" % (server_addr, port, username, topic))


# Choose one of the handlers:
if handler_type == "basic":
    handler = BaseHandlerClass("basic")
elif handler_type == "redis":
    handler = RedisHandler("redis_handler")
elif handler_type == "mongodb":
    handler = MongoDBHandler("mongodb_handler")
elif handler_type == "cassandra":
    handler = CassandraHandler("cassandra_handler")
elif handler_type == "neo4j":
    handler = Neo4jHandler("neo4j_handler")
else:
    handler = BaseHandlerClass("basic")


#print(f'{username} home directory is {home_dir}')

# This is the Subscriber
#hostname
broker=server_addr #"bthermalappliance.westeurope.cloudapp.azure.com"
#port
port=1883
#time to live
timelive=60
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(topic)

def on_message(client, userdata, msg):
    print("***** " + datetime.datetime.now().isoformat())
    print(f"topic: {msg.topic}\nmessage:\n {msg.payload.decode()}")
    if handler is not None:
        handler.on_message(topic=msg.topic, message=msg.payload.decode())


client = mqtt.Client()

if username is not None and password is not None:
    client.username_pw_set(username, password)

client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
