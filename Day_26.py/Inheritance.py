class Person :
    def move(self):
        print("Moves 4 places")
    def rest(self):
        print("Gains 4 health points")

class Doctor (Person) :
    def heal (self):
        print("Heals 10 Health points")

class Fighter (Person) :
    def fight(self):
        print("Does 10 health points of damage")
character_1 = Doctor()
                   
