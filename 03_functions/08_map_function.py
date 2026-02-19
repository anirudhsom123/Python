
# eg. 1
res=map(lambda n:n**2,[1,2,3,5,6])
print(list(res))

# eg. 2
oddEven=map(lambda num:'even' if num%2==0 else 'odd' , [1,2,3,4,5])
print(list(oddEven))

# eg. 3
users=[
    {
    'name':'anirudh',
    'age': 22,
    'gender' : 'male'
    },
    {
    'name':'anirudh som ',
    'age': 22,
    'gender' : 'male'
    },
    {
    'name':'dinesh kumar',
    'age': 22,
    'gender' : 'male'

    }
]

print(list(map(lambda d:d['name'],users)))