#Q12). Write a Python program to convert a list of tuples into a dictionary

a=[("Ben",21),("Alex",22),("Dean",20),("Opie",21)]
d={}
def conversion(a,d):
    d=dict(a)
    return d
print(conversion(a, d))