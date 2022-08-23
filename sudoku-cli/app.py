from dokusan import generators
from subprocess import call
import numpy as np

def clear():
    rc = call("./clear.sh")

arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))
    
print(arr.reshape(9,9))

# inputs
index = input("your index: ")
row = input("Select row: ")

# make inputs as integer
index = int(index)
row = int(row)

if index > 0:
    arr[row] = index
    print(arr.reshape(9,9))
    



# if see == '1':
#     arr[] = 1
#     print(arr.reshape(9,9))    
