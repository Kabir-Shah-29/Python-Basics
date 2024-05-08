"""Q6). Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 
'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string """


def repl_str(rs):
  rs1=rs
  c=d=0
  c=rs.find("not")
  d=rs.find("poor")
  if(c>=0 and d>=0):
    rs1=rs.replace(rs[c:d+4],"good")
  return rs1

rs=input(("Please enter a string : "))
print("The replaced string is : ",repl_str(rs))