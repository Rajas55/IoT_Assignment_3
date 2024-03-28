import network
import time
import urandom
from umqtt.simple import MQTTClient

broker_client_id = "HBcePSk7BhkCBxM9KDs2DSY"
broker_user = "HBcePSk7BhkCBxM9KDs2DSY"
broker_password = "h0WuyMoePagwXN38JfDJkUzJ"
broker_host = "mqtt3.thingspeak.com"
broker_port = 1883
topic_temp = "channels/2486696/publish/fields/field1"
topic_hum = "channels/2486696/publish/fields/field2"
topic_co2_level = "channels/2486696/publish/fields/field3"

network_name = "Wokwi-GUEST"
network_password = ""

def create_sensor_values():
    temp_value = urandom.uniform(-50, 50)
    hum_value = urandom.uniform(0, 100)
    co2_value = urandom.uniform(300, 2000)
    return temp_value, hum_value, co2_value

def send_to_broker(temp, hum, co2):
    mqtt_client = MQTTClient(broker_client_id, broker_host, user=broker_user, password=broker_password)
    mqtt_client.connect()
    mqtt_client.publish(topic_temp, str(temp))
    mqtt_client.publish(topic_hum, str(hum))
    mqtt_client.publish(topic_co2_level, str(co2))
    mqtt_client.disconnect()

wifi_interface = network.WLAN(network.STA_IF)
wifi_interface.active(True)
wifi_interface.connect(network_name, network_password)

while not wifi_interface.isconnected():
    pass

print("Connected to Wi-Fi")

while True:
    temp, hum, co2 = create_sensor_values()
    send_to_broker(temp, hum, co2)
    print("Published: Temperature={:.2f}C, Humidity={:.2f}%, CO2={:.2f}ppm".format(temp, hum, co2))
    time.sleep(10)
