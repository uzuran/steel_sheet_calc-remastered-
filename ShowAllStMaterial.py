from tkinter import ttk
import tkinter as tk


import Connection
import Components
import Languages


class ShowAllStMaterial:
    def __init__(self, frame1):
        super().__init__()
        self.frame1 = frame1

        # Select all material from database.
        Connection.select_all_material()
        my_result = Connection.cursor_fetch_all()

        wrapper = tk.LabelFrame(frame1, text=Languages.current_lang["frame1"])
        wrapper.pack(fill="both", expand=1)

        # SCROLL BAR
        scroll_bar = tk.Scrollbar(frame1, orient=tk.VERTICAL)
        self.my_tree = ttk.Treeview(wrapper, selectmode='browse', height=20)

        # Insert treeview ----->>
        self.my_tree.pack()
        # Binding my_tree for double click and select id material.
        self.my_tree.bind("<Double-1>", self.get_row)

        self.my_tree.configure(yscrollcommand=scroll_bar.set)
        self.my_tree.configure(selectmode="extended")

        # Number of columns
        self.my_tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        # Show headings
        self.my_tree['show'] = 'headings'

        # Width of columns and alignment
        self.my_tree.column("1", width=150, anchor='c')
        self.my_tree.column("2", width=150, anchor='c')
        self.my_tree.column("3", width=150, anchor='c')
        self.my_tree.column("4", width=150, anchor='c')
        self.my_tree.column("5", width=150, anchor='c')
        self.my_tree.column("6", width=150, anchor='c')
        self.my_tree.column("7", width=150, anchor='c')

        # Headings.
        # Headings.
        self.my_tree.heading("1", text=Languages.current_lang["treeview_id"])
        self.my_tree.heading("2", text=Languages.current_lang["treeview_thickness"])
        self.my_tree.heading("3", text=Languages.current_lang["treeview_x"])
        self.my_tree.heading("4", text=Languages.current_lang["treeview_y"])
        self.my_tree.heading("5", text=Languages.current_lang["treeview_in_storage"])
        self.my_tree.heading("6", text=Languages.current_lang["treeview_order"])
        self.my_tree.heading("7", text=Languages.current_lang["treeview_write_off"])
        for dt in my_result:
            self.my_tree.insert("", 'end', iid=dt[0], text=dt[0],
                                values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

        # Delete material button
        self.delete_material_button = tk.Button(self.frame1, Components.delete_material_button())
        self.delete_material_button["command"] = self.delete
        self.delete_material_button.pack(side=tk.LEFT)

        # Update material button.
        self.update_material_button = tk.Button(self.frame1, Components.update_records_button())
        self.update_material_button["command"] = self.build_tree
        self.update_material_button.pack(side=tk.LEFT)

        # TODO: multi language.
        # Search label
        label_for_search = tk.Label(self.frame1, text="Search: ")
        label_for_search.pack(side=tk.LEFT, ipady=3)

        self.id_variable_string = tk.StringVar()

        # Search entry.
        self.entry_search = tk.Entry(self.frame1, textvariable=self.id_variable_string)
        self.entry_search.pack(side=tk.LEFT, ipady=3)
        self.entry_search.bind("<KeyRelease>", self.search)

        # Selected material label.
        selected_material_label = tk.Label(self.frame1, text="Selected material: ")
        selected_material_label.pack(side=tk.LEFT, ipady=3)

        # ID mat entry.
        self.id_variable = tk.StringVar()
        id_mat = tk.Entry(self.frame1, textvariable=self.id_variable)
        id_mat.pack(side=tk.LEFT, ipady=3)

        # Spinbox storage.
        self.variable_to_storage = tk.IntVar()
        self.spin_box_storage = ttk.Spinbox(
            self.frame1,
            textvariable=self.variable_to_storage,
            from_=0,
            to=200,
            width=3,
        )
        self.spin_box_storage.pack(side=tk.LEFT, padx=5, ipady=1)

        # Bind spinbox for enter using.
        self.spin_box_storage.bind("<Return>", self.add_to_storage)

        # Add to storage button.
        add_to_storage_material_button = tk.Button(frame1, Components.add_material_to_storage_button())
        add_to_storage_material_button["command"] = self.add_to_storage
        add_to_storage_material_button.pack(side=tk.LEFT)

        # Spinbox storage.
        self.variable_to_order = tk.StringVar()
        self.spin_box_order = ttk.Spinbox(
            self.frame1,
            textvariable=self.variable_to_order,
            from_=0,
            to=200,
            width=3,
        )
        self.spin_box_order.pack(side=tk.LEFT, padx=5, ipady=1)

        # Add to ordered material button.
        add_to_ordered_material_button = tk.Button(frame1, Components.add_to_order_button())
        add_to_ordered_material_button["command"] = self.add_ordered_mat
        add_to_ordered_material_button.pack(side=tk.LEFT)

        # Plus material button.
        plus_material_button = tk.Button(frame1, text="+")
        plus_material_button["command"] = self.plus_material_btn_press
        plus_material_button.pack(side=tk.RIGHT, ipadx=10)

        self.write_off = tk.StringVar()

        self.spin_box = ttk.Spinbox(
            master=frame1,
            textvariable=self.write_off,
            from_=0,
            to=200,
            width=3,
            validate='all',
        )
        self.spin_box.pack(side=tk.RIGHT, padx=5, ipady=1)

        # Minus material button.
        minus_material_button = tk.Button(frame1, text="-")
        minus_material_button["command"] = self.minus_material_btn_press
        minus_material_button.pack(side=tk.RIGHT, ipadx=10, )

    # Function for update records button, firstly select all from database table, then delete treeview
    # and load again.

    def build_tree(self):
        # Select all material from database.
        Connection.select_all_material()
        result = Connection.cursor_fetch_all()
        # First delete
        for i in self.my_tree.get_children():
            self.my_tree.delete(i)
        # Then add in to.
        for i in result:
            self.my_tree.insert("", 'end',
                                values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    # Select item from treeview message yes/no for delete.
    def delete(self):
        selected_item = self.my_tree.selection()

        if selected_item:

            if Components.warning_for_delete_material(self.frame1):
                x = selected_item[0]
                self.my_tree.delete(x)
                # Delete material from database.
                Connection.delete_material_from_database(x)

            else:
                return True

    def update(self, rows):
        self.my_tree.delete(*self.my_tree.get_children())
        for row in rows:
            self.my_tree.insert("", "end", values=row)

    # Function for search material by ID.
    def search(self, event=None):
        id_get = self.entry_search.get()
        # Assuming Connection is a class with search_material_in_database and cursor_fetch_all methods
        Connection.search_material_in_database(id_get)
        rows = Connection.cursor_fetch_all()
        self.update(rows)

    def clear(self):
        # Select all material.
        Connection.select_all_material()
        rows = Connection.cursor_fetch_all()
        self.update(rows)

    def get_row(self, event):
        item_id = self.my_tree.identify_row(event.y)
        item = self.my_tree.item(item_id)
        self.id_variable.set(item["values"][0])


    def add_ordered_mat(self, event=None):
        order_get = self.variable_to_order.get()

        if order_get.isalpha():
            Components.tk_tlc_error_msg(self.frame1)
        elif Components.warning_msg_for_add_mat_to_order(self.frame1):
            for selected in self.my_tree.selection():
                self.set_selection = self.my_tree.set(selected, "#1")

            try:
                Connection.update_ordered_material(order_get, self.set_selection)
            except AttributeError:
                Components.warning_for_selecting_material(self.frame1)

            Connection.mydb.commit()
            self.clear()
            self.spin_box.delete(0, tk.END)
        else:
            return True

    def add_to_storage(self, event=None):
        try:
            self.variable_to_storage.get()
        except tk.TclError:
            # Warning for TlcError
            Components.tk_tlc_error_msg(self.frame1)

        to_storage_var_get = self.variable_to_storage.get()

        if Components.warning_msg_for_add_material_to_storage(self.frame1):
            # Select item from treeview
            for selected in self.my_tree.selection():
                self.set_selection = self.my_tree.set(selected, "#1")
            try:
                # Update material in storage.
                Connection.update_material_in_storage(to_storage_var_get, self.set_selection)
            except AttributeError:
                Components.attribute_error_warning(self.frame1)

            self.spin_box_storage.delete(0, tk.END)
            Connection.mydb.commit()

            self.clear()
        else:
            return True

    def minus_material_btn_press(self):
        self.update_write_off()

    def plus_material_btn_press(self):
        self.update_write_off(del_from_storage=False)

    def update_write_off(self, del_from_storage=True):

        """
        Change write_off for each selected material. Remove from storage if del_from_storage=True,
        else remove from write_off and add to storage.
        """
        # TODO - all values taken from class should be given as params: write_off_change, spin_box

        try:
            int(self.spin_box.get()) if self.spin_box.get() else 0
        except ValueError:
            Components.tk_tlc_error_msg(self.frame1)

        write_off_change = int(self.spin_box.get()) if self.spin_box.get() else 0
        # if spin_box.get():
        #     write_off_change = int(spin_box.get())
        # else:
        #     write_off_change = 0

        # Selected materials from treeview
        for selection in self.my_tree.selection():
            selected_material = self.my_tree.set(selection, "#1")

            material = list(Connection.select_material(selected_material))
            if material:
                in_storage = material[4] if material[4] else 0
                write_off = material[6] if material[6] else 0
            else:
                continue

            if in_storage - write_off_change < 0:
                Components.warning_message_write_off_is_bigger_then_mat_in_storage(self.frame1)
                continue
            else:
                material[4] = in_storage - write_off_change if del_from_storage else in_storage + write_off_change
                material[6] = write_off_change if del_from_storage else write_off - write_off_change
                if material[6] < 0:
                    material[6] = 0
                Connection.update_material(material)
            self.spin_box.delete(0, tk.END)
            self.clear()


