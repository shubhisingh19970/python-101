csv = 'Eeic,John,Michael,Terry,Graham:Terry G : Brain '
friends_list = ['Exercise : fill me with names']
print(friends_list)
# From the list above fill a list (friends_list) properly
# With the names of all the friends . One per "slot"
# You may need to run some commands several times
# Use print () statements to work your way through the exercise 
friends_list = (','.join (','.join(csv.split (' : ')).split(':'))).split(' , ')
print (friends_list)

