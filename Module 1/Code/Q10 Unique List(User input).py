#Q10). Write a Python program to get unique values from a list.

a=list(input("Please enter a list : "))
print(a)
b=[]
def unique_list(a):
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
unique_list(a)