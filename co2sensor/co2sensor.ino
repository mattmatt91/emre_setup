/***************************************************
* Infrared CO2 Sensor 0-50000ppm(Wide Range)
****************************************************
* The following example is used to detect CO2 concentration.
* Author: lg.gang(lg.gang@qq.com)
* Version: V1.0
* Date: 2016-6-6
* GNU Lesser General Public License.
* See <http://www.gnu.org/licenses/> for details.
* All the above must be included in any redistribution.
****************************************************/

unsigned char hexdata[9] = {0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79}; // Read the gas density command /Don't change the order

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    // Wait for serial port to connect
  }
  Serial1.begin(9600);
}

void loop() {
  Serial1.write(hexdata, 9);
  delay(500);

  for (int i = 0, j = 0; i < 9; i++) {
    if (Serial1.available() > 0) {
      long hi, lo, CO2;
      int ch = Serial1.read();

      if (i == 2) {
        hi = ch;
      }   // High concentration
      if (i == 3) {
        lo = ch;
      }   // Low concentration
      if (i == 8) {
        CO2 = hi * 256 + lo;  // CO2 concentration
        Serial.println("{'co2ppm': " + String(CO2) + "}");
      }
    }
  }
}
