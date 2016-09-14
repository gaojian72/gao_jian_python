
"""
Created on Thu Sep  8 19:33:43 2016

Homework 1 Group C

@author: Jian Gao
"""
# Question 1.    
d = {'merry': 'god', 'god':'merry', 'christmas': 'jul', 'jul':'christmas',
'and': 'och', 'och':'and','happy': 'gott', 'gott':'happy', 
'new':'nytt','nytt':'new','year': 'år','år':'year'}
def translate(x): 
    a=""
    for i in x.split():
        if i in d:
            a+=d[i]+" "
        else:
            a+=i
    return a
print(translate('merry christmas and happy new year'))
#############################################################
# Question 1 another version 
d = {"merry": "god", "christmas": "jul", "and": "och", 
      "happy": "gott", "new": "nytt", "year": "år"}
def translate(x): 
# define a new function named translate()
#This function used to translate English words into Swedish words in the dictionary d listed. 
    y = [] # define an array y to save Swedish vocabulary
    for i in x: # manipulate every elements in parameter x by using for loop.  
        y += [d[i]] # put the dictionary elements in array y. 
    return y #function output
print("Translate ['merry', 'christmas', 'and', 'happy', 'new', 'year']") # test content 
print(translate(['merry','christmas','and','happy','new','year'])) # test output


# Question 2.
def char_freq(x): 
# define a new function named char_freq() to calculate the fereuqncy of the listing characters.
    d = {} # define a dictiontionary d to save characters and it's frequency
    print(x)    
    for i in range(len(x)): # manipulate every characters in inputstring x
        if x[i] in d:    # case1: let x[1] denotes the character if the character is in the dictionary         
            d[x[i]]= int(d.get(x[i]))+1 # then increase the character's frequency by 1 
        else: # case 2: if the character is not in the dictionary 
            d[x[i]]= 1 # assign value 1 to the character's frequency 
    return d     # function output
print(str(char_freq("abbabcbdbabdbdbabababcbcbab")))  # test output


# Question 3.
key = {'a':'n', 'b':'o',
'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v',
'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X',
'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
'Z':'M'} 
def encoderanddecoder(x):
# define a new function to encode and decode strings from dictionary key.
# find the following letter for each one in dictionary key
    a= "" #declare a new empty variable a
    for i in x:
        if i in key: 
            a+=key[i] #key[i] is the following value of each letter.
    # at the beginning the letter is not in the list a, we need to at those letter's following value to the list a
        else:
            a+=i
    # when the letters's value are on the list, add them up to the list 
    return a
#print(encoderanddecoder('SHPX LBH CLGUBA!'))
print(encoderanddecoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))


# Question 4.
import re 
def correct(x):
# define a new function that takes string and sees to it that 
#1) two or more occurrences of the spac character is compressed into one, and 
#2) inserts an extra space after a period if the period is directly followed by a letter.     
# My idea is to seperate two cases, one is delete the space and another is add space between the words
  x=re.sub('\ +',' ',x) #substitue spaces between words to one space
  x=re.sub('\.','. ',x) #substitue period end with no space
  return (x)
print(correct("This  is very funny    and cool.Indeed!"))


# Question 5. 
def make_3sg_form(x):
# define a function to change the verbs to their correct third person singular form.
# if the verbs end up with y, changed y to -ies.
# if the verbs end up with "o,ch,s,sh,x,z" then add -es    
# else just add -s at the end.
  es=('o','ch','s','sh','x','z') # create a list to save those words whose end up with "o,ch,s,sh,x,z"
  x=input('Enter your verb:') # create a variable x which you can type whatever words you want 
  if x.endswith('y'): 
      x=x.replace(x[-1],'ies') # if the word end up with y, changes the y to -ies
  elif x.endswith(es):
      x=x+'es' # if the word end up with the letter shown in the list es, just plus -es at the end
  else:
      x=x+'s' # besides the previous two cases, just plus -s at the end 
  return x
print(make_3sg_form('x')) # test output


# Question 6 
vowel="aeiou" # create a list to save all vowel
consonant="qwrtpsdfghjklzxcvbnm" # create a list to save all consonant
def make_ing_form(x):
# define a function to change the verbs to their correct ing form
# if the verb end up with e, changes e to -ing.
# if the verb end up with ie, chenges -ie to y and add up -ing.
# if the last three letter of the verb is a consonant, vowel and consonant then repeat the last letter and add up -ing.  
    x=input('Enter your verb:') 
    # create a variable x which you can type whatever words you want
    if x.endswith('e'):
        x=x.replace(x[-1],'ing') 
        # case 1: if the verb ends up with e, changes -e to -ing.
    elif x.endswith('ie'):
        x=x.replace(x[-2],'ying') 
        # case 2: if the verb ends up with ie, changes -ie to y and add up -ing.
    elif x[-3] in consonant and x[-2] in vowel and x[-1] in consonant:
        x=x+x[-1]+'ing' 
        # case 3: if the verb ends up with consonant-vowel-consonant, 
        # repeat the last letter and add up -ing.
    else:
        x=x+'ing' # case 4: else, just add up -ing. 
    return x
print(make_ing_form('x')) # test output


# Question 7 
from functools import reduce 
# import higher order function reduce from module
def max_in_list(x):
# define a function to find the maximum number in a list of number 
    x=[int(i) for i in input('enter your numbers:').split()]
    # create a list x to input whatever number you like into that list 
    return reduce(max, x) 
    # the reduce function is used to compare the first two numbers which one is larger 
    # and then compare the next one with the first result, for the larger one, and so on. 
print(max_in_list('x')) # test output


# Question 8 
## using for loop 
def listlength(x):  
# define a function list the length of a list of words as integers using for loop
   items=input('enter your lists:').split()  
   # input whatever list you want like "Fuck You Python"
   list1=[] # create an empty lsit
   for i in items:
        list1.append(len(i))
        #add the length of each word in list"word" to list"length"
   return list1
print(listlength('items')) # test output [4, 3, 6]
    
# using the higher order function map()
def listlength(x):
# define a function list the length of a list of words as integers using function map()    
    x=input('enter your lists:').split()
    # input whatever list you want like "Fuck You Python"
    return list(map(len,x))
print(listlength('x')) # test output [4, 3, 6]

# using list comprehensions 
def listlength(x):
# define a function list the length of a list of words as integers using list comprehensions
    x=input('enter your lists:').split()
    # inpuit whatever list you want like "Fuck You Python"
    list1=[len(i) for i in x] 
    # create another list named list, let the elements in list1 be the length of list x
    return list1 
print(listlength('list1'))# test output [4, 3, 6]


# Question 9 
def find_longest_word(x):
# defne a funcion takses a list of words and returns the length of the longest one
    x=input('enter your lists:').split()
    # inpuit whatever list you want like "Fuck You Python"
    return max(map(len,x))
    # using the map() print the length of x corresponds to each words in x
print(find_longest_word('x')) # test output 6 


# Question 10 
def filter_long_words(x, n):
    x=input('enter your lists:').split()
    # inpuit whatever list you want
    #n=input('enter the value for n:')
    return(list(filter(lambda i:len(i)>n, x)))
    # lambda function len(i)>n can see if length of word in x >n. 
    # filter function pick those words up.
print(filter_long_words('x',3))


# Question 11
d = {"merry": "god", "christmas": "jul", "and": "och", 
      "happy": "gott", "new": "nytt", "year": "år"}
def translate(x): 
    return list(map(d.get,x))
    #return the value from the given dictionary d
print(translate(['merry','christmas','and','happy','new','year']))


# Question 12 
## define a function map()
def map(f,items):
# define a function map() with a function:f and a list:items
    items=[1, 2, 3, 4 ,5] 
    # create a list including some integers
    item1=[]
    # create an empty list
    for i in items:
        item1.append(f(i))
    # for every elements in the list items, put them into function f 
    # and then append the output to the list item1
    return item1
print(map(lambda x:x**2,'items'))
# test output. For instance, make the function f be square. 
# We should have [1, 4, 9, 16, 25]

## define a function filter()
def filter(f,items):
# define a function filter() with a condition function:f and a list:items
    items=[1, 2, 3, 4, 5]
    # create a list including some integers
    item1=[]
    # create an empty list
    for i in items:
        if f(i) == True:
            item1.append(i)
        # if the condition function f is true 
        # then put the output for items into list item1
    return item1
print(filter(lambda x:x>3, 'items'))
# test output. For instance, make the condition function f be every element larger than 3
# the output shuld be [4, 5]

## define a function reduce()
def reduce(items):
# define a function reduce() with a list:items    
    items=[1, 2, 3, 4, 5, 6]
    # create a list including some integers
    item1=[]
    # create an empty list
    for i in items[1:]:
        item1.append(max(items))
    # put the maximum value of list items into list item1
    return item1
print(reduce('item1'))

############### Done!!!! #############################################
