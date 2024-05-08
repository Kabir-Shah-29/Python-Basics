# Write a Python program to sort a dictionary ascending by value.

d={
    'c':3,
    'd':4,
    'a':1,
    'e':5,
    'b':2
}
print(d)
for i in sorted(d,key=d.get):
    print(i,d[i])