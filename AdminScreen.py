import mysql.connector
from tkinter import messagebox as msg
from tkinter import *
import tkinter as tk
from tkinter import ttk
from CreateNewMaterial import CreateNewMaterial
from ShowAllStMaterial import ShowAllStMaterial
from Connection import *

my_cursor = mydb.cursor(buffered=True)


class AdminScreen(tk.Toplevel):

    def __init__(self, child, user_name_label_get):
        super().__init__(child)
        self.title("Steel sheet calculator.")
        # setting tkinter window size
        self.child = child
        self.geometry("1000x600")
        self.title("Steel sheet calculator.")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

        # Main label.
        label_option = {"text": "Steel sheet calculator",
                        "bg": "#d1dffa",
                        "width": "300",
                        "height": "2",
                        "font": "Calibri, 13"}

        main_label = Label(self, **label_option)
        main_label.pack()

        # Check users,  who is log in.
        user_name_label = user_name_label_get

        check_user = Label(self, text=str(user_name_label.capitalize()) + " Is log in now.",
                           fg="green",
                           font="Arial",

                           )
        check_user.pack(anchor="e")

        create_new_material = Button(self)
        create_new_material["text"] = "Create new material"
        create_new_material["command"] = self.open_create_material_window
        create_new_material.pack()

        # Add notebook of a materials to the second frame.
        notebook = ttk.Notebook(self)
        notebook.pack()

        # Add frame options.
        frame_options = {"width": "500",
                         "height": "400"}

        frame1 = Frame(notebook, **frame_options)
        frame2 = Frame(notebook, **frame_options)
        frame3 = Frame(notebook, **frame_options)
        frame4 = Frame(notebook, **frame_options)
        frame5 = Frame(notebook, **frame_options)

        # Add notebook on screen.
        notebook.add(frame1, text="Steel material")
        notebook.add(frame2, text="Aluminium material")
        notebook.add(frame3, text="Stainless steel material")
        notebook.add(frame4, text="Special material")
        notebook.add(frame5, text="Write off")

        ShowAllStMaterial(frame1)

    # Function for create material in new window.
    def open_create_material_window(self):
        window = CreateNewMaterial(self)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()



