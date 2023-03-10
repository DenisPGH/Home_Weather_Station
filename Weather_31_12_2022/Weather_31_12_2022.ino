
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

//////////////////////// OLED start ////////////////////////////////////////
// Reset pin not used but needed for library
#define OLED_RESET 9                         // pin D8 is frei !!!!!!
Adafruit_SSD1306 display(OLED_RESET);

//////////////////////// OLED stop ////////////////////////////////////////
float TEMP=0;
float HUMIDITY=0; //Humidity
float ALTITUDE =0; //Altitude
float PRESSURE=0; // Pressure

String show_text="DENISLAV";
float show_value=0;
String show_units="A"; // C, 

unsigned long interval=2000;
unsigned long current_time=0;
unsigned long last_time=0;
int state=0;


//////////////////////////////// BME280 start ///////////////////////////////////////////////////
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme; // I2C
#define SEALEVELPRESSURE_HPA (1013.25)
//////////////////////////////// BME280 stop ///////////////////////////////////////////////////








void setup(void)
{

 
  Wire.begin();
  //////////////////////// OLED start ////////////////////////////////////////
   // initialize OLED with I2C addr 0x3C
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // adress !!!!!
  //////////////////////// OLED stop ////////////////////////////////////////
  // start serial port
  Serial.begin(9600);

  //////////////////////////////// BME280 start ///////////////////////////////////////////////////
  while(!Serial);    // time to get serial running
    Serial.println(F("BME280 test"));
     unsigned status;
     status = bme.begin();  
      if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        while (1);
      }
//////////////////////////////// BME280 stop ///////////////////////////////////////////////////

 

}




void loop(void)
{ 
      current_time=millis();
  
    if (current_time-last_time>=interval){
          state++;
          if (state>4){state=1;}
          last_time=current_time;
    }
        Serial.print("state: ");
        Serial.println(state);
        sensor_values();
        status_showing(state);
  
        displayRobo();
        display.display();
}


void displayRobo(){
  
 // Clear the display
  display.clearDisplay();  // clear the display
  display.setTextColor(WHITE); // color
  display.setTextSize(2);  // size of text
  
 display.setCursor(0,0); //0,17
 display.print(show_text);

// display.setCursor(110,0); //0,17
// display.print( " :");

 display.setCursor(0,17); //70,17
 display.print(show_value);

              display.setCursor(110,17); //110,17
              display.print(show_units);

// display.setCursor(0,17); //0,17
// display.print("min:");
//
// display.setCursor(70,17); //70,17
// display.print(ALTITUDE);
//
//          display.setCursor(110,17); //110,17
//          display.print("C");

   
}

void sensor_values(){
    TEMP=bme.readTemperature();
    PRESSURE=bme.readPressure() / 100.0F;
    ALTITUDE=bme.readAltitude(SEALEVELPRESSURE_HPA);
    HUMIDITY=bme.readHumidity();
    
    Serial.print("Temperature = ");
    Serial.print(TEMP);
    Serial.println(" ??C");
    Serial.print("Pressure = ");
    Serial.print(PRESSURE);
    Serial.println(" hPa");
    Serial.print("Approx. Altitude = ");
    Serial.print(ALTITUDE);
    Serial.println(" m");

    Serial.print("Humidity = ");
    Serial.print(HUMIDITY);
    Serial.println(" %");

    Serial.println();
  
}

void status_showing(int state_show){
  

  switch(state_show) {
  case 1:  
        show_value=TEMP; show_text= "Temperature :"; show_units= " ??C";
        break;
  case 2:
        show_value=HUMIDITY; show_text= "Humidity :"; show_units=" %";
        
        break;
  case 3:
        show_value=PRESSURE; show_text= "Pressure :"; show_units=" hPa";
        break;
  case 4:
        show_value=ALTITUDE; show_text= "Altitude :"; show_units=" m";
        break;
    
  default:
        show_value= 1990; show_text= "Denislav :"; show_units=" born";
        break;
}
  
  
}
