# Wi-Fi Sensor Data Publisher to ThingSpeak

This Python script enables a device to connect to a Wi-Fi network, simulate sensor data for temperature, humidity, and CO2 levels, and publish the data to a ThingSpeak channel using MQTT.

## Features

- **Wi-Fi Connection**: Utilizes a predefined SSID and password for network connectivity.
- **Random Sensor Data Generation**:
  - **Temperature**: Simulates temperature readings in °C.
  - **Humidity**: Simulates humidity readings in %.
  - **CO2 Concentration**: Simulates CO2 levels in ppm.
- **MQTT Publishing**: Sends sensor data to a ThingSpeak channel via MQTT.
- **Continuous Publishing**: Data is published at 10-second intervals.

## Requirements

- A device capable of running Python scripts and connecting to Wi-Fi.
- Network access to the MQTT broker at `mqtt3.thingspeak.com`.

## Setup

1. **Prepare Your Device**: Ensure your device is Wi-Fi capable and has Python installed.
2. **Configure Wi-Fi**: Replace `WIFI_SSID` and `WIFI_PASSWORD` in the script with your actual Wi-Fi credentials.
3. **MQTT Broker Configuration**: If different from the defaults, configure the following:
   - MQTT Client ID
   - MQTT User
   - MQTT Password
   - MQTT Server (`mqtt3.thingspeak.com` by default)
   - MQTT Port (`1883` by default)
4. **ThingSpeak Channel Setup**:
   - Set up your ThingSpeak channel and note the channel ID and Write API Key.
   - Update `mqtt_topic_temperature`, `mqtt_topic_humidity`, and `mqtt_topic_co2` variables with your channel's specifics.

## Usage

Run the script using a Python interpreter. The device will automatically connect to the Wi-Fi network and begin publishing simulated sensor data to the configured ThingSpeak channel.

## Note

This script uses random values for sensor data simulation and is intended for testing purposes. For a production environment, replace the `generate_sensor_data()` function with actual sensor readings from physical sensors.

