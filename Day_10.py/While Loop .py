#LOOP : Codes that run again and again until a certain condition is met.

print ("1. * Loops are great *")
print ("2.* * Loops are great * *")
print ("3.* * * Loops are great * * *")

i = 1
while i < 4:
    print ("* Loops are great *")
    print (f" {i} . "+ "*" * i + " Loops are great " + "*" * i)
    i = i + 1
