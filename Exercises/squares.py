"""

squares of 1 - 10
display the list
display the first and last in list
display the square of 5,6,7


"""

# comment


squares = []

count = 1

while count < 11:
    result = count * count
    #squares[count-1] = result
    squares.append(result)
    count = count + 1


print("\nThe list of squares 1-10 is: ")
print(squares)
print("The first in the list is: ")
print(squares[0])
print("The last in the list is: ")
print(squares[-1])
print("The squre of 5, 6 and 7 is: ")
print(squares[4:7])
