int echo = 5;
int trig = 7;

long tiempo, distancia;

void setup(){
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
}

void loop(){
  digitalWrite(trig, 0);
  delayMicroseconds(5);
  digitalWrite(trig,HIGH);
  tiempo = pulseIn(echo, HIGH);
  tiempo = tiempo / 2;
  distancia = tiempo / 29;
  Serial.println(distancia);
  delay(300);
}
