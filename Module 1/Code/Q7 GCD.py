#Q7). Program to find Greatest Common Divisor of two numbers.

a=int(input("Please enter number 1 : "))
b=int(input("Please enter number 2 : "))
def gcd(a,b):
    if a>b:
        sn=b
    else:
        sn=a
    for i in range(1,sn+1):
        if (a%i==0) and (b%i==0):
            gcd=i
    return gcd

print(f"The GCD of {a} and {b} is ", gcd(a, b))