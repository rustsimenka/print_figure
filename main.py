from input_data import InputData
from figures import Figure
from figures import SwitchFigure


def main() -> None:
    input_data = InputData()
    height = input_data.input_height()
    num_figure = input_data.input_index(height)
    figure = Figure(height)
    choice_figure = SwitchFigure(num_figure, height)
    print('печать окончил' + '\n' + 'Нарисуем ещё одну!', end='\n\n')
    return main()


if __name__ == '__main__':
    main()
