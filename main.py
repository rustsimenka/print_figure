from input_data import InputData
from figures import Figure
from figures import SwitchFigure


def commands() -> None:
    input_data = InputData()
    height = input_data.height()
    num_figure = input_data.num_figure(height)
    figure = Figure(height)
    choice_figure = SwitchFigure(num_figure, height)


if __name__ == '__main__':
    commands()
