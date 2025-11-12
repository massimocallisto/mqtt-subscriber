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

## Run Locally with `starter.sh`

The repo includes a helper script to run the subscriber locally without Docker.

1) Create and activate a virtual environment (first time only):
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) (Optional) Configure environment via `.env` file. The script will load values from `.env` if present and override defaults:
```
SERVER_ADDR=localhost
PORT=1883
#USERNAME=
#PASSWORD=
TOPIC=#
```

3) Run the script:
```
./starter.sh
```

Notes:
- `starter.sh` activates the `venv` at `venv/bin/activate` and then runs `app.py`.
- You can also export variables in your shell instead of using `.env`.
- Leave `USERNAME`/`PASSWORD` unset if your broker does not require auth.
