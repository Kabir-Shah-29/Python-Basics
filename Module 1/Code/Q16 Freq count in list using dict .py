#Q16).Counting the frequencies in a list using a dictionary in Python.
l = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
print(l)
def freq_count(l):
    l1={}
    for i in l:
        l.count(i)
        l1.update({i:l.count(i)})
    print(l1)
freq_count(l)