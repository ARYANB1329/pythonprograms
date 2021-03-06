# Program to Represent a Sparse Matrix
# J. Raghuramjee - 121910313004

# Declare the 2-D matrix
arr = [[0,0,0,3],[0,1,3,0],[9,0,0,0],[0,0,0,4]]
r = len(arr) # Number of Rows
c = len(arr[0]) # Number of columns

# Printing the original array
print("The Original Matrix")
for i in arr:
    print(*i)
print()

# Declaring an array to store sparse matrix
sp = []

# Finding the non zero elements
for i in range(r):
    for j in range(c):
        if arr[i][j]!=0:
            sp.append([i,j,arr[i][j]])

# Printing the sparse matrix
print("The Sparse Matrix")
for i in sp:
    print(*i)
