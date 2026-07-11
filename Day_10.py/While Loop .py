#LOOP : Codes that run again and again until a certain condition is met.

print ("1. * Loops are great *")
print ("2.* * Loops are great * *")
print ("3.* * * Loops are great * * *")

#Three Loop Questions :
#1. What do I want to repeat ?
#2. How many times do I want to repeat it ?
#3. What is the condition for repeating it ?

i = 1
while i < 4:
   
    print (f" {i} . "+ "*" * i + " Loops are great " + "*" * i)
    i = i + 1
