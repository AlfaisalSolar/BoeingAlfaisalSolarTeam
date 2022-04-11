void loop(){RPM = random(2000,600000); 
motorI = random(8000,40000);
batteryV = random(2000,18000); 
Serial.println(String("Speed of RPM: ") + String(RPM, DEC));
Serial.println(String("total voltage: ") + String(batteryV, DEC));
Serial.println(String("current motor: ") + String(motorI, DEC));
 sendInfoToCAN(RPM, motorI, batteryV);
    delay(40); }
