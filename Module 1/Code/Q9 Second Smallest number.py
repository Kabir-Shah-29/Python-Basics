#Q9).Write a Python program to find the second smallest number in a list.

a=[2,6,3,8,9,-1,7]
def smallestnum(a):
    print(a)
    l=len(a)
    a.sort()
    print("Second smallest number is : ",a[1])
smallestnum(a)