// incluyendo headers/encabezados
#include <Servo.h>
#include <Adafruit_NeoPixel.h>
#include <math.h>		// para el pow()

// variable global
Servo miServo;			// se declara la variable del servo
#define PIN        2
#define NUMPIXELS 12
// declara los pixeles de tipo Adafruit_NeoPixel
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
#define DELAYVAL 10

double interpolar(double x);
void colorear(int rojo, int verde, int azul);

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
  double valorPorcentaje = valorLeido/914.0;
  Serial.print("Fuerza ejercida: ");
  double fuerza = interpolar(valorPorcentaje);
  Serial.println(fuerza);
  
  // Mensaje de advertencia
  if (fuerza > 8.0)
  {
    miServo.write(0);
    delay(1000);
  }
  
  
  // si el valor del sensor es > 0.7, servo a 40º
  if (valorPorcentaje > 0.7)
  {
    miServo.write(40);
    // luz roja, algo anda mal
    colorear(255,0,0);
  }
  else
  {
    miServo.write(0);
    // luz verde, todo bien
    colorear(0,255,0);
  }
  colorear(1,15,5);
}

// Aproximación de la curva obtenido por polinomios de lagrange
double interpolar(double x)
{
  double calc = x*(8795.2214*pow(x,8)
    -41755.7105*pow(x,7)
    +84740.1864*pow(x,6)
    -95271.2307*pow(x,5)
    +64303.4701*x*x*x*x
    -26370.0766*pow(x,3)
    +6326.5762*pow(x,2)
    -799.6546*x
    +41.2183);
   return(calc);
}

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
