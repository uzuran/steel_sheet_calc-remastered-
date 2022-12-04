import tkinter as tk

import Components
from LoginScreen import LoginScreen
from RegisterUserScreen import RegisterUserScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()

    # Configure the root window.
        self.title("Steel sheet calculator.")
        self.geometry("350x200")
        self.eval("tk::PlaceWindow . center")

        # Enter label.
        self.enter_label = tk.Label(self, Components.main_label_conf())
        self.enter_label.pack(Components.option_for_labels())
        self.attributes()

        # Log in button.
        self.log_in_button = tk.Button(self, Components.main_button_conf_login())
        # Command for button
        self.log_in_button['command'] = self.open_login_window
        self.log_in_button.pack(Components.option_for_labels())

        # Register button.
        self.register_button = tk.Button(self, Components.main_button_conf_registration())
        # Command for button
        self.register_button['command'] = self.open_register_user_screen
        self.register_button.pack(Components.option_for_labels())

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
