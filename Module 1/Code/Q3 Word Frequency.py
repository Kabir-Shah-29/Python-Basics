#Q3). Write a Python program to count the occurrences of each word in a given sentence.#

s=input("Please enter a string : ")
def wordfreq(s):
    count=dict()
    words=s.split()

    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count 

print("The number of occurences of each word are : ", wordfreq(s))