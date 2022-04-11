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


mwin=tk.Tk() # Main Window for GUI Add mwin.mainloop() at the end of the code
#mwin.attributes('-fullscreen',True) # However this does not even show the title bar Alt+F4 to close it
#mwin.attributes('-zoomed',True) # keeps the title bar
mwin.geometry('1000x500')
mwin.title("BSCP Driver Interface")
mwin.configure(bg="black")

# Define CAN Message IDs
msgID_mot=7
msgID_bat=9

Gr=3.522 # Gear Ratio
rWh = 0.27# radius of the wheel

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

gg_rpm=tk.Label(mwin,bg='black',text="0")
gg_rpm.config(font=('Helvetica Bold',40))
gg_rpm.place(relx=0.525, rely=0.20, anchor="n")
text_rpm=tk.Label(mwin,bg='black',text='Rpm',fg='#FFFFFF')
text_rpm.config(font=('Helvetica',30))
text_rpm.place(relx=0.65,rely=0.22,anchor="n")
#tk_tools.Gauge(mwin,min_value=-1,max_value=3000.0, width=00, height=00, #                     yellow=70, red=90, yellow_low=0, red_low=0, divisions=10,
#                    label='Motor RPM', unit='rpm', bg='silver')
# e.g., yellow=80, means yellow range starts at 80% of 10000 - 5000 = 3000 rpm
# yellow_low is where the negative range of yellow starts 20% of 10000 - 5000= -3000 rpm
#gg_rpm.place(relx=0.4, rely=0.3, anchor="n")
#gg_rpm.set_value(0)

text_kph=tk.Label(mwin,bg='black',text='Kph',fg='#FFFFFF')
text_kph.config(font=('Helvetica',30))
text_kph.place(relx=0.28,rely=0.15,anchor="n")

gg_kph=tk.Label(mwin,bg='black',text="0")
gg_kph.config(font=('Helvetica Bold',95))
gg_kph.place(relx=0.13, rely=0.0, anchor="n")

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
text_Pwr=tk.Label(mwin,bg='black',text='W',fg='#FFFFFF')
text_Pwr.config(font=('Helvetica Bold',30))
text_Pwr.place(relx=0.371,rely=0.7,anchor="n")

gg_Pwr=tk.Label(mwin,text="0")
gg_Pwr.config(font=('Helvetica Bold',80))
gg_Pwr.place(relx=0.2, rely=0.60, anchor="n")

gg_VtB=tk.Label(mwin,bg='black',text="0 ")
gg_VtB.config(font=('Helvetica Bold',50))
gg_VtB.place(relx=0.58, rely=0.00, anchor="n")

text_ItB=tk.Label(mwin,bg='black',text='A',fg='#FFFFFF')
text_ItB.config(font=('Helvetica Bold',30))
text_ItB.place(relx=0.371,rely=0.45,anchor="n")

gg_ItB=tk.Label(mwin,text="0 ")
gg_ItB.config(font=('Helvetica Bold',90))
gg_ItB.place(relx=0.18, rely=0.3, anchor="n")

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
D_VtM=0 # The terminal voltage of the motor, will be received as a short int (2 bytes)
#and then converted in this code to a float by dividing by 100, i.e., V is sent in 10's of mV
D_ItM=0 # The terminal current will be received as a short int in 10's of mA
#and then converted in this code to a float by dividing by 10                           0
mwin.update()
#mwin.mainloop()

while flag_keep_connect: # Disconnect if no one is talking for 10s
    msg = can0.recv(100000.0) # I.e., receive any message
    #print(msg.arbitration_id==msgID_mot)
    #D_flag_ComStatM = False
    if msg is None:
        TxtBxM.insert(tk.INSERT,"Timeout occurred, no message \n")
        print('Timeout occurred, no message.')
        flag_keep_connect=False
        led_ComStatM.to_red(on=True)#turns to Green only, but not to red
    elif (msg.arbitration_id==msgID_mot):
        print("***---Motor Frame---***");
        D_flag_ComStatM=bool(msg.data[0]) 
        D_flag_MotStat=bool(msg.data[1])
        print(D_flag_MotStat)
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
        
       # gg_rpm.set_value(float(D_rpm))
        def set_gg_rpm(D_rpm):   #This method should enable the gg_kph label to change numbers(speed should update)
            gg_rpm.config(bg='black',text="{0:.0f}".format(D_rpm),fg='#FFFFFF')
            
        set_gg_rpm(float(D_rpm))# cast as float or int since it is int16,
        #which isn't recognized by the guage set_value function
        # Note: If D_rpm> MAX Value then the display needle is frozen
        #gg_VtM.set_value(float(VtM))
        #gg_ItM.set_value(float(ItM))
        #velo = (((D_rpm*0.104719755)/3.522)*0.27)*3.6
        omega = D_rpm*(2*(np.pi)/60)
        velo = rWh*(1/Gr)*omega
        def set_gg_kph(velo):   #This method should enable the gg_kph label to change numbers(speed should update)
            gg_kph.config(bg='black',text="{0:.0f}".format(velo),fg='#FFFFFF')
            
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
            gg_VtB.config(bg='black',text=format(VtB)+"V",fg='#FFFFFF') 

        #gg_VtB.set_value(float(vBat))cant use .set for lable
        set_gg_VtB(float(vBat))
        #gg_ItB.set_value(float(iBat)) cant use .set for a lable
        def set_gg_ItB(ItB):#FUnction for setting the label for the Current
            gg_ItB.config(bg='black',text=format(ItB),fg='#FFFFFF')
        set_gg_ItB(float(iBat))
        
        def set_gg_Pwr(ItB,VtB):#FUnction for setting the label for the Power(P=IV w)
            gg_Pwr.config(bg='black',text="{0:.1f}".format(ItB*VtB),fg='#FFFFFF')
            
        set_gg_Pwr(iBat,vBat)
        
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
        
        
    
        
    mwin.bind('<Escape>',lambda x:mwin.destroy())
    mwin.attributes('-fullscreen',True)

  
    mwin.update()

#os.system('sudo ifconfig can0 down')

mwin.update()

