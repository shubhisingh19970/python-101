
with open('friends.csv','r') as f:
    print(f.read())
    friends = f.read().splitlines()
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())