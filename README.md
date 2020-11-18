# mqtt-subscriber
MQTT Subscriber, a simpel python MQTT client that subscribe to a topic and print the oput to a local file.
You can use this client as test subscriber to check if other ocmponents make publish as expected over an MQTT broker.

## Example
```
docker run --rm \
	--name mqtt-sub \
    -e SERVER_ADDR="remote_host" \
    -e PORT="1883" \
    -e USERNAME="user" \
    -e PASSWORD="password" \
    -e TOPIC="#" \
	massimocallisto/mqtt_subscriber:1.0
```

The subscriber will print the otput on the default file `/opt/mqtt_client.dump` You can map this file locally in order to persist changes and track changes outside the container.


Docker image available at: https://hub.docker.com/r/massimocallisto/mqtt_subscriber
