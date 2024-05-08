#Q13). Write a Python program to sort a dictionary descending by value.

d={
    'c':2,
    'd':5,
    'a':3,
    'e':4,
    'b':1
}
print(d)
for i in sorted(d,key=d.get,reverse=True):
    print(i,d[i])