from Lib.modules import createuser as cu, hereismodules as mod,viewencdata as ved

mod.imports()
while True:
    choice=int(input(
        "You are-----\n1.Administrator\n2.End User(You can only view based on your string or QR.)\n3.Exit\n-->"))
    try:
        if choice==1:

            while True:
                ch = int(input(
                    "Enter your choice-----\n1.Create new identity\n2.Search identity\n3.Modify identity\n4.Delete identity\n5.Exit\n-->"))
                if ch == 1:
                    cu.create_identity()

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