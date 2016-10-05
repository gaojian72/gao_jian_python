# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:45:30 2016

@author: Jian Gao

Group c

"""

##Prof G - This does not work. Part of the reason is that the reason is that the
##Prof G - "is_palindrome" function calls a function called "reverse", which is
##Prof G - undefined.

# Question 1
def palindrome(string):
    """"
    This function reverses a string, e.g. "abcd" to "dcba"
    Parameter:
    A string 
    Returns:
    The reverse of x
    """
    # get the length of the string and subtract 1
    end_of_str=len(string)-1
    revStr=''
    for Char in string:
        # start at the end of the string and work back to
        # beginning to build the reversed string
        revStr += string[end_of_str]
        end_of_str=end_of_str - 1
    return revStr 
    
def is_palindrome(input_word):
    """
    This function, is_palindromo(), recognizes
    palindromes (i.e. words that look the same written backwards).
    For instance, is_palindrome("radar") should return True.
    
    Parameters:
    input_word: any word with alphabetic characters
    
    Returns:
    True is the word is a palindrome, false otherwise 
    """
    palindrome = False # Initialize our return variable to False
    input_word=input_word.upper() # Take care of mixed by case by upper
                                  # casing the word
    input_word=input_word.replace(" ","") # Take care of spaces
    if not input_word.isalpha():
        return palindrome
    if reverse(input_word) == input_word:
        palindrome = True
    return palindrome
    
def palindrome_file(file):
    file1=open(file) # open a file
    for line in file1.read().split('\n'): # read file by lines seperated 
        if is_palindrome(line):
            print(line)  # print the line if it is palindrome
    return None
palindrome_file('C:/GJ/110.txt')
    

# Question 2
##Prof G - This does not work. there is no checking that the word pairs are 
##Prof G - actually semordnilap
def semordnilap(file):
    '''
    This function works  that accepts a file name (pointing to a list of words)
    from the user and finds and prints all pairs of words that are
    semordnilaps to the screen. 

    Parameter:
        file

    Returns:
        A list of paired words
        '''
    list1=list(open(file).read().split()) 
    # open a text file and convert into list1
    list2=[] # create an empty list
    for i in list1:
        list2.append(i+' '+i[::-1])
            # word + space + backward word 
    return list2
semordnilap('C:/GJ/110.txt')


# Question 3
##Prof G - Nice, handles mixed case but should not count blanks and CR's
def char_freq_table(file):
    '''
    This function accepts a file name from the user, builds a frequency listing of
    the characters contained in the file, and prints a sorted and
    nicely formatted character frequency table to the screen.
    
    Parameter:
    A file
    
    Returns:
    A table showing frequency of characters
    '''
    string=open(file).read()#open a file and read each line
    d={}
    # define a dictiontionary d to save characters and it's frequency
    print(string)
    for i in range(len(string)):
        # manipulate every characters in inputstring string
        if string[i] in d:
 # case1: let string[1] denotes the character if the character is in the dictionary
            d[string[i]]= int(d.get(string[i]))+1
        else:
            d[string[i]]= 1
# case 2: if the character is not in the dictionary 
# assign value 1 to the character's frequency 
    return d 
print(char_freq_table('C:/GJ/110.txt')) # local file 


# Question 4 
d={'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
'y':'yankee', 'z':'zulu'} #define dictionary d
import os 
import time
##Prof G - Does not work on my machine
def speak_out(string,ICAO_pause,word_pause_time):
    '''
    This function translate string into ICAO words and speak the out.
    Parameter:
    A string 
    Returns:
    Speak ICAO words
    '''
    for k in string.split():#split a string into words
        for i in k:#i represents each character
            if i not in "`~!@#$%^&*()_-=+[]{}\|;:,<.>/?": #not punctuation
                os.system('say'+d[i.lower()])#speak
            # speak out
                time.sleep(ICAO_pause)
            # pause between ICAO words
    time.sleep(word_pause_time)# pause between words.
    
##Prof G - Inappropriate test phrase
speak_out('Fuck you Python',0.5,3)
    
    
# Question 5 
##Prof G - Works well.
def hapax(file):
    '''
    Define a function that gives the file of text words only appear once
    Ignore the capitalization and punctions
    Parameter:
    A file
    Return:
    A list containing all hapaxes
    '''
    string=open(file).read() # open a file and read each line
    string=string.lower() # ignore the capitalization
    puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
    # ignore punctions
    for i in string:
        if i in puncspace:
            string=string.replace(i,'')
            # ignore all punctuations in string
    hapax1=[] # create an empty list for hapax
    for k in string.split():
        if string.count(k)==1:
        # if the word only appears once
            hapax1.append(k)
        # put that word into list hapax1
    return hapax1
print(hapax('C:/GJ/110.txt'))
    

# Question 6
##Prof G - This will not work properly if file contains the full path name. May 
##Prof G - consider accepting both the input and output file or finding a more
##Prof G - robust method of creating an output file name (using regex)
def numberfile(file):
    '''
    This function gives a text file will create a new text file in
    which all the lines from the original file are numbered from 1 to n.   
    Parameter:
    A file
    Returns:
    A new file with numbered lines
    '''
    file1=open(file).readlines() # file1 is a list
    file2=open('new'+file,'w') # new empty file
    for i in range(len(file1)):
        file2.write('line'+str(i+1)+': '+file1[i]) # add 'line#: ' to the begining of each line, put them together into line2
    file2.close() # save and close
numberfile('C:/GJ/110.txt') 
    
    
# Question 7 
def average(file):
    ##Prof G - Nice, works well.
    '''
    Define a function average to calculate the average word length
    of a text in a file.
    Parameter:
    A file
    Return:
    A number 
    '''
    x=open(file).read() # open a file and read it
    x=x.lower()
    puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/? "
    x=x.replace('\n',' ')
    # no space in string x
    number1=len(x.split())
    # calculate the number of total files define as number1
    for i in x:
        if i in puncspace:
            x=x.replace(i,'') # no spaces and punctuations in string x
    number2=len(x) # calculate the number of characters
    return number2/number1
print(average('C:/GJ/110.txt'))        
    
    
# Question 8 
##Prof G - Should make this a function. Otherwise, it works well.
'''
This program is able to play the 'Guess the number' game.
Parameter:
A number x
Return:
You guess is correct or wrong.
'''
Attempt=1
Answer=18 # given 
Name=input("What is your name?") 
# input your name
while True:
    x=int(input('{} I am thinking of a number between 1 and 20. Take a guess.'.format(Name)))
    # input a number x
    if x==Answer:
        print('Congradulation, {}! You guessed the number in the {} attempt!'.format(Name,Attempt))
        break # stop this game 
    elif x<Answer:
        print('Your guess number is too low. Try again!')
        Attempt+=1 # Attempt plus 1
    else:
        print('Your guess number is too high. Try again!')
        Attempt+=1 # Attempt plus 1
        

# Question 10 
'''
This game is to find the correct word by gussing, and in return
receive two kinds of clues:
1) the characters that are correct with correct order, mark that character with[]
2) the characters that are correct with wrong order, mark that character with()
Parameter:
a list of characters with the same range as the answer
Return:
list of characters
'''
answer='lingo'
# input correct answer
while True:
    guess=input('Enter your guess word:')
    new=''
    
    for i in range(len(guess)):
        if guess[i] in answer[i]:
            new+='['+guess[i]+']' 
            # add [] to the correct character with correct order
        ##Prof G - This is meant to mean, in the word but in the wrong position.
        ##Prof G - If I guess lllll the output should be [l]llll (there are no
        ##Prof G - more l's after the first position)
        elif guess[i] in answer:
            new+='('+guess[i]+')'
            # add () to the correct character but with incorrect order 
        else:
            new+=guess[i]
            # if nothing is correct just add those characters
    if guess==answer:
        print('Clue:' +new)
        break
    else:
        print('Clue:' +new)

    
# Question 11
import re

def splitter(file_name):
    ##Prof G - Did not work on my test file.
    '''
    This function opens a txt file and works as a sentence splitter to
    write its sentences with each sentences on a separate line.
    Sentence boundaries occur at one of "." (periods), "?" or "!", except that
    a. Periods followed by whitespace followed by a lower case letter
    are not sentence boundaries.
    b. Periods followed by a digit with no intervening whitespace are
    not sentence boundaries.
    c. Periods followed by whitespace and then an upper case letter,
    but preceded by any of a short list of titles are not sentence
    boundaries. Sample titles include Mr., Mrs., Dr., and so on.
    d. Periods internal to a sequence of letters with no adjacent
    whitespace are not sentence boundaries (for example,
    www.aptex.com, or e.g).
    e. Periods followed by certain kinds of punctuation (notably comma
    and more periods) are probably not sentence boundaries.   
    Parameter:
    A file
    Returns:
    The modified file
    '''
    file=open(file_name, 'r')
    text=file.read()
    
    S=re.sub(r'\n', '', text)
    # remove the newline we already have there
    # substitute \n with empty string
    
    S=re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', S)  
    # preceded by 'Mr', 'Mrs' or 'Dr' and is followed by a space and an uppercase letter
    
    S=re.sub(r'!\s', '!\n', S)
    # substitute after every '!'
    
    S=re.sub(r'\?\s', '?\n', S)
    # substitute after every '?'
    
    print(S)
    
print(splitter('C:/GJ/Q11.txt'))
    
    
    



        
    

