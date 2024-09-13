
class InputData:

    def __init__(self):
        self.figures = {1: 'треугольник',
                        2: 'квадрат',
                        3: 'обратный треугольник',
                        4: 'ромб'}

    def display_figures(self) -> None:
        """Отображает доступные фигуры."""
        print("Доступные фигуры:")
        for key, figure in self.figures.items():
            print(f"{key}. {figure}")

    def check_correct(self, x: str) -> bool:
        """Возвращает True, если x состоит только из цифр, и False в противном случае."""
        return x.isdigit()

    def height(self) -> int:
        """Запрашивает высоту фигуры и проверяет корректность ввода."""
        print('Введите высоту фигуры')
        x = input()
        if self.check_correct(x) and int(x) > 1:
            return int(x)
        else:
            print('Некорректный ввод высоты, попробуйте ещё раз:', end='\n''\n')
            return self.height()

    def num_figure(self, height) -> int:
        """Запрашивает номер фигуры и проверяет корректность ввода."""
        self.height = height
        self.display_figures()
        print(f'Введите номер фигуры c высотой {self.height}:')
        input_num = input()
        if self.check_correct(input_num) and 0 < int(input_num) <= len(self.figures):
            return int(input_num)
        else:
            print('Некорректный ввод номера фигуры, попробуйте ещё раз:', end='\n''\n')
            return self.num_figure(height)