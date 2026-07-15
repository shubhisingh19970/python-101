#Party Invitation 
# You are having a party and want to invite your friends.
# You want the print out invitations for each friend using for loops.
# The names are in two lists ,'names' and 'names1'.
# You also need to add two extra names to the lists using an 'input' box , when you rum the code .
# Printout one invitation to each friend per line .
# Names should be properly capitalized .
# Hint : You may need two (for) loops to solve this exercise .

names = ['john ClEEse','Fric IDLE','michael']
names1 = ['graHam chapman','TERRY','terry jones']
msg = 'You are invited to my party on Saturday!'

names = names + names1
for index in range (2) :
    names .append(input('Enter a name to invite: '))
for name in names:
    msg1 = f' {name.title ()} ! {msg}'
    print(msg1)
