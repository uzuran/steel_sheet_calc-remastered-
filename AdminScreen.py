import mysql.connector
from tkinter import messagebox as msg
from tkinter import *
import tkinter as tk
from tkinter import ttk
from CreateNewMaterial import CreateNewMaterial
from ShowAllStMaterial import ShowAllStMaterial


# Db connect.
mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="datapass",
                               database='car_wash_material')

my_cursor = mydb.cursor(buffered=True)


class AdminScreen(tk.Toplevel):

    def __init__(self, child, user_name_v):
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
        user_name_label = user_name_v

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

        my_frame1 = Frame(notebook, **frame_options)
        my_frame2 = Frame(notebook, **frame_options)
        my_frame3 = Frame(notebook, **frame_options)
        my_frame4 = Frame(notebook, **frame_options)
        my_frame5 = Frame(notebook, **frame_options)

        # Add notebook on screen.
        notebook.add(my_frame1, text="Steel material")
        notebook.add(my_frame2, text="Aluminium material")
        notebook.add(my_frame3, text="Stainless steel material")
        notebook.add(my_frame4, text="Special material")
        notebook.add(my_frame5, text="Write off")

        ShowAllStMaterial(my_frame1)

    # Function for create material in new window.
    def open_create_material_window(self):
        window = CreateNewMaterial(self)
        window.grab_set()
        window.lift()
        window.focus_force()
        window.grab_release()



