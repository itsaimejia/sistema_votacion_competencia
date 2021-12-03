int pin = 6;

void setup() {
  pinMode(pin, INPUT_PULLUP);
  Serial.begin(9600);

}

void loop() {
  if(digitalRead(pin) == 0){
    Serial.println("presionado");
    delay(500);
  }

}
