"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)
# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
x=64 
y=32
z=x+y
print (z)
# 3.- Make a program that prints a sentence that includes at least 3 variables.
a='today is thursday.'
b='today is sunny.'
c='sky is blue'
d=a+b+c
print (d)
# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
e='This is my first Python program.'
print(len(e))
# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
f=1920*1.1
g=1080*1.1
h=int(f)
i=int(g)
h_new=str(h)
i_new=str(i)
result='The 10% overscan of 1920 is '+h_new+' , and the 1080 is '+i_new
print (result)

