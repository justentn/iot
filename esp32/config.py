import json
from lib.gpio.constants import *
from lib.gpio.pin_wrapper import PinWrapper


def load_config():
    with open('config.json') as f:
        return json.load(f)


config = load_config()

WIFI_SSID = config['wifi']['ssid']
WIFI_PASSWORD = config['wifi']['password']
API_URL = config['api']['url']

PINS = [
    PinWrapper(p['id'], p['type'])
    for p in config['pins']
]
