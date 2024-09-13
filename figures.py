from input_data import InputData


class Figure:
    def __init__(self, height: int):
        self.height = height

    def triangle(self) -> None:
        for i in range(self):
            print(' ' * (self - i) + '*' * i * 2 + '*')

    def square(self) -> None:
        for i in range(self):
            print(self * '*')

    def triangle_revers(self) -> None:
        for i in range(self):
            print(' ' + ' ' * i + '*' * (self - i - 1) * 2 + '*')

    def rhombus(self) -> None:
        height_median = self // 2
        self.triangle()
        print('*' * self) if self % 2 != 0 else None
        triangle_revers(height_median)

    def switch_figure(self, num_figure):
        num_figure = num_figure

        match num_figure:
            case 1:
                print(f'печатаю треугольник с высотой {self.height}:', end='\n''\n')
                return Figure.triangle(self.height)
            case 2:
                print(f'печатаю квадрат с высотой {self.height}:', end='\n''\n')
                return Figure.square(self.height)
            case 3:
                print(f'печатаю обратный треугольник с высотой {self.height}:', end='\n''\n')
                return Figure.triangle_revers(self.height)
            case 4:
                print(f'печатаю ромб с высотой {self.height}:', end='\n''\n')
                return Figure.rhombus(self.height)
