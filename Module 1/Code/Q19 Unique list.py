#Q19). Write a Python function that takes a list and returns a new list with unique elements of the first list.

A=[2,2,2,7,0,0,5,9,4,4,4,4]
print(A)
B=[]
def unique_list(A):
    for i in A:
        if i not in B:
            B.append(i)
    print(B)
unique_list(A)