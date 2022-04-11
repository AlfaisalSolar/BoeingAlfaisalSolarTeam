void sendBatInfoToCAN(float vBat, float iBat, float BatTemp, byte BatState, byte BatErrorCode){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_vBat = (short)(vBat*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_iBat = (short) (iBat*100); // Convert to 10s of milli amperes
    short CAN_BatTemp = (short) (BatTemp*100);
    byte CAN_BatState = BatState;
    byte CAN_BatErrorCode = BatErrorCode;
    // Prepare transmit ID, data and data length in CAN0 mailbox 0
    outMsg.data[0] = highByte(CAN_vBat);//send high byte first, big Endian
    outMsg.data[1] = lowByte(CAN_vBat);
    outMsg.data[2] = highByte(CAN_iBat);
    outMsg.data[3] = lowByte(CAN_iBat); 
    outMsg.data[4] = highByte(CAN_BatTemp);
    outMsg.data[5] = lowByte(CAN_BatTemp); //
    outMsg.data[6] = (byte) CAN_BatState; //
    outMsg.data[7] = (byte) CAN_BatErrorCode; // Empty for now 
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//2
  void sendBatInfoToCAN2(float a, float b, float c, float d){
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
    mcp2515_send_message(&outMsg2); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//3
  void sendBatInfoToCAN3(float a, float b, float c, float d){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_a = (short)(a*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_b = (short)(b*100); // Convert to 10s of milli amperes
    short CAN_c = (short)(c*100);
    short CAN_d = (short)(d*100);
    
    // Prepare transmit ID, data and data length in CAN0 mailbox 
    outMsg3.data[0] = highByte(CAN_a);//send high byte first, big Endian
    outMsg3.data[1] = lowByte(CAN_a);
    outMsg3.data[2] = highByte(CAN_b);
    outMsg3.data[3] = lowByte(CAN_b); 
    outMsg3.data[4] = highByte(CAN_c);
    outMsg3.data[5] = lowByte(CAN_c); //
    outMsg3.data[6] = highByte(CAN_d);
    outMsg3.data[7] = lowByte(CAN_d);
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg3); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//4
  void sendBatInfoToCAN4(float a, float b, float c, float d){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_a = (short)(a*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_b = (short)(b*100); // Convert to 10s of milli amperes
    short CAN_c = (short)(c*100);
    short CAN_d = (short)(d*100);
    
    // Prepare transmit ID, data and data length in CAN0 mailbox 
    outMsg4.data[0] = highByte(CAN_a);//send high byte first, big Endian
    outMsg4.data[1] = lowByte(CAN_a);
    outMsg4.data[2] = highByte(CAN_b);
    outMsg4.data[3] = lowByte(CAN_b); 
    outMsg4.data[4] = highByte(CAN_c);
    outMsg4.data[5] = lowByte(CAN_c); //
    outMsg4.data[6] = highByte(CAN_d);
    outMsg4.data[7] = lowByte(CAN_d);
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg4); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//5
  void sendBatInfoToCAN5(float a, float b, float c, float d){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_a = (short)(a*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_b = (short)(b*100); // Convert to 10s of milli amperes
    short CAN_c = (short)(c*100);
    short CAN_d = (short)(d*100);
    
    // Prepare transmit ID, data and data length in CAN0 mailbox 
    outMsg5.data[0] = highByte(CAN_a);//send high byte first, big Endian
    outMsg5.data[1] = lowByte(CAN_a);
    outMsg5.data[2] = highByte(CAN_b);
    outMsg5.data[3] = lowByte(CAN_b); 
    outMsg5.data[4] = highByte(CAN_c);
    outMsg5.data[5] = lowByte(CAN_c); //
    outMsg5.data[6] = highByte(CAN_d);
    outMsg5.data[7] = lowByte(CAN_d);
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg5); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//6
  void sendBatInfoToCAN6(float a, float b, float c, float d){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_a = (short)(a*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_b = (short)(b*100); // Convert to 10s of milli amperes
    short CAN_c = (short)(c*100);
    short CAN_d = (short)(d*100);
    
    // Prepare transmit ID, data and data length in CAN0 mailbox 
    outMsg6.data[0] = highByte(CAN_a);//send high byte first, big Endian
    outMsg6.data[1] = lowByte(CAN_a);
    outMsg6.data[2] = highByte(CAN_b);
    outMsg6.data[3] = lowByte(CAN_b); 
    outMsg6.data[4] = highByte(CAN_c);
    outMsg6.data[5] = lowByte(CAN_c); //
    outMsg6.data[6] = highByte(CAN_d);
    outMsg6.data[7] = lowByte(CAN_d);
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg6); 
//    CAN_send_counter = 0
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//7
  void sendBatInfoToCAN7(float a, float b, float c, float d){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_a = (short)(a*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_b = (short)(b*100); // Convert to 10s of milli amperes
    short CAN_c = (short)(c*100);
    short CAN_d = (short)(d*100);
    
    // Prepare transmit ID, data and data length in CAN0 mailbox 
    outMsg7.data[0] = highByte(CAN_a);//send high byte first, big Endian
    outMsg7.data[1] = lowByte(CAN_a);
    outMsg7.data[2] = highByte(CAN_b);
    outMsg7.data[3] = lowByte(CAN_b); 
    outMsg7.data[4] = highByte(CAN_c);
    outMsg7.data[5] = lowByte(CAN_c); //
    outMsg7.data[6] = highByte(CAN_d);
    outMsg7.data[7] = lowByte(CAN_d);
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg7); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }

//8
  void sendBatInfoToCAN8(float a, float b, float c, float d){
  // Boolean is 1 Byte and Short is 2 Bytes
//  if(CAN_send_counter == CAN_SEND_EVERY){
    short CAN_a = (short)(a*100); // KEEP PARANTHESES! Convert to 10s of milli volts
    short CAN_b = (short)(b*100); // Convert to 10s of milli amperes
    short CAN_c = (short)(c*100);
    short CAN_d = (short)(d*100);
    
    // Prepare transmit ID, data and data length in CAN0 mailbox 
    outMsg8.data[0] = highByte(CAN_a);//send high byte first, big Endian
    outMsg8.data[1] = lowByte(CAN_a);
    outMsg8.data[2] = highByte(CAN_b);
    outMsg8.data[3] = lowByte(CAN_b); 
    outMsg8.data[4] = highByte(CAN_c);
    outMsg8.data[5] = lowByte(CAN_c); //
    outMsg8.data[6] = highByte(CAN_d);
    outMsg8.data[7] = lowByte(CAN_d);
    mcp2515_bit_modify(CANCTRL, (1<<REQOP2)|(1<<REQOP1)|(1<<REQOP0), 0);
    mcp2515_send_message(&outMsg8); 
//    CAN_send_counter = 0;
//    }
//  CAN_send_counter++;
  //Serial.println("CAN Sent!");
  }
