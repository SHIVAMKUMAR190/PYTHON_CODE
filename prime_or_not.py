number = int(input("enter the number : "))

factors = 0

for i in range(1, number + 1):
    if number % i == 0:
        factors = factors + 1

if factors == 2:
    print("it is a prime no")
else:
    print("it is not a prime no")