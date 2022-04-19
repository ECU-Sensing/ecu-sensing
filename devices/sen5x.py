import time
from sensirion_i2c_driver import I2cConnection, LinuxI2cTransceiver
from sensirion_i2c_sen5x import Sen5xI2cDevice

def get_data():
    with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
        device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))

        # Print some device information
        print("Version: {}".format(device.get_version()))
        print("Product Name: {}".format(device.get_product_name()))
        print("Serial Number: {}".format(device.get_serial_number()))

        # Perform a device reset (reboot firmware)
        device.device_reset()

        # Start measurement
        device.start_measurement()
        # Wait until next result is available
        print("Waiting for new data...")
        while device.read_data_ready() is False:
            time.sleep(0.1)

        # Read measured values -> clears the "data ready" flag
        values = device.read_measured_values()
        print(values)

        # Access a specific value separately (see Sen5xMeasuredValues)
        mass_concentration = values.mass_concentration_2p5.physical
        ambient_temperature = values.ambient_temperature.degrees_celsius

        mc_1p0 = values.mass_concentration_1p0.physical
        mc_2p5 = values.mass_concentration_2p5.physical
        mc_4p0 = values.mass_concentration_4p0.physical
        mc_10p0 = values.mass_concentration_10p0.physical
        ambient_rh = values.ambient_humidity.percent_rh
        ambient_t = values.ambient_temperature.degrees_celsius
        voc_index = values.voc_index.scaled
        nox_index = values.nox_index.scaled

        # Read device status
        status = device.read_device_status()
        print("Device Status: {}\n".format(status))

        # Stop measurement
        device.stop_measurement()
        print("Measurement stopped.")
        
        return [mc_1p0, mc_2p5,mc_4p0, mc_10p0, ambient_rh, ambient_t, voc_index, nox_index]
