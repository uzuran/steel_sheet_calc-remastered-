import mysql.connector
from tkinter import messagebox as msg
from tkinter import *
import tkinter as tk
from ShowAllStMaterial import ShowAllStMaterial


# Db connect.

mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="datapass",
                               database='users_data')

my_cursor = mydb.cursor(buffered=True)


class CreateNewMaterial(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title("Create new material.")

        new_material_label_option = {
            "text": "Create new material.",
            "bg": "#d1dffa",
            "width": "300",
            "height": "2",
            "font": "Calibri, 12"
        }

        global material_type, type_material_entry, m_identification, ID_entry, \
            thickness, material_thickness_entry
        global xsize, x_size_entry, ysize, y_size_entry

        # String variables for material entry
        material_type = StringVar()
        m_identification = StringVar()
        thickness = StringVar()
        xsize = StringVar()
        ysize = StringVar()

        # Register new material window label.
        create_material_label = Label(self, **new_material_label_option)
        create_material_label.pack()

        # Basic information about registered material.
        type_material = Label(self, text='Type material')
        type_material.pack()

        type_material_entry = Entry(self, textvariable=material_type)
        type_material_entry.pack()

        material_id = Label(self, text="Id")
        material_id.pack()

        # ID entry.
        ID_entry = Entry(self, textvariable=m_identification)
        ID_entry.pack()

        # Material thickness.
        material_thickness = Label(self, text='Thickness')
        material_thickness.pack()

        # Material thickness entry.
        material_thickness_entry = Entry(self, textvariable=thickness)
        material_thickness_entry.pack()

        # Material size_x
        x_size = Label(self, text='X_size')
        x_size.pack()

        # Material size_x entry
        x_size_entry = Entry(self, textvariable=xsize)
        x_size_entry.pack()

        # Material size_y
        y_size = Label(self, text='Y_size')
        y_size.pack()

        # Material size_y entry
        y_size_entry = Entry(self, textvariable=ysize)
        y_size_entry.pack()

        # Empty space
        e_space = Label(self, text=' ')
        e_space.pack()

        # Button for material register.
        button_for_register_material = Button(self, text='Register material')
        button_for_register_material['command'] = lambda: [self.create_new_material_click()]
        button_for_register_material.pack()
        # Free space.
        free_space = Label(self, text='')
        free_space.pack()

        # Free space.
        free_space = Label(self, text='')
        free_space.pack()

        # Free space.
        free_space = Label(self, text='')
        free_space.pack()

        info_label = Label(self, text='Please register your new material.')
        info_label.pack()

    # Function for button for add material to database.
    def create_new_material_click(self):
        get_material_type = material_type.get()
        get_material_id = m_identification.get()
        get_thickness = thickness.get()
        get_xsize = xsize.get()
        get_ysize = ysize.get()

        # Check if material exist  in database
        sql = "SELECT * FROM st_material WHERE id = '%s'" % get_material_id
        my_cursor.execute(sql)

        def killer():
            reg_suc.destroy()

        # Condition.
        if my_cursor.fetchone():
            msg.showwarning(title="Warning!", message="This material already exist!")

        elif get_material_type == "st" and get_thickness != ""\
                and get_xsize.isdigit()\
                and get_ysize.isdigit():

            # If condition complete add material in to database.
            sql = "INSERT INTO st_material (id, thickness, size_x, size_y) VALUES(%s, %s, %s, %s)"
            val = (get_material_id, get_thickness, get_xsize, get_ysize)
            my_cursor.execute(sql, val)
            mydb.commit()
            # Success registration Label.
            reg_suc = Label(self, text=f'You register ID: {m_identification.get()}'
                                                            f' Thickness: {thickness.get()} '
                                                            f'X: {xsize.get()} Y: {ysize.get()}', fg="green")
            reg_suc.pack()
            reg_suc.after(2000, killer)

        else:
            msg.showwarning(title="Warning!", message="You cant add this specification of material.")

