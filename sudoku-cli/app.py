from dokusan import generators
from subprocess import call
import numpy as np

def clear():
    rc = call("./clear.sh")

arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))
    
print(arr.reshape(9,9))


a = True

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
        clear()
        print(arr.reshape(9,9))
        
