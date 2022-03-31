import os
from tkinter import *

#def __init__() :
#    window = Tk()
#    window.resizable(0, 0)
#    window.geometry('375x667')
#    window.title('Mathomify')
#    window.mainloop()
#__init__()

def __calculator__() :
    #Detects inputs from user
    first = input("First: ")
    second = input("Second: ")

    #Checks if there are no 0s inputted
    if(float(first) == 0) :
        print("SYNTAX ERROR")
        while 1:
            print("Restarting...") 
            os.system("python Calculator.py")
            exit()

    elif(float(second) == 0) :
        print("SYNTAX ERROR")
        while 1:
            print("Restarting...") 
            os.system("python Calculator.py")
            exit()

    if(float(second) and float(first) == 0) :
        print("SYNTAX ERROR")
        while 1:
            print("Restarting...") 
            os.system('python Calculator.py')
            exit()

    e_type = input("Type: ")

    #Adds the numbers up or subtracts them
    add = float(first) + float(second)
    subtract = float(first) - float(second)
    multiply = float(first) * float(second)
    divide = float(first) / float(second)

    #Conditional structure checking if all requirements are met and if there are no s
    if(str(e_type) == "*") :
        if(multiply > 32767) :
            print("Integers above 32767 are not calculated")
            while 1:
                print("Restarting...") 
                os.system("python Calculator.py")
                exit()

        elif(multiply < 0) :
            print("Integers below 0 are not calculated")
            while 1:
                print("Restarting...") 
                os.system("python Calculator.py")
                exit()

        else :
            print(multiply)

    elif(str(e_type) == "/") :
        if(divide > 32767) :
            print("Integers above 32767 are not calculated")
            while 1:
                print("Restarting...") 
                os.system("python Calculator.py")
                exit()
        elif(divide < 0) :
            print("Integers below 0 are not calculated")
            while 1:
                print("Restarting...") 
                os.system("python Calculator.py")
                exit()
        else :
            print(divide)

    elif(str(e_type) == "+") :
        if(add > 32767) :
            print("Integers above 32767 are not calculated")

        elif(add < 0) :
            print("Integers below 0 are not calculated")
            while 1:
                print("Restarting...") 
                os.system("python Calculator.py")
                exit()

        else :
            print(add)

    elif(str(e_type) == "-") :
        if(subtract > 32767) :
            print("Integers above 32767 are not calculated")


        elif(subtract < 0) :
            print("Integers below 0 are not calculated")
            while 1:
                print("Restarting...") 
                os.system("python Calculator.py")
                exit()

        else :
            print(subtract)
__calculator__()