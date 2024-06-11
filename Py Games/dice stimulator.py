import random

b = "y"
while b == "y":
    x = random.randint(1,6)
    print(x)
    if(x == 1):
        print("--------")
        print("|      |")
        print("|  1   |") 
        print("|      |")
        print("--------")
    if(x == 2):
        print("--------")
        print("|   1  |")
        print("|      |")
        print("|   1  |")
        print("--------")
    if(x == 3):
        print("--------")
        print("|   1  |")
        print("|   1  |")
        print("|   1  |")
        print("--------")
    if(x==4):
        print("--------")
        print("| 1   1|")
        print("|      |")
        print("| 1   1|")
        print("--------")
    if(x == 5):
        print("--------")
        print("| 1   1|")
        print("|   1  |")
        print("| 1   1|")
        print("--------")
    if(x==6):
        print("--------")
        print("|1    1|")
        print("|1    1|")
        print("|1    1|")
        print("--------")
    b = input("Press y to roll the dice again : ")
