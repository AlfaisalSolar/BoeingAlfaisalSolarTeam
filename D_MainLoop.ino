void loop() {
  
  for(int i = 0; i<14; i++)
  {
    //this loop gives random number for cell voltage 
    myVcells[i] = random(395,401)/100.0; //division to get numbers after decimal
    delay(100);
    Serial.println(String("cell ") + String(i+1, DEC) + String(" V :")+ String(myVcells[i], DEC));// i+1 cuz i starts from zero
    vPack = myVcells[i]+vPack; // to get the total voltage
  }
  
  for(int i = 0; i<14; i++)
  {
    //this loop gives random number for cell temp 
    myTcells[i] = random(3500,4200)/100.0; 
    delay(100);
    Serial.println(String("cell ") + String(i+1, DEC) + String(" T: ")+ String(myTcells[i], DEC));
    if(myTcells[i]>maxTemp)//to get the max
    {
      maxTemp = myTcells[i];
      maxTempCell = i+1; //to get the index for max cell temp
    }
  }
  

  batState = random(1,4);
  errorCode = random(1,43);

  iPack = random(8000,15000)/100.0;
   
  Serial.println(String("total voltage: ") + String(vPack, DEC));
  Serial.println(String("max temp: ") + String(maxTemp, DEC) + String(" cell ") + String(maxTempCell, DEC));
  Serial.println(String("current: ") + String(iPack, DEC));
  Serial.println(String("bat state: ") + String(batState, DEC));
  Serial.println(String("error code: ") + String(errorCode, DEC));
  Serial.println();
  
  //Sending to CAN
  if(CAN_send_counter >= CAN_SEND_EVERY)
  {
    sendBatInfoToCAN(vPack, iPack, maxTemp ,batState, errorCode);
    delay(40); 
    sendBatInfoToCAN2(myVcells[0], myVcells[1], myVcells[2] ,myVcells[3]);
    delay(80);
    sendBatInfoToCAN3(myVcells[4], myVcells[5], myVcells[6] ,myVcells[7]);
    delay(40);
    sendBatInfoToCAN4(myVcells[8], myVcells[9], myVcells[10] ,myVcells[11]);
    delay(80);
    sendBatInfoToCAN5(myVcells[12], myVcells[13], myTcells[0] ,myTcells[1]);
    delay(40);
    sendBatInfoToCAN6(myTcells[2], myTcells[3], myTcells[4] ,myTcells[5]);
    delay(90);
    sendBatInfoToCAN7(myTcells[6], myTcells[7], myTcells[8] ,myTcells[9]);
    delay(40);
    sendBatInfoToCAN8(myTcells[10], myTcells[11], myTcells[12] ,myTcells[13]);
    delay(90);
    CAN_send_counter = 0;
  }
  CAN_send_counter++;
  
  
  vPack=0; //to reset
  maxTemp = 0;
  
}                           
