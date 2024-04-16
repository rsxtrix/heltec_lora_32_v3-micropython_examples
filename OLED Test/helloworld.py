import machine
import ssd1306
import time

# Define pin assignments
scl_pin = machine.Pin(18)  # Clock
sda_pin = machine.Pin(17)  # Data
reset_pin = machine.Pin(21, machine.Pin.OUT)  # Reset

# Initialize SoftI2C
i2c = machine.SoftI2C(scl=scl_pin, sda=sda_pin)

# Function to reset the OLED display
def reset_oled(reset_pin):
    reset_pin.value(0)  # Pull reset pin low to reset OLED
    time.sleep(0.1)     # Wait 100 ms
    reset_pin.value(1)  # Pull reset pin high to resume normal operation
    time.sleep(0.1)     # Wait 100 ms after resetting

# Call reset function to ensure proper startup
reset_oled(reset_pin)

# Set up SSD1306 OLED Display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Clear the display before writing new text
oled.fill(0)

# Write text "Hello World" at coordinates (0, 0)
oled.text('Hello World', 0, 0)

# Update OLED to show text
oled.show()
