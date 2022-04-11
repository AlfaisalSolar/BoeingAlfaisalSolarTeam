void sendInfoToCAN(float RPM, float motorI, float batteryV){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_RPM = (short)(RPM); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_motorI = (short) (motorI); // Convert to 10s of milli amperes
    short CAN_batteryV = (short) (batteryV);
  
    // Prepare transmit ID, data and data length in CAN0 mailbox 0
    outMsg1.data[0] = highByte(RPM);//send high byte first, big Endian
    outMsg1.data[1] = lowByte(RPM);
    outMsg1.data[2] = highByte(motorI);
    outMsg1.data[3] = lowByte(motorI); 
    outMsg1.data[4] = highByte(batteryV);
    outMsg1.data[5] = lowByte(batteryV); //
    outMsg1.data[6] = highByte() //Empty for now 
    outMsg1.data[7] = lowByte() // Empty for now 
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg1); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//2
 /* void sendBatInfoToCAN2(float a, float b, float c, float d){
  // Boolean is 1 Byte and Short is 2 Bytes
  //if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_a = (short)(a*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_b = (short)(b*100); // Convert to 10s of milli amperes
    short CAN_c = (short)(c*100);
    short CAN_d = (short)(d*100);
    
    // Prepare transmit ID, data and data length in CAN0 mailbox 
    outMsg2.data[0] = highByte(CAN_a);//send high byte first, big Endian
    outMsg2.data[1] = lowByte(CAN_a);
    outMsg2.data[2] = highByte(CAN_b);
    outMsg2.data[3] = lowByte(CAN_b); 
    outMsg2.data[4] = highByte(CAN_c);
    outMsg2.data[5] = lowByte(CAN_c); //
    outMsg2.data[6] = highByte(CAN_d);
    outMsg2.data[7] = lowByte(CAN_d);
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg2); */
    
