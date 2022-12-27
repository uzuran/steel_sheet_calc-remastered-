import tkinter as tk


import Components
from LoginScreen import LoginScreen
from RegisterUserScreen import RegisterUserScreen
import Languages
from OptionScreen import OpenWindowSettings


class App(tk.Tk):
    def __init__(self):
        super().__init__()

    # Configure the root window.
        self.geometry("350x200")
        self.eval("tk::PlaceWindow . center")
        self.put_all()

    def put_all(self):
        self.title(Languages.conf_lang["main_work_label"])
        # Enter label.
        self.enter_label = tk.Label(self, Components.main_label_conf())
        self.enter_label.pack(Components.option_for_labels())

        # Setting button.
        self.setting_button = tk.PhotoImage(file="img/settings-icon.png")
        self.button_for_setting = tk.Button(self, image=self.setting_button, borderwidth=0)
        self.button_for_setting.pack(anchor="e", padx=20)
        self.button_for_setting["command"] = self.open_window_for_settings

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

    # # Function for refresh labels and buttons.
    # def refresh(self):
    #     widgets = [f for f in self.children]
    #     for f_name in widgets:
    #         self.nametowidget(f_name).destroy()
    #     Languages.change_language("")
    #     self.put_all()

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

    # Open window for users settings.
    def open_window_for_settings(self):
        window = OpenWindowSettings(self)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()


if __name__ == "__main__":
    app = App()
    app.mainloop()



