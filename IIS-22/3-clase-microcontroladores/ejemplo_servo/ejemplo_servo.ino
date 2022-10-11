// Importar header de Servo.h
#include "Servo.h"

// Macro para númeo de pin
#define PIN_SERVO 7
// Botón que define funcionamiento del servo
#define PIN_BOTON 5
#define PIN_POTENCIOMETRO A15

// Instanciar el servo
Servo un_servo_ejemplo;

// Configurar el pin para el servo
void setup() {
  un_servo_ejemplo.attach(PIN_SERVO);
  pinMode(PIN_BOTON, INPUT);
  pinMode(PIN_POTENCIOMETRO, INPUT);
  // Serial para impirmir texto
  Serial.begin(9600); // Indica velocidad de microprocesador
}

void loop() {
  // Guardar en variable booleana (1 o 0), (verdadero o falso) el botón
  bool estado_boton = digitalRead(PIN_BOTON);
  // int numeros enteros negativos a positivos
  // long numeros enteros más grandes negativos a positivos
  // float numeros decimales negativos a positivos
  // double numeros decimales más grandes negativos a positivos
  int estado_pot = analogRead(PIN_POTENCIOMETRO);

  // Mapear de 7 a 900 como si fuera 400 ms a 2 s
  estado_pot = map(estado_pot, 7, 900, 400, 2000);
  
  Serial.println(estado_pot);
  if (estado_boton) { // se activa si el botón está presionado
    un_servo_ejemplo.write(0); // 0º de rotación
    delay(estado_pot);
    un_servo_ejemplo.write(180); // 180º de rotación
    delay(estado_pot);
  }
}
