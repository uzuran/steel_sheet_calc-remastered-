import mysql.connector
from tkinter import messagebox as msg
from tkinter import *
from tkinter import ttk


# Db connect.
mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="datapass",
                               database='car_wash_material')

my_cursor = mydb.cursor(buffered=True)


class ShowAllStMaterial:

    def __init__(self, my_frame1):
        super().__init__()


        my_cursor = mydb.cursor()

        my_cursor.execute("SELECT * FROM st_material;")
        my_result = my_cursor.fetchall()
        mydb.commit()

        # SCROLL BAR
        scrolllbary = Scrollbar(my_frame1, orient=VERTICAL)
        my_tree = ttk.Treeview(my_frame1, selectmode='browse', height=20)
        my_tree.pack()

        my_tree.configure(yscrollcommand=scrolllbary.set)
        my_tree.configure(selectmode="extended")

        # Number of columns
        my_tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        # Show headings
        my_tree['show'] = 'headings'

        # width of columns and alignment
        my_tree.column("1", width=80, anchor='c')
        my_tree.column("2", width=80, anchor='c')
        my_tree.column("3", width=80, anchor='c')
        my_tree.column("4", width=80, anchor='c')
        my_tree.column("5", width=80, anchor='c')
        my_tree.column("6", width=80, anchor='c')
        my_tree.column("7", width=80, anchor='c')

        # Headings.
        # respective columns.
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

        def delete():
            # Db connect.
            mydb = mysql.connector.connect(host="127.0.0.1",
                                           user="root",
                                           passwd="datapass",
                                           database='car_wash_material')

            selected_item = my_tree.selection()
            if selected_item:
                x = selected_item[0]
                my_tree.delete(x)
                sql = "DELETE FROM st_material WHERE id=%s"
                cursor = mydb.cursor()
                cursor.execute(sql, (x,))
                mydb.commit()

        create_material_button = Button(my_frame1, text="Delete material", command=delete)
        create_material_button.pack(side=LEFT)
        create_material_button = Button(my_frame1, text="Update records", command=_build_tree)
        create_material_button.pack(side=LEFT)