#include <Servo.h>
#include <SharpIR.h>

Servo panServo;
int pan=0;
int panSteps=75;
int panIncrement=1;
int distance_cm;

SharpIR mySensor(SharpIR::GP2Y0A02YK0F, A0);
char buffer[40];

void setup() {
  panServo.attach(8);
  panServo.write(0);
  Serial.begin(9600);
  
}

void loop() {
  for (pan=0;pan<panIncrement*panSteps;pan+=panIncrement) {
      panServo.write(pan);
      delay(300);
      distance_cm = mySensor.getDistance();
      sprintf (buffer,"%d, %d",distance_cm, pan);
      Serial.println(buffer);
    }
    Serial.println("done");
    panServo.write(0);

}
