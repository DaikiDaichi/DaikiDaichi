# -*- coding: utf-8 -*-

# imports
import os
import sys
from random import randint

#Funktionen
def SaveUserAccountBalance():
    file = open(Userpath + name + ".txt", "w")
    file.writelines(str(coins))
    file.close()

def getInput(message):
    if sys.version_info[0] == 2:
        return raw_input(message)
    else:
        return input(message)

def endingGame():
    gameFinisherRepeater = True
    operatingNote = 0
    while gameFinisherRepeater:
        gameFinisher = getInput("Wollen Sie nochmal spielen? ")
        if operatingNote == 1:
            print("Geben Sie N für Nein oder Y für Ja ein.")
        elif gameFinisher == "N":
            quit()
        elif gameFinisher == "Y":
            gameFinisherRepeater = False
            operatingNote = 0
        operatingNote = operatingNote+1

# variablen-mainloop
Userpath = r"Nutzerprofile/"
mainloopswitch = True
previousDiceNumber = 0
coins = 500

# Benutzerspeicherung und Spielerklärung
name = getInput("Sag mir, wie lautet ihr Name? \n")

SearchfileName = Userpath+name+".txt"
if not os.path.isfile(SearchfileName):
    file = open(SearchfileName, "w+")
else:
    print("Sie werden auf einem bereits existierenden Account spielen")
    with open(Userpath+name+".txt", "r") as f:
        firstline = f.readline()
        firstline = float(firstline)
        coins = firstline

print("\n"+name + ", lassen Sie uns ein Spiel spielen.\nDie Regeln sind ganz leicht.\nEs werden zwei Würfel geworfen.\n"
        "Ergeben die Augenzahlen 7 oder 11 gewinnen Sie.\nErgeben die Augen jedoch 2,3 oder 12, gewinne ich.\nDen "
        "Einsatz bestimmen Sie.\nMomentan beträgt ihr Kontostand",coins,"cz.")

# mainloop
while mainloopswitch:
    # Einsatz setzen
    insertloopswitch = True

    while insertloopswitch:
        try:
            insert = input("\nIhr Einsatz, bitte:\n")
            insert = float(insert)
            insertloopswitch = False
        except ValueError:
            print("Bitte geben Sie nur eine Zahl ein!")

    if insert > coins:
        print("Sie haben nicht so viel Guthaben!")
        break

    # Die zwei Würfel
    dicenumber = randint(2, 12)

    # visuelle Überprüfung
    print(dicenumber)

    # Verarbeitung
    if dicenumber == 7 or dicenumber == 11 or dicenumber == previousDiceNumber:
        print("Glückwunsch, Sie haben gewonnen!")
        coins = coins+insert

    elif dicenumber == 2 or dicenumber == 3 or dicenumber == 12:
        print("Verloren")
        coins = coins-insert
        if coins <= 0:
            mainloopswitch = False

    else:
        print("Sie haben weder gewonnen noch verloren.\n")
        previousDiceNumber = dicenumber

    print(coins,"cz")
    SaveUserAccountBalance()
    endingGame()