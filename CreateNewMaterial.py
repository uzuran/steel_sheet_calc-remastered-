from tkinter import *
import tkinter as tk

import Components
import Connection
import Languages


class CreateNewMaterial(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title(Languages.current_lang["user_create_button"])

        # String variables for material entry
        self.material_type = StringVar()
        self.m_identification = StringVar()
        self.thickness = StringVar()
        self.x_size = StringVar()
        self.y_size = StringVar()

        # Register new material window label.
        create_material_label = tk.Label(self, Components.create_new_material_label())
        create_material_label.pack()

        # Basic information about registered material.
        type_material = tk.Label(self, text=Languages.current_lang["type_of_material_label"])
        type_material.pack()

        type_material_entry = tk.Entry(self, textvariable=self.material_type)
        type_material_entry.pack()

        material_id = tk.Label(self, text=Languages.current_lang["id_label"])
        material_id.pack()

        # ID entry.
        ID_entry = tk.Entry(self, textvariable=self.m_identification)
        ID_entry.pack()

        # Material thickness.
        material_thickness = tk.Label(self, text=Languages.current_lang["thickness_label"])
        material_thickness.pack()

        # Material thickness entry.
        material_thickness_entry = tk.Entry(self, textvariable=self.thickness)
        material_thickness_entry.pack()

        # Material size_x
        x_size = tk.Label(self, text=Languages.current_lang["x_size_label"])
        x_size.pack()

        # Material size_x entry
        self.x_size_entry = tk.Entry(self, textvariable=self.x_size)
        self.x_size_entry.pack()

        # Material size_y
        y_size = tk.Label(self, text=Languages.current_lang["y_size_label"])
        y_size.pack()

        # Material size_y entry
        self.y_size_entry = tk.Entry(self, textvariable=self.y_size)
        self.y_size_entry.pack()

        # Empty space
        e_space = tk.Label(self, text=' ')
        e_space.pack()

        # Button for material register.
        button_for_register_material = tk.Button(self, text=Languages.current_lang["registration_material_button"])
        button_for_register_material['command'] = lambda: [self.create_new_material_click()]
        button_for_register_material.pack()
        # Free space.
        free_space = tk.Label(self, text='')
        free_space.pack()

        # Free space.
        free_space = tk.Label(self, text='')
        free_space.pack()

        # Free space.
        free_space = tk.Label(self, text='')
        free_space.pack()

        info_label = tk.Label(self, text=Languages.current_lang["registration_material_label"])
        info_label.pack()

    # Function for button for add material to database.
    def create_new_material_click(self):
        get_material_type = self.material_type.get()
        get_material_id = self.m_identification.get()
        get_thickness = self.thickness.get()
        get_x_size = self.x_size.get()
        get_y_size = self.y_size.get()

        # Check if material is in database.
        Connection.check_if_material_is_exist_in_database(get_material_id)

        # Condition.
        if Connection.check_if_material_is_exist_in_database(get_material_id):
            Components.warning_material_is_exist_msg()

        elif get_material_type == "st" and get_thickness != ""\
                and get_x_size.isdigit()\
                and get_y_size.isdigit():

            # If condition complete add material in to database.
            Connection.add_material_to_database(get_material_id, get_thickness, get_x_size, get_y_size)
            # Success registration Label.
            Components.registration_success()

        else:
            Components.warning_material_specification()

