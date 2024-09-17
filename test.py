import pytest
from unittest.mock import patch
from io import StringIO
from input_data import InputData


def test_1():
    assert 1 == 1


class TestInputData:

    @pytest.mark.parametrize("input_value, expected", [
        ("123", True),
        ("abc", False),
        ("123abc", False),
        ("", False),
    ])
    def test_check_correct(self, input_value, expected):
        input_data = InputData()
        assert input_data.check_correct(input_value) == expected

    @patch('builtins.input', side_effect=['2'])
    def test_height_correct(self, mock_input):
        input_data = InputData()
        result = input_data.height()
        assert result == 2

    @patch('builtins.input', side_effect=['-1', '0', '3'])
    def test_height_incorrect(self, mock_input):
        input_data = InputData()
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            result = input_data.height()
            assert result == 3  # Последнее корректное значение
            output = mock_output.getvalue()
            assert 'Некорректный ввод высоты' in output

    @patch('builtins.input', side_effect=['2'])
    def test_num_figure_correct(self, mock_input):
        input_data = InputData()
        height = 2  # Задаем корректную высоту
        result = input_data.num_figure(height)
        assert result == 2

    @patch('builtins.input', side_effect=['-1', '5', '1'])
    def test_num_figure_incorrect(self, mock_input):
        input_data = InputData()
        height = 3  # Задаем высоту, чтобы было 3 фигуры
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            result = input_data.num_figure(height)
            assert result == 1  # Последнее корректное значение
            output = mock_output.getvalue()
            assert 'Некорректный ввод номера фигуры' in output

    def test_display_figures(self):
        input_data = InputData()

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            input_data.display_figures()
            output = mock_output.getvalue()

        expected_output = "Доступные фигуры:\n1. треугольник\n2. квадрат\n3. обратный треугольник\n4. ромб\n"
        assert output == expected_output
