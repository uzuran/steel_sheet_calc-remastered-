from tkinter import *
import tkinter as tk
from tkinter import ttk

import Components
import Connection
import Languages


class OpenWindowSettings(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("200x250")
        self.title(Languages.current_lang["user_create_button"])

        # Dropdown menu for options
        drop_down_label = tk.Label(self, text=Languages.current_lang["choice_your_lang"])
        drop_down_label.pack(side="top")

        self.drop = ttk.Combobox(self, )
        self.drop.pack(side="top")

        self.save_button = tk.Button(self, text=Languages.current_lang["save_button"])
        self.save_button.pack(pady=10)
