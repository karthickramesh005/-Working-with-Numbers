# Python program to find HCF of Two Numbers :

n1 = int(input("Enter a first number : "))
n2 = int(input("Enter a second number : "))
hcf = 1

for i in range(1,min(n1,n2)):
    if (n1 % i == 0) and n2 % i == 0 :
        fact = i
print("HCF of ",n1," and ",n2, " is ",hcf)
