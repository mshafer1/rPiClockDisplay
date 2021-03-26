#!/usr/bin/env python3

print("display::importing")
from rpi_clock_display import i2c_driver
from datetime import datetime
import time
import logging

from . import backlight
from . import large_numbers2


def _hours_to_12_mode(hours):
    """
    >>> _hours_to_12_mode(0)
    12
    >>> _hours_to_12_mode(1)
    1
    >>> _hours_to_12_mode(13)
    1
    >>> _hours_to_12_mode(14)
    2
    """
    result = hours
    if result > 12:
        result -= 12
    elif result == 0:
        result += 12
    return result

def main(n=-1):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
    mylcd = i2c_driver.LCD()
    logging.info("lcd loaded")

    large_numbers2.generate_big(mylcd)

    i = 0
    while n < 0 or i < n:
        i += 1
        now = datetime.now()
        hours = _hours_to_12_mode(now.hour)
        large_numbers2.write_time(mylcd, hours, now.minute)
        display_time = datetime.now().strftime("%I : %M %p")
        logging.info("display time: %s", display_time)
        #if display_time.startswith("0"):
        #    display_time = " " + display_time.lstrip("0")
        #mylcd.lcd_display_string("  " + display_time, 2)

        #display_date_parts = [
        #    datetime.now().strftime("%A %B"),
        #    '{: >2},'.format(datetime.now().strftime("%d").lstrip("0")),
        #    datetime.now().strftime("%Y"),
        #]

        # mylcd.lcd_display_string(" ".join(display_date_parts), 2)
        time.sleep(1)


if __name__ == "__main__":
    main()
