FULL_WIDTH = 0x1F
EMPTY = 0x0
LEFT_THREE = 0x1C
RIGHT_THREE = 0x07
SPACE = ord(" ")

TOP_BAR = [FULL_WIDTH] * 3 + [EMPTY] * 5

BOTTOM_BAR = [EMPTY] * 5 + [FULL_WIDTH] * 3

LEFT_BAR = [LEFT_THREE] * 8

RIGHT_BAR = [RIGHT_THREE] * 8

TOP_RIGHT = [FULL_WIDTH - 2 ** n for n in range(3)] + [RIGHT_THREE] * 5

TOP_LEFT = [FULL_WIDTH - 2 ** n for n in range(4, 1, -1)] + [RIGHT_THREE] * 5

BOTTOM_RIGHT = [RIGHT_THREE] * 5 + [FULL_WIDTH - 2 ** n for n in range(3, 0, -1)]

BOTTOM_LEFT = [LEFT_THREE] * 5 + [FULL_WIDTH - 2 ** n for n in range(2, 5)]

CHAR_LIST = [
    TOP_BAR,
    BOTTOM_BAR,
    LEFT_BAR,
    RIGHT_BAR,
    TOP_LEFT,
    TOP_RIGHT,
    BOTTOM_LEFT,
    BOTTOM_RIGHT,
]


def generate_big(lcd):
    lcd.lcd_load_custom_chars(CHAR_LIST)


CHAR_REVERSE_LOOKUP = {tuple(char): i for i, char in enumerate(CHAR_LIST)}

CHAR_MAP = {
    0: [
        CHAR_REVERSE_LOOKUP[tuple(o)] if isinstance(o, list) else o
        for o in [
            TOP_LEFT,
            TOP_BAR,
            TOP_BAR,
            TOP_RIGHT,
            LEFT_BAR,
            SPACE,
            SPACE,
            RIGHT_BAR,
            LEFT_BAR,
            SPACE,
            SPACE,
            RIGHT_BAR,
            BOTTOM_LEFT,
            BOTTOM_BAR,
            BOTTOM_BAR,
            BOTTOM_RIGHT,
        ]
    ],
    1: [
        CHAR_REVERSE_LOOKUP[tuple(o)] if isinstance(o, list) else o
        for o in [
            SPACE,
            SPACE,
            SPACE,
            RIGHT_BAR,
        ]
        * 4
    ],
}


def write_big(lcd, char, pos):
    parts = CHAR_MAP[char]
    for i in range(4):
        for j in range(4):
            lcd.lcd_display_string_pos(chr(parts[i * 4 + j]), j+1, pos + i)


if __name__ == "__main__":
    from rpi_clock_display import i2c_driver
    import time

    mylcd = i2c_driver.LCD()

    generate_big(mylcd)

    import time
    while True:
        write_big(mylcd, 0, 0)
        write_big(mylcd, 0, 5)
        write_big(mylcd, 0, 11)
        write_big(mylcd, 0, 16)
        time.sleep(2)
        write_big(mylcd, 1, 0)
        write_big(mylcd, 1, 5)
        write_big(mylcd, 1, 11)
        write_big(mylcd, 1, 16)

