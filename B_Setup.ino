void setup() {

  Serial.begin(9600);
  randomSeed(analogRead(0));

  //***********CAN Setup Start***************
flag_CAN_INIT=Canbus.init(CANSPEED_250);//Initialise MCP2515 CAN controller
 
//  if(flag_CAN_INIT)  
//    //Serial.println("CAN Init ok");
//  else
//    //Serial.println("Can't init CAN");

  
  outMsg.id = ID_Sender;
  outMsg.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg.header.rtr = 0;

  outMsg2.id = ID_Sender2;
  outMsg2.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg2.header.rtr = 0;

  outMsg3.id = ID_Sender3;
  outMsg3.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg3.header.rtr = 0;

  outMsg4.id = ID_Sender4;
  outMsg4.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg4.header.rtr = 0;

  outMsg5.id = ID_Sender5;
  outMsg5.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg5.header.rtr = 0;

  outMsg6.id = ID_Sender6;
  outMsg6.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg6.header.rtr = 0;

  outMsg7.id = ID_Sender7;
  outMsg7.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg7.header.rtr = 0;

  outMsg8.id = ID_Sender8;
  outMsg8.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg8.header.rtr = 0;

//***********CAN Setup END***************** 
  
}
