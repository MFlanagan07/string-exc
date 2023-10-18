#excercies 86
pw = input("enter a new password ")
pw2 = input("enter it again ")
while pw != pw2:
    print("incorrect case try again")
    pw2 = input("enter it again ")
    if pw == pw2:
        print("sound")
    elif pw != pw2:
        print("incorrect case try again")
        pw2 = input("enter it again ")
        if pw == pw2:
            print("sound")
        elif pw != pw2:
            print("incorrect case try again")
            pw2 = input("enter it again ")
            if pw == pw2:
                print("sound")
            elif pw != pw2:
                print("incorrect case try again")
                pw2 = input("enter it again ")
                if pw == pw2:
                    print("sound")
                elif pw != pw2:
                    print("incorrect case try again")
                    pw2 = input("enter it again ")
                    if pw == pw2:
                        print("sound")
                    elif pw != pw2:
                       print("incorrect case try again")
                       pw2 = input("enter it again ")
                       if pw == pw2:
                           print("sound")
                       elif pw != pw2:
                           print("incorrect case try again")
                           pw2 = input("enter it again ")
                           if pw == pw2:
                            print("sound")
                           elif pw != pw2:
                            print("incorrect case try again")
                            pw2 = input("enter it again ")
                            if pw == pw2:
                             print("sound")
                            elif pw != pw2:
                             print("incorrect case try again")
                             pw2 = input("enter it again ")
if pw.upper() == pw2.upper():
    print("sound")
    