from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk

import Components
import Connection
import Languages


class CreateNewMaterial(tk.Toplevel):
    def __init__(self, child):
        super().__init__(child)

        self.geometry("350x450")
        self.title(Languages.current_lang["create_new_material_title"])

        # String variables for material entry
        self.material_type_variable = StringVar()
        self.m_identification_variable = StringVar()
        self.thickness_variable = StringVar()
        self.x_size_variable = StringVar()
        self.y_size_variable = StringVar()

        # Register new material window label.
        create_material_label = tk.Label(self, Components.create_new_material_label())
        create_material_label.pack()

        # Info material button.
        self.info_button_image = tk.PhotoImage(file="img/question.png")
        self.image_button_info = tk.Button(self, image=self.info_button_image, borderwidth=0)
        self.image_button_info.pack(side="top")
        self.image_button_info["command"] = self.info_material_registration

        # Basic information about registered material.
        type_material_label = tk.Label(self, text=Languages.current_lang["type_of_material_label"])
        type_material_label.pack()

        self.materials_types = ["st", "al", "sp"]

        drop_material_type = ttk.Combobox(self, values=self.materials_types, state="readonly")
        drop_material_type.current(0)  # Set the default selection
        drop_material_type.pack(side="top")
        self.selected_material = drop_material_type.get()

        material_id_label = tk.Label(self, text=Languages.current_lang["id_label"])
        material_id_label.pack()

        # ID entry.
        id_entry = tk.Entry(self, textvariable=self.m_identification_variable)
        id_entry.pack()

        # Material thickness.
        material_thickness_label = tk.Label(self, text=Languages.current_lang["thickness_label"])
        material_thickness_label.pack()

        # Material thickness entry.
        material_thickness_entry = tk.Entry(self, textvariable=self.thickness_variable)
        material_thickness_entry.pack()

        # Material size_x
        x_size_label = tk.Label(self, text=Languages.current_lang["x_size_label"])
        x_size_label.pack()

        # Material size_x entry
        self.x_size_entry = tk.Entry(self, textvariable=self.x_size_variable)
        self.x_size_entry.pack()

        # Material size_y
        y_size_label = tk.Label(self, text=Languages.current_lang["y_size_label"])
        y_size_label.pack()

        # Material size_y entry
        self.y_size_entry = tk.Entry(self, textvariable=self.y_size_variable)
        self.y_size_entry.pack()

        # Empty space
        empty_space = tk.Label(self, text=' ')
        empty_space.pack()

        # Button for material register.
        button_for_register_material = tk.Button(self, text=Languages.current_lang["registration_material_button"])
        button_for_register_material['command'] = lambda: [self.create_new_material_click()]
        button_for_register_material.pack()
        # Free space.

        empty_space = tk.Label(self, text='')
        empty_space.pack()

    # Function for button for add material to database.
    def create_new_material_click(self):
        get_material_id = self.m_identification_variable.get()
        get_thickness = self.thickness_variable.get()
        get_x_size = self.x_size_variable.get()
        get_y_size = self.y_size_variable.get()

        # Check if material is in database.
        Connection.check_if_material_is_exist_in_database(get_material_id)

        # Condition.
        if Connection.check_if_material_is_exist_in_database(get_material_id):
            Components.warning_material_is_exist_msg()

        elif self.selected_material == "st" and get_thickness != "" \
                and get_x_size.isdigit() \
                and get_y_size.isdigit():

            # If condition complete add material in to database.
            Connection.add_material_to_database(get_material_id, get_thickness, get_x_size, get_y_size)
            # Success registration Label.
            Components.registration_success()

        else:
            Components.warning_material_specification()

    # Info.
    def info_material_registration(self):
        info = msg.showinfo(title=Languages.current_lang["warning_title"],
                            message=Languages.current_lang["info_warning"],
                            parent=self
                            )
        return info