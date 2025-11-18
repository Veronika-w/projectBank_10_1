import json
from typing import Any
from unittest import mock

from src.utils import read_json_operation

# @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
# @patch("os.path.exists")
# @patch("os.path.getsize")
# def test_read_json_operation(mock_getsize, mock_exists, mock_open):
#     mock_exists.return_value = True
#     mock_getsize.return_value = 1
#     result = read_json_operation("test_file.json")
#     assert isinstance(result, dict), "Функция должна возвращать словарь"


@mock.patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_open: Any) -> None:
    result = read_json_operation("fake_path.json")
    assert result == []


@mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load: Any) -> None:
    result = read_json_operation("fake_path.json")
    assert result == []
