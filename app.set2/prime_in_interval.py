# Python program to print all
# prime number in an interval

def prime(x, y):
    prime_list = []
    for i in range(x, y): 
        if (i == 0) or (i == 1):
            continue 
        else:
            count = 1
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    count = count + 1
                    break
            if count == 1:
                prime_list.append(i)
    return prime_list

# Driver program
starting_range = 5
ending_range = 100
lst = prime(starting_range, ending_range)
if len(lst) == 0: 
    print("There are no prime numbers in this range")
else: 
    print("The prime numbers in this range are: ", lst)

