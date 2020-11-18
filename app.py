import paho.mqtt.client as mqtt
import os
 
server_addr =os.environ['SERVER_ADDR']
port = int(os.environ['PORT'])
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
topic = os.environ['TOPIC']

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
    print(msg.payload.decode())
    f = open("mqtt_client.dump", "w")
    f.write(msg.payload.decode())
    f.close()
    
client = mqtt.Client()

if username is not None and password is not None:
    client.username_pw_set("user", "user")

client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()