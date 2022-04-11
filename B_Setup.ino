void setup() {

  Serial.begin(9600);
  randomSeed(analogRead(0));

  //***********CAN Setup Start***************
flag_CAN_INIT=Canbus.init(CANSPEED_250);//Initialise MCP2515 CAN controller
 
//  if(flag_CAN_INIT)  
//    //Serial.println("CAN Init ok");
//  else
//    //Serial.println("Can't init CAN");

  
  outMsg1.id = ID_Sender1;
  outMsg1.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg1.header.rtr = 0;

 /* outMsg2.id = ID_Sender2;
  outMsg2.header.length = MAX_CAN_FRAME_DATA_LEN;
  outMsg2.header.rtr = 0;
  //***********CAN Setup END***************** 
  */
}
