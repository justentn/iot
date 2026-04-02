from umqtt.simple import MQTTClient
from logger import Logger
from config import MQTT_HOST, MQTT_PORT
import machine

logger = Logger()


class MqttClient:
    """A MQTT client used to communicate sensor data"""

    client: MQTTClient
    uuid: str

    def __init__(self):
        self.uuid = machine.unique_id().hex()
        self.client = None

    def send(self, msg):
        pass

    def try_connect(self):
        try:
            logger.info(
                'MQTTClient',
                f'Attempting to connect to {MQTT_HOST}:{MQTT_PORT}')
            self.client = MQTTClient(self.uuid, MQTT_HOST, int(MQTT_PORT))
            self.client.connect()
            logger.info('MQTTClient', 'Client connected!')
            self.client.ping()
            logger.info('MQTTClient', 'Ping successful!')
        except Exception as e:
            logger.error('MqttClient', f'Failed to connect with {e}')

    def send(self, topic: str, msg: dict):
        if self.client is None:
            logger.error('MqttClient', 'Not connected')
            return
        try:
            import json
            self.client.publish(topic, json.dumps(msg))
            logger.info('MqttClient', f'Published to {topic}')
        except Exception as e:
            logger.error('MqttClient', f'Failed to publish: {e}')
