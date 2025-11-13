from src.utils import read_json_operation
from unittest.mock import patch, mock_open


@patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
@patch('os.path.exists')
@patch('os.path.getsize')
def test_read_json_operation(mock_getsize, mock_exists, mock_open):
    mock_exists.return_value = True
    mock_getsize.return_value = 1
    result = read_json_operation('test_file.json')
    assert isinstance(result, dict), "Функция должна возвращать словарь"




