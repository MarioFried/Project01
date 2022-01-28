# Function for nth Fibonacci number

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        anterior = 0
        atual = 1
        for i in range(3,n+1):
            number = anterior + atual 
            anterior = atual
            atual = number
        return number

# Driver Program
num = int(input("Nth Number of Fibbonacci Sequence : "))
print(Fibonacci(num))

# This code is contributed by Saket Modi

