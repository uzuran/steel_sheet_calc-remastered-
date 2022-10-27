from tkinter import *
from tkinter import ttk
from steel_admin import *
import mysql.connector
from tkinter import messagebox as msg


# Db connect.
mydb = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               passwd="datapass",
                               database='car_wash_material')

my_cursor = mydb.cursor(buffered=True)


# Admin screen
def admin_screen_window(user_name_v):
    admin_screen = Toplevel()
    admin_screen.title("Steel sheet calculator.")

    # setting tkinter window size
    admin_screen.geometry("1000x600")
    admin_screen.title("Steel sheet calculator.")
    #admin_screen.iconbitmap('./assets/pythontutorial.ico')

    # Main label.
    label_option = {"text": "Steel sheet calculator",
                    "bg": "#d1dffa",
                    "width": "300",
                    "height": "2",
                    "font": "Calibri, 13"}

    main_label = Label(admin_screen, ** label_option)
    main_label.pack()

    # Check users,  who is log in.
    user_name_label = user_name_v

    check_user = Label(admin_screen, text=str(user_name_label.capitalize()) + " Is log in now.",
                       fg="green",
                       font="Arial",

                       )
    check_user.pack(anchor="e")

    # Function for create material in new window.
    def create_new_material():
        global create_new_material_window

        create_new_material_window = Toplevel(admin_screen)
        create_new_material_window.geometry("350x450")
        create_new_material_window.title("Create new material.")

        new_material_label_option = {
            "text": "Create new material.",
            "bg": "#d1dffa",
            "width": "300",
            "height": "2",
            "font": "Calibri, 12"
        }

        global material_type, type_material_entry, m_identification,ID_entry,\
               thickness, material_thickness_entry
        global xsize,x_size_entry, ysize, y_size_entry

        # String variables for material entry
        material_type = StringVar()
        m_identification = StringVar()
        thickness = StringVar()
        xsize = StringVar()
        ysize = StringVar()

        # Register new material window label.
        create_material_label = Label(create_new_material_window, **new_material_label_option)
        create_material_label.pack()

        # Basic information about registered material.
        type_material = Label(create_new_material_window, text='Type material')
        type_material.pack()

        type_material_entry = Entry(create_new_material_window, textvariable=material_type)
        type_material_entry.pack()

        material_id = Label(create_new_material_window, text="Id")
        material_id.pack()

        # ID entry.
        ID_entry = Entry(create_new_material_window, textvariable=m_identification)
        ID_entry.pack()

        # Material thickness.
        material_thickness = Label(create_new_material_window, text='Thickness')
        material_thickness.pack()

        # Material thickness entry.
        material_thickness_entry = Entry(create_new_material_window, textvariable=thickness)
        material_thickness_entry.pack()

        # Material size_x
        x_size = Label(create_new_material_window, text='X_size')
        x_size.pack()

        # Material size_x entry
        x_size_entry = Entry(create_new_material_window, textvariable=xsize)
        x_size_entry.pack()

        # Material size_y
        y_size = Label(create_new_material_window, text='Y_size')
        y_size.pack()

        # Material size_y entry
        y_size_entry = Entry(create_new_material_window, textvariable=ysize)
        y_size_entry.pack()

        # Empty space
        e_space = Label(create_new_material_window, text=' ')
        e_space.pack()

        # Button for material register.
        button_for_register_material = Button(create_new_material_window, text='Register material')
        button_for_register_material['command'] = lambda: [create_new_material_click()]
        button_for_register_material.pack()
        # Free space.
        free_space = Label(create_new_material_window, text='')
        free_space.pack()

        # Free space.
        free_space = Label(create_new_material_window, text='')
        free_space.pack()

        # Free space.
        free_space = Label(create_new_material_window, text='')
        free_space.pack()

        info_label = Label(create_new_material_window, text='Please register your new material.')
        info_label.pack()

    # Button for create material.
    create_material_button = Button(admin_screen, text="Create material")
    create_material_button["command"] = create_new_material
    create_material_button.place(x=120, y=90)

    # Function for button for add material to database.
    def create_new_material_click():
        get_material_type = material_type.get()
        get_material_id = m_identification.get()
        get_thickness = thickness.get()
        get_xsize = xsize.get()
        get_ysize = ysize.get()

        # Check if material exist  in database
        sql = "SELECT * FROM st_material WHERE id = '%s'" % get_material_id
        my_cursor.execute(sql)

        # Condition.
        if my_cursor.fetchone():
            msg.showwarning(title="Warning!", message="This material already exist!")

        elif get_material_type == "st" and\
                get_material_id.isdigit() \
                and get_thickness != ""\
                and get_xsize.isdigit()\
                and get_ysize.isdigit():

            # If condition complete add material in to database.
            sql = "INSERT INTO st_material (id, thickness, size_x, size_y) VALUES(%s, %s, %s, %s)"
            val = (get_material_id, get_thickness, get_xsize, get_ysize)
            my_cursor.execute(sql, val)
            mydb.commit()
            # Success registration Label.
            reg_suc = Label(create_new_material_window, text=f'You register ID: {m_identification.get()}'
                                                             f' Thickness: {thickness.get()} '
                                                             f'X: {xsize.get()} Y: {ysize.get()}', fg="green")
            reg_suc.pack()

        else:
            msg.showwarning(title="Warning!", message="You cant add this specification of material.")

    # Add notebook of a materials to the second frame.
    notebook = ttk.Notebook(admin_screen)
    notebook.pack()

    # Add frame options.
    frame_options = {"width": "500",
                     "height": "400"}

    my_frame1 = Frame(notebook, ** frame_options)
    my_frame2 = Frame(notebook, ** frame_options)
    my_frame3 = Frame(notebook, ** frame_options)
    my_frame4 = Frame(notebook, **frame_options)
    my_frame5 = Frame(notebook, **frame_options)

    # Add notebook on screen.
    notebook.add(my_frame1, text="Steel material")
    notebook.add(my_frame2, text="Aluminium material")
    notebook.add(my_frame3, text="Stainless steel material")
    notebook.add(my_frame4, text="Special material")
    notebook.add(my_frame5, text="Write off")

    show_all_material(my_frame1)


    #show_who_write_off_admin(my_frame5, admin_screen)


