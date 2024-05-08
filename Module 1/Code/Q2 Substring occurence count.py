##Q2). Write a Python program to count occurrences of a substring in a string.##

b=input("Please enter a string : ")
b1=input("Plese enter a sub string to count its occurences : ")

def countofoccurence(b,b1):
    

    count=0
    start=0

    while start<len(b):
        position=b.find(b1,start)

        if position!=-1:
            start=position+1
            count+=1
        
        else:
            break
    return count

print("The number of occurences : ",countofoccurence(b, b1))