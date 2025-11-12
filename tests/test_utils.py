from src.utils import read_json_operation
from unittest.mock import patch, Mock, mock_open

m = mock_open()


@patch("json.load")
@patch("builtins.open", m)
def test_read_json_operation(mock_open_file, mock_json_load):
    data = [{"amount": "100", "currency": "RUB"}]
    mock_json_load.return_value = data
    result = read_json_operation("test")
    assert result == data




