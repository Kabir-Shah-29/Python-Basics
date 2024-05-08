#Q18). Python Program to Find Factorial of Number Using Recursion

n1=int(input("Please enter a number :"))
factorial=1
if n1==1 and n1==0:
  print("The factorial of ",n1," is 1")
else:
  for i in range(1,n1+1):
    factorial=factorial*i
  print("The factorial of ",n1," is ",factorial)