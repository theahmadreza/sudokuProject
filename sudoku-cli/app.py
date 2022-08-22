from dokusan import generators
import numpy as np


arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))
    
print(arr.reshape(9,9))

see = input("your index as length: ")

if see == '1':
    arr[0] = 1
    print(arr.reshape(9,9))    
