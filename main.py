import tkinter as tk

import Languages
import LoginScreen
import RegisterUserScreen
import StartPage
import OptionScreen
import Connection


class App(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("400x450")
        self.eval("tk::PlaceWindow . center")

        Connection.create_tables()
        self.title(Languages.current_lang["main_work_label"])

        # creating a container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts

        for F in (StartPage.StartPage, LoginScreen.LoginPage, RegisterUserScreen.RegistrationPage,
                  OptionScreen.OptionPage):
            frame = F(self.container, self)

            # initializing frame of that object
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage.StartPage)

    def refresh(self):
        self.destroy()
        self.__init__()

    # to display the current frame passed as
    # parameter
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
