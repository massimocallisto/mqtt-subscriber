from cassandra.cluster import Cluster
from handlers.base_handler import BaseHandlerClass
import json
from datetime import datetime, timezone
import uuid

class CassandraHandler(BaseHandlerClass):
    def __init__(self, name, contact_points=['localhost'], keyspace='mqtt_space'):
        super().__init__(name)
        self.cluster = Cluster(contact_points)
        self.session = self.cluster.connect()
        
        # Create keyspace if not exists
        self.session.execute("""
            CREATE KEYSPACE IF NOT EXISTS mqtt_space
            WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
        """)
        
        self.session.set_keyspace(keyspace)
        
        # Create table if not exists with all fields from the sensor message
        self.session.execute("""
            CREATE TABLE IF NOT EXISTS sensor_data (
                uuid uuid,
                topic text,
                timestamp timestamp,
                tenant_id text,
                installation_id text,
                device_id text,
                pan_id text,
                battery_value double,
                co2 int,
                humidity double,
                pressure double,
                rssi int,
                sensor_type text,
                status text,
                temperature double,
                message_type text,
                presence boolean,
                PRIMARY KEY ((tenant_id, installation_id), timestamp, uuid)
            )
        """)

    def on_message(self, topic: str, message: str):
        try:
            # Parse the JSON message
            data = json.loads(message)
            
            # Prepare the query
            query = """
                INSERT INTO sensor_data (
                    uuid, topic, timestamp, tenant_id, installation_id,
                    device_id, pan_id,
                    battery_value, co2, humidity, pressure, rssi,
                    sensor_type, status, temperature, message_type,
                    presence
                )
                VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s
                )
            """
            
            # Convert timestamp string to datetime
            timestamp = datetime.now() # datetime.fromisoformat(data['tz'].replace('Z', '+00:00'))


            # Execute the query with parameters
            self.session.execute(query, (
                uuid.UUID(data['uuid']),
                topic,
                timestamp,
                data['tenant'],
                data['installation_id'],
                data['id'],
                data['panid'],
                float(data['battery value']),
                int(data['c02']),
                float(data['humidity']),
                float(data['pressure']),
                int(data['rssi']),
                data['sensorType'],
                data['status'],
                float(data['temperature']),
                data['type'],
                bool(data['presence'])
            ))
            
            print(f"Stored sensor data in Cassandra - Topic: {topic}")
            
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON message format")
        except KeyError as e:
            print(f"Error: Missing required field in message: {e}")
        except Exception as e:
            print(f"Error storing message in Cassandra: {e}")

    def close(self):
        self.cluster.shutdown()