class InputData:
    def __init__(self):

        self.figures = {1: 'треугольник',
                        2: 'квадрат',
                        3: 'обратный треугольник',
                        4: 'ромб'}

    def input_data(self) -> int:
        """Возвращает int, если input_data состоит только из цифр"""
        data = input()
        if data.isdigit():
            return int(data)
        else:
            print('Некорректный ввод числа. Введите целое число:', end='\n''\n')
            return self.input_data()

    def check_height(self, height) -> bool:
        """Возвращает True, если input_data True и больше нуля."""
        return height > 0

    def check_index(self, index) -> bool:
        """Возвращает True, если input_data True и в диапазоне от нуля до длины списка фигур"""
        return 0 < index <= len(self.figures)

    def input_height(self) -> int:
        """Запрашивает высоту фигуры"""
        print('Введите высоту фигуры:')
        height = self.input_data()
        if self.check_height(height):
            return height
        else:
            print('Некорректный ввод высоты, попробуйте ещё раз:', end='\n''\n')
            return self.input_height()

    def input_index(self, height) -> int:
        """Запрашивает номер фигуры"""
        self.display_figures()
        print(f'Введите номер фигуры c высотой {height}:')
        index = self.input_data()
        if self.check_index(index) and 0 < index <= len(self.figures):
            return index
        else:
            print('Некорректный ввод номера фигуры, попробуйте ещё раз:', end='\n''\n')
            return self.input_index()

    def display_figures(self) -> None:
        """Отображает доступные фигуры"""
        print("Доступные фигуры:")
        for key, figure in self.figures.items():
            print(f"{key}. {figure}")
