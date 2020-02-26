import pprint
import random


print("""Welcome to Simple DND character creator!
      Please enter the amount of players in your game:""")
players = int(input())

#create a small program that will iterate however many players there are
#


#bug instead of printing out iterating a single character at a time
#the program prints out every single characters stats.
for i in range(int(players)):
    name = input("What is your character's name? ")
    race = input("What is the race of %s ? " %(name))
    age = input("How old is %s? " %(name))
    bio = input("Provide a brief description of who %s is. " %(name))
    alignment = input("State %s\'s alignment. " %(name))
    classLevel = input("What is %s\'s class/level? " %(name))


class DND():
    #this method stores the info into variables
    def __init__(self, name, race, age, bio, players, alignment, classLevel):
        self.name = name
        self.race = race
        self.age = age
        self.bio = bio
        self.players = players
        self.alignment = alignment
        self.classLevel = classLevel

    #this function is supposed to append the users' input into a list
    def playerstats(self):
        playerInfo = {}
        playerInfo.setdefault('name', []).append(self.name)
        playerInfo.setdefault('race', []).append(self.race)
        playerInfo.setdefault('age', []).append(self.age)
        playerInfo.setdefault('bio', []).append(self.bio)
        playerInfo.setdefault('players', []).append(self.players)
        playerInfo.setdefault('alignment', []).append(self.alignment)
        playerInfo.setdefault('classLevel', []).append(self.classLevel)
        print(playerInfo)


#these two lines store in the information into the __init__ method
#then into a dictionary
Character_1 = DND(name, race, age, bio, players, alignment, classLevel)
Character_1.playerstats()
