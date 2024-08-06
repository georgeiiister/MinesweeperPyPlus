import tkinter as tk
import random


class MButton(tk.Button):
    def __init__(self, master, xy, width=None, height=None):
        tk.Button.__init__(self, master=master, width=width, height=height)
        self.__xy = xy

    @property
    def xy(self):
        return self.__xy


class MFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)

    def create_widgets(self):
        size_game_field = get_tuning_item('size_game_field')
        size_game_field_x = range(size_game_field[0])
        size_game_field_y = range(size_game_field[1])

        game_field = {(x, y): MButton(master=self, xy=(x, y)) for x in size_game_field_x for y in size_game_field_y}

        for item in game_field:
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
    tuning_dict = {'size_game_field': (4, 4)}
    return tuning_dict


def get_tuning_item(item_code) -> tuple:
    return get_tuning_dict()[item_code]


root = MWin()

root.mainloop()