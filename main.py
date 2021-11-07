#  -----------------------------------------------------------
# Tic Tac Toe
#
# Author:   Valerii Tsekhmaistruk
# GitHub: https://github.com/ValeriiTsekhmaistruk/TicTacToe
# Email: valeriitseh1305@gmail.com
# -----------------------------------------------------------

from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class TicTacToeApp(App):

    def build(self):
        self.figure = 'O'  # default, the first step - 'O'
        self.arr = ['_', '_', '_', '_', '_', '_', '_', '_', '_']  # cell list

        def press_btn(instance):
            if not instance.text.isdigit():
                return

            self.arr[int(instance.text)] = self.figure  # add figure in cell list by index

            if self.figure == 'O':  # draw 'O' in cell
                instance.color = (0, 0, 1, 1)
                instance.text = self.figure
                instance.font_size = 70
                self.figure = 'X'
            else:  # draw 'X' in cel
                instance.text = self.figure
                instance.color = (1, 0, 0, 1)
                instance.font_size = 70
                self.figure = 'O'

            check_combination(self.arr)     # check wining combination

        def check_combination(arr):
            wining_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

            for (x, y, z) in wining_combination:    # if there is a winner
                if arr[x] == arr[y] and arr[y] == arr[z] and (arr[x] == 'X' or arr[x] == 'O'):
                    self.label.text = f'{arr[x]} WON'
                    self.field.disabled = True
                    Clock.schedule_once(restart_game, 1.5)
                    return

            if '_' not in arr:  # if draw
                self.label.text = 'DRAW'
                self.field.disabled = True
                Clock.schedule_once(restart_game, 1.5)  # wait 1.5 sec
                return

        def restart_game(dt):  # clear field and cell list
            self.field.clear_widgets()
            self.label.text = 'PLAY'
            self.field.disabled = False
            self.figure = 'O'
            self.arr = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            render_field()

        def render_field():  # add button in GrigLayout
            for id_num in range(9):
                self.field.add_widget(Button(text=str(id_num), font_size=0, on_press=press_btn, color=(0, 0, 0, 0)))
                # cell index is written to Button.text

        main_bl = BoxLayout(orientation='vertical', spacing=5, padding=3)
        self.label = Label(text='PLAY', font_size=50, size_hint=(1, .3))
        self.field = GridLayout(cols=3, spacing=3)

        render_field()

        main_bl.add_widget(self.label)
        main_bl.add_widget(self.field)

        return main_bl


if __name__ == '__main__':
    TicTacToeApp().run()
