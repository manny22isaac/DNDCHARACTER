import pprint
import random
import sys


print("""Welcome to Simple DND character creator!
      Please enter the amount of players in your game.(UP TO 6) :""")

players = int(input())

characterinfo = {'name':[], 'race':[], 'age':[], 'bio':[],
                 'alignment':[], 'classLevel':[]}

name = []
race = []
age = []
bio = []
alignment = []
classLevel =[]


if players <= 6:
    for i in range(int(players)):
        name = input("What is your character's name? ")
        characterinfo.setdefault('name', []).append(name)
        race = input("What is the race of %s ? " %(name))
        characterinfo.setdefault('race', []).append(race)
        age = input("How old is %s? " %(name))
        characterinfo.setdefault('age', []).append(age)
        bio = input("Provide a brief description of who %s is. " %(name))
        characterinfo.setdefault('bio', []).append(bio)
        alignment = input("State %s\'s alignment. " %(name))
        characterinfo.setdefault('alignment', []).append(alignment)
        classLevel = input("What is %s\'s class/level? " %(name))
        characterinfo.setdefault('classLevel', []).append(classLevel)

elif players > 6 or players <= 0:
    print("Sorry, but you do not meet the required amount of players.")
    sys.exit()


class DND():
    #this method stores the info into variables
    def __init__(self, characterinfo, players):
        self.characterinfo = characterinfo
        self.players = players
    #this function is supposed to append the users' input into a list
    def playerstats(self):
        playerInfo = characterinfo
        print(playerInfo)


Characters = DND(characterinfo, players)
Characters.playerstats()
