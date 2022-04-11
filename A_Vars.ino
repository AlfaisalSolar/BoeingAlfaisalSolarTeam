float RPM = 0; //Speed of RPM
float motorI = 0; // motor current
float batteryV = 0; //battery voltage 
int Err=0; 
 

//***********CAN Libs Start***************
// Install this library SparkFun_CAN_BSCP.zip instead of the regular SparkFun library
#include <Canbus.h>
#include <defaults.h> // Modify CS pin from pin 10 (B,2) (used by BMS IC) to pin 3 (D,3)
#include <global.h>
#include <mcp2515.h>
#include <mcp2515_defs.h>
//***********CAN Libs END*****************

//***********CAN Vars Start***************
#define ID_Sender1 0x01     //  MSG ID
//#define ID_Sender2 0x02

//#define MSG_PRIOR    15 //0-15 lower is higher priority
#define MAX_CAN_FRAME_DATA_LEN   0x08 // CAN frame max data length
tCAN outMsg1;
//tCAN outMsg2;

bool flag_CAN_INIT=false;
byte CAN_send_counter = 20;// initially set to 50 to send the first time
byte CAN_SEND_EVERY = 3;

//***********CAN Vars END*****************
