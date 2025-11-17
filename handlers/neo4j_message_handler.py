from neo4j import GraphDatabase
from handlers.base_handler import BaseHandlerClass

class Neo4jHandler(BaseHandlerClass):
    def __init__(self, name, uri='bolt://localhost:7687', username='neo4j', password='password'):
        super().__init__(name)
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def on_message(self, topic: str, message: str):
        with self.driver.session() as session:
            # Create nodes and relationships
            session.execute_write(self._create_message_node, topic, message)
        print(f"Stored in Neo4j - Topic: {topic}, Message: {message}")

    def _create_message_node(self, tx, topic, message):
        # Create topic node if not exists
        query = """
        MERGE (t:Topic {name: $topic})
        CREATE (m:Message {content: $message, timestamp: datetime()})
        CREATE (m)-[:BELONGS_TO]->(t)
        """
        tx.run(query, topic=topic, message=message)

    def close(self):
        self.driver.close()
