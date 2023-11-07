# Python Program for LCM Of Two Numbers :

n1 = int(input("Enter a first number : "))
n2 = int(input("Enter a second number : "))

for i in range(max(n1,n1), 1 + (n1 *  n2)):
    if i % n1== i  %  n2 == 0 :
        lcm = i
        break
print("LCM of ",n1," and ",n2," is ",lcm)
