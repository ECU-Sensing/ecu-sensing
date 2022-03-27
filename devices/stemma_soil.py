"""
`hydros`
================================================================================
Python library for Hydros21 or Decagon CDT-10 water level sensor.
* Author(s): Colby Sawyer
Implementation Notes
--------------------
**Hardware:**
* `Hydros 21 Conductivity, Temperature, and Depth Sensor <https://www.metergroup.com/en/meter-environment/products/hydros-21-water-level-sensor-conductivity-temperature-depth>`_

**Software and Dependencies:**

"""

import time
import board
from adafruit_seesaw.seesaw import Seesaw



def get_data():
    i2c_bus = board.I2C()
    ss = Seesaw(i2c_bus, addr=0x36)
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp = ss.get_temp()

    print("temp: " + str(temp) + "  moisture: " + str(touch))
    return [temp, touch]
