# Python program to check if
# given number is prime or not

num = int(input("Check the Number : "))

# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1): 
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        count = 1
        if (num % i) == 0:
            count = count + 1
            break

if count == 1:
    print(num, "is a prime number") 
else:
    print(num, "is not a prime number")

