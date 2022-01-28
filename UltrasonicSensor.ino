// Pins anf variables
const int trigPin = 2;
const int echoPin = 3;
long elaspedTime;
long duration;
float distance;

void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  elaspedTime = millis();
  
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  // Send out 10 microsecond chirp
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);

  // Reads the echoPin and returns the sound
  // wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  //Prints time elasped to Serial
  Serial.print(elaspedTime);
  Serial.print(',');
  //  343m/s = .0343 cm/microsecond
  distance = .0343*duration/2;
  Serial.println(distance);
  
  delay(5);
}
