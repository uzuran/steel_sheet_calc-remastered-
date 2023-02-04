from tkinter import *
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
        my_tree = ttk.Treeview(wrapper, selectmode='browse', height=20)

        my_tree.pack()

        my_tree.configure(yscrollcommand=scroll_bar.set)
        my_tree.configure(selectmode="extended")

        # Number of columns
        my_tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        # Show headings
        my_tree['show'] = 'headings'

        # Width of columns and alignment
        my_tree.column("1", width=150, anchor='c')
        my_tree.column("2", width=150, anchor='c')
        my_tree.column("3", width=150, anchor='c')
        my_tree.column("4", width=150, anchor='c')
        my_tree.column("5", width=150, anchor='c')
        my_tree.column("6", width=150, anchor='c')
        my_tree.column("7", width=150, anchor='c')

        # Headings.
        # Headings.
        my_tree.heading("1", text=Languages.current_lang["treeview_id"])
        my_tree.heading("2", text=Languages.current_lang["treeview_thickness"])
        my_tree.heading("3", text=Languages.current_lang["treeview_x"])
        my_tree.heading("4", text=Languages.current_lang["treeview_y"])
        my_tree.heading("5", text=Languages.current_lang["treeview_in_storage"])
        my_tree.heading("6", text=Languages.current_lang["treeview_order"])
        my_tree.heading("7", text=Languages.current_lang["treeview_write_off"])
        for dt in my_result:
            my_tree.insert("", 'end', iid=dt[0], text=dt[0],
                           values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

        my_tree.pack()

        # Function for update records button, firstly select all from database table, then delete treeview
        # and load again.
        def _build_tree():
            # Select all material from database.
            Connection.select_all_material()
            result = Connection.cursor_fetch_all()
            # First delete
            for i in my_tree.get_children():
                my_tree.delete(i)
            # Then add in to.
            for i in result:
                my_tree.insert("", 'end',
                               values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        # Select item from treeview message yes/no for delete.
        def delete():
            selected_item = my_tree.selection()

            if selected_item:

                if Components.warning_for_delete_material(frame1):
                    x = selected_item[0]
                    my_tree.delete(x)
                    # Delete material from database.
                    Connection.delete_material_from_database(x)

                else:
                    return True

        id_variable = tk.StringVar()

        def update(rows):
            entry_search.delete(0, tk.END)
            my_tree.delete(*my_tree.get_children())
            for i in rows:
                my_tree.insert("", "end", values=i)

        # Function for search material by ID.
        def search(event=None):
            id_get = id_variable.get()
            # Search material in database where id.
            Connection.search_material_in_database(id_get)
            rows = Connection.cursor_fetch_all()
            update(rows)

        def clear():
            # Select all material.
            Connection.select_all_material()
            rows = Connection.cursor_fetch_all()
            update(rows)

        def get_row(event):
            my_tree.identify_row(event.y)
            item = my_tree.item(my_tree.focus())
            id_variable.set(item["values"][0])
            variable_order.set(item["values"][5])

        my_tree.bind("<Double 1>", get_row)

        def add_ordered_mat(event=None):
            order_get = variable_order.get()
            if order_get is not int:
                Components.tk_tlc_error_msg(frame1)

            elif Components.warning_msg_for_add_mat_to_order(frame1, order_get):

                for selected in my_tree.selection():
                    self.set_selection = my_tree.set(selected, "#1")

                try:
                    Connection.update_ordered_material(order_get, self.set_selection)
                except AttributeError:
                    Components.warning_for_selecting_material(frame1)

                Connection.mydb.commit()
                clear()
                spin_box.delete(0, tk.END)
            else:
                return True

        id_variable = tk.StringVar()

        # Delete material button
        delete_material_button = tk.Button(frame1, Components.delete_material_button())
        delete_material_button["command"] = delete
        delete_material_button.pack(side=tk.LEFT)

        # Update material button.
        update_material_button = tk.Button(frame1, Components.update_records_button())
        update_material_button["command"] = _build_tree
        update_material_button.pack(side=tk.LEFT)

        # Search entry.
        entry_search = tk.Entry(frame1, textvariable=id_variable)
        entry_search.pack(side=tk.LEFT, ipady=3)

        # Search button.
        search_material_button = tk.Button(frame1, Components.search_button())
        search_material_button["command"] = search
        search_material_button.pack(side=LEFT)
        # Bind entry search for enter using.
        entry_search.bind("<Return>", search)

        # ID mat entry.
        id_mat = tk.Entry(frame1, textvariable=id_variable)
        id_mat.pack(side=tk.LEFT, ipady=3)

        # Spinbox order.
        variable_order = tk.StringVar()

        spin_box = ttk.Spinbox(
            frame1,
            textvariable=variable_order,
            from_=0,
            to=200,
            width=3,

        )
        spin_box.pack(side=tk.LEFT, padx=5, ipady=1)

        # Bind spinbox for enter using.
        spin_box.bind("<Return>", add_ordered_mat)

        # Add to storage button.
        add_to_ordered_material_button = tk.Button(frame1, Components.add_to_order_button())
        add_to_ordered_material_button["command"] = add_ordered_mat
        add_to_ordered_material_button.pack(side=tk.LEFT)

        # Spinbox storage.
        variable_to_storage = tk.IntVar()

        spin_box_storage = ttk.Spinbox(
            frame1,
            textvariable=variable_to_storage,
            from_=0,
            to=200,
            width=3,

        )
        spin_box_storage.pack(side=LEFT, padx=5, ipady=1)

        # Function for adding material into storage
        def add_to_storage(event=None):
            try:
                variable_to_storage.get()
            except tk.TclError:
                # Warning for TlcError
                Components.tk_tlc_error_msg(frame1)

            to_storage_var_get = variable_to_storage.get()

            if Components.warning_msg_for_add_material_to_storage(frame1, to_storage_var_get):
                # Select item from treeview
                for selected in my_tree.selection():
                    self.set_selection = my_tree.set(selected, "#1")
                try:
                    # Update material in storage.
                    Connection.update_material_in_storage(to_storage_var_get, self.set_selection)
                except AttributeError:
                    Components.attribute_error_warning(frame1)

                spin_box_storage.delete(0, END)
                Connection.mydb.commit()

                clear()
            else:
                return True

        def minus_material_btn_press():
            update_write_off()

        def plus_material_btn_press():
            update_write_off(del_from_storage=False)

        def update_write_off(del_from_storage=True):

            """
            Change write_off for each selected material. Remove from storage if del_from_storage=True,
            else remove from write_off and add to storage.
            """
            # TODO - all values taken from class should be given as params: write_off_change, spin_box

            try:
                int(spin_box.get()) if spin_box.get() else 0
            except ValueError:
                Components.tk_tlc_error_msg(frame1)

            write_off_change = int(spin_box.get()) if spin_box.get() else 0
            # if spin_box.get():
            #     write_off_change = int(spin_box.get())
            # else:
            #     write_off_change = 0

            # Selected materials from treeview
            for selection in my_tree.selection():
                selected_material = my_tree.set(selection, "#1")

                material = list(Connection.select_material(selected_material))
                if material:
                    in_storage = material[4] if material[4] else 0
                    write_off = material[6] if material[6] else 0
                else:
                    continue

                if in_storage - write_off_change < 0:
                    Components.warning_message_write_off_is_bigger_then_mat_in_storage(frame1)
                    continue
                else:
                    material[4] = in_storage - write_off_change if del_from_storage else in_storage + write_off_change
                    material[6] = write_off_change if del_from_storage else write_off - write_off_change
                    if material[6] < 0:
                        material[6] = 0
                    Connection.update_material(material)
                spin_box.delete(0, END)
                clear()

        # Bind spinbox for enter using.
        spin_box_storage.bind("<Return>", add_to_storage)

        # Add to storage button.
        add_to_storage_material_button = Button(frame1, Components.add_material_to_storage_button())
        add_to_storage_material_button["command"] = add_to_storage
        add_to_storage_material_button.pack(side=LEFT)

        plus_material_button = Button(frame1, text="+")
        plus_material_button["command"] = plus_material_btn_press
        plus_material_button.pack(side=RIGHT, ipadx=10)

        self.write_off = tk.StringVar()

        spin_box = ttk.Spinbox(
            master=frame1,
            textvariable=self.write_off,
            from_=0,
            to=200,
            width=3,
            validate='all',



        )
        spin_box.pack(side=RIGHT, padx=5, ipady=1)

        minus_material_button = Button(frame1, text="-")
        minus_material_button["command"] = minus_material_btn_press
        minus_material_button.pack(side=RIGHT, ipadx=10, )


