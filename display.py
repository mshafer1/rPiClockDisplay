#!/usr/bin/env python3

import i2c_driver
import time

def main():
    mylcd = i2c_driver.lcd()

    while True:
        display_time = time.strftime('%I:%M %p')
        if display_time.startswith("0"):
            display_time = " " + display_time.lstrip("0")
        mylcd.lcd_display_string(display_time, 1)
        mylcd.lcd_display_string(time.strftime('%A %B %d, %Y'), 2)
        time.sleep(1)

if __name__ == "__main__":
    main()
