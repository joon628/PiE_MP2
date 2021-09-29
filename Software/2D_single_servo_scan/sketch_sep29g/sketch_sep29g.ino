#include <Servo.h>

Servo panServo;
int pan=0;
int panSteps=75;
int panIncrement=1;

void setup() {
  panServo.attach(8);
  panServo.write(0);
  Serial.begin(9600);
  
}

void loop() {
  for (pan=0;pan<panIncrement*panSteps;pan+=panIncrement) {
      delay(300);
      panServo.write(pan);
      distance_cm = mySensor.getDistance();
      sprintf (buffer,"%d, %d, %d",distance_cm, pan, tilt);
      Serial.println(buffer);
    }
    Serial.println("done");
    panServo.write(0);

}
