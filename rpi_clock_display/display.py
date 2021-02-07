#!/usr/bin/env python3

import i2c_driver
from datetime import datetime
import time


def main(n=-1):
    mylcd = i2c_driver.LCD()

    i = 0
    while n > 0 and i < n:
        i += 1
        display_time = datetime.now().strftime("%I:%M %p")
        if display_time.startswith("0"):
            display_time = " " + display_time.lstrip("0")
        mylcd.lcd_display_string(display_time, 1)

        display_date_parts = [
            datetime.now().strftime("%A %B"),
            f'{datetime.now().strftime("%d").lstrip("0"): >2},',
            datetime.now().strftime("%Y"),
        ]

        mylcd.lcd_display_string(" ".join(display_date_parts), 2)
        time.sleep(1)


if __name__ == "__main__":
    main()
