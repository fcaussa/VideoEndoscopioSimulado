/**********************************************************************************************
*********************** Francisco Caussa - 2020 ***********************************************
***********************************************************************************************
**El siguiente Sketch se entrega AS IS. Con licencia GPL v3. 
**Utilicie y modifiquese libremente.
**El mismo se implementa sobre una placa de desarrollo Arduino Pro Micro con AVR atmega32u4
**Fue seleccionado por la capacidad de emular un teclado/mouse a traves de la interface USB
**Se implementa a traves de un pedal, o boton, conectado a la entrada 4
**Al presionarse, envia una señal de presion de tecla "q" la cual es interpretada por el 
**programa de videoendoscopia simulada para alternar entre la camara del boroscopio
**y un video pregrabado de una video endscopia ALTA
**
**
**
***********************************************************************************************/

#include "Keyboard.h"

const int pedal = 4;          // input pin for pushbutton

void setup() {
  // make the pushButton pin an input:
  pinMode(pedal, INPUT_PULLUP);
  digitalWrite(pedal, HIGH); 
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
delay(100);
  if(!digitalRead(pedal)){
    delay(50);
    if(!digitalRead(pedal)){
      Keyboard.write('q');
      while(!digitalRead(pedal)){
        delay(10);
        }
      }
    }
}
