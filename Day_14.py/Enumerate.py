friends = ['John Cleese', 'Eric Idle', 'Michael Palin', 'Graham Chapman', 'Terry Gilliam', 'Terry Jones']

for friend in friends :
    print (friend)
# But we want to print with numbers that's where enumerators steps in ('i')

print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

i = 0
for friend in friends:
    print(i, friend)
    i = i +1 # += 1

print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]

#i = 51
#for friend in friends:
#    print(i, friend)
#    i = i +1 # += 1
for num, friend in enumerate(friends,51):
    print(num, friend)
    
print(type(enumerate(friends)))
print(list(enumerate(friends)))        