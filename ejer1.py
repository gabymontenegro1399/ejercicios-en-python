Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> firstName= input("what is your first name?")
what is your first name? Bob
>>> print("Hello" +fistName+"¡")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print("Hello" +fistName+"¡")
NameError: name 'fistName' is not defined
>>> firstName= input("what is your first name?")
what is your first name? Bob
>>> print("Hello" +firstName+"¡")
Hello Bob¡

>>> 
