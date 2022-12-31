
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

//////////////////////// OLED start ////////////////////////////////////////
// Reset pin not used but needed for library
#define OLED_RESET 9                         // pin D8 is frei !!!!!!
Adafruit_SSD1306 display(OLED_RESET);

//////////////////////// OLED stop ////////////////////////////////////////
float TEMP=0;
float min_temp=0;








void setup(void)
{

 
  Wire.begin();
  //////////////////////// OLED start ////////////////////////////////////////
   // initialize OLED with I2C addr 0x3C
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // adress !!!!!
  //////////////////////// OLED stop ////////////////////////////////////////
  // start serial port
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");

}

void displayRobo(){
  

 // Clear the display
  display.clearDisplay();  // clear the display
  display.setTextColor(WHITE); // color
  display.setTextSize(2);  // size of text
  
 display.setCursor(0,0); //0,17
 display.print("TEMP:");

 display.setCursor(70,0); //70,17
 display.print(TEMP);

              display.setCursor(110,0); //110,17
              display.print("C");

 display.setCursor(0,17); //0,17
 display.print("min:");

 display.setCursor(70,17); //70,17
 display.print(min_temp);

          display.setCursor(110,17); //110,17
          display.print("C");

   
 
}


void loop(void)
{ 
  
  displayRobo();
  display.display();
}
