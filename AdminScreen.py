from tkinter import *
import tkinter as tk
from tkinter import ttk

import Components
from CreateNewMaterial import CreateNewMaterial
from ShowAllStMaterial import ShowAllStMaterial
import Languages


class AdminScreen(tk.Toplevel):

    def __init__(self, child, user_name_label_get):
        super().__init__(child)
        # setting tkinter window size
        self.child = child
        self.geometry("1000x600")
        self.title(Languages.current_lang["main_work_label"])
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

        main_label = tk.Label(self, Components.admin_label_conf())
        main_label.pack()

        # Check who is login
        Components.check_who_is_login(self, user_name_label_get)

        create_new_material_button = tk.Button(self, Components.create_new_material_button())
        create_new_material_button["command"] = self.open_create_material_window
        create_new_material_button.pack()

        # Add notebook of a materials to the second frame.
        notebook = ttk.Notebook(self)
        notebook.pack()

        frame1 = Frame(notebook, Components.option_for_size_frame())
        frame2 = Frame(notebook, Components.option_for_size_frame())
        frame3 = Frame(notebook, Components.option_for_size_frame())
        frame4 = Frame(notebook, Components.option_for_size_frame())
        frame5 = Frame(notebook, Components.option_for_size_frame())

        # Add notebook on screen.
        notebook.add(frame1, text=Languages.current_lang["frame1"])
        notebook.add(frame2, text=Languages.current_lang["frame2"])
        notebook.add(frame3, text=Languages.current_lang["frame3"])
        notebook.add(frame4, text=Languages.current_lang["frame4"])
        notebook.add(frame5, text=Languages.current_lang["frame5"])

        ShowAllStMaterial(frame1)

    # Function for create material in new window.
    def open_create_material_window(self):
        if not any(isinstance(x, tk.Toplevel) for x in self.winfo_children()):
            CreateNewMaterial(self)



