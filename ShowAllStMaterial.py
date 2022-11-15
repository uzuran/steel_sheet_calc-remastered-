from tkinter import messagebox as msg
from tkinter import *
from tkinter import ttk
import tkinter as tk
from Connection import *

my_cursor = mydb.cursor(buffered=True)


class ShowAllStMaterial:

    def __init__(self, my_frame1):
        super().__init__()

        my_cursor = mydb.cursor()

        my_cursor.execute("SELECT * FROM st_material;")
        my_result = my_cursor.fetchall()
        mydb.commit()

        wraper1 = LabelFrame(my_frame1, text="Steel material")
        wraper1.pack(fill="both", expand=1)

        # SCROLL BAR
        scrolllbary = Scrollbar(my_frame1, orient=VERTICAL)
        my_tree = ttk.Treeview(wraper1, selectmode='browse', height=20)

        my_tree.pack()

        my_tree.configure(yscrollcommand=scrolllbary.set)
        my_tree.configure(selectmode="extended")

        # Number of columns
        my_tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        # Show headings
        my_tree['show'] = 'headings'

        # Width of columns and alignment
        my_tree.column("1", width=80, anchor='c')
        my_tree.column("2", width=80, anchor='c')
        my_tree.column("3", width=80, anchor='c')
        my_tree.column("4", width=80, anchor='c')
        my_tree.column("5", width=80, anchor='c')
        my_tree.column("6", width=80, anchor='c')
        my_tree.column("7", width=80, anchor='c')

        # Headings.
        # Headings.
        my_tree.heading("1", text="Id:")
        my_tree.heading("2", text="Thickness:")
        my_tree.heading("3", text="X size:")
        my_tree.heading("4", text="Y size:")
        my_tree.heading("5", text="In storage:")
        my_tree.heading("6", text="Ordered:")
        my_tree.heading("7", text="Write off:")
        for dt in my_result:
            my_tree.insert("", 'end', iid=dt[0], text=dt[0],
                           values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

        my_tree.pack()

        # Function for update records button, firstly select all from database table, then delete treeview
        # and load again.
        def _build_tree():
            cursor = mydb.cursor(buffered=True)
            cursor.execute("SELECT * FROM st_material;")
            result = cursor.fetchall()
            mydb.commit()
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

                if msg.askyesno(title="Warning !", message="Are you sure"
                                                           " that you want delete this material ?"):
                    x = selected_item[0]
                    my_tree.delete(x)
                    sql = "DELETE FROM st_material WHERE id=%s"
                    cursor = mydb.cursor()
                    cursor.execute(sql, (x,))
                    mydb.commit()
                else:
                    return True
        id_variable = StringVar()

        def update(rows):
            entry_search.delete(0, END)
            my_tree.delete(*my_tree.get_children())
            for i in rows:
                my_tree.insert("", "end", values=i)

        # Function for search material by ID.
        def search(event=None):
            id_variable2 = id_variable.get()
            query = "SELECT * FROM st_material WHERE id LIKE '%"+id_variable2+"%'"
            my_cursor.execute(query)
            rows = my_cursor.fetchall()
            update(rows)

        def clear():
            query = "SELECT * from st_material"
            my_cursor.execute(query)
            rows = my_cursor.fetchall()
            update(rows)

        def get_row(event):
            rowid = my_tree.identify_row(event.y)
            item = my_tree.item(my_tree.focus())
            id_string.set(item["values"][0])
            variable.set(item["values"][5])

        my_tree.bind("<Double 1>", get_row)

        def add_ordered_mat(event=None):
            order_value = variable.get()
            cursor = mydb.cursor(buffered=True)
            item = my_tree.item(my_tree.focus())
            if msg.askyesno(title="Warning", message=f"Dou you really "
                                                     f"want add this {order_value} count "
                                                     f"of material ?"):

                query = "UPDATE st_material  SET ordered = %s WHERE id = %s"
                try:
                    cursor.execute(query, (order_value, item["values"][0]))
                except IndexError:
                    msg.showwarning(title="WARNING", message="Firstly you need select the material !")

                mydb.commit()
                clear()
                spin_box.delete(0, END)
            else:
                return True

        id_string = StringVar()

        # Delete material button
        delete_material_button = Button(my_frame1)
        delete_material_button["text"] = "Delete material"
        delete_material_button["command"] = delete
        delete_material_button.pack(side=LEFT)

        # Update material button.
        update_material_button = Button(my_frame1)
        update_material_button["text"] = "Update records"
        update_material_button["command"] = _build_tree
        update_material_button.pack(side=LEFT)

        # Search entry.
        entry_search = Entry(my_frame1, textvariable=id_variable)
        entry_search.pack(side=LEFT, ipady=3)

        # Search button.
        search_material_button = Button(my_frame1)
        search_material_button["text"] = "Search"
        search_material_button["command"] = search
        search_material_button.pack(side=LEFT)
        # Bind entry search for enter using.
        entry_search.bind("<Return>", search)

        # ID mat entry.
        id_mat = Entry(my_frame1, textvariable=id_string)
        id_mat.pack(side=LEFT, ipady=3)

        # Spinbox order.
        variable = StringVar()

        spin_box = ttk.Spinbox(
            my_frame1,
            textvariable=variable,
            from_=0,
            to=200,
            width=3,

        )
        spin_box.pack(side=LEFT, padx=5, ipady=1)

        # Bind spinbox for enter using.
        spin_box.bind("<Return>", add_ordered_mat)

        # Add to storage button.
        add_to_ordered_material_button = Button(my_frame1)
        add_to_ordered_material_button["text"] = "Add material ordered material"
        add_to_ordered_material_button["command"] = add_ordered_mat
        add_to_ordered_material_button.pack(side=LEFT)

        # Spinbox order.
        variable_to_storage = IntVar()

        spin_box_storage = ttk.Spinbox(
            my_frame1,
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
                msg.showwarning(title="WARNING", message="You need add only numbers into entry !")

            to_storge_var = variable_to_storage.get()

            cursor = mydb.cursor(buffered=True)
            item = my_tree.item(my_tree.focus())
            if msg.askyesno(title="Warning", message=f"Dou you really "
                                                     f"want add this {to_storge_var} count "
                                                     f"of material ?"):

                query = "UPDATE st_material  SET in_storage = %s WHERE id = %s"
                try:
                    cursor.execute(query, (to_storge_var, item["values"][0]))
                except IndexError:
                    msg.showwarning(title="WARNING", message="Firstly you need select the material !")
                spin_box_storage.delete(0, END)
                mydb.commit()

                clear()
            else:
                return True

        # Bind spinbox for enter using.
        spin_box_storage.bind("<Return>", add_to_storage)

        # Add to storage button.
        add_to_storage_material_button = Button(my_frame1)
        add_to_storage_material_button["text"] = "Add to storage"
        add_to_storage_material_button["command"] = add_to_storage
        add_to_storage_material_button.pack(side=LEFT)

        plus_material_button = Button(my_frame1, text="+")
        plus_material_button.pack(side=LEFT, ipadx=10)

        # Spinbox order.
        plus_minus = IntVar()

        #def write_off_from_storage():
        #    var = plus_minus.get()
        #    query = "SELECT in_storage, concat(in_storage - '%"+var_str+"%') AS write_off \
        #             FROM st_material"
            # Execute the query
        #    my_cursor.execute(query)
        #    clear()

        spin_box = ttk.Spinbox(
            my_frame1,
            textvariable=plus_minus,
            from_=0,
            to=200,
            width=3,

        )
        spin_box.pack(side=LEFT, padx=5, ipady=1)

        minus_material_button = Button(my_frame1, text="-")
        minus_material_button.pack(side=LEFT, ipadx=10)


