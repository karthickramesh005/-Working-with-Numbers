# Python Program to calculate number of digits in an integer :
import math
num = int(input("Enter a numbers : "))

digit = math.floor(math.log10(num)+1)
print("Number of digits : ",digit)
