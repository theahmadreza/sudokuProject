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

        # core
        t[row] = index
        # clear()
        print(renderers.colorful(sudoku))

