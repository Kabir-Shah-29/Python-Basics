#Q15). Given a number n, write a python program to make and print the list of Fibonacci series up to n.

n=int(input("Please enter a number : "))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()