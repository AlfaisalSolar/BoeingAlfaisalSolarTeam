# 
# Receiving CAN messages from two DUEs to RPI V3 by Dr. Ahmed Oteafy 07/12/2020
import os
import can
import struct
import numpy as np
import tkinter as tk
from tkinter import scrolledtext
import tk_tools
from tkinter import Label
import error_reader
# import random
# import requests
# import time as t
from cloud_update import get_data 

mwin=tk.Tk() # Main Window for GUI Add mwin.mainloop() at the end of the code
#mwin.attributes('-fullscreen',True) # However this does not even show the title bar Alt+F4 to close it
#mwin.attributes('-zoomed',True) # keeps the title bar
mwin.geometry('1000x500')
mwin.title("BSCP Driver Interface")
mwin.configure(bg="grey")

# Define CAN Message IDs
msgID_mot=7
msgID_bat=9

# Note: A tkinter window requires either .mainloop() which is a blocking function
# or .update() which is not blocking. These are necessary to keep track of events and update
# the window, such as button clicks. So either use threading with .mainloop() if it is
# necessary to keep track of events quickly, or keep updating with .update() in your active
# loop. Without either options, you do not have a window! The latter solution is used here.

#labelT=tk.Label(text="Driver Interface GUI for AU-BSCP",relief=tk.RAISED,font=("Courier",24),fg="black",bg="silver",width=40,height=2)
#labelT.place(x=50, y=5) 
#labelT.place(relx=0.5, rely=0.1, anchor="n") #coordinates relative to the width and height of the window
# and anchored at the north of the label block

labelTxtBxM=tk.Label(text="Incoming Motor Messages",font=("Courier",12),relief=tk.RAISED,fg="black",bg="silver",width=25,height=1)
labelTxtBxM.place(relx=0.85, rely=0.45, anchor="n")
TxtBxM=scrolledtext.ScrolledText(mwin,wrap=tk.WORD,relief=tk.SUNKEN,width=30,height=6, font=("Times New Roman",12))
TxtBxM.place(relx=0.85, rely=0.50, anchor="n")
TxtBxM.insert(tk.INSERT,"No Incoming Data   \n")
TxtBxM.delete(1.0,tk.END) # Use this to delete the text in the scrolled textbox

gg_rpm=tk_tools.Gauge(mwin,min_value=-1,max_value=3000.0, width=00, height=00,
                      yellow=70, red=90, yellow_low=0, red_low=0, divisions=10,
                      label='Motor RPM', unit='rpm', bg='silver')
# e.g., yellow=80, means yellow range starts at 80% of 10000 - 5000 = 3000 rpm
# yellow_low is where the negative range of yellow starts 20% of 10000 - 5000= -3000 rpm
gg_rpm.place(relx=0.4, rely=0.3, anchor="n")
gg_rpm.set_value(0)

gg_kph=tk.Label(mwin,text="0 Kph")
gg_kph.config(font=('Times New Roman',90))
gg_kph.place(relx=0.25, rely=0.0, anchor="n")
#gg_kph.set_value(0) #You cant set value for a label of course.

#gg_VtM=tk_tools.Gauge(mwin,min_value=0.0,max_value=100.0, width=200, height=100,yellow=50, red=60, yellow_low=20, red_low=10, divisions=10,label='Motor Voltage', unit='V', bg='silver')
#gg_VtM.place(relx=0.6, rely=0.00, anchor="n")
#gg_VtM.set_value(0)

#gg_ItM=tk_tools.Gauge(mwin,min_value=-300.0,max_value=300.0, width=200, height=100,yellow=80, red=90, yellow_low=20, red_low=10, divisions=10,label='Motor Current', unit='A', bg='silver')
#gg_ItM.place(relx=0.6, rely=0.20, anchor="n")
#gg_ItM.set_value(0)

#plt_VtM=tk_tools.Graph()

label_led_ComStatM=tk.Label(text="Comm\nStatM",font=("Courier",12),relief=tk.RAISED,fg="black",bg="silver",width=5,height=2)
label_led_ComStatM.place(relx=0.6, rely=0.65, anchor="n")
led_ComStatM=tk_tools.Led(mwin, size=28)
led_ComStatM.place(relx=0.685, rely=0.65, anchor="n")

led_ComStatM.to_red(on=True)

#label_led_MotStat=tk.Label(text="Motor\nStat",font=("Courier",12),relief=tk.RAISED,fg="black",bg="silver",width=5,height=2)
#label_led_MotStat.place(relx=0.575, rely=0.75, anchor="n")
#led_MotStat=tk_tools.Led(mwin, size=28)
#led_MotStat.place(relx=0.625, rely=0.75, anchor="n")
#led_MotStat.to_red(on=True)

# Battery GUI components
gg_Pwr=tk.Label(mwin,text="0 W")
gg_Pwr.config(font=('Times New Roman',50))
gg_Pwr.place(relx=0.2, rely=0.60, anchor="n")

gg_VtB=tk.Label(mwin,text="0 V")
gg_VtB.config(font=('Times New Roman',50))
gg_VtB.place(relx=0.625, rely=0.00, anchor="n")

gg_ItB=tk.Label(mwin,text="0 A")
gg_ItB.config(font=('Times New Roman',90))
gg_ItB.place(relx=0.2, rely=0.3, anchor="n")

label_led_ComStatB=tk.Label(text="Comm\nStatB",font=("Courier",12),relief=tk.RAISED,fg="black",bg="silver",width=5,height=2)
label_led_ComStatB.place(relx=0.6, rely=0.45, anchor="n")
led_ComStatB=tk_tools.Led(mwin, size=28)
led_ComStatB.place(relx=0.685, rely=0.45, anchor="n")

led_ComStatB.to_red(on=True)

#label_led_BatStat=tk.Label(text="Batt\nStat",font=("Courier",12),relief=tk.RAISED,fg="black",bg="silver",width=5,height=2)
#label_led_BatStat.place(relx=0.575, rely=0.55, anchor="n")
#led_BatStat=tk_tools.Led(mwin, size=28)
#led_BatStat.place(relx=0.625, rely=0.55, anchor="n")
#led_BatStat.to_red(on=True)

labelTxtBxB=tk.Label(text="Incoming Battery Messages",font=("Courier",12),relief=tk.RAISED,fg="black",bg="silver",width=25,height=1)
labelTxtBxB.place(relx=0.85, rely=0.00, anchor="n")
TxtBxB=scrolledtext.ScrolledText(mwin,wrap=tk.WORD,relief=tk.SUNKEN,width=30,height=6, font=("Times New Roman",12))
TxtBxB.place(relx=0.85, rely=0.05, anchor="n")
TxtBxB.insert(tk.INSERT,"No Incoming Data \n")
TxtBxB.delete(1.0,tk.END) # Use this to delete the text in the scrolled textbox

flag_keep_connect=True

os.system('sudo ip link set can0 type can bitrate 250000')
os.system('sudo ifconfig can0 up')

#can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native
#msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native

# 8 bytes of data can be sent in a regular CAN frame
# Let us define the variables as following for a motor data example:
D_flag_ComStatM=True # A flag to maintain CAN communication or terminate it.
D_flag_MotStat=False # The motor status is on or off

D_rpm=0 # The rpm of the motor as a short int (2 bytes) can go from about -32000 to 32000
# def getRpm():
#     return random.randrange(50)

D_VtM=0 # The terminal voltage of the motor, will be received as a short int (2 bytes)
#and then converted in this code to a float by dividing by 100, i.e., V is sent in 10's of mV
# def getTerminalVoltage():
#      return random.randrange(50)

D_ItM=0 # The terminal current will be received as a short int in 10's of mA
#and then converted in this code to a float by dividing by 10                           0
# def getTerminalCurrent():
#      return random.randrange(50)

mwin.update()
#mwin.mainloop()

# url = "http://bscpalfaisal.hub.ubeac.io/bscpalfaisal"
# i = 0
# reconnect_count = 0
# timeout = 2
# uid = 'bscpalfaisal'
# # voltage = random.randrange(10)
# # current = random.randrange(10)
# # rpm = random.randrange(10)
# # accl = random.randrange(50)
# # temp = random.randrange(50)

# def send_data(update):
#   #Used to send data to cloud
#   global i, reconnect_count, voltage, current, rpm, accl, temp
#   t.sleep(2)
  
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
#     while update:
#       t.sleep(1)
#       voltage = int(getBatteryVoltage())
#       current = int(getBatteryCurrent())
#       rpm = int(getRpm())
#       velocity = int(getVelocity())
#       temp = int(getBatteryTemp())
#       power = int(getBatteryPower())
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
#             'id': 'Velocity',
#             'data': velocity
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
# #      t.sleep(1)
#       update = False
#   except ConnectionError:
#     print('Connection Lost...')
#     send_data(True)
#   except TimeoutError:
#     print('Request was Timed out')
#     send_data(True)
#   except KeyboardInterrupt:
#     print('Execution Stopped !!!')
#     exit(0)
#   except Exception as err:
#     print(f'Exception occured while sending data: \n{err}')
#     send_data(True)

# send_data()

velo = 0

while flag_keep_connect: # Disconnect if no one is talking for 10s
    msg = can0.recv(100000.0) # I.e., receive any message
    #print(msg.arbitration_id==msgID_mot)

    if msg is None:
        TxtBxM.insert(tk.INSERT,"Timeout occurred, no message \n")
        print('Timeout occurred, no message.')
        flag_keep_connect=False
        led_ComStatM.to_red(on=True)
    elif (msg.arbitration_id==msgID_mot):
        D_flag_ComStatM=bool(msg.data[0]) 
        D_flag_MotStat=bool(msg.data[1])
        D_rpm_high=msg.data[2].to_bytes(1,'big')
        D_rpm_low=msg.data[3].to_bytes(1,'big')
        D_rpm=np.int16((ord(D_rpm_high) << 8) + ord(D_rpm_low))
        D_rpm = D_rpm
        D_VtM_high=msg.data[4].to_bytes(1,'big')
        D_VtM_low=msg.data[5].to_bytes(1,'big')
        D_VtM=np.int16((ord(D_VtM_high) << 8) + ord(D_VtM_low))
        VtM=D_VtM/100.0; # Convert back to V from 10s of mV
        D_ItM_high=msg.data[6].to_bytes(1,'big')
        D_ItM_low=msg.data[7].to_bytes(1,'big')
        D_ItM=np.int16((ord(D_ItM_high) << 8) + ord(D_ItM_low))
        ItM=D_ItM/100.0; # Convert back to A from 10s of mA
        
        gg_rpm.set_value(float(D_rpm))# cast as float or int since it is int16,
        #which isn't recognized by the guage set_value function
        # Note: If D_rpm> MAX Value then the display needle is frozen
        #gg_VtM.set_value(float(VtM))
        #gg_ItM.set_value(float(ItM))
#        global velos
        velo = (((D_rpm*0.104719755)/3.522)*0.27)*3.6
        def set_gg_kph(velo):   #This method should enable the gg_kph label to change numbers(speed should update)
            gg_kph.config(text="({0:.1f})".format(velo)+"Kph")
            
        set_gg_kph(float(velo))    #gg_kph.set_value(float(velo)) #this is used for the guage constr. It updates the speed, but got changed becuase there is no guage anymore. It's a label
                        
        TxtBxM.insert(tk.INSERT,"flag_ComStatM=",tk.INSERT,D_flag_ComStatM,tk.INSERT,"\n")
        TxtBxM.insert(tk.INSERT,"flag_MotStat=",tk.INSERT,D_flag_MotStat,tk.INSERT,"\n")
        TxtBxM.insert(tk.INSERT,"n=",tk.INSERT,D_rpm,tk.INSERT,"rpm \n")
        TxtBxM.insert(tk.INSERT,"VtM=",tk.INSERT,VtM,tk.INSERT,"V \n")
        TxtBxM.insert(tk.INSERT,"ItM=",tk.INSERT,ItM,tk.INSERT,"A \n")
        TxtBxM.insert(tk.INSERT,"Velocity=",tk.INSERT,velo,tk.INSERT,"Kph \n")
        TxtBxM.see("end") # Moves the text box to the end to show the latest data
            
        if D_flag_ComStatM:
            led_ComStatM.to_green(on=True)
        else:
            led_ComStatM.to_red(on=True)
        
#        if D_flag_MotStat:
#            led_MotStat.to_green(on=True)
#        else:
#            led_MotStat.to_red(on=True)

        # Also print in terminal window
        print("D_flag_ComStatM=",D_flag_ComStatM)
        print("D_flag_MotStat=",D_flag_MotStat)
        print("D_rpm=",D_rpm)
        print("VtM=",VtM,"V")
        print("ItM=",ItM,"A")
        if D_flag_ComStatM==False: # End transmission
            TxtBxM.insert(tk.INSERT,"Received terminating message \n")
            TxtBxM.see("end") # Moves the text box to the end to show the latest data
            print("Received terminating message")
            #flag_keep_connect=False
    elif (msg.arbitration_id==msgID_bat):
        print("I'm Here!")
        CAN_vBat_High=msg.data[0].to_bytes(1,'big')
        CAN_vBat_Low=msg.data[1].to_bytes(1,'big')
        CAN_vBat=np.int16((ord(CAN_vBat_High) << 8) + ord(CAN_vBat_Low))
        vBat=CAN_vBat/100.0;
        CAN_iBat_High=msg.data[2].to_bytes(1,'big')
        CAN_iBat_Low=msg.data[3].to_bytes(1,'big')
        CAN_iBat=np.int16((ord(CAN_iBat_High) << 8) + ord(CAN_iBat_Low))
        iBat=CAN_iBat/100.0;
        CAN_BatTemp_High=msg.data[4].to_bytes(1,'big')
        CAN_BatTemp_Low=msg.data[5].to_bytes(1,'big')
        CAN_BatTemp=np.int16((ord(CAN_BatTemp_High) << 8) + ord(CAN_BatTemp_Low))
        BatTemp=CAN_BatTemp/100.0;
        CAN_BatState=msg.data[6]
        CAN_BatError = msg.data[7]
        
        def set_gg_VtB(VtB):#Function for setting the label for the Voltage
            gg_VtB.config(text=format(VtB)+"V") 

        #gg_VtB.set_value(float(vBat))cant use .set for lable
        set_gg_VtB(float(vBat))
        #gg_ItB.set_value(float(iBat)) cant use .set for a lable
        def set_gg_ItB(ItB):#Function for setting the label for the Current
            gg_ItB.config(text=format(ItB)+"A")
        set_gg_ItB(float(iBat))

        
        def set_gg_Pwr(ItB,VtB):#Function for setting the label for the Power(P=IV w)
            gg_Pwr.config(text="({0:.1f})".format(ItB*VtB)+"W")
            
        set_gg_Pwr(iBat,vBat)

        def getBatteryCurrent():
            # return iBat
            return random.randrange(50)
        def getBatteryVoltage():
            # return vBat
            return random.randrange(50)
        def getBatteryPower():
            # return iBat*vBat
            return random.randrange(50)
        def getVelocity():
            # return velo 
            return random.randrange(50)
        def getRpm():
            # return D_rpm 
            return random.randrange(50)
        def getBatteryTemp():
            # return BatTemp
            return random.randrange(50)

        

        #error_reader.Display_Error.bat_error(CAN_BatError)
        #Instead of having 20 if statments in the main class, They were moved to error_reader class, and replced with a method instead. This way we shrunk the code a little bit.//check output location
        
        TxtBxB.insert(tk.INSERT,"BatState=",tk.INSERT,CAN_BatState,tk.INSERT,"\n")
        TxtBxB.insert(tk.INSERT,"VtB=",tk.INSERT,vBat,tk.INSERT,"V \n")
        TxtBxB.insert(tk.INSERT,"ItB=",tk.INSERT,iBat,tk.INSERT,"A \n")
        TxtBxB.insert(tk.INSERT,"Temp=",tk.INSERT,BatTemp,tk.INSERT,"C \n")
        TxtBxB.insert(tk.INSERT,"Error=",tk.INSERT, error_reader.Display_Error.bat_error(CAN_BatError),tk.INSERT,"\n")
        TxtBxB.see("end") # Moves the text box to the end to show the latest data

#        if CAN_BatStat:
#            led_BatStat.to_green(on=True)
#        else:
#            led_BatStat.to_red(on=True)

        # Also print in terminal window
        print("D_flag_MotStat=",D_flag_MotStat)
        print("D_rpm=",D_rpm)
        print("VtB=",vBat,"V")
        print("ItB=",iBat,"A")
#        if CAN_BatStat==False: # End transmission
#            TxtBxB.insert(tk.INSERT,"Received terminating message \n")
#            TxtBxB.see("end") # Moves the text box to the end to show the latest data
#            print("Received terminating message")
            #flag_keep_connect=False
        
    else:
        print("Message not intended for me.")
        print(msg)
        
    
    mwin.update()
    print('sending data...')
    get_data_data(current = getBatteryCurrent(), voltage = getBatteryVoltage(), velocity = getVelocity(), rpm = getRpm(), temp = getBatteryTemp(), power = getBatteryPower())
    print('Continue GUI update')
    

#os.system('sudo ifconfig can0 down')

mwin.update()