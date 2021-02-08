from unittest import mock

import pytest

import sys


@pytest.fixture()
def mock_smbus(mocker):
    _mock = mocker.patch.dict(sys.modules, {"smbus": mock.MagicMock()})
    yield _mock


@pytest.fixture()
def mock_i2c_driver(mocker, mock_smbus):
    from rpi_clock_display import i2c_driver

    mock = mocker.patch.object(i2c_driver, "LCD")

    def get_displayed_strings():
        calls = mock.return_value.lcd_display_string.call_args_list
        return "\n".join([c[0][0] for c in calls])

    mock.get_displayed_strings = get_displayed_strings
    yield mock
