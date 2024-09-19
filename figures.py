from input_data import InputData


class Figure:
    def __init__(self, height: int):
        self.height = height

    def print_triangle(self) -> None:
        for i in range(self.height):
            print(' ' * (self.height - i) + '*' * i * 2 + '*')

    def print_square(self) -> None:
        for _ in range(self.height):
            print('*' * self.height)

    def print_triangle_revers(self) -> None:
        for i in range(self.height):
            print(' ' + ' ' * i + '*' * (self.height - i - 1) * 2 + '*')

    def print_rhombus(self) -> None:

        for i in range(self.height // 2):
            print(' ' * (self.height // 2 - i) + '*' * i * 2 + '*')
        if self.height % 2 != 0:
            print('*' * self.height)
        for k in range(self.height // 2):
            print(' ' + ' ' * k + '*' * (self.height // 2 - k - 1) * 2 + '*')


class SwitchFigure:
    def __init__(self, num_figure, height):
        self.num_figure = num_figure
        self.height = height

        match num_figure:
            case 1:
                print(f'печатаю треугольник с высотой {self.height}:', end='\n''\n')
                return Figure.print_triangle(self)
            case 2:
                print(f'печатаю квадрат с высотой {self.height}:', end='\n''\n')
                return Figure.print_square(self)
            case 3:
                print(f'печатаю обратный треугольник с высотой {self.height}:', end='\n''\n')
                return Figure.print_triangle_revers(self)
            case 4:
                print(f'печатаю ромб с высотой {self.height}:', end='\n''\n')
                return Figure.print_rhombus(self)
