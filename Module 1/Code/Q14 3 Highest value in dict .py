#Q14). Write a Python program to find the highest 3 values in a dictionary.

d={
    "Alex":50,
    "Hales":65,
    "Ben":52,
    "Stebin":71,
    "Matt":67,
    "Quagmire":69
}
print(d)
d1=list(d.values())
d1.sort(reverse=True)
print("The 3 highest values in d are : ")
for i in d1[0:3]:
    print(i)