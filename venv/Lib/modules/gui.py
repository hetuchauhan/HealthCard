import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import sv_ttk
from tkinter import messagebox
from Lib.modules import createuser as cu, hereismodules as him, searchuser as su


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
        if him.is_correct_input("gender", Gender) == True:
            pass
        else:
            Genderentry.delete(0, 'end')
            error(1)
        Mobile = str(Mobileentry.get())
        if him.is_correct_input("mob", Mobile) == True:
            pass
        else:
            Mobileentry.delete(0, 'end')
            error(1)
        Aadhaar = str(Aadhaarentry.get())
        if him.is_correct_input("aadhaar", Aadhaar) == True:
            pass
        else:
            Aadhaarentry.delete(0, 'end')
            error(1)
        Pin = str(Pinentry.get())
        if him.is_correct_input("zip", Pin) == True:
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


def searchuserwindow():

    def hide(obj):
        obj.grid_forget()
    def display_result(result,hideobj):
        hide(hideobj)
        searchuser_result = Frame(searchuserframe, height=100, width=100)
        searchuser_result.grid(column=1, row=10, pady=10)
        Resultlabel = Label(searchuser_result, text="Row count: " + str(result[1]))
        Resultlabel.grid(column=1, row=1, pady=10)
        if result[1]!=0:
            #Resultlabel2 = Label(searchuser_result, text="Sr No.: "+result[0][0][0])
            #Resultlabel2.grid(column=1, row=len(i), pady=10)
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
        elif result[1]==0:
            hide(searchuser_result)
            Resultlabel2 = Label(searchuserframe, text="No record found!!!")
            Resultlabel2.grid(column=1, row=5, pady=10)

        #search_button.grid_forget()
    clicks = 0
    def searchuser_aadhaar():

        def submitdata():
            Aadhaar = str(Aadhaarentry.get())
            if him.is_correct_input("aadhaar", Aadhaar) == True:
                pass
            else:
                Aadhaarentry.delete(0, 'end')
                error(2)
            result = su.searchuser(1, Aadhaar)
            display_result(result,searchuser_aadhaarframe)

        searchuser_aadhaarframe = Frame(searchuserframe, height=100)
        searchuser_aadhaarframe.grid(column=1, row=5, pady=10)
        Title = Label(searchuser_aadhaarframe, text="Aadhaar")
        Title.grid(column=1, row=1, pady=10)
        Aadhaarentry = Entry(searchuser_aadhaarframe, width=30)
        Aadhaarentry.grid(column=1, row=2)
        search_button = Button(searchuser_aadhaarframe, text="Search", command=submitdata)
        search_button.grid(column=1, row=3, pady=10)



    def searchuser_mobile():
        def submitdata():
            Mobile = str(Mobileentry.get())
            if him.is_correct_input("mob", Mobile) == True:
                pass
            else:
                Mobileentry.delete(0, 'end')
                error(2)
            result = su.searchuser(2, Mobile)
            display_result(result,searchuser_mobileframe)

        searchuser_mobileframe = Frame(searchuserframe, height=100)
        searchuser_mobileframe.grid(column=1, row=5, pady=10)
        Title = Label(searchuser_mobileframe, text="Mobile")
        Title.grid(column=1, row=1, pady=10)
        Mobileentry = Entry(searchuser_mobileframe, width=30)
        Mobileentry.grid(column=1, row=2)
        button = Button(searchuser_mobileframe, text="Search", command=submitdata)
        button.grid(column=1, row=3, pady=10)


    def searchuser_name():
        def submitdata():
            Name = str(Nameentry.get())

            result = su.searchuser(3, Name)

            display_result(result,searchuser_nameframe)

        searchuser_nameframe = Frame(searchuserframe, height=100)
        searchuser_nameframe.grid(column=1, row=5, pady=10)
        LT = Label(searchuser_nameframe, text="Name")
        LT.grid(column=1, row=1, pady=10)
        Nameentry = Entry(searchuser_nameframe, width=30)
        Nameentry.grid(column=1, row=2)
        button = Button(searchuser_nameframe, text="Search", command=submitdata)
        button.grid(column=1, row=3, pady=10)


    searchuserwindow = Tk()
    searchuserwindow.geometry("500x400")
    searchuserwindow.title("Search User Window")
    searchuserframe = Frame(searchuserwindow, height=100)
    searchuserframe.grid(column=1, row=1, pady=10)

    selected = tk.StringVar()
    r1 = Radiobutton(searchuserframe, text='Aadhaar', value=1, variable=selected,
                         command=searchuser_aadhaar)
    r2 = Radiobutton(searchuserframe, text='Mobile', value=2, variable=selected, command=searchuser_mobile)
    r3 = Radiobutton(searchuserframe, text='Name', value=3, variable=selected, command=searchuser_name)
    r1.grid(column=1,row=1, padx=5, pady=5)
    r2.grid(column=1,row=2, padx=5, pady=5)
    r3.grid(column=1,row=3, padx=5, pady=5)

    print(selected.get())


master = Tk()
master.geometry("200x200")
master.title("Database Management")
sv_ttk.set_theme("light")
create = Button(master, text="Create User", command=createuserwindow).pack(pady=10)
search = Button(master, text="Search User", command=searchuserwindow).pack(pady=10)

mainloop()
