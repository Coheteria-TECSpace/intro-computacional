/*
 *  Código escrito para introducción a cohetería computacional
 *  usando el simulador web TinkerCAD para circuitos de Arduino
 */

// incluyendo headers/encabezados
#include <Servo.h>
#include <Adafruit_NeoPixel.h>

// variable global
Servo miServo;			// se declara la variable del servo
#define PIN        2
#define NUMPIXELS 12
// declara los pixeles de tipo Adafruit_NeoPixel
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
#define DELAYVAL 200

void colorear(int rojo, int verde, int azul)
{
  // enciende leds
  for(int i=0; i<NUMPIXELS; i++) {
	// RGB -> R : rojo, G: verde, B: azul de 0 a 255
    pixels.setPixelColor(i, pixels.Color(rojo, verde, azul));
    pixels.show();
    delay(DELAYVAL);
  }
}

void setup()
{
  pinMode(A5,INPUT);
  Serial.begin(9600);
  miServo.attach(9,490,2500);	// se inicializa en pin del servo
  miServo.write(0);
  pixels.begin();				// inicializar pixeles
}

void loop()
{
  pixels.clear();	// limpiar colores
  pixels.show();	// actualizar colores
  
  int valorLeido = analogRead(A5);
  // convertirlo de escala 0 a 914
  // a escala de 0 a 1
  float valorPorcentaje = valorLeido/914.0;
  Serial.println(valorPorcentaje);
  
  // si el valor del sensor es > 0.7, servo a 40º
  if (valorPorcentaje > 0.7)
  {
    miServo.write(40);
    // luz roja, algo anda mal
    colorear(255,0,0);
    delay(30);
  }
  else
  {
    miServo.write(0);
    // luz verde, todo bien
    colorear(0,255,0);
    delay(30);
  }

  colorear(1,15,5);
}
