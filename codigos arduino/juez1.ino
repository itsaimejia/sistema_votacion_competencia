int btnRojo = 6;
int btnBlanco = 8;
int btnVerde = 10;

void setup() {
  pinMode(btnRojo, INPUT_PULLUP);
  pinMode(btnBlanco, INPUT_PULLUP);
  pinMode(btnVerde, INPUT_PULLUP);
  Serial.begin(9600);

}

void loop() {
  if(digitalRead(btnRojo) == 0){
    Serial.println("ROJOJUEZ1");
    delay(200);
  }
  if(digitalRead(btnBlanco) == 0){
    Serial.println("BLANCOJUEZ1");
    delay(200);
  }
  if(digitalRead(btnVerde) == 0){
    Serial.println("VERDEJUEZ1");
    delay(200);
  }

}
