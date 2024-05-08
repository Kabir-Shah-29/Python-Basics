#Q8). Write a Python program to check whether a list contains a sublist.

a=input("Please enter a list : ")
b=input("Please enter a list : ")
if (all(i in a for i in b)):
    print("The sublist is present in the list")
else:
    print("The sublist isn't present in the list")