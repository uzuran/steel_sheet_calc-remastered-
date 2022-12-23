import tkinter as tk
from tkinter import ttk


import Languages


class OpenWindowSettings(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("200x250")
        self.title(Languages.current_lang["settings_title"])

        # Dropdown menu for options
        self.drop_down_label = tk.Label(self, text=Languages.current_lang["choice_your_lang"])
        self.drop_down_label.pack(side="top")

        self.languages = ["English", "Czech"]

        drop = ttk.Combobox(self, values=self.languages)
        drop.current(0)
        drop.pack(side="top")

        # Button for save options
        self.save_button = tk.Button(self, text=Languages.current_lang["save_button"],
                                     command=Languages.change_language())
        self.save_button.pack(pady=10)

