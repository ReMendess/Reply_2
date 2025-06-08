#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>


#define DHTPIN 26         
#define DHTTYPE DHT22

#define POT_CORRENTE 33   
DHT dht(DHTPIN, DHTTYPE);
Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  
  dht.begin();
  Serial.println("Iniciando sensores");

  Wire.begin(22, 23);  // SDA, SCL
  if (!mpu.begin()) {
    Serial.println("Falha ao iniciar o MPU6050");
    while (1);
  }
}

void loop() {
  float temp = dht.readTemperature();
  float umid = dht.readHumidity();

  sensors_event_t acc, gyro, temp_event;
  mpu.getEvent(&acc, &gyro, &temp_event);

  // corrente
  int corrente_raw = analogRead(POT_CORRENTE);
  float corrente_simulada = (corrente_raw / 4095.0) * 30.0; 
  
  Serial.printf("Temp: %.2f °C | Umid: %.2f %%\n", temp, umid);
  Serial.printf("Vibração: X=%.2f | Y=%.2f | Z=%.2f\n", acc.acceleration.x, acc.acceleration.y, acc.acceleration.z);
  Serial.printf("Corrente: %.2f A \n", corrente_simulada); 
  Serial.printf("==========  ========== \n");

  delay(2000);
}
