#Q11). Write a Python program to unzip a list of tuples into individual lists.

a=[(3,4,5),(2,4,6),(5,12,13)]
print(a)
def unziplist(a):
    for b in a:
        c=list(b)
        print(c)
unziplist(a)
