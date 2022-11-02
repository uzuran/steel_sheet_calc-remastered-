import tkinter as tk
from tkinter import *
from LoginScreen import LoginScreen
from RegisterUserScreen import RegisterUserScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()

    # configure the root window
        self.title("Steel sheet calculator.")
        self.geometry("350x200")
        self.eval("tk::PlaceWindow . center")

        options = {"padx": 5, "pady": 5}
        enter_label_options = {"text": "Please login, or register.",
                                "bg": "#d1dffa",
                                "width": "300",
                                "height": "2",
                                "font": "Calibri, 12"}

        # Enter label.
        self.enter_label = Label(self, **enter_label_options)
        self.enter_label.pack(**options)
        self.attributes()

        # Options for buttons.
        btn_options_l = {"text": "Log in",
                         "width": "30",
                         "height": "2"
                         }

        # Log in button.
        self.log_in_button = Button(self, **btn_options_l)
        # Command for button
        self.log_in_button['command'] = self.open_login_window
        self.log_in_button.pack(**options)

        btn_options_r = {"text": "Register",
                         "width": "30",
                         "height": "2"

                         }

        # Register button.
        self.register_button = Button(self, **btn_options_r)
        # Command for button
        self.register_button['command'] = self.open_register_user_screen
        self.register_button.pack(**options)

    # Open login screen window function.
    def open_login_window(self):
        window = LoginScreen(self)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()
        self.wm_state('iconic')

    # Open window for users registration.
    def open_register_user_screen(self):
        window = RegisterUserScreen(self)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()


if __name__ == "__main__":
    app = App()
    app.mainloop()
