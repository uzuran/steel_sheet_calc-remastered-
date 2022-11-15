from tkinter import messagebox as msg
from tkinter import *
import tkinter as tk
from Connection import *
from ShowAllStMaterial import ShowAllStMaterial


# Db connect.


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

        # String variables for material entry
        self.material_type = StringVar()
        self.m_identification = StringVar()
        self.thickness = StringVar()
        self.x_size = StringVar()
        self.y_size = StringVar()

        # Register new material window label.
        create_material_label = Label(self, **new_material_label_option)
        create_material_label.pack()

        # Basic information about registered material.
        type_material = Label(self, text='Type material')
        type_material.pack()

        type_material_entry = Entry(self, textvariable=self.material_type)
        type_material_entry.pack()

        material_id = Label(self, text="Id")
        material_id.pack()

        # ID entry.
        ID_entry = Entry(self, textvariable=self.m_identification)
        ID_entry.pack()

        # Material thickness.
        material_thickness = Label(self, text='Thickness')
        material_thickness.pack()

        # Material thickness entry.
        material_thickness_entry = Entry(self, textvariable=self.thickness)
        material_thickness_entry.pack()

        # Material size_x
        x_size = Label(self, text='X_size')
        x_size.pack()

        # Material size_x entry
        x_size_entry = Entry(self, textvariable=self.x_size)
        x_size_entry.pack()

        # Material size_y
        y_size = Label(self, text='Y_size')
        y_size.pack()

        # Material size_y entry
        y_size_entry = Entry(self, textvariable=self.y_size)
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
        get_material_type = self.material_type.get()
        get_material_id = self.m_identification.get()
        get_thickness = self.thickness.get()
        get_x_size = self.x_size.get()
        get_y_size = self.y_size.get()

        # Check if material exist  in database
        sql = "SELECT * FROM st_material WHERE id = '%s'" % get_material_id
        my_cursor.execute(sql)

        def killer():
            reg_suc.destroy()

        # Condition.
        if my_cursor.fetchone():
            msg.showwarning(title="Warning!", message="This material already exist!")

        elif get_material_type == "st" and get_thickness != ""\
                and get_x_size.isdigit()\
                and get_y_size.isdigit():

            # If condition complete add material in to database.
            sql = "INSERT INTO st_material (id, thickness, size_x, size_y) VALUES(%s, %s, %s, %s)"
            val = (get_material_id, get_thickness, get_x_size, get_y_size)
            my_cursor.execute(sql, val)
            mydb.commit()
            # Success registration Label.
            reg_suc = Label(self, text=f'You register ID: {self.m_identification.get()}'
                                                           f' Thickness: {self.thickness.get()} '
                                                           f'X: {self.x_size.get()} Y: {self.y_size.get()}',
                                                           fg="green")
            reg_suc.pack()
            reg_suc.after(2000, killer)

        else:
            msg.showwarning(title="Warning!", message="You cant add this specification of material.")

