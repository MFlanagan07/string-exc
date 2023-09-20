fname = input("enter your first name ")
if len(fname) < 5:
    sname = input("what is your surname")
    FULLNAME = (fname + sname)
    FULLNAME = FULLNAME.upper()
    print(FULLNAME)
else:
    fname = fname.lower()
    print(fname)