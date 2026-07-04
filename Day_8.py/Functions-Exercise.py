#def greeting (name,age = 28):
    # Greets user with 'name; from 'input box' and 'age' , if available , defaault age is used
  name = input("Enter your name: ")
  age = input ("Enter your age:  ")
#print ('Hello' + { name } + ', you are' + str(age) + '!')
#print(f'Hello {name}, you are {age}!')

#greeting (name,32)
    #1 Add new print statement on a new line which says 'We hear you like the colours xxx ! xxx ia a string with colour
#print (f'we hear you like the colour { colour } ! ')

    #2 Extend the function with another input parameter 'colour' , that depends to 'red'
#def greeting ( name,age = 28 ,colour = 'red') :

#3 Capture the colour via an input box as variable : colour 
 #colour = input ('Enter your favourite colour: ')

 def greeting(name, age=28, colour='red'):
    # Greets user with 'name' and 'age' (or 'age's default), and now 'colour' too
    print('Hello ' + name + ', you are ' + str(age) + '!')
    print(f'Hello {name}, you are {age}!')

    # Task 1: new print statement using the colour parameter
    print(f'We hear you like the colour {colour}!')


# --- Main program (this runs OUTSIDE the function definition) ---
name = input('Enter your name:  ')
age = input('Enter your age:   ')
colour = input('Enter your favourite colour: ')

greeting(name, int(age), colour)
