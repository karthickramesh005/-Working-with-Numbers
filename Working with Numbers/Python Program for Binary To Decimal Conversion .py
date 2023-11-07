# Python Program for Binary To Decimal Conversion :

'''
num = int(input("Enter a binary number : "))
binary_val = num
decimal_val = 0
base = 1

while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print("Binary Number is {}\nDecimal Number is {}".format(binary_val, decimal_val))
'''

# OR


binary_value = input("Enter a binary number : ")  # Replace this with your binary value
decimal_value = int(binary_value, 2)
print(decimal_value)
