from Lib.modules import createuser as cu, hereismodules as mod

mod.imports()
while True:

    ch = int(input(
        "Enter your choice-----\n1.Create new identity\n2.Search identity\n3.Modify identity\n4.Delete identity\n5.Exit\n-->"))
    if ch == 1:
        cu.create_identity()

    elif ch == 5:
        break
    else:
        pass
