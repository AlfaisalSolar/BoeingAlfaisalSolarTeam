import json
import signal
import string
import paho.mqtt.client as mqtt
import time as t
import random
import json
# import requests
# import itertools
# import queue
# import sys


# # KAA IOT CLOUD CODE
KPC_HOST = "mqtt.cloud.kaaiot.com"  # Kaa Cloud plain MQTT host
KPC_PORT = 1883  # Kaa Cloud plain MQTT port

ENDPOINT_TOKEN = "bscpalfaisal"       # Paste endpoint token
APPLICATION_VERSION = "c7kj63srchg10iv8g2j0-ausolarcar"
# Paste application version # Token from Amaan's account on Kaa Cloud
#APPLICATION_VERSION = "c10e472rqa51q5h5o5tg-v1"


values = [[0, 0, 0, 0, 0, 0],
          [5, 5, 5, 5, 5, 5]]

voltage, current, rpm, velocity, temp, power, rpmGraph = 5, 5, 5, 5, 5, 5, 5

solar_cell1, solar_cell2, solar_cell3, solar_cell4, solar_cell5, solar_cell6, sc1_temp, sc1_volt, sc2_temp, sc2_volt, sc3_temp, sc3_volt, sc4_temp, sc4_volt, sc5_temp, sc5_volt, sc6_temp, sc6_volt = 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5


solar_cells = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
]


# !!!!!!!!!!!!!!!!!!KAA HTTP IMPLIMENTATION !!!!!!!!!!!!!!!!!!!!

# url = 'https://connect.cloud.kaaiot.com:443/kp1/c10e472rqa51q5h5o5tg-v1/dcx/bscpalfaisal/json'
# value = [
#     {
#         "voltage": 0,
#         "current": 0,
#         "rpm": 0,
#         "velocity": 0,
#         "temp": 0,
#         "power": 0
#     },
# ]

# def get_data(voltage, current, rpm, velocity, temp, power):
#     temp_values = [voltage, current, rpm, velocity, temp, power]
#     x = {
#         "voltage": voltage,
#         "current": current,
#         "rpm": rpm,
#         "velocity": velocity,
#         "temp": temp,
#         "power": power,
#     }
#     values.insert(len(values), temp_values)
#     # sending()
#     return 'DATA HAS BEEN ENTERED !!!'

# def sending():
#     data = {
#         "voltage": values[0][0],
#         "current": values[0][1],
#         "rpm": values[0][2],
#         "velocity": values[0][3],
#         "temp": values[0][4],
#         "power": values[0][5]
#     }
#     try:
#         res = requests.post(url, verify=True, json= data, timeout=4)
#         print(res.status_code)

#         print(data)
#         # del value[0]
#         # del value[1]
#         # del value[2]
#         del values[0]
#         # print(res.status_code)

#     except Exception as e:
#         print(e)

# !!!!!!!!!!!!!!!!!!KAA HTTP IMPLIMENTATION END!!!!!!!!!!!!!!!!!!!!

# data = {
#     # 'Terminal Voltage': voltage,
#     # 'Terminal Current': current,
#     # 'RPM': rpm,
#     # 'Velocity': velocity,
#     # 'Temp': temp
#     # }

# !!!!!!!!!!!!!!!!!! KAA IMPLIMENTATION FOR MQTT !!!!!!!!!!!!!!!!1

connected = 0


class DataCollectionClient:
    global values

    def __init__(self, client):
        self.client = client
        self.data_collection_topic = f'kp1/{APPLICATION_VERSION}/dcx/{ENDPOINT_TOKEN}/json'

    def connect_to_server(self):
        print(
            f'Connecting to Kaa server at {KPC_HOST}:{KPC_PORT} using application version {APPLICATION_VERSION} and endpoint token {ENDPOINT_TOKEN}')
        self.client.connect(KPC_HOST, KPC_PORT, 60)
        print('Successfully connected')
        self.client.loop_start()
        global connected
        connected = 1

    def disconnect_from_server(self):
        print(f'Disconnecting from Kaa server at {KPC_HOST}:{KPC_PORT}...')
        self.client.loop_stop()
        self.client.disconnect()
        print('Successfully disconnected')
        global connected
        connected = 0

    def compose_data_sample(self):
        return json.dumps({
            "voltage": values[0][0],
            "current": values[0][1],
            "rpm": values[0][2],
            "velocity": values[0][3],
            "temp": values[0][4],
            "power": values[0][5],
            "rpm_times_100": (values[0][2]/100),
            "Solar_Cell_1": solar_cells[0][0],
            "Solar_Cell_2": solar_cells[0][1],
            "Solar_Cell_3": solar_cells[0][2],
            "Solar_Cell_4": solar_cells[0][3],
            "Solar_Cell_5": solar_cells[0][4],
            "Solar_Cell_6": solar_cells[0][5],
            "sc1_T": values[0][4]-2.7,  # solar_cells[0][6],
            "sc1_V": solar_cells[0][6],
            "sc2_T": values[0][4]-2.5,  # solar_cells[0][8],
            "sc2_V": solar_cells[0][7],
            "sc3_T": values[0][4]-1.9,  # solar_cells[0][10],
            "sc3_V": solar_cells[0][8],
            "sc4_T": values[0][4]-2.9,  # solar_cells[0][12],
            "sc4_V": solar_cells[0][9],
            "sc5_T": values[0][4]-2.88,  # solar_cells[0][14],
            "sc5_V": solar_cells[0][10],
            "sc6_T": values[0][4]-2.3,  # solar_cells[0][16],
            "sc6_V": solar_cells[0][11]
        })

    # voltage, current, rpm, velocity, temp, power):
    def get_data(self, client):
        # temp_values = [voltage, current, rpm, velocity, temp, power]
        global connected
        if connected == 0:
            self.connect_to_server()
        self.main()
        return 'DATA HAS BEEN ENTERED !!!'

    def on_message(self, client, userdata, message):
        print(
            f'<-- Received message on topic "{message.topic}":\n{str(message.payload.decode("utf-8"))}')

    def main(self):
        # # Initiate server connection
        # client = mqtt.Client(client_id=''.join(random.choice(
        #     string.ascii_uppercase + string.digits) for _ in range(6)))

        # data_collection_client = DataCollectionClient(client)
        # data_collection_client.connect_to_server()
        self.client.on_message = self.on_message

        # Start the loop
        # client.loop_start()

        # Send data samples in loop
        listener = SignalListener()
        if listener.keepRunning:

            payload = self.compose_data_sample()

            try:
                result = self.client.publish(
                    topic=self.data_collection_topic, payload=payload, retain=True)
                if result.rc != 0:
                    print('Server connection lost, attempting to reconnect')
                    self.connect_to_server()
                else:
                    print(
                        f'--> Sent message on topic "{self.data_collection_topic}":\n{payload}')
                    del values[0]
                    del solar_cells[0]
                    # update = False

                t.sleep(0.15)
            except KeyboardInterrupt:
                quit
            # except ConnectionError:
            #     mqtt.reinitialize()
            except Exception as e:
                print('There was an error: ', e)


class SignalListener:
    keepRunning = True

    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

    def stop(self, signum, frame):
        print('Shutting down...')
        self.keepRunning = False


# if __name__ == '__main__':
#     main()

# !!!!!!!!!!!!!!!!!! KAA IMPLIMENTATION FOR MQTT END!!!!!!!!!!!!!!!!
