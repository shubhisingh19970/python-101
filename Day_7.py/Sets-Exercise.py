#1. Check if 'Eric' and 'John' exist in friends.
#2. Combine or add the two sets together.
#3. Find names that are in both sets.
#4. Find names that are in either set but not both.
#5. Show only the names who only appear in one of the lists.
#6. Create a new cars-list without duplicates.

print (" 'Eric' in friends and 'John' in friends ")
friends = { 'John','Michael','Terry','Graham','Eric'}
my_friends = {'Reg','Liya','Colin','Eric','Graham'}
cars = ['345','463','F46','20T','345','F46','20T']
print ( friends.union(my_friends))
print (friends.intersection(my_friends))
print(friends & my_friends)