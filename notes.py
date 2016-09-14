# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## for loop example 

#ex1
for n in 'python':
    print ('current letter:',n)

#ex2    
fruits = ['banana','apple','mango']
for fruits in fruits:
    print('current fruit:', fruits)
    
print("Good Bye~")

#ex3
fruits = ['banana','apple','mango']
for index in range(len(fruits)): 
    print('current fruit:', fruits[index])
print('Good Bye!')
print(len(fruits))
print(range(len(fruits)))

#ex4


x='blue,red,green'
x.split(",")
a,b,c=x.split(",")

dic={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"}
s=""
s=s+dic[1]+""

d={'alpha':'xavi','beta':'yes','theta':'zore','delta':'while'}
def fuck(x):
    a=""
    for i in x.split():
        if i in d:
            a+=d[i]+" "
        else:
            a+=i
    return(a)
print(fuck('alpha beta theta delta'))


import re #import regular expression module
def correct(string):
    '''
    Define a simple "spelling correction" function correct()that takes a
    string and sees to it that 1) two or more occurrences of the space
    character is compressed into one, and 2) inserts an extra space
    after a period if the period is directly followed by a letter.
    My thought: use regular expression, correct the sentence in two steps.
    '''
    string=re.sub('\ +',' ',string) #substitute one or more spaces between two words to one space
    string=re.sub('\.','. ',string) #substitute period end with no space to period end with one space
    return(string)
    
print(correct("This  is very funny    and cool.Indeed!"))


import re
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print( "No match!!")

re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
       r'static PyObject*\npy_\1(void)\n{',
       'def myfunc():')



x='fuck'
y=x.replace(x[-1],'shit')
print(y)

person = input('Enter your name: ')
print('Hello', person)

from functools import reduce  #import reduce module
def max_in_list(list1):
    '''
    This function uses the higher order function reduce() to takes a list of numbers and returns the largest
    one.
    '''
    return reduce(max,list1) #compare the first two numbers, and then compare the largest number in the first two with the thrid number, and so on.

print(max_in_list([1,2,3,4,5]))

def listlength(word):
    '''
    The following functions map a list of words into a list of integers
    representing the lengths of the correponding words. Three functions are written using a for-loop.
    '''
    length = [] #empty list
    for i in word:
        length.append(len(i)) #add the length of each word in list"word" to list"length"
    return length
print(listlength(['I','love','python']))


## map() function example

items=[1, 2, 3, 4, 5]
def sqrt(x):
    return x ** 2
list(map(sqrt,items))








