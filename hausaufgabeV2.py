# -*- coding: utf-8 -*-

# imports
import json
import os
import sys
from datetime import datetime
from random import randint

#Funktionen
def saveuserdata():
    userdata = {
        "balance": coins,
        "rating": finalrating
    }
    with open(Userpath+".json", "w") as file:
        file.writelines(json.dumps(userdata))
        file.close()

def rating():
    ratingtxt = getInput("Hat ihnen ihr Aufenthalt gefallen?")
    temp2 = datetime.now().strftime(' %d-%m-%Y %H:%M:%S')
    global finalrating
    finalrating = ratingtxt+temp2

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
        if gameFinisher == "N":
            rating()
            saveuserdata()
            print("Sie verlassen uns mit einem Guthaben von ", coins, "cz")
            quit()
        elif gameFinisher == "Y":
            gameFinisherRepeater = False
        else:
            print("Geben Sie N für Nein oder Y für Ja ein.")

name = getInput("Sag mir, wie lautet ihr Name? \n")

# variablen-mainloop
Userpath = r"Nutzerprofile/"+name
mainloopswitch = True
previousDiceNumber = 0
coins = 500

#Accountsuche und -erstellung
SearchfileName = Userpath+".json"
if not os.path.isfile(SearchfileName):
    file = open(SearchfileName, "w+")
else:
    print("Sie werden auf einem bereits existierenden Account spielen")
    with open(Userpath+".json", "r") as data:
        openExistingAcc = json.load(data)
        coins = openExistingAcc['balance']

#Spielerklärung
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
    input("\nDrücke eine beliebige Taste zum Würfeln.")
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

    endingGame()