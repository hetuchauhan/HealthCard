import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import sv_ttk
from tkinter import messagebox
from Lib.modules import createuser as cu, hereismodules as him, searchuser as su, deleteid as di
import os


def error(a):
    if a == 1:
        messagebox.showerror("Invalid Input", "You have made an invalid input. Enter details as stated.")

    if a == 2:
        messagebox.showerror("Invalid Input", "You have made an invalid input. Enter details as stated.")


def createuserwindow():
    def clearfields():
        Nameentry.delete(0, 'end')
        Ageentry.delete(0, 'end')
        Genderentry.delete(0, 'end')
        Aadhaarentry.delete(0, 'end')
        Mobileentry.delete(0, 'end')
        Pinentry.delete(0, 'end')
        Deptentry.delete(0, 'end')

    def submitdata():
        Name = str(Nameentry.get())

        Age = str(Ageentry.get())
        Gender = str(Genderentry.get())
        if him.is_correct_input("gender", Gender) is True:
            pass
        else:
            Genderentry.delete(0, 'end')
            error(1)
        Mobile = str(Mobileentry.get())
        if him.is_correct_input("mob", Mobile) is True:
            pass
        else:
            Mobileentry.delete(0, 'end')
            error(1)
        Aadhaar = str(Aadhaarentry.get())
        if him.is_correct_input("aadhaar", Aadhaar) is True:
            pass
        else:
            Aadhaarentry.delete(0, 'end')
            error(1)
        Pin = str(Pinentry.get())
        if him.is_correct_input("zip", Pin) is True:
            pass
        else:
            Pinentry.delete(0, 'end')
            error(1)
        Dept = str(Deptentry.get())

        cu.create_identity(2, Name, Age, Gender, Aadhaar, Mobile, Pin, Dept)
        messagebox.showinfo("Success!!!", "User created successfully.")
        clearfields()

    newuserwindow = Toplevel(master)
    newuserwindow.title("New User Creation")
    newuserwindow.geometry("370x600")
    newuserframe = Frame(newuserwindow, height=100)
    newuserframe.pack(fill=X)
    Label(newuserframe, text="Name").grid(column=1, row=1, pady=10)
    Label(newuserframe, text="Age").grid(column=1, row=3, pady=10)
    Label(newuserframe, text="Gender").grid(column=1, row=5, pady=10)
    Label(newuserframe, text="Aadhaar").grid(column=1, row=7, pady=10)
    Label(newuserframe, text="Mobile").grid(column=1, row=9, pady=10)
    Label(newuserframe, text="Pin").grid(column=1, row=11, pady=10)
    Label(newuserframe, text="Dept").grid(column=1, row=13, pady=10)

    Nameentry = Entry(newuserframe, width=50)
    Nameentry.focus_set()
    Nameentry.grid(column=1, row=2)
    Ageentry = Entry(newuserframe, width=50)
    Ageentry.grid(column=1, row=4)
    Genderentry = Entry(newuserframe, width=50)
    Genderentry.grid(column=1, row=6)
    Aadhaarentry = Entry(newuserframe, width=50)
    Aadhaarentry.grid(column=1, row=8)
    Mobileentry = Entry(newuserframe, width=50)
    Mobileentry.grid(column=1, row=10)
    Pinentry = Entry(newuserframe, width=50)
    Pinentry.grid(column=1, row=12)
    Deptentry = Entry(newuserframe, width=50)
    Deptentry.grid(column=1, row=14)

    button = Button(newuserframe, text="Submit", command=submitdata)
    button.grid(column=1, row=16, pady=10)
    button.focus_set()


def searchuserwindow():

    def submitdata():
        nonlocal selected
        nonlocal entry
        print('working2')
        typ = selected.get()
        print(typ, ";isok")
        data = entry.get()
        print(data)
        print("working3")

        if typ == 1:
            if him.is_correct_input("aadhaar", data) is True:
                pass
            else:
                entry.delete(0, 'end')
                error(2)
            result = su.searchuser(1, data)
            display_result(result)
        elif typ == 2:
            if him.is_correct_input("mob", data) is True:
                pass
            else:
                entry.delete(0, 'end')
                error(2)
            result = su.searchuser(2, data)
            display_result(result)
        elif typ == 3:
            result = su.searchuser(3, data)
            display_result(result)

    def clearprev():
        nonlocal searchuser_result
        searchuser_result.grid_forget()
        searchuser_result.destroy()
        searchuser_result = Frame(searchuserframe, height=100, width=100)

    def deletedata():
        typ = selected.get()
        data = entry.get()
        if typ == 1:
            returnedcode = di.deleteid(1, data)
            if returnedcode[1] == 200:
                clearprev()
                searchuser_result.grid(column=1, row=10, pady=10)
                Resultlabel = Label(searchuser_result, text="Record deleted!!!" + str(returnedcode[0]))
                Resultlabel.grid(column=1, row=1, pady=10)
        elif typ == 2:
            returnedcode = di.deleteid(2, data)
        elif typ == 3:
            returnedcode = di.deleteid(3, data)

    def display_result(result):

        searchuser_result.grid(column=1, row=10, pady=10)

        Resultlabel = Label(searchuser_result, text="Row count: " + str(result[1]))
        Resultlabel.grid(column=1, row=1, pady=10)
        if result[1] != 0:
            Resultlabel3 = Label(searchuser_result, text="Name: "+str(result[0][0][1]))
            Resultlabel3.grid(column=1, row=3, pady=10)
            Resultlabel4 = Label(searchuser_result, text="Age: "+str(result[0][0][2]))
            Resultlabel4.grid(column=1, row=5, pady=10)
            Resultlabel5 = Label(searchuser_result, text="Gender: "+str(result[0][0][3]))
            Resultlabel5.grid(column=1, row=7, pady=10)
            Resultlabel6 = Label(searchuser_result, text="Aadhaar: "+str(result[0][0][4]))
            Resultlabel6.grid(column=1, row=9, pady=10)
            Resultlabel7 = Label(searchuser_result, text="Moble: "+str(result[0][0][5]))
            Resultlabel7.grid(column=1, row=11, pady=10)
            Resultlabel8 = Label(searchuser_result, text="Pin: "+str(result[0][0][6]))
            Resultlabel8.grid(column=1, row=13, pady=10)
            Resultlabel9 = Label(searchuser_result, text="Date: "+str(result[0][0][7]))
            Resultlabel9.grid(column=1, row=15, pady=10)
            Resultlabel10 = Label(searchuser_result, text="Dept.: "+str(result[0][0][8]))
            Resultlabel10.grid(column=1, row=17, pady=10)
            delete_button = Button(searchuser_result, text="Delete Record", command=deletedata)
            delete_button.grid(column=1, row=19, pady=10)
        elif result[1] == 0:

            Resultlabel2 = Label(searchuser_result, text="No record found!!!")
            Resultlabel2.grid(column=1, row=5, pady=10)

    searchuserwindow = Tk()
    # Main Window min width
    searchuserwindow.geometry("500x700")
    searchuserwindow.title("Search User Window")

    searchuserframe = Frame(searchuserwindow, height=100)
    searchuserframe.grid(column=0, row=0, pady=10, sticky="ns")
    sv_ttk.set_theme("light")

    # radiobuttons
    selected = tk.IntVar(searchuserframe)
    r1 = Radiobutton(searchuserframe, text='Aadhaar', variable=selected, value=1, command=clearprev)
    r2 = Radiobutton(searchuserframe, text='Mobile', variable=selected, value=2, command=clearprev)
    r3 = Radiobutton(searchuserframe, text='Name', variable=selected, value=3, command=clearprev)

    r1.grid(column=1, row=1, padx=5, pady=5)
    r2.grid(column=1, row=2, padx=5, pady=5)
    r3.grid(column=1, row=3, padx=5, pady=5)

    # inputbox
    searchuser_inputframe = Frame(searchuserframe, height=100)
    searchuser_inputframe.grid(column=1, row=5, pady=10, sticky='ns')

    entry = Entry(searchuser_inputframe, width=30)
    entry.grid(column=1, row=2)

    Title = Label(searchuser_inputframe, text="Enter data: ")

    Title.grid(column=1, row=1, pady=10)

    searchuserframe.wait_variable(selected)

    search_button = Button(searchuser_inputframe, text="Search", command=submitdata)
    search_button.grid(column=1, row=3, pady=10)

    searchuser_result = Frame(searchuserframe, height=100, width=100)

    searchuserwindow.mainloop()


master = Tk()
master.geometry("200x200")
master.title("Database Management")
sv_ttk.set_theme("light")
create = Button(master, text="Create User", command=createuserwindow).pack(pady=10)
search = Button(master, text="Search User", command=searchuserwindow).pack(pady=10)
print(os.getpid())
mainloop()
