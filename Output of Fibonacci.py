Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  i = 2 while True: if i%3 == 0: break print(i) i += 2
 
SyntaxError: unexpected indent
>>> i = 2
>>> while True:
	if i%3 == 0:
		break
	print(i) i += 2
	
SyntaxError: invalid syntax
>>> i = 2
>>> while True:
	if i%3 == 0:
		break
	print(i)
	i += 2

	
2
4
>>> 
= RESTART: C:/Users/kabir/AppData/Local/Programs/Python/Python39-32/Fibonacci.py
1
1
2
3
5
8
13
21
34
>>> 
= RESTART: C:/Users/kabir/AppData/Local/Programs/Python/Python39-32/Fibonacci.py
1
1
2
3
5
8
13
21
34
55
89
144
>>> 