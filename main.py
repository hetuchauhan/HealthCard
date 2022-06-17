from Lib.modules import createuser as cu, hereismodules as mod,viewencdata as ved, searchuser as su,deleteid as di
mod.imports()
while True:
    choice=int(input("You are-----\n1.Administrator\n2.End User(You can only view based on your string or QR.)\n3.Exit\n-->"))
    try:
        if choice==1:

            while True:
                ch = int(input(
                    "Enter your choice-----\n1.Create new identity\n2.Search identity\n3.Delete identity\n5.Exit\n-->"))
                if ch == 1:
                    cu.create_identity(1)
                elif ch == 2:
                    pref = int(input("How would you like to search the record\n1. By Aadhaar No.\n2. By Mobile\n3. By Name\n4. Exit\n--->"))
                    if pref == 1:

                        aadhaar = input("Enter Aadhaar No.: ")
                        a = mod.is_correct_input("aadhaar", aadhaar)
                        if a == True:
                            print("oktest")
                            pass
                        else:
                            mod.error()
                        records = su.searchuser(1, aadhaar)
                        for i in records:
                            print(i)

                    elif pref == 2:

                        mob = input("Enter Mobile No.: ")
                        a = mod.is_correct_input("mob", mob)
                        if a == True:
                            pass
                        else:
                            mod.error()
                        records = su.searchuser(2, mob)
                        for i in records:
                            print(i)

                    elif pref == 3:

                        name1 = input("Enter Name: ")
                        records = su.searchuser(3, name1)
                        for i in records:
                            print(i)

                    elif pref == 4:
                        quit()

                    else:
                        print("Wrong input!")


                elif ch==3:
                    pref = int(input(
                        "How would you like to delete the record\n1. By Aadhaar No.\n2. By Mobile\n3. By Name\n4. Exit\n--->"))
                    if pref == 1:

                        aadhaar = input("Enter Aadhaar No.: ")
                        a = mod.is_correct_input("aadhaar", aadhaar)
                        if a == True:
                            pass
                        else:
                            mod.error()
                        records = di.deleteid(1, aadhaar)
                        for i in records:
                            print(i)
                        break

                    elif pref == 2:

                        mob = input("Enter Mobile No.: ")
                        a = mod.is_correct_input("mob", mob)
                        if a == True:
                            pass
                        else:
                            mod.error()
                        records = di.deleteid(2, mob)
                        for i in records:
                            print(i)
                        break

                    elif pref == 3:

                        name1 = input("Enter Name: ")
                        records = di.deleteid(3, name1)
                        for i in records:
                            print(i)
                        break

                    elif pref == 4:
                        quit()

                    else:
                        print("Wrong input!")
                elif ch == 5:
                    break
                else:
                    pass
        elif choice==2:
            ask="y"
            while ask=="y":
                ved.frontendinput()
                ask=input("Want to check other record?(Y/N): ").lower()
        else:
            break
    except:
        mod.error()