import tkinter as tk

import Components
import OptionScreen
import RegisterUserScreen
from screens import LoginScreen


class StartPage(tk.Frame):
    def __init__(self, children, controller):
        tk.Frame.__init__(self, children)
        self.register_button = None
        self.log_in_button = None
        self.image_button_for_settings = None
        self.setting_button_image = None
        self.logo = None
        self.enter_label = None
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Enter label.
        self.enter_label = tk.Label(self, Components.main_label_conf())
        self.enter_label.pack()

        self.logo = tk.PhotoImage(file="img/logo.png")
        main_logo = tk.Label(self, image=self.logo)
        main_logo.pack()

        # Setting button.
        self.setting_button_image = tk.PhotoImage(file="img/settings-icon.png")
        self.image_button_for_settings = tk.Button(self, image=self.setting_button_image, borderwidth=0)
        self.image_button_for_settings.pack(anchor="e", padx=20)
        self.image_button_for_settings["command"] = lambda: self.controller.show_frame(OptionScreen.OptionPage)

        # Log in button.
        self.log_in_button = tk.Button(self, Components.main_button_conf_login())
        # Command for button
        self.log_in_button['command'] = lambda: self.controller.show_frame(LoginScreen.LoginPage)
        self.log_in_button.pack(Components.option_for_labels())

        # Register button.
        self.register_button = tk.Button(self, Components.main_button_conf_registration())
        # Command for button
        self.register_button['command'] = lambda: self.controller.show_frame(RegisterUserScreen.RegistrationPage)
        self.register_button.pack(Components.option_for_labels())
