a = 0
b = 1

n = int(input("How many Fibonacci numbers do you want to print?"))  # Get user input for count

for i in range(n):
    c = a + b
    print(c)
    a, b = b, c