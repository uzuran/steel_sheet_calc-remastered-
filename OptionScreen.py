import tkinter as tk
from tkinter import ttk
import Languages


class OpenWindowSettings(tk.Toplevel):

    def save(self, value):
        Languages.change_language(Languages.lang[value])

    def __init__(self, parent):
        super().__init__(parent)
        app = parent

        self.geometry("200x250")
        self.title(Languages.current_lang["settings_title"])

        # Dropdown menu for options
        self.drop_down_label = tk.Label(self)
        self.drop_down_label["text"] = Languages.current_lang["choice_your_lang"]
        self.drop_down_label.pack(side="top")
        self.languages = [Languages.current_lang["language_en"], Languages.current_lang["language_cz"]]

        drop = ttk.Combobox(self, values=self.languages, state="readonly")
        drop.current(0)
        drop.pack(side="top")

        # Button for save options
        self.save_button = tk.Button(self, text=Languages.current_lang["save_button"])
        self.save_button["command"] = lambda: [self.save(drop.current()), app.refresh()]
        self.save_button.pack(pady=10)

