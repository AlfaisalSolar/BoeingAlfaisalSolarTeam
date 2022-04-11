float vPack = 0; //voltage
float myVcells[14] = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0}; //cells

float maxTemp = 0;
int maxTempCell = 0; //no of cell with max temp
float myTcells[14] = {0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0};

float iPack = 0;

byte batState =0;
byte errorCode = 0;

//***********CAN Libs Start***************
// Install this library SparkFun_CAN_BSCP.zip instead of the regular SparkFun library
#include <Canbus.h>
#include <defaults.h> // Modify CS pin from pin 10 (B,2) (used by BMS IC) to pin 3 (D,3)
#include <global.h>
#include <mcp2515.h>
#include <mcp2515_defs.h>
//***********CAN Libs END*****************

//***********CAN Vars Start***************
#define ID_Sender 0x01     // Battery MSG ID
#define ID_Sender2 0x02
#define ID_Sender3 0x03
#define ID_Sender4 0x04
#define ID_Sender5 0x05
#define ID_Sender6 0x06
#define ID_Sender7 0x07
#define ID_Sender8 0x08
//#define MSG_PRIOR    15 //0-15 lower is higher priority
#define MAX_CAN_FRAME_DATA_LEN   0x08 // CAN frame max data length
tCAN outMsg;
tCAN outMsg2;
tCAN outMsg3;
tCAN outMsg4;
tCAN outMsg5;
tCAN outMsg6;
tCAN outMsg7;
tCAN outMsg8;
bool flag_CAN_INIT=false;
byte CAN_send_counter = 20;// initially set to 50 to send the first time
byte CAN_SEND_EVERY = 3;
// Variables for transmission:
//short CAN_Vtot = 0;
//short CAN_Ipack = 0;
//short CAN_MaxTemp = 0;
//***********CAN Vars END*****************
