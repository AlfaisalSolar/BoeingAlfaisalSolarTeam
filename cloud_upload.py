# checking the internet connection
# import requests, time as t

# # url = "http://www.google.com"
# url = "https://hook.ubeac.io/QCDqblDO"
# timeout = 2

# Used to check the network connection
# def net_check():
#   #Used to check the network connection
#   print("Trying to Connect :)")
#   try:
#     request = requests.get(url, timeout=2)
#     print("Connected to the Internet :)")
#     print(request.status_code)
#     send_data()
#   except Exception:
#     re_connect()


# import requests
# import time as t

# url = "http://www.google.com"
# import time as t
# import requests
# timeout = 2
# reconnect_count = 0
# Used to reconnect after loosing connection
# def re_connect():
#   #Used to reconnect after loosing connection
#   global reconnect_count
#   print('Trying to Re-Connect...')
#   try:
#     r = requests.get(url, timeout = 2)
#     connection_status = r.status_code
#     print(connection_status)
#     if(connection_status == 200):
#       print('Connected !')
#       reconnect_count = 0
#       send_data()
#   except Exception:
#     t.sleep(5)
#     if(reconnect_count < 10):
#       reconnect_count += 1
#       re_connect()
#     else:
#       print('Could not Connect :(')

# i = 0
# def send_data():
#   #Used to send data to cloud
#   global i
#   try:
#     while True:
#       querystring = {"foo": ["bar", "baz"]}
#       payload = "{\"foo\": \"bar\"}"
#       headers = {
#           'cookie': "foo=bar; bar=baz",
#           'accept': "application/json",
#           'content-type': "application/json",
#           'x-pretty-print': "2"
#       }
#       response = requests.request(
#           "POST", url, data=payload, headers=headers, params=querystring)
#       print(f'Statuc Code: {response.status_code} = Data sent {i} time(s)')
#       i +=1
#       t.sleep(2)
#   except ConnectionError:
#     print('Connection Lost...')
#     re_connect()
#   except TimeoutError:
#     print('Request wasn Timed out')
#     re_connect()
#   except KeyboardInterrupt:
#     print('Execution Stopped !!!')
#   except Exception as err:
#     print(f'Exception occured: {err}')
#     re_connect()


# THE CODE DOWN IS USED TO SEND DATA TO THE CLOUD

# import random
# import requests
# import time as t

# url = "http://bscpalfaisal.hub.ubeac.io/bscpalfaisal"

# i = 0
# reconnect_count = 0
# timeout = 2
# uid = 'bscpalfaisal'
# voltage = random.randrange(10)
# current = random.randrange(10)
# rpm = random.randrange(10)
# accl = random.randrange(10)
# temp = random.randrange(10)
# def send_data():
#   #Used to send data to cloud
#   global i, reconnect_count, voltage, current, rpm, accl, temp

#   try:
#     print('Trying to connect...')
#     r = requests.get(url, timeout = timeout)
#     connection_status = r.status_code
#     print(connection_status)
#     if(connection_status == 200):
#       print('Connected !')
#       reconnect_count = 0
#       # send_data()
#   except Exception:
#     t.sleep(5)
#     if(reconnect_count < 10):
#       reconnect_count += 1
#       send_data()
#     else:
#       print('Could not Connect :(')

#   try:
#     while True:
#       voltage = random.randrange(100)
#       current = random.randrange(100)
#       rpm = random.randrange(100)
#       accl = random.randrange(100)
#       temp = random.randrange(100)
#       data = {
#           "id": uid,
#           "sensors": [
#           {
#             'id': 'Terminal Voltage',
#             'data': voltage
#           },
#           {
#             'id': 'Terminal Current',
#             'data': current
#           },
#           {
#             'id': 'RPM',
#             'data': rpm
#           },
#           {
#             'id': 'Acceleration',
#             'data': accl
#           },
#           {
#             'id': 'Temp',
#             'data': temp
#           },
#               ]
#       }

#       response = requests.post(url, verify=False, json=data, timeout = timeout)
#       print(f'Status Code: {response.status_code} = Data sent {i} time(s)')
#       i +=1
#       t.sleep(1)
#   except ConnectionError:
#     print('Connection Lost...')
#     send_data()
#   except TimeoutError:
#     print('Request was Timed out')
#     send_data()
#   except KeyboardInterrupt:
#     print('Execution Stopped !!!')
#     exit(0)
#   except Exception as err:
#     print(f'Exception occured while sending data: \n{err}')
#     send_data()


# # Calling the function for sending the data
# send_data()


import cloud_kaa as ck
import random
import time
import paho.mqtt.client as mqtt
import string

# Initiate server connection
# client = mqtt.Client(client_id=''.join(random.choice(
#     string.ascii_uppercase + string.digits) for _ in range(6)), clean_session=False, userdata=None, protocol=mqtt.MQTTv311, transport="websockets")
# client = mqtt.Client()
client = mqtt.Client(client_id=''.join(random.choice(
    string.ascii_uppercase + string.digits) for _ in range(6)))

dcc = ck.DataCollectionClient(client)

# while True:
#     v = random.randrange(1, 3)
#     print('Executing')
#     if v == 1:
#         current = random.randrange(60, 100)
#         voltage = random.randrange(10, 55)
#         power = current * voltage
#         rpm = current + 2000
#     else:
#         current = random.randrange(10, 55)
#         voltage = random.randrange(60, 100)
#         power = current * voltage
#         rpm = current + 1800

#     temp = [voltage, current, rpm, random.randrange(15, 30), random.randrange(
#         30, 50), power, random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100)]

#     # temp = [random.randrange(10, 60), random.randrange(50, 100), random.randrange(2000, 3200), random.randrange(5, 50), random.randrange(100), random.randrange(
#     #     100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100)]

#     ck.values.insert(len(ck.values), temp)
#     response = dcc.get_data(client)

#     print(response)
#     print('Continue outside')
#     time.sleep(1)

##  NOTES  ##

# current nd voltage inversely propotional
# solar cell temp same as car
# solar cell voltages between 3.6V - 3.8V

##  NOTES  ENDS  ##

current = 0  # low = 0 high at 240
voltage = 56.8  # low 38.6 high at 58.5
rpm = 0  # low = 0 high at 120
temp = 33  # low = 33 high  = 45
velocity = 0  # low = 0 high = 130

while range(20):
    print('Executing')

    time.sleep(2)

    while current < 240:
        current += 5
        voltage -= 0.5
        rpm += 40
        temp += 0.25
        power = current*voltage
        velocity += 2.75

        val = [voltage, current, rpm, velocity, temp, power]

        solar_cells = [random.randrange(125, 200), random.randrange(125, 200), random.randrange(
            125, 200), random.randrange(125, 200), random.randrange(125, 200), random.randrange(125, 200),  random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79)]

        # print(random.uniform(3.6, 3.8))

        ck.values.insert(len(ck.values), val)
        ck.solar_cells.insert(len(ck.solar_cells), solar_cells)
        response = dcc.get_data(client)

        print(response)
        print('Continue outside')
        # time.sleep(0.5)

    for i in range(7):
        val = [voltage, current, rpm, velocity, temp, power]

        solar_cells = [random.randrange(125, 200), random.randrange(125, 200), random.randrange(
            125, 200), random.randrange(125, 200), random.randrange(125, 200), random.randrange(125, 200),  random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79)]

        ck.values.insert(len(ck.values), val)
        ck.solar_cells.insert(len(ck.solar_cells), solar_cells)
        response = dcc.get_data(client)

        print(response)
        # print('Continue outside')
        time.sleep(0.3)

    while current > 10:
        current -= 5
        voltage += 0.5
        rpm -= 40
        temp -= 0.25
        power = current*voltage
        velocity -= 2.75

        val = [voltage, current, rpm, velocity, temp, power]

        solar_cells = [random.randrange(125, 200), random.randrange(125, 200), random.randrange(
            125, 200), random.randrange(125, 200), random.randrange(125, 200), random.randrange(125, 200),  random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79)]

        # temp = [random.randrange(10, 60), random.randrange(50, 100), random.randrange(2000, 3200), random.randrange(5, 50), random.randrange(100), random.randrange(
        #     100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100), random.randrange(100)]

        ck.values.insert(len(ck.values), val)
        ck.solar_cells.insert(len(ck.solar_cells), solar_cells)
        response = dcc.get_data(client)

        print(response)
        print('Continue outside')
        # time.sleep(0.5)

    for i in range(5):
        val = [voltage, current, rpm, velocity, temp, power]

        solar_cells = [random.randrange(125, 200), random.randrange(125, 200), random.randrange(
            125, 200), random.randrange(125, 200), random.randrange(125, 200), random.randrange(125, 200),  random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79), random.uniform(3.70, 3.79)]

        ck.values.insert(len(ck.values), val)
        ck.solar_cells.insert(len(ck.solar_cells), solar_cells)
        response = dcc.get_data(client)

        print(response)
        # print('Continue outside')
        time.sleep(0.3)
