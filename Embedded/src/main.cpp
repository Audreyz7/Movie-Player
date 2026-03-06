#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <SPI.h>

// ST7735S 1.8" TFT LCD display
// VCC: 3.3V
// GND: GND
// SCL: SCK (D18)
// SDA: MOSI (D23)
// RST: RST (D16)
// DC: D/C (D2)
// CS: CS (D15)
// BLK: 3.3V
#define TFT_CS   15
#define TFT_DC   2
#define TFT_RST  16

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

// Touch Sensor
// VCC: 3.3V
// GND: GND
// I/O: D4
#define TOUCH_PIN 4

// LM386
// VCC: 3.3V (Pin6)
// GND: GND (Pin4)
// Speaker +: V Out (Pin5)
// Speaker -: GND
// GPIO25: Non INV In (Pin3)
#define AUDIO_PIN 25

void setup() {
  // put your setup code here, to run once:
  int result = myFunction(2, 3);
}

void loop() {
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}