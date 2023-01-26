import tkinter as tk
from tkinter import ttk
import Languages


import StartPage


class OptionPage(tk.Frame):

    def save(self, value):
        Languages.change_language(Languages.lang[value])

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.put_all()

    def put_all(self):
            # Dropdown menu for options
            self.drop_down_label = tk.Label(self)
            self.drop_down_label["text"] = Languages.current_lang["choice_your_lang"]
            self.drop_down_label.pack(side="top")

            # Back to main page button.
            self.back_button = tk.PhotoImage(file="img/back.png")
            self.button_for_back = tk.Button(self, image=self.back_button, borderwidth=0)
            self.button_for_back['command'] = lambda: self.controller.show_frame(StartPage.StartPage)
            self.button_for_back.pack()

            self.languages = [Languages.current_lang["language_en"], Languages.current_lang["language_cz"]]

            drop = ttk.Combobox(self, values=self.languages, state="readonly")

            drop.current(0)
            drop.pack(side="top")

            # Button for save options
            self.save_button = tk.Button(self, text=Languages.current_lang["save_button"])
            self.save_button["command"] = lambda: [self.save(drop.current()), self.controller.refresh()]
            self.save_button.pack(pady=10)
