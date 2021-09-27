// asigna valor 2 a variable pinDos
int pinDos = 2;
int pinCinco = 5;

void parpadear()
{
    // enciende a maxima intensidad
    analogWrite(pinCinco,255);
    delay(200);
    analogWrite(pinCinco,0);
    delay(200);
}

void setup()
{
    // funcion de Arduino pinMode
    pinMode(pinDos, INPUT);
    pinMode(pinCinco, OUTPUT);
    // Para poder imprimir valores
    Serial.begin(9600);
}

void loop()
{
    // valor se guarda lo que lee el pinDos
    int valor = digitalRead(pinDos);

    // if/else
    if(valor == 1)
    {
        analogWrite(pinCinco,0);
    }
    else
    {
        parpadear();
    }
}

