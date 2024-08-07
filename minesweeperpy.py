import tkinter as tk
import random
import tkinter.messagebox as mb
import logging

logging.basicConfig(filename='MinesweeperPy.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

size_game_field = 'size_game_field'
number_of_bombs_coordinates = 'number_of_bombs_coordinates'
title_for_boom = 'title_for_boom'
message_for_boom = 'message_for_boom'


class MButton(tk.Button):
    def __init__(self, master, xy, width=None, height=None):
        tk.Button.__init__(self, master=master, command=self.check_bomb, width=width, height=height, text='?')
        self.__xy = xy
        self.__bomb = False

    @property
    def bomb(self):
        return self.__bomb

    @bomb.setter
    def bomb(self, value):
        self.__bomb = value

    @property
    def xy(self):
        return self.__xy

    def check_bomb(self):
        if self.bomb:
            mb.showinfo(title=get_tuning_item(title_for_boom), message=get_tuning_item(message_for_boom))
            self.__set_disabled_boom()
        else:
            self.__set_disabled_ok()

    def __set_disabled_ok(self):
        self.config(state='disabled', text='ok')

    def __set_disabled_boom(self):
        self.config(state='disabled', text=':(')


class MFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)
        self.__count_check_bomb = 0
        self.__size_x = None
        self.__size_y = None

    def __set_count_check_bomb(self):
        self.__count_check_bomb += 1

    @property
    def count_check_bomb(self):
        return self.__count_check_bomb

    @property
    def size_x(self):
        return self.__size_x

    @property
    def size_y(self):
        return self.__size_y

    def create_widgets(self):
        size = get_tuning_item('size_game_field')
        logging.debug(f'size game field {size}')

        self.__size_x = size[0]
        self.__size_y = size[1]

        range_x = range(self.__size_x)
        range_y = range(self.__size_y)

        game_field = {(x, y): MButton(master=self, xy=(x, y)) for x in range_x for y in range_y}

        bombs = random.sample(population=tuple(game_field.keys()), k=get_tuning_item(number_of_bombs_coordinates))
        logging.debug(f'bombs coordinate {bombs}')

        for item in game_field:
            if item in bombs:
                game_field[item].bomb = True
            game_field[item].grid(column=item[0], row=item[1])


class MWin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('MinesweeperPy')
        self.geometry('500x500')
        self.set_frame()

        self.frame.create_widgets()

    def set_frame(self):
        self.frame = MFrame(self)
        self.frame.grid()


def get_tuning_dict() -> dict:
    tuning_dict = {size_game_field: (3, 3),
                   number_of_bombs_coordinates: 1,
                   title_for_boom: 'it is bomb',
                   message_for_boom: 'BOOM!'}
    return tuning_dict


def get_tuning_item(item_code) -> tuple | int | str:
    return get_tuning_dict()[item_code]


if __name__ == '__main__':
    logging.debug(f'start debug')
    root = MWin()
    root.mainloop()
