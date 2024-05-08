'''Q4). Write a Python program to get a single string from two given strings, separated by a space and swap the first 
    two characters of each string.'''

def str_cc(a,b):
  c=(b[0:2]+a[2:]+" ")
  d=(a[0:2]+b[2:])
  e=c+d
  return e
a=input("Please enter string a : ")
b=input("Please enter string b : ")
print("The final string after concat. and swaping is : ",str_cc(a, b))