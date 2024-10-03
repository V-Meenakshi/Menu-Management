from tkinter import *
from tkinter import Toplevel, Button, Tk, messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3


def create_login_frames():
    main_title = Label(root,text = "Campus Kitchen",font=("Goudy old style", 45, "bold"), fg="#d25d17", bg="Lavender")
    main_title.place(x=410,y=20)
    frame1 = Frame(root, bg="White")
    frame1.place(x=80, y=150, height=340, width=500)

    title1 = Label(frame1, text="LOGIN", font=("Impact", 35, "bold"), fg="#d77337", bg="White")
    title1.place(x=90, y=30)
    desc1 = Label(frame1, text="ADMIN LOGIN", font=("Goudy old style", 13, "bold"), fg="#d25d17", bg="White").place( x=90, y=100)

    img1 = Image.open(r"C:\Users\gayat\Downloads\chef-removebg-preview.png")
    img1 = img1.resize((115, 115), Image.BICUBIC)
    img1 = ImageTk.PhotoImage(img1)

    image_label1 = Label(frame1, image=img1, bg="White")
    image_label1.image = img1
    image_label1.place(x=270, y=40)

    admin_user = Label(frame1, text="USERNAME", font=("Goudy old style", 12, "bold"), fg="gray", bg="White")
    admin_user.place(x=90, y=140)

    admin_user_entry= Entry(frame1, font=("times new roman", 12), bg="lightgray")
    admin_user_entry.place(x=90, y=170, width=340, height=30)

    admin_pass = Label(frame1, text="PASSWORD", font=("Goudy old style", 12, "bold"), fg="gray", bg="White")
    admin_pass.place(x=90, y=210)

    admin_pass_entry = Entry(frame1, font=("times new roman", 12), bg="lightgray", show="*")
    admin_pass_entry.place(x=90, y=240, width=350, height=35)

    login_btn1 = Button(root, text="Login", fg="White",bg="#d77337", font=("times new roman", 15),command=lambda: validate_admin(admin_user_entry,admin_pass_entry))
    login_btn1.place(x=230, y=470, width=180, height=40)

    frame2 = Frame(root, bg="White")
    frame2.place(x=650, y=150, height=340, width=500)

    title2 = Label(frame2, text="LOGIN", font=("Impact", 35, "bold"), fg="#d77337", bg="White")
    title2.place(x=90, y=30)
    desc2 = Label(frame2, text="STUDENT LOGIN", font=("Goudy old style", 12, "bold"), fg="#d25d17",bg="White").place(x=90, y=100)

    img2 = Image.open(r"C:\Users\gayat\Downloads\student1.png")
    img2 = img2.resize((100, 100), Image.BICUBIC)
    img2 = ImageTk.PhotoImage(img2)

    image_label2 = Label(frame2, image=img2, bg="White")
    image_label2.image = img2
    image_label2.place(x=270, y=40)

    stu_user = Label(frame2, text="USERNAME", font=("Goudy old style", 12, "bold"), fg="gray", bg="White")
    stu_user.place(x=90, y=140)

    stu_user_entry = Entry(frame2, font=("times new roman", 12), bg="lightgray")
    stu_user_entry .place(x=90, y=170, width=350, height=30)

    stu_pass = Label(frame2, text="PASSWORD", font=("Goudy old style", 12, "bold"), fg="gray", bg="White")
    stu_pass.place(x=90, y=210)

    stu_pass_entry = Entry(frame2, font=("times new roman", 12), bg="lightgray", show="*")
    stu_pass_entry.place(x=90, y=240, width=350, height=30)

    login_btn2 = Button(root, text="Login", fg="White",bg="#d77337", font=("times new roman", 15), command=lambda: validate_student(stu_user_entry, stu_pass_entry))
    login_btn2.place(x=820, y=470, width=180, height=40)

def get_person(id):
    cursor.execute("SELECT * FROM login_page WHERE user_id = ?", (id,))
    return cursor.fetchone()

def validate_admin(eAA, eAB):
    user_id = eAA.get()
    password = eAB.get()
    t = get_person(user_id)
    if t:
        if t[1] == password and t[2] == "admin":
            messagebox.showinfo('Admin Signed ', 'Admin Signed In')
            open_week_selection_admin()
            eAA.delete(0,'end')
            eAB.delete(0,'end')
        else:
            messagebox.showinfo('Wrong Password', 'Admin not Signed In')
    else:
        messagebox.showinfo('Wrong entry ', 'Admin not Signed In')

def validate_student(eAA, eAB):
    user_id = eAA.get()
    password = eAB.get()
    t = get_person(user_id)
    if t:
        if t[1] == password and t[2] == "student":
            messagebox.showinfo('Student Signed ', 'Student Signed In')
            open_week_selection(user_id)
            eAA.delete(0, 'end')
            eAB.delete(0, 'end')
        else:
            messagebox.showinfo('Wrong Password', 'Student not Signed In')
    else:
        messagebox.showinfo('Wrong entry ', 'Student not Signed In')

def open_week_selection(user_id):
    global week_window
    root.withdraw()
    week_window = Toplevel(root)
    week_window.title("Campus Kitchen")
    week_window.geometry("1199x600+100+50")
    week_window.resizable(False, False)
    week_window.configure(bg='lavender')
    week_window.wm_iconphoto(False, photo)
    week_title = Label(week_window,text = "Select Week",font=("Goudy old style", 45, "bold"), fg="#d25d17", bg="Lavender")
    week_title.place(x=455,y=20)
    monday_btn = Button(week_window, text="Monday",font=("Goudy old style", 15, "bold") ,bg='violet', width=23, height=5, command= lambda: open_firstmenu(user_id,"Monday"))
    monday_btn.place(x=220, y=100)
    tuesday_btn = Button(week_window, text="Tuesday",font=("Goudy old style", 15, "bold"), bg='indigo', width=23, height=5, command=lambda: open_firstmenu(user_id,"Tuesday"))
    tuesday_btn.place(x=220, y=230)
    wednesday_btn = Button(week_window, text="Wednesday",font=("Goudy old style", 15, "bold") ,bg='blue', width=23, height=5, command=lambda:open_firstmenu(user_id,"Wednesday"))
    wednesday_btn.place(x=220, y=360)
    thursday_btn = Button(week_window, text="Thursday",font=("Goudy old style", 15, "bold"), bg='yellow', width=23, height=5, command=lambda:open_secondmenu(user_id,"Thursday"))
    thursday_btn.place(x=740, y=100)
    friday_btn = Button(week_window, text="Friday",font=("Goudy old style", 15, "bold"),bg='orange', width=23, height=5, command=lambda: open_secondmenu(user_id,"Friday"))
    friday_btn.place(x=740, y=230)
    saturday_btn = Button(week_window, text="Saturday",font=("Goudy old style", 15, "bold"), bg='red', width=23, height=5, command=lambda:open_secondmenu(user_id,"Saturday"))
    saturday_btn.place(x=740, y=360)
    sunday_btn = Button(week_window, text="Sunday",font=("Goudy old style", 15, "bold"), bg='light green', width=23, height=5, command=lambda:open_thirdmenu(user_id,"Sunday"))
    sunday_btn.place(x=480, y=230)


def open_week_selection_admin():
    global week_window

    root.withdraw()
    week_window = Toplevel(root)
    week_window.title("Campus Kitchen")
    week_window.geometry("1199x600+100+50")
    week_window.resizable(False, False)
    week_window.configure(bg='lavender')
    week_window.wm_iconphoto(False, photo)
    week_title = Label(week_window,text = "Select Week",font=("Goudy old style", 45, "bold"), fg="#d25d17", bg="Lavender")
    week_title.place(x=455,y=20)
    monday_btn = Button(week_window, text="Monday",font=("Goudy old style", 13, "bold") ,bg='violet', width=23, height=5, command= lambda :print_most_frequent_items("Monday"))
    monday_btn.place(x=240, y=100)
    tuesday_btn = Button(week_window, text="Tuesday",font=("Goudy old style", 13, "bold"), bg='indigo', width=23, height=5, command= lambda: print_most_frequent_items("Tuesday"))
    tuesday_btn.place(x=240, y=200)
    wednesday_btn = Button(week_window, text="Wednesday",font=("Goudy old style", 13, "bold") ,bg='blue', width=23, height=5, command= lambda:print_most_frequent_items("Wednesday"))
    wednesday_btn.place(x=240, y=300)
    thursday_btn = Button(week_window, text="Thursday",font=("Goudy old style", 13, "bold"), bg='yellow', width=23, height=5,command= lambda: print_most_frequent_items("Thursday"))
    thursday_btn.place(x=720, y=100)
    friday_btn = Button(week_window, text="Friday",font=("Goudy old style", 13, "bold"),bg='orange', width=23, height=5,command= lambda:print_most_frequent_items("Friday"))
    friday_btn.place(x=720, y=200)
    saturday_btn = Button(week_window, text="Saturday",font=("Goudy old style", 13, "bold"), bg='red', width=23, height=5,command= lambda:print_most_frequent_items("Saturday"))
    saturday_btn.place(x=720, y=300)
    sunday_btn = Button(week_window, text="Sunday",font=("Goudy old style", 13, "bold"), bg='light green', width=23, height=5,command= lambda:print_most_frequent_items("Sunday"))
    sunday_btn.place(x=480, y=200)

def print_most_frequent_items(selected_week):
    global week_window

    def go_back_admin():
        admin_window.withdraw()
        open_week_selection_admin()
    if week_window:
        week_window.withdraw()
    admin_window = Toplevel()
    admin_window.geometry('1270x690+0+0')
    admin_window.title("Campus Kitchen")
    admin_window.resizable(FALSE, FALSE)
    admin_window.wm_iconphoto(False, photo)
    admin_window.config(bg="lavender")

    output = ""
    columns = ['Breakfast', 'LunchRice', 'LunchFry', 'LunchCurry', 'LunchRasam', 'LunchPapad',
               'Snacks', 'DinnerSweet', 'DinnerFry', 'DinnerFruit', 'DinnerDal','Dinnericecream','DinnerNonveg','Dinnerveg']

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", background="lavender", fieldbackground="lavender", font=('Arial', 13))

    # Create a Treeview widget
    tree = ttk.Treeview(admin_window)
    tree['columns'] = ('Item')
    tree.heading('#0', text='Category', anchor='center')
    tree.heading('Item', text='Item', anchor='center')

    # Set column width and alignment
    tree.column("#0", width=150, anchor='center')
    tree.column("Item", width=300, anchor='center')
    tree.tag_configure('big', font=('Arial', 14))

    # Execute the query for each column
    for column in columns:
        query = f"""
                SELECT {column}, COUNT(*) AS count
                FROM menu_items
                WHERE Week = ?
                GROUP BY {column}
                HAVING COUNT(*) = (
                    SELECT MAX(cnt)
                    FROM (
                        SELECT COUNT(*) AS cnt
                        FROM menu_items
                        WHERE Week = ?
                        GROUP BY {column}
                    ) AS max_counts
                );
            """
        cursor.execute(query, (selected_week, selected_week))
        results = cursor.fetchall()
        conn.commit()
        if results and results[0][0] is not None:
            category = f"{column}"
            items = ', '.join([item[0] for item in results])
            tree.insert('', 'end', values=('',))
            tree.insert('', 'end', text=category, values=(items,))

    tree.grid(row=0, column=0, sticky='nsew')
    admin_window.grid_rowconfigure(0, weight=1)
    admin_window.grid_columnconfigure(0, weight=1)
    back_button = Button(admin_window, text="Back", font=('arial', 15, 'bold'), bg="light grey", bd=10,
                         relief='ridge', command=go_back_admin)
    back_button.place(x=100, y=520)
    okay_button = Button(admin_window, text="OKAY", font=('arial', 15, 'bold'), bg="light grey", bd=10,
                         relief='ridge',command = lambda : redirect_to_login(admin_window))
    okay_button.place(x=1000, y=520)


def user_in_menu(id,week):
    cursor.execute("SELECT * FROM menu_items WHERE user_id = ?  and Week =  ?", (id,week))
    return cursor.fetchone()

def insert_menu(id,selected_week):
    cursor.execute("INSERT INTO menu_items (user_id,Week) VALUES (?,?)", (id,selected_week))
    conn.commit()


def redirect_to_login(window):
    window.destroy()
    # week_window.destroy()
    root.deiconify()


def open_firstmenu(user_id, selected_week):
    global first_window, week_window
    if user_in_menu(user_id, selected_week):
        pass
    else:
        insert_menu(user_id, selected_week)

    def go_back():
        first_window.withdraw()
        open_week_selection(user_id)

    if week_window:
        week_window.withdraw()

    root.withdraw()
    first_window = Toplevel(root)
    first_window.geometry('1270x690+0+0')
    first_window.title("Campus Kitchen")
    first_window.config(bg="plum")
    first_window.geometry("1199x600+100+50")
    first_window.resizable(False, False)
    first_window.wm_iconphoto(False, photo)

    def update_selected_items():
        selected_items.set(
            f"Selected items:\n{var1.get()}\n{var2.get()}\n{var3.get()}\n{var4.get()}\n{var5.get()}\n{var6.get()}\n{var7.get()}\n{var8.get()}\n{var9.get()}\n{var10.get()}\n{var11.get()}")

    def submit_action(id, selected_week):
        if not all([var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
                    var9.get(), var10.get(), var11.get()]) or not any(
            [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
             var9.get(), var10.get(), var11.get()]):
            messagebox.showwarning("Select Item", "Please select at least one item in each category before submitting.")
        else:
            selected_breakfast = var1.get()
            selected_lunch_rice = var2.get()
            selected_lunch_fry = var3.get()
            selected_lunch_curry = var4.get()
            selected_lunch_rasam = var5.get()
            selected_lunch_papad = var6.get()
            selected_snack = var7.get()
            selected_dinner_sweet = var8.get()
            selected_dinner_fry = var9.get()
            selected_dinner_fruit = var10.get()
            selected_dinner_dal = var11.get()

            # Insert the selected items into the database
            cursor.execute(
                "UPDATE menu_items SET BreakFast=?, LunchRice=?, LunchFry=?, LunchCurry=?, LunchRasam=?, LunchPapad=?, Snacks=?, DinnerSweet=?, DinnerFry=?, DinnerFruit=?, DinnerDal=? WHERE user_id=? AND Week=?",
                (selected_breakfast, selected_lunch_rice, selected_lunch_fry, selected_lunch_curry,
                 selected_lunch_rasam, selected_lunch_papad, selected_snack, selected_dinner_sweet, selected_dinner_fry,
                 selected_dinner_fruit, selected_dinner_dal, id, selected_week))
            conn.commit()
            selected_items.set(
                f"Selected items:\n{var1.get()}\n{var2.get()}\n{var3.get()}\n{var4.get()}\n{var5.get()}\n{var6.get()}\n{var7.get()}\n{var8.get()}\n{var9.get()}\n{var10.get()}\n{var11.get()}\n")
            messagebox.showinfo("Submission", "Menu selected successfully")

            # Disable the radio buttons after submission
            for widget in [Idly_Dosa, Idly_BreadJam, Idly_Bajji, JeeraRice, BagaraRice, TomatoRice, CabbageFry, AaloFry,
                           Gobi65, Potato, Ladysfinger, Mixedveg, Sambar, TomatoRasam, AllamRasam, Samosachips,
                           Wheelchips, Chittipapad, PaniPuri, Samosa, Creamcake, GulabJamun, Kesari, Halwa, PotatoFry,
                           BendiFry, CarrotFry, Watermelon, Banana, Guava, Tomato, Beerakaya, Dosakaya]:
                widget.configure(state=DISABLED)
            redirect_to_login(first_window)

    topFrame = Frame(first_window, bd=10, relief=RIDGE)
    topFrame.pack(side=TOP)

    labelTitle = Label(topFrame, text='Campus Kitchen', font=("Goudy old style", 35, 'bold'), bg="light grey", fg="black")
    labelTitle.grid(row=0, column=0)

    breakfastFrame = LabelFrame(first_window, text='Breakfast', font=('arial', 15, 'bold'), bd=10,
                                highlightbackground='black',
                                highlightthickness=4, relief=RIDGE)
    breakfastFrame.place(x=100, y=100)

    lunchFrame = LabelFrame(first_window, text='Lunch', font=('arial', 15, 'bold'), highlightbackground='black',
                            highlightthickness=4, bd=10, relief=RIDGE)
    lunchFrame.place(x=100, y=200)

    snackFrame = LabelFrame(first_window, text='Snack', font=('arial', 15, 'bold'), highlightbackground='black',
                            highlightthickness=4, bd=10, relief=RIDGE)
    snackFrame.place(x=500, y=100)

    DinnerFrame = LabelFrame(first_window, text='Dinner', font=('arial', 15, 'bold'), highlightbackground='black',
                             highlightthickness=4, bd=10, relief=RIDGE)
    DinnerFrame.place(x=500, y=200)

    # frames in lunch
    lunchrice = LabelFrame(lunchFrame, text='Rice', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchrice.grid(row=0, column=0)

    lunchFry = LabelFrame(lunchFrame, text='Fry', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchFry.grid(row=1, column=0)

    lunchCurry = LabelFrame(lunchFrame, text='Curry', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchCurry.grid(row=2, column=0)

    lunchRasam = LabelFrame(lunchFrame, text='Rasam', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchRasam.grid(row=3, column=0)

    lunchPapad = LabelFrame(lunchFrame, text='Papad', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchPapad.grid(row=4, column=0)

    # frames in dinner
    dinnerSweet = LabelFrame(DinnerFrame, text='Sweet', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerSweet.grid(row=1, column=0)
    dinnerFry = LabelFrame(DinnerFrame, text='Fry', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerFry.grid(row=2, column=0)
    dinnerFruit = LabelFrame(DinnerFrame, text='Fruit', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerFruit.grid(row=3, column=0)
    dinnerDal = LabelFrame(DinnerFrame, text='Dal', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerDal.grid(row=4, column=0)

    var1 = StringVar(value="")
    var2 = StringVar(value="")
    var3 = StringVar(value="")
    var4 = StringVar(value="")
    var5 = StringVar(value="")
    var6 = StringVar(value="")
    var7 = StringVar(value="")
    var8 = StringVar(value="")
    var9 = StringVar(value="")
    var10 = StringVar(value="")
    var11 = StringVar(value="")
    selected_items = StringVar(value="Selected items:\n")

    # breakfast
    Idly_Dosa = Radiobutton(breakfastFrame, text="Idly_Dosa", font=("Arial", 10), indicatoron=0, variable=var1,
                            value="Idly_Dosa", command=update_selected_items)
    Idly_Dosa.grid(row=0, column=0)
    Idly_BreadJam = Radiobutton(breakfastFrame, text="Idly_BreadJam", font=("Arial", 10), indicatoron=0, variable=var1,
                                value="Idly_BreadJam", command=update_selected_items)
    Idly_BreadJam.grid(row=0, column=5)
    Idly_Bajji = Radiobutton(breakfastFrame, text="Idly_Bajji", font=("Arial", 10), indicatoron=0, variable=var1,
                             value="Idly_Bajji", command=update_selected_items)
    Idly_Bajji.grid(row=0, column=10)

    # lunchrice
    JeeraRice = Radiobutton(lunchrice, text="JeeraRice", font=("Arial", 10), indicatoron=0, variable=var2,
                            value="JeeraRice", command=update_selected_items)
    JeeraRice.grid(row=0, column=0)
    BagaraRice = Radiobutton(lunchrice, text="BagaraRice", font=("Arial", 10), indicatoron=0, variable=var2,
                             value="BagaraRice", command=update_selected_items)
    BagaraRice.grid(row=0, column=5)
    TomatoRice = Radiobutton(lunchrice, text="TomatoRice", font=("Arial", 10), indicatoron=0, variable=var2,
                             value="TomatoRice", command=update_selected_items)
    TomatoRice.grid(row=0, column=10)

    # Lunchfry
    CabbageFry = Radiobutton(lunchFry, text="CabbageFry", font=("Arial", 10), indicatoron=0, variable=var3,
                             value="CabbageFry", command=update_selected_items)
    CabbageFry.grid(row=0, column=0)
    AaloFry = Radiobutton(lunchFry, text="AaloFry", font=("Arial", 10), indicatoron=0, variable=var3, value="AaloFry",
                          command=update_selected_items)
    AaloFry.grid(row=0, column=5)
    Gobi65 = Radiobutton(lunchFry, text="Gobi65", font=("Arial", 10), indicatoron=0, variable=var3, value="Gobi65",
                         command=update_selected_items)
    Gobi65.grid(row=0, column=10)

    # LunchCurry
    Potato = Radiobutton(lunchCurry, text="Potato", font=("Arial", 10), indicatoron=0, variable=var4, value="Potato",
                         command=update_selected_items)
    Potato.grid(row=0, column=0)
    Ladysfinger = Radiobutton(lunchCurry, text="Ladysfinger", font=("Arial", 10), indicatoron=0, variable=var4,
                              value="Ladysfinger", command=update_selected_items)
    Ladysfinger.grid(row=0, column=5)
    Mixedveg = Radiobutton(lunchCurry, text="Mixedveg", font=("Arial", 10), indicatoron=0, variable=var4,
                           value="Mixedveg", command=update_selected_items)
    Mixedveg.grid(row=0, column=10)

    # LunchRasam
    Sambar = Radiobutton(lunchRasam, text="Sambar", font=("Arial", 10), indicatoron=0, variable=var5, value="Sambar",
                         command=update_selected_items)
    Sambar.grid(row=0, column=0)
    TomatoRasam = Radiobutton(lunchRasam, text="TomatoRasam", font=("Arial", 10), indicatoron=0, variable=var5,
                              value="TomatoRasam", command=update_selected_items)
    TomatoRasam.grid(row=0, column=5)
    AllamRasam = Radiobutton(lunchRasam, text="AllamRasam", font=("Arial", 10), indicatoron=0, variable=var5,
                             value="AllamRasam", command=update_selected_items)
    AllamRasam.grid(row=0, column=10)

    # lunchPapad
    Samosachips = Radiobutton(lunchPapad, text="Samosachips", font=("Arial", 10), indicatoron=0, variable=var6,
                              value="Samosachips", command=update_selected_items)
    Samosachips.grid(row=0, column=0)
    Wheelchips = Radiobutton(lunchPapad, text="Wheelchips", font=("Arial", 10), indicatoron=0, variable=var6,
                             value="Wheelchips", command=update_selected_items)
    Wheelchips.grid(row=0, column=5)
    Chittipapad = Radiobutton(lunchPapad, text="Chittipapad", font=("Arial", 10), indicatoron=0, variable=var6,
                              value="Chittipapad", command=update_selected_items)
    Chittipapad.grid(row=0, column=10)

    # snacks
    PaniPuri = Radiobutton(snackFrame, text="PaniPuri", font=("Arial", 12), indicatoron=0, variable=var7,
                           value="PaniPuri", command=update_selected_items)
    PaniPuri.grid(row=0, column=0)
    Samosa = Radiobutton(snackFrame, text="Samosa", font=("Arial", 12), indicatoron=0, variable=var7, value="Samosa",
                         command=update_selected_items)
    Samosa.grid(row=0, column=5)
    Creamcake = Radiobutton(snackFrame, text="Creamcake", font=("Arial", 12), indicatoron=0, variable=var7,
                            value="Creamcake", command=update_selected_items)
    Creamcake.grid(row=0, column=10)

    # Dinner
    # sweet
    GulabJamun = Radiobutton(dinnerSweet, text="GulabJamun", font=("Arial", 10), indicatoron=0, variable=var8,
                             value="GulabJamun", command=update_selected_items)
    GulabJamun.grid(row=0, column=0)
    Kesari = Radiobutton(dinnerSweet, text="Kesari", font=("Arial", 10), indicatoron=0, variable=var8, value="Kesari",
                         command=update_selected_items)
    Kesari.grid(row=0, column=5)
    Halwa = Radiobutton(dinnerSweet, text="Halwa", font=("Arial", 10), indicatoron=0, variable=var8, value="Halwa",
                        command=update_selected_items)
    Halwa.grid(row=0, column=10)
    # fry
    PotatoFry = Radiobutton(dinnerFry, text="PotatoFry", font=("Arial", 10), indicatoron=0, variable=var9,
                            value="PotatoFry", command=update_selected_items)
    PotatoFry.grid(row=0, column=0)
    BendiFry = Radiobutton(dinnerFry, text="BendiFry", font=("Arial", 10), indicatoron=0, variable=var9,
                           value="BendiFry", command=update_selected_items)
    BendiFry.grid(row=0, column=5)
    CarrotFry = Radiobutton(dinnerFry, text="CarrotFry", font=("Arial", 10), indicatoron=0, variable=var9,
                            value="CarrotFry", command=update_selected_items)
    CarrotFry.grid(row=0, column=10)
    # Fruit
    Watermelon = Radiobutton(dinnerFruit, text="Watermelon", font=("Arial", 10), indicatoron=0, variable=var10,
                             value="Watermelon", command=update_selected_items)
    Watermelon.grid(row=0, column=0)
    Banana = Radiobutton(dinnerFruit, text="Banana", font=("Arial", 10), indicatoron=0, variable=var10, value="Banana",
                         command=update_selected_items)
    Banana.grid(row=0, column=5)
    Guava = Radiobutton(dinnerFruit, text="Guava", font=("Arial", 10), indicatoron=0, variable=var10, value="Guava",
                        command=update_selected_items)
    Guava.grid(row=0, column=10)
    # Dal
    Tomato = Radiobutton(dinnerDal, text="Tomato", font=("Arial", 10), indicatoron=0, variable=var11, value="Tomato",
                         command=update_selected_items)
    Tomato.grid(row=0, column=0)
    Beerakaya = Radiobutton(dinnerDal, text="Beerakaya", font=("Arial", 10), indicatoron=0, variable=var11,
                            value="Beerakaya", command=update_selected_items)
    Beerakaya.grid(row=0, column=5)
    Dosakaya = Radiobutton(dinnerDal, text="Dosakaya", font=("Arial", 10), indicatoron=0, variable=var11,
                           value="Dosakaya", command=update_selected_items)
    Dosakaya.grid(row=0, column=10)

    label_selected_items = Label(first_window, textvariable=selected_items, highlightbackground='black',
                                 highlightthickness=4, font=('arial', 12, 'bold'), bd=10, relief=RIDGE)
    label_selected_items.place(x=1000, y=150)

    submit_button = Button(first_window, text="Submit", font=('arial', 15, 'bold'), fg="black", bg="light green", bd=10,
                           relief=RIDGE, command=lambda: submit_action(user_id, selected_week))
    submit_button.place(x=1010, y=500)

    back_button = Button(first_window, text="Back", font=('arial', 15, 'bold'), bg="light grey", bd=10, relief='ridge',
                         command=go_back)
    back_button.place(x=100, y=520)


def open_secondmenu(user_id,selected_week):
    global second_window, week_window
    if user_in_menu(user_id,selected_week):
        pass
    else:
        insert_menu(user_id,selected_week)

    def go_back1():
        second_window.withdraw()
        open_week_selection(user_id)

    if week_window:
        week_window.withdraw()

    root.withdraw()
    second_window = Toplevel(root)
    second_window.geometry('1270x690+0+0')
    second_window.title("Campus Kitchen")
    second_window.config(bg="pink")
    second_window.geometry("1199x600+100+50")
    second_window.resizable(False, False)
    second_window.wm_iconphoto(False, photo)

    def update_selected_items():
        selected_items.set(
            f"Selected items:\n{var1.get()}\n{var2.get()}\n{var3.get()}\n{var4.get()}\n{var5.get()}\n{var6.get()}\n{var7.get()}\n{var8.get()}\n{var9.get()}\n{var10.get()}\n{var11.get()}")

    def submit_action(id, selected_week):
        if not all([var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
                    var9.get(), var10.get(), var11.get()]) or not any(
            [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
             var9.get(), var10.get(), var11.get()]):
            messagebox.showwarning("Select Item", "Please select at least one item in each category before submitting.")

        else:
            selected_breakfast = var1.get()
            selected_lunch_rice = var2.get()
            selected_lunch_fry = var3.get()
            selected_lunch_curry = var4.get()
            selected_lunch_rasam = var5.get()
            selected_lunch_papad = var6.get()
            selected_snack = var7.get()
            selected_dinner_sweet = var8.get()
            selected_dinner_fry = var9.get()
            selected_dinner_fruit = var10.get()
            selected_dinner_dal = var11.get()

            # Insert the selected items into the database
            cursor.execute(
                "UPDATE menu_items SET BreakFast=?, LunchRice=?, LunchFry=?, LunchCurry=?, LunchRasam=?, LunchPapad=?, Snacks=?, DinnerSweet=?, DinnerFry=?, DinnerFruit=?, DinnerDal=? WHERE user_id=? AND Week=?",
                (selected_breakfast, selected_lunch_rice, selected_lunch_fry, selected_lunch_curry,
                 selected_lunch_rasam, selected_lunch_papad, selected_snack, selected_dinner_sweet, selected_dinner_fry,
                 selected_dinner_fruit, selected_dinner_dal, id, selected_week))
            conn.commit()

            selected_items.set(
                f"Selected items:\n{var1.get()}\n{var2.get()}\n{var3.get()}\n{var4.get()}\n{var5.get()}\n{var6.get()}\n{var7.get()}\n{var8.get()}\n{var9.get()}\n{var10.get()}\n{var11.get()}\n")
            messagebox.showinfo("Submission", "Menu selected successfully")


            # Disable the radio buttons after submission
            for widget in [Idly_Vada, Chapati_Upma, Poori_BreadJam, LemonRice, MangoRice, BreadPulav, AlooFry,
                           GerkinsFry,
                           PaneerFry, CarrotBeetroot, PrawnsFry, FishFry, Sambar, TomatoRasam, Miriyalarasam,
                           Samosachips,
                           Wheelchips, Chittipapad, Vegpuff, Dilpasand, CreamBun, Sweetpongal, Semiya, Kheer, PotatoFry,
                           BendiFry, CarrotFry, Watermelon, Banana, Guava, Tomato, Beerakaya, Dosakaya]:
                widget.configure(state=DISABLED)

            redirect_to_login(second_window)

    topFrame = Frame(second_window, bd=10, relief=RIDGE)
    topFrame.pack(side=TOP)

    labelTitle = Label(topFrame, text='Campus Kitchen', font=("Goudy old style", 35, 'bold'), bg="light grey", fg="black")
    labelTitle.grid(row=0, column=0)

    breakfastFrame = LabelFrame(second_window, text='Breakfast', font=('arial', 15, 'bold'), bd=10,highlightbackground='black',highlightthickness=4, relief=RIDGE)
    breakfastFrame.place(x=100, y=100)

    lunchFrame = LabelFrame(second_window, text='Lunch', font=('arial', 15, 'bold'), highlightbackground='black',highlightthickness=4, bd=10, relief=RIDGE)
    lunchFrame.place(x=100, y=200)

    snackFrame = LabelFrame(second_window, text='Snack', font=('arial', 15, 'bold'), highlightbackground='black',highlightthickness=4, bd=10, relief=RIDGE)
    snackFrame.place(x=500, y=100)

    DinnerFrame = LabelFrame(second_window, text='Dinner', font=('arial', 15, 'bold'), highlightbackground='black',highlightthickness=4, bd=10, relief=RIDGE)
    DinnerFrame.place(x=500, y=200)

    # frames in lunch
    lunchrice = LabelFrame(lunchFrame, text='Rice', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchrice.grid(row=0, column=0)

    lunchFry = LabelFrame(lunchFrame, text='Fry', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchFry.grid(row=1, column=0)

    lunchCurry = LabelFrame(lunchFrame, text='Curry', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchCurry.grid(row=2, column=0)

    lunchRasam = LabelFrame(lunchFrame, text='Rasam', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchRasam.grid(row=3, column=0)

    lunchPapad = LabelFrame(lunchFrame, text='Papad', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchPapad.grid(row=4, column=0)

    # frames in dinner
    dinnerSweet = LabelFrame(DinnerFrame, text='Sweet', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerSweet.grid(row=1, column=0)
    dinnerFry = LabelFrame(DinnerFrame, text='Fry', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerFry.grid(row=2, column=0)
    dinnerFruit = LabelFrame(DinnerFrame, text='Fruit', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerFruit.grid(row=3, column=0)
    dinnerDal = LabelFrame(DinnerFrame, text='Dal', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerDal.grid(row=4, column=0)

    var1 = StringVar(value="")
    var2 = StringVar(value="")
    var3 = StringVar(value="")
    var4 = StringVar(value="")
    var5 = StringVar(value="")
    var6 = StringVar(value="")
    var7 = StringVar(value="")
    var8 = StringVar(value="")
    var9 = StringVar(value="")
    var10 = StringVar(value="")
    var11 = StringVar(value="")
    selected_items = StringVar(value="Selected items:\n")

    # breakfast
    Idly_Vada = Radiobutton(breakfastFrame, text="Idly_Vada", font=("Arial", 10), indicatoron=0, variable=var1,
                            value="Idly_Vada", command=update_selected_items)
    Idly_Vada.grid(row=0, column=0)
    Poori_BreadJam = Radiobutton(breakfastFrame, text="Poori_BreadJam", font=("Arial", 10), indicatoron=0,
                                 variable=var1,
                                 value="Poori_BreadJam", command=update_selected_items)
    Poori_BreadJam.grid(row=0, column=5)
    Chapati_Upma = Radiobutton(breakfastFrame, text="Chapati_Upma", font=("Arial", 10), indicatoron=0, variable=var1,
                               value="Chapati_Upma", command=update_selected_items)
    Chapati_Upma.grid(row=0, column=10)

    # lunchrice
    LemonRice = Radiobutton(lunchrice, text="LemonRice", font=("Arial", 10), indicatoron=0, variable=var2,
                            value="LemonRice", command=update_selected_items)
    LemonRice.grid(row=0, column=0)
    MangoRice = Radiobutton(lunchrice, text="MangoRice", font=("Arial", 10), indicatoron=0, variable=var2,
                            value="MangoRice", command=update_selected_items)
    MangoRice.grid(row=0, column=5)
    BreadPulav = Radiobutton(lunchrice, text="BreadPulav", font=("Arial", 10), indicatoron=0,
                                      variable=var2,
                                      value="BreadPulav", command=update_selected_items)
    BreadPulav.grid(row=0, column=10)

    # Lunchfry
    PaneerFry = Radiobutton(lunchFry, text="PaneerFry", font=("Arial", 10), indicatoron=0, variable=var3,
                            value="PaneerFry", command=update_selected_items)
    PaneerFry.grid(row=0, column=0)
    AlooFry = Radiobutton(lunchFry, text="AlooFry", font=("Arial", 10), indicatoron=0, variable=var3, value="AlooFry",
                          command=update_selected_items)
    AlooFry.grid(row=0, column=5)
    GerkinsFry = Radiobutton(lunchFry, text="GerkinsFry", font=("Arial", 10), indicatoron=0, variable=var3,
                             value="GerkinsFry",
                             command=update_selected_items)
    GerkinsFry.grid(row=0, column=10)

    # LunchCurry
    CarrotBeetroot = Radiobutton(lunchCurry, text="CarrotBeetroot", font=("Arial", 10), indicatoron=0,
                                      variable=var4, value="CarrotBeetroot",
                                      command=update_selected_items)
    CarrotBeetroot.grid(row=0, column=0)
    PrawnsFry = Radiobutton(lunchCurry, text="PrawnsFry", font=("Arial", 10), indicatoron=0, variable=var4,
                            value="PrawnsFry", command=update_selected_items)
    PrawnsFry.grid(row=0, column=5)
    FishFry = Radiobutton(lunchCurry, text="FishFry", font=("Arial", 10), indicatoron=0, variable=var4,
                          value="FishFry", command=update_selected_items)
    FishFry.grid(row=0, column=10)

    # LunchRasam
    Sambar = Radiobutton(lunchRasam, text="Sambar", font=("Arial", 10), indicatoron=0, variable=var5, value="Sambar",
                         command=update_selected_items)
    Sambar.grid(row=0, column=0)
    TomatoRasam = Radiobutton(lunchRasam, text="TomatoRasam", font=("Arial", 10), indicatoron=0, variable=var5,
                              value="TomatoRasam", command=update_selected_items)
    TomatoRasam.grid(row=0, column=5)
    Miriyalarasam = Radiobutton(lunchRasam, text="Miriyalarasam", font=("Arial", 10), indicatoron=0, variable=var5,
                                value="Miriyalarasam", command=update_selected_items)
    Miriyalarasam.grid(row=0, column=10)

    # lunchPapad
    Samosachips = Radiobutton(lunchPapad, text="Samosachips", font=("Arial", 10), indicatoron=0, variable=var6,
                              value="Samosachips", command=update_selected_items)
    Samosachips.grid(row=0, column=0)
    Wheelchips = Radiobutton(lunchPapad, text="Wheelchips", font=("Arial", 10), indicatoron=0, variable=var6,
                             value="Wheelchips", command=update_selected_items)
    Wheelchips.grid(row=0, column=5)
    Chittipapad = Radiobutton(lunchPapad, text="Chittipapad", font=("Arial", 10), indicatoron=0, variable=var6, value="Chittipapad", command=update_selected_items)
    Chittipapad.grid(row=0, column=10)

    # snacks
    Vegpuff = Radiobutton(snackFrame, text="Vegpuff", font=("Arial", 12), indicatoron=0, variable=var7,value="Vegpuff", command=update_selected_items)
    Vegpuff.grid(row=0, column=0)
    Dilpasand = Radiobutton(snackFrame, text="Dilpasand", font=("Arial", 12), indicatoron=0, variable=var7,value="Dilpasand", command=update_selected_items)
    Dilpasand.grid(row=0, column=5)
    CreamBun = Radiobutton(snackFrame, text="CreamBun", font=("Arial", 12), indicatoron=0, variable=var7,
                           value="CreamBun", command=update_selected_items)
    CreamBun.grid(row=0, column=10)

    # Dinner
    # sweet
    Sweetpongal = Radiobutton(dinnerSweet, text="Sweetpongal", font=("Arial", 10), indicatoron=0, variable=var8,
                              value="Sweetpongal", command=update_selected_items)
    Sweetpongal.grid(row=0, column=0)
    Semiya = Radiobutton(dinnerSweet, text="Semiya", font=("Arial", 10), indicatoron=0, variable=var8, value="Semiya",
                         command=update_selected_items)
    Semiya.grid(row=0, column=5)
    Kheer = Radiobutton(dinnerSweet, text="Kheer", font=("Arial", 10), indicatoron=0, variable=var8, value="Kheer",
                        command=update_selected_items)
    Kheer.grid(row=0, column=10)
    # fry
    PotatoFry = Radiobutton(dinnerFry, text="PotatoFry", font=("Arial", 10), indicatoron=0, variable=var9,
                            value="PotatoFry", command=update_selected_items)
    PotatoFry.grid(row=0, column=0)
    BendiFry = Radiobutton(dinnerFry, text="BendiFry", font=("Arial", 10), indicatoron=0, variable=var9,
                           value="BendiFry", command=update_selected_items)
    BendiFry.grid(row=0, column=5)
    CarrotFry = Radiobutton(dinnerFry, text="CarrotFry", font=("Arial", 10), indicatoron=0, variable=var9,
                            value="CarrotFry", command=update_selected_items)
    CarrotFry.grid(row=0, column=10)
    # Fruit
    Watermelon = Radiobutton(dinnerFruit, text="Watermelon", font=("Arial", 10), indicatoron=0, variable=var10,
                             value="Watermelon", command=update_selected_items)
    Watermelon.grid(row=0, column=0)
    Banana = Radiobutton(dinnerFruit, text="Banana", font=("Arial", 10), indicatoron=0, variable=var10, value="Banana",
                         command=update_selected_items)
    Banana.grid(row=0, column=5)
    Guava = Radiobutton(dinnerFruit, text="Guava", font=("Arial", 10), indicatoron=0, variable=var10, value="Guava",
                        command=update_selected_items)
    Guava.grid(row=0, column=10)
    # Dal
    Tomato = Radiobutton(dinnerDal, text="Tomato", font=("Arial", 10), indicatoron=0, variable=var11, value="Tomato",
                         command=update_selected_items)
    Tomato.grid(row=0, column=0)
    Beerakaya = Radiobutton(dinnerDal, text="Beerakaya", font=("Arial", 10), indicatoron=0, variable=var11,
                            value="Beerakaya", command=update_selected_items)
    Beerakaya.grid(row=0, column=5)
    Dosakaya = Radiobutton(dinnerDal, text="Dosakaya", font=("Arial", 10), indicatoron=0, variable=var11,
                           value="Dosakaya", command=update_selected_items)
    Dosakaya.grid(row=0, column=10)

    label_selected_items = Label(second_window, textvariable=selected_items,highlightbackground='black',highlightthickness=4,  font=('arial', 12, 'bold'), bd=10,
                                 relief=RIDGE)
    label_selected_items.place(x=1000, y=150)

    submit_button = Button(second_window, text="Submit", font=('arial', 15, 'bold'),fg="black",bg = "light green",  bd=10, relief=RIDGE,command=lambda: submit_action(user_id,selected_week))
    submit_button.place(x=1010, y=500)

    back_button = Button(second_window, text="Back", font=('arial', 15, 'bold'),bg = "light grey",  bd=10, relief='ridge',command=go_back1)
    back_button.place(x=100, y=520)


def open_thirdmenu(user_id,selected_week):
    global third_window, week_window
    if user_in_menu(user_id,selected_week):
        pass
    else:
        insert_menu(user_id,selected_week)

    def go_back2():
        third_window.withdraw()
        open_week_selection(user_id)

    if week_window:
        week_window.withdraw()

    root.withdraw()
    third_window = Toplevel(root)
    third_window.geometry('1270x690+0+0')
    third_window.title("Campus Kitchen")
    third_window.config(bg="light blue")
    third_window.geometry("1199x600+100+50")
    third_window.resizable(False, False)
    third_window.wm_iconphoto(False, photo)

    def update_selected_items():
        selected_items.set(
            f"Selected items:\n{var1.get()}\n{var2.get()}\n{var3.get()}\n{var4.get()}\n{var5.get()}\n{var6.get()}\n{var7.get()}\n{var8.get()}\n{var9.get()}\n{var10.get()}\n{var11.get()}")

    def submit_action(id, selected_week):
        if not all([var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
                    var9.get(), var10.get(), var11.get()]) or not any(
            [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(),
             var9.get(), var10.get(), var11.get()]):
            messagebox.showwarning("Select Item", "Please select at least one item in each category before submitting.")
        else:
            selected_breakfast = var1.get()
            selected_lunch_rice = var2.get()
            selected_lunch_fry = var3.get()
            selected_lunch_curry = var4.get()
            selected_lunch_rasam = var5.get()
            selected_lunch_papad = var6.get()
            selected_snack = var7.get()
            selected_dinner_sweet = var8.get()
            selected_dinner_icecream = var9.get()
            selected_dinner_Nonveg = var10.get()
            selected_dinner_veg = var11.get()

            # Insert the selected items into the database
            cursor.execute(
                "UPDATE menu_items SET BreakFast=?, LunchRice=?, LunchFry=?, LunchCurry=?, LunchRasam=?, LunchPapad=?, Snacks=?, DinnerSweet=?, Dinnericecream=?, DinnerNonveg=?, DinnerVeg=? WHERE user_id=? AND Week=?",
                (selected_breakfast, selected_lunch_rice, selected_lunch_fry, selected_lunch_curry,
                 selected_lunch_rasam, selected_lunch_papad, selected_snack, selected_dinner_sweet, selected_dinner_icecream,
                 selected_dinner_Nonveg, selected_dinner_veg, id, selected_week))
            conn.commit()
            selected_items.set(
                f"Selected items:\n{var1.get()}\n{var2.get()}\n{var3.get()}\n{var4.get()}\n{var5.get()}\n{var6.get()}\n{var7.get()}\n{var8.get()}\n{var9.get()}\n{var10.get()}\n{var11.get()}\n")
            messagebox.showinfo("Submission", "Okay")

            # Disable the radio buttons after submission
            for widget in [Ravapunukulu_upma, Uttapam_upma, Chapati_Upma,CoconutRice, GonguraRice, Kichidi, VankayaBatani, Kadipakodi, Soyamasala,Potato,Ladysfinger,Mixedveg,Sambar,TomatoRasam,MiriyalaRasam,
                           Samosachips, Wheelchips,Chittipapad,Kachori,FruitCake,Vegroll,BreadHalva,Kesari,GulabJamun,Vannila,Strawberry,ButterScotch,Biryani,ChickenCurry,ChickenFriedrice,MushroomCurry,AaloChana,Paneer]:
                widget.configure(state=DISABLED)

            redirect_to_login(third_window)
    topFrame = Frame(third_window, bd=10, relief=RIDGE)
    topFrame.pack(side=TOP)

    labelTitle = Label(topFrame, text='Campus Kitchen', font=("Goudy old style", 35, 'bold'),highlightbackground='black',highlightthickness=4,  bg="light grey", fg="black")
    labelTitle.grid(row=0, column=0)

    breakfastFrame = LabelFrame(third_window, text='Breakfast', font=('arial', 15, 'bold'), bd=10,
                                highlightbackground='black',
                                highlightthickness=4, relief=RIDGE)
    breakfastFrame.place(x=100, y=100)

    lunchFrame = LabelFrame(third_window, text='Lunch', font=('arial', 15, 'bold'), highlightbackground='black',highlightthickness=4, bd=10, relief=RIDGE)
    lunchFrame.place(x=100, y=200)

    snackFrame = LabelFrame(third_window, text='Snack', font=('arial', 15, 'bold'), highlightbackground='black',
                            highlightthickness=4, bd=10, relief=RIDGE)
    snackFrame.place(x=500, y=100)

    DinnerFrame = LabelFrame(third_window, text='Dinner', font=('arial', 15, 'bold'), highlightbackground='black',
                             highlightthickness=4, bd=10, relief=RIDGE)
    DinnerFrame.place(x=500, y=200)

    # frames in lunch
    lunchrice = LabelFrame(lunchFrame, text='Rice', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchrice.grid(row=0, column=0)

    lunchFry = LabelFrame(lunchFrame, text='Fry', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchFry.grid(row=1, column=0)

    lunchCurry = LabelFrame(lunchFrame, text='Curry', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchCurry.grid(row=2, column=0)

    lunchRasam = LabelFrame(lunchFrame, text='Rasam', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchRasam.grid(row=3, column=0)

    lunchPapad = LabelFrame(lunchFrame, text='Papad', font=('arial', 10, 'bold'), bd=2, relief=RIDGE)
    lunchPapad.grid(row=4, column=0)

    # frames in dinner
    dinnerSweet = LabelFrame(DinnerFrame, text='Sweet', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerSweet.grid(row=1, column=0)
    dinnericecreme = LabelFrame(DinnerFrame, text='Icecream', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnericecreme.grid(row=2, column=0)
    dinnerNonveg= LabelFrame(DinnerFrame, text='Nonveg', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerNonveg.grid(row=3, column=0)
    dinnerVeg = LabelFrame(DinnerFrame, text='Veg', font=('arial', 10, 'bold'), bd=10, relief=RIDGE)
    dinnerVeg.grid(row=4, column=0)

    var1 = StringVar(value="")
    var2 = StringVar(value="")
    var3 = StringVar(value="")
    var4 = StringVar(value="")
    var5 = StringVar(value="")
    var6 = StringVar(value="")
    var7 = StringVar(value="")
    var8 = StringVar(value="")
    var9 = StringVar(value="")
    var10 = StringVar(value="")
    var11 = StringVar(value="")
    selected_items = StringVar(value="Selected items:\n")

    # breakfast
    Ravapunukulu_upma = Radiobutton(breakfastFrame, text="Ravapunukulu_upma", font=("Arial", 10), indicatoron=0,variable=var1,value="Ravapunukulu_upma", command=update_selected_items)
    Ravapunukulu_upma.grid(row=0, column=0)
    Uttapam_upma = Radiobutton(breakfastFrame, text="Uttapam_upma", font=("Arial", 10), indicatoron=0, variable=var1,value="Uttapam_upma", command=update_selected_items)
    Uttapam_upma.grid(row=0, column=5)
    Chapati_Upma = Radiobutton(breakfastFrame, text="Chapati_Upma", font=("Arial", 10), indicatoron=0,variable=var1, value="Chapati_Upma", command=update_selected_items)
    Chapati_Upma.grid(row=0, column=10)

    # lunchrice
    CoconutRice = Radiobutton(lunchrice, text="CoconutRice", font=("Arial", 10), indicatoron=0, variable=var2,
                              value="CoconutRice", command=update_selected_items)
    CoconutRice.grid(row=0, column=0)
    Kichidi = Radiobutton(lunchrice, text="Kichidi", font=("Arial", 10), indicatoron=0, variable=var2,
                          value="Kichidi", command=update_selected_items)
    Kichidi.grid(row=0, column=5)
    GonguraRice = Radiobutton(lunchrice, text="GonguraRice  ", font=("Arial", 10), indicatoron=0, variable=var2,
                              value="GonguraRice", command=update_selected_items)
    GonguraRice.grid(row=0, column=10)

    # Lunchfry
    VankayaBatani = Radiobutton(lunchFry, text="VankayaBatani", font=("Arial", 10), indicatoron=0, variable=var3,
                                value="VankayaBatani", command=update_selected_items)
    VankayaBatani.grid(row=0, column=0)
    Kadipakodi = Radiobutton(lunchFry, text="Kadipokadi", font=("Arial", 10), indicatoron=0, variable=var3,
                             value="Kadipakodi",
                             command=update_selected_items)
    Kadipakodi.grid(row=0, column=5)
    Soyamasala = Radiobutton(lunchFry, text="Soyamasala", font=("Arial", 10), indicatoron=0, variable=var3,
                             value="Soyamasala",
                             command=update_selected_items)
    Soyamasala.grid(row=0, column=10)

    # LunchCurry
    Potato = Radiobutton(lunchCurry, text="Potato", font=("Arial", 10), indicatoron=0, variable=var4, value="Potato",
                         command=update_selected_items)
    Potato.grid(row=0, column=0)
    Ladysfinger = Radiobutton(lunchCurry, text="Ladysfinger", font=("Arial", 10), indicatoron=0, variable=var4,
                              value="Ladysfinger", command=update_selected_items)
    Ladysfinger.grid(row=0, column=5)
    Mixedveg = Radiobutton(lunchCurry, text="Mixedveg", font=("Arial", 10), indicatoron=0, variable=var4,
                           value="Mixedveg", command=update_selected_items)
    Mixedveg.grid(row=0, column=10)

    # LunchRasam
    Sambar = Radiobutton(lunchRasam, text="Sambar", font=("Arial", 10), indicatoron=0, variable=var5, value="Sambar",
                         command=update_selected_items)
    Sambar.grid(row=0, column=0)
    TomatoRasam = Radiobutton(lunchRasam, text="TomatoRasam", font=("Arial", 10), indicatoron=0, variable=var5,
                              value="TomatoRasam", command=update_selected_items)
    TomatoRasam.grid(row=0, column=5)
    MiriyalaRasam = Radiobutton(lunchRasam, text="MiriyalaRasam ", font=("Arial", 10), indicatoron=0, variable=var5,
                                value="MiriyalaRasam ", command=update_selected_items)
    MiriyalaRasam.grid(row=0, column=10)

    # lunchPapad
    Samosachips = Radiobutton(lunchPapad, text="Samosachips", font=("Arial", 10), indicatoron=0, variable=var6,
                              value="Samosachips", command=update_selected_items)
    Samosachips.grid(row=0, column=0)
    Wheelchips = Radiobutton(lunchPapad, text="Wheelchips", font=("Arial", 10), indicatoron=0, variable=var6,
                             value="Wheelchips", command=update_selected_items)
    Wheelchips.grid(row=0, column=5)
    Chittipapad = Radiobutton(lunchPapad, text="Chittipapad", font=("Arial", 10), indicatoron=0, variable=var6,
                              value="Chittipapad", command=update_selected_items)
    Chittipapad.grid(row=0, column=10)

    # snacks
    Kachori = Radiobutton(snackFrame, text="Kachori", font=("Arial", 12), indicatoron=0, variable=var7,
                          value="Kachori", command=update_selected_items)
    Kachori.grid(row=0, column=0)
    FruitCake = Radiobutton(snackFrame, text="FruitCake", font=("Arial", 12), indicatoron=0, variable=var7,value="FruitCake",command=update_selected_items)
    FruitCake.grid(row=0, column=5)
    Vegroll = Radiobutton(snackFrame, text="Vegroll", font=("Arial", 12), indicatoron=0, variable=var7,value="Vegroll", command=update_selected_items)
    Vegroll.grid(row=0, column=10)

    # Dinner
    # sweet
    BreadHalva = Radiobutton(dinnerSweet, text="BreadHalva", font=("Arial", 10), indicatoron=0, variable=var8,value="BreadHalva", command=update_selected_items)
    BreadHalva.grid(row=0, column=0)
    Kesari = Radiobutton(dinnerSweet, text="Kesari", font=("Arial", 10), indicatoron=0, variable=var8, value="Kesari", command=update_selected_items)
    Kesari.grid(row=0, column=5)
    GulabJamun = Radiobutton(dinnerSweet, text="GulabJamun", font=("Arial", 10), indicatoron=0, variable=var8, value="GulabJamun",command=update_selected_items)
    GulabJamun.grid(row=0, column=10)

    # icecreme
    Vannila = Radiobutton(dinnericecreme, text="Vannila", font=("Arial", 10), indicatoron=0, variable=var9,value="icecreme", command=update_selected_items)
    Vannila.grid(row=0, column=0)
    Strawberry = Radiobutton(dinnericecreme, text="Strawberry", font=("Arial", 10), indicatoron=0, variable=var9,value="Strawberry", command=update_selected_items)
    Strawberry.grid(row=0, column=5)
    ButterScotch = Radiobutton(dinnericecreme, text="ButterScotch", font=("Arial", 10), indicatoron=0, variable=var9, value="ButterScotch",command=update_selected_items)
    ButterScotch.grid(row=0, column=10)

    # Rice
    Biryani = Radiobutton(dinnerNonveg, text="Biryani", font=("Arial", 10), indicatoron=0, variable=var10,value="Biryani", command=update_selected_items)
    Biryani.grid(row=0, column=0)
    ChickenCurry = Radiobutton(dinnerNonveg, text="ChickenCurry", font=("Arial", 10), indicatoron=0, variable=var10,value="ChickenCurry",command=update_selected_items)
    ChickenCurry.grid(row=0, column=5)
    ChickenFriedrice = Radiobutton(dinnerNonveg, text="Chickenfriedrice", font=("Arial", 10), indicatoron=0, variable=var10,value="Chickenfriedrice", command=update_selected_items)
    ChickenFriedrice.grid(row=0, column=10)

   #veg
    MushroomCurry = Radiobutton(dinnerVeg, text="MushroomCurry", font=("Arial", 10), indicatoron=0, variable=var11,value="MushroomCurry",command=update_selected_items)
    MushroomCurry.grid(row=0, column=0)
    AaloChana = Radiobutton(dinnerVeg, text="AaloChana", font=("Arial", 10), indicatoron=0, variable=var11,value="AaloChana", command=update_selected_items)
    AaloChana.grid(row=0, column=5)
    Paneer = Radiobutton(dinnerVeg, text="Paneer", font=("Arial", 10), indicatoron=0, variable=var11,value="Paneer", command=update_selected_items)
    Paneer.grid(row=0, column=10)

    label_selected_items = Label(third_window, textvariable=selected_items,highlightbackground='black',highlightthickness=4,  font=('arial', 12, 'bold'), bd=10,relief=RIDGE)
    label_selected_items.place(x=1000, y=150)

    submit_button = Button(third_window, text="Submit", font=('arial', 15, 'bold'),  bd=10,fg="black",bg = "light green", relief=RIDGE,command=lambda: submit_action(user_id,selected_week))
    submit_button.place(x=1010, y=500)

    back_button = Button(third_window, text="Back", font=('arial', 15, 'bold'),  bd=10,bg="light grey", relief='ridge', command=go_back2)
    back_button.place(x=100, y=520)






root = Tk()
root.title("Campus Kitchen")
root.geometry("1199x600+100+50")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.resizable(False, False)
root.configure(bg='lavender')
ico = Image.open(r"C:\Users\gayat\Downloads\vishnuicon.png")
conn = sqlite3.connect("login.db")
cursor = conn.cursor()
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
create_login_frames()
root.mainloop()