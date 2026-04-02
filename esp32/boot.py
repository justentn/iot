import network
from config import WIFI_SSID, WIFI_PASSWORD


def connect_wifi(ssid, password):
    """ Connects the device to the wifi network.

    Args:
        ssid: The name of the network to connect to.
        password: Password used for authentication
    """

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('WiFi connected:', wlan.ifconfig())


connect_wifi(WIFI_SSID, WIFI_PASSWORD)
