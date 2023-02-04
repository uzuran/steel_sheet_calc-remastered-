import tkinter as tk
from tkinter import ttk

import Components
import Languages


import StartPage


class OptionPage(tk.Frame):

    def save(self, value):
        Languages.change_language(Languages.lang[value])

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.create_widgets()

    def create_widgets(self):

            # Dropdown menu for options
            self.option_screen_label = tk.Label(self, Components.label_for_option_screen())
            self.option_screen_label.pack()

            # Back to main page image button.
            self.back_image = tk.PhotoImage(file="img/back.png")
            self.button_image_for_back = tk.Button(self, image=self.back_image, borderwidth=0)
            self.button_image_for_back['command'] = lambda: self.controller.show_frame(StartPage.StartPage)
            self.button_image_for_back.pack()

            self.languages = [Languages.current_lang["language_en"], Languages.current_lang["language_cz"]]

            drop = ttk.Combobox(self, values=self.languages, state="readonly")
            drop.current(0)
            drop.pack(side="top")

            # Button for save options
            self.save_button = tk.Button(self, text=Languages.current_lang["save_button"])
            self.save_button["command"] = lambda: [self.save(drop.current()), self.controller.refresh()]
            self.save_button.pack(pady=10)
