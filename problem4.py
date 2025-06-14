# WAP to input age from user and display if eligible for voting or not(18+)

age  = int(input("enter age : "))
if(age < 18):
    print(f"Sorry! You cannot particitapate in voting,  you will be able to particiapte after {18-age} years.")
else:
    print("Allowed to vote!")