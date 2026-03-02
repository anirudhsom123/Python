# editing Strings
s="hello world"
print(id(s))
# s[0]='H'  not allowed strings and immutable
s='anirudh'
print(id(s))

#  Deleting String
del s
#print(s) # s is not defined error will come since s is deleted
s="hello world"
# del s[-1:-5:3]
#print(s) # will through an error since string is immutable we can't edit string