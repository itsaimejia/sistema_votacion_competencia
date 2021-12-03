int btnRojo = 6;
int btnBlanco = 8;

void setup() {
  pinMode(btnRojo, INPUT_PULLUP);
  pinMode(btnBlanco, INPUT_PULLUP);
  Serial.begin(9600);

}

void loop() {
  if(digitalRead(btnRojo) == 0){
    Serial.println("ROJOJUEZ3");
    delay(200);
  }
  if(digitalRead(btnBlanco) == 0){
    Serial.println("BLANCOJUEZ3");
    delay(200);
  }
  

}
