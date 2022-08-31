from dokusan import solvers, renderers,generators
from dokusan.boards import BoxSize, Sudoku
from subprocess import call
import requests
import getpass


# function for clear terminal after each answer
def clear():
    rc = call("./clear.sh")


# function for get data from db
def getInfo():
    pass
    userName = input("your Username: ")
    password = getpass.getpass(prompt='your Password: ')

    if password.lower() == password:
        login = True
    else:
        login = False


# core of project
r = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')
t = r.json()["board"]

sudoku = Sudoku.from_list(t, box_size=BoxSize(3, 3),)

# solution = solvers.backtrack(sudoku)
print(renderers.colorful(sudoku))


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

        if 0<row<10:
            if row == 1:
                row = 0
            if row == 2:
                row = 1
            if row == 3:
                row = 2           
            if row == 4:
                row = 3
            if row == 5:
                row = 4
            if row == 6:
                row = 5
            if row == 7:
                row = 6           
            if row == 8:
                row = 7
            if row == 9:
                row = 8
        
            argument = input("select your argument: ")
            argument = int(argument)
            
            if argument == 1:
                argument = 0
            if argument == 2:
                argument = 1
            if argument == 3:
                argument = 2
            if argument == 4:
                argument = 3
            if argument == 5:
                argument = 4
            if argument == 6:
                argument = 5
            if argument == 7:
                argument = 6
            if argument == 8:
                argument = 7
            if argument == 9:
                argument = 8    
            
            t[row][argument] = index

            # clear()
            print(renderers.colorful(sudoku))

