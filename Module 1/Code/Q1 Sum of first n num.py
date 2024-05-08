#Q1). Write a python program to sum of the first n positive integers.#
a=int(input("Please enter a number : "))
def sumation(a):
    b=0
    for i in range(1,a+1):
        b+=i
    return b

print("The sum of first n numbers is : ",sumation(a))  
