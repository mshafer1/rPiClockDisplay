from rpi_clock_display import config
import pigpio

pi = pigpio.pi()

pi.set_PWM_dutycycle(config.LED_pin, 2)
