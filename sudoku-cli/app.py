from dokusan import generators
from subprocess import call
import numpy as np
import getpass


# function for clear terminal after each answer
def clear():
    rc = call("./clear.sh")


# function for get data from db
def getInfo():
    pass
    userName = input("your Username: ")
    password = getpass.getpass(prompt='your Password: ')

    if password.lower() == PASSWORD:
        login = True
    else:
        login = False


# core of project
arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))

print(arr.reshape(9,9))


a = True

# while loggin == True
while True:
    
    if a == True:

        # inputs
        index = input("your index: ")
        row = input("Select row: ")

        # make inputs integer
        index = int(index)
        row = int(row)

        # core
        arr[row] = index
        # clear()
        print(arr.reshape(9,9))
        
