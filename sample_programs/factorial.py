

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

no=int(input("Enter the number"))
print(factorial(no))



