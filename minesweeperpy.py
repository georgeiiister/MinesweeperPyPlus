import tkinter as tk
import random
import tkinter.messagebox as mb

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
            self.config(state='disabled', text=':(')
        else:
            self.config(state='disabled', text='ok')


class MFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)

    def create_widgets(self):
        size = get_tuning_item('size_game_field')
        size_game_field_x = range(size[0])
        size_game_field_y = range(size[1])

        game_field = {(x, y): MButton(master=self, xy=(x, y)) for x in size_game_field_x for y in size_game_field_y}

        bombs = random.sample(population=tuple(game_field.keys()), k=get_tuning_item(number_of_bombs_coordinates))

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


root = MWin()

root.mainloop()
