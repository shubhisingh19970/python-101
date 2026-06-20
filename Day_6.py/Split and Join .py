msg = 'Welcome to Python 101 : Split and Join' 
cvs = ' Eric,John , Michael , Terry , Graham '
friends_list = [ 'Eric' , 'John' , 'Michael' , 'Terry' , 'Graham' ]
print(msg.split())
print(cvs.split(','))
print(msg.split(' , '), type (msg.split))
print ('-' . join (friends_list))
print ('-'.join (friends_list + friends_list))
print (' '.join (msg.split(' ')))
print (msg.replace ( ' ' ,' '))