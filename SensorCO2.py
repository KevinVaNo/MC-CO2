# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 03:07:57 2021

@author: Federico
"""
#import smbus2
#import bme280
import gpiozero
import asyncio
import time
import json
import RPi.GPIO as GPIO
from azure.iot.device.aio import IoTHubDeviceClient

# port = 1
# address = 0x77
# bus = smbus2.SMBus(port)

# calibration_params = bme280.load_calibration_params(bus, address)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

def get_co2():
    data = gpiozero.MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
    return data.value
def get_co2_2():
    data = gpiozero.MCP3008(channel=1, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)
    return data.value

# def get_temp():
#     data = bme280.sample(bus, address, calibration_params)
#     return data.temperature

def handle_twin(twin):
    print("Twin received", twin)
    if ('desired' in twin):
        desired = twin['desired']
        if ('led' in desired):
            GPIO.output(24, desired['led'])

async def main():

    conn_str = "HostName=IoT-CO2.azure-devices.net;DeviceId=Sensor_CO2;SharedAccessKey=/e+CL2RJLvj6FGbmogV6DkKbDAMkSH1RS87+TCl68Bc="
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    await device_client.connect()

    last_temp = ""

    while True:
        t_prev=(get_co2()+get_co2_2())/2
        temp = "{0:0.3f}".format(t_prev)
        print("CO2", temp)

        if temp != last_temp:
            last_temp = temp;

            data = {}
            data['co2'] = temp
            data[]
            json_body = json.dumps(data)
            print("Sending message: ", json_body)
            await device_client.send_message(json_body)

        twin = await device_client.get_twin()
        handle_twin(twin)

        time.sleep(5)

    await device_client.disconnect()



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())