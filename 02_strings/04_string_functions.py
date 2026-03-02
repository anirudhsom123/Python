# common functions , that can be applied to all data types in python
# len
s='Hello world'
print(len(s)) # return the length of the string include spaces as well
print(max(s)) # return the value with greatest ascii value
print(min(s)) # return the value with minimum ascii value
print(sorted(s)) # returns a list sorted on basis of ascii value (smaller to greater)
print(sorted(s,reverse=True)) # returns a list sorted on basis of ascci value( greater to smaller)

# functions that only works on strings , i.e specific to strings
s='hello world'
print(s.capitalize()) # capitalize the 1st char of the string
print(s.title()) # convert every first char of word in a sentence to capital letter
print(s.upper()) # convert all characters to upper char
print(s.lower()) # convert all characters to upper char
print('HlEoo wOrld'.swapcase()) # converts capital char to smal char and smal char to capital char


# some other functions
# COUNT/FIND/INDEX

print('my name is anirudh'.count('i',10,15),"************") # count for the frequency of the character provided
print('my name is anirudh'.find('is')) # returns the starting index of the string from where the string we want to find starts
# if the string we are searching is not in the parent string it will return -1

# print('my name is anirudh'.index('x')) # returns the stating index of the string from where the string we want to find starts
# if the string we are searching is not in the parent string it will throw an error



# ENDSWITH/ STARTSWITH
print('hello'.endswith('llo')) # true since ends with llo
print('hello'.startswith('e')) # false since not starts with e

# FORMAT
name="Anirudh"
gender='male'

greetings="Hello my name is {} and my gender is {}".format(name,gender)
print(greetings)

# ISALNUM/ISALPHA/ISDIGIT/ISIDENTIFIER

print('anirudh1234'.isalnum()) # return True check is string  alpha or numeric or not , can be numeric only and can be alphabetic only
print('anirudh1234%'.isalnum()) # return False since % is not alphabet neither number
print('1234'.isdigit())
print('first_name'.isidentifier()) # return true check for is its a valid identifer or not


# SPLIT/JOIN
print('my name is anirudh som'.split()) # return list with splited words
print('my name is anirudh som'.split('i')) # return list with splited words with break point as 'i'

print(' '.join(['my', 'name', 'is', 'anirudh', 'som']))
print('i'.join(['my name ', 's an', 'rudh som']))

# REPLACE
print('hi my name is anirudh'.replace('anirudh','ani')) # will replace anirudh with ani
print('hi my name is anirudh'.replace('dhu','xyz')) # no change since no word like dhu in sentence

# STRIP
# removes trailg spaces
print('anirudh     '.strip())
