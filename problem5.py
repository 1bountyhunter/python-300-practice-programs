# WAP to perform all arithmetic operations of any 2 user inputs.

print("enter the numbers a and b:")
a, b = map(int, input().split())

# can be done more concisely wiith functions but we're doing it for beginners:
sum = a + b
print(f"sum: {sum}")

difference = abs(a - b)
print(f"difference: {difference}")

product = a * b
print(f"product: {product}")

result = a / b # float division
print(f"div_result: {result}")

quotient2 = a // b # floor division
print(f"quotient: {quotient2}")

remainder = a % b
print(f"remainder: {remainder}")

exponent = a ** b
print(f"exponent: {exponent}")


