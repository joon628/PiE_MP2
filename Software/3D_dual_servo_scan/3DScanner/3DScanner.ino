#include <Wire.h>
#include <SharpIR.h>
#include <Servo.h>

Servo panServo;
Servo tiltServo;

int tilt=0;
int pan=0;
int panSteps=75;
int tiltSteps=15;
int panIncrement=1;
int tiltIncrement=1;

int distance_cm;
char buffer[40];

SharpIR mySensor(SharpIR::GP2Y0A02YK0F, A0);

void setup()
{

  tiltServo.attach(9);
  panServo.attach(8);
  tiltServo.write(0);
  panServo.write(0);


  Serial.begin(9600);
}

void loop()
{

  delay(2000);
  for (tilt=0;tilt<tiltIncrement*tiltSteps;tilt+=tiltIncrement)  {
    tiltServo.write(tilt);
    delay(300);

    for (pan=0;pan<panIncrement*panSteps;pan+=panIncrement) {
      delay(300);
      panServo.write(pan);
      distance_cm = mySensor.getDistance();
      sprintf (buffer,"%d, %d, %d",distance_cm, pan, tilt);
      Serial.println(buffer);
    }
  }
  Serial.println("done");

  panServo.write(0);
  tiltServo.write(0);
}
