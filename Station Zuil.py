from datetime import datetime
from datetime import date
import random
from tkinter import *
from functools import partial

#bestand openen waar alle berichten naartoe worden geschreven
bestand = open("StationBericht.txt", "a")

#hier is alle informatie dat er nodig is om de database ermee te vullen
naam = input('Voer hier uw naam in: ').strip()
bericht = input('Voer hier uw bericht in: ').strip()
tijd = datetime.now()
datum = date.today()
currentTime = tijd.strftime("%H:%M:%S")
station = ['Arnhem', 'Almere', 'Amersfoort']

#als de lengte van de naam 0 is dan wordt de naam automatisch anoniem
if len(naam) == 0:
    naam = 'Anoniem'

#als de lengte van het bericht meer is dan 140, dan moet je opnieuw het goede hoeveelheid characters invullen
while len(bericht) >= 140:
    bericht = 'te veel characters'
    print(bericht)
    bericht = input('Voer hier uw text opnieuw in: ')

#dit is alle informatie geschreven in 1 lijn
uikomst = bestand.write('{}] {}] {}] {}] {}'.format(naam, bericht, random.choice(station), str(datum), str(currentTime)) + '\n')
bestand.close()

#hier kan je in de terminal zien wat je hebt geschreven
print(naam)
print(bericht)
print(datum, currentTime)
print(random.choice(station))