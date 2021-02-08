import pytest

import datetime

# NOTE: 2006 started on a Sunday, so day of month and week align
@pytest.mark.parametrize(
    "current_time, expected_string",
    (
        (datetime.datetime(2006, 1, 1, 6, 0), " 6:00 AM\nSunday January  1, 2006"),
        (datetime.datetime(2006, 1, 1, 16, 0), " 4:00 PM\nSunday January  1, 2006"),
        (datetime.datetime(2006, 1, 2, 6, 0), " 6:00 AM\nMonday January  2, 2006"),
    ),
)
def test___current_time__display__writes_expected_string_to_display(
    current_time, expected_string, mock_i2c_driver, freezer
):
    from rpi_clock_display import display

    freezer.move_to(current_time)

    display.main(1)

    result = mock_i2c_driver.get_displayed_strings()
    assert result == expected_string
