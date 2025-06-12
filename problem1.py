#WAP to calculate square of given numbers, as taken input from usergit 
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(f"The square of {i} is: {i**2}")


#using enumerate: 

n = int(input("Enter a number: "))
squares = [i**2 for i in range(1, n+1)]
for i, square in enumerate(squares, start=1):
    print(f"The square of {i} is: {square}")
