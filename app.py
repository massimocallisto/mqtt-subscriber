import datetime
import time

import paho.mqtt.client as mqtt
import os
 
server_addr =os.getenv('SERVER_ADDR', "")
port = int(os.getenv('PORT', ""))
username = os.getenv('USERNAME', "")
password = os.getenv('PASSWORD', "")
topic = os.getenv('TOPIC', "")

if topic is None:
    topic = "#"
if username == "-":
    username = None
if password == "-":
    password = None

print("Connecting to %s:%d with %s on topic %s" % (server_addr, port, username, topic))

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


client = mqtt.Client()

if username is not None and password is not None:
    client.username_pw_set(username, password)

client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
