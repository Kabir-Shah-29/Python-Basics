#Write a python program using function to find the sum of odd series and even series
#Odd series: 12/ 1! + 32/ 3! + 52/ 5!+……n 
#Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n
import math
n=int(input("Please enter value of n : "))
def sum(n):
    for i in range(0,n+1):
        s=(((10*i)+2)/math.factorial(i))
    print(s)

sum(n)