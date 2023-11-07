# Python program to find Prime Numbers between starting to ending :

def prime(n):
    if n < 2:
        return 0
    else:
        x= n
        for j in range(2,x):
            if n % j == 0:
                return 0
    return 1





start = int(input("Enter a starting number : "))
end = int(input("Enter a finishing number : "))

for i in range(start,end + 1):
    if prime(i):
        print(i,end=" ")
