"""Q5). Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead If the string length of the given 
string is less than 3, leave it unchanged """


def mod_str(ms):
  M=len(ms)
  C="ing"
  D="ly"
  if M>2:
    if C not in (ms[-3:]):
      print(ms+C)
    else:
      print(ms+D)
  return ms

ms=input("Please enter a string : ")
mod_str(ms)