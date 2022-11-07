from datetime import datetime
from datetime import date
import random
from tkinter import *
from functools import partial

bestand = open("StationBericht.txt", "a")

naam = input('Voer hier uw naam in: ').strip()
bericht = input('Voer hier uw bericht in: ').strip()
tijd = datetime.now()
datum = date.today()
currentTime = tijd.strftime("%H:%M:%S")
station = ['Arnhem', 'Almere', 'Amersfoort']


if len(naam) == 0:
    naam = 'Anoniem'

while len(bericht) >= 140:
    bericht = 'te veel characters'
    print(bericht)
    bericht = input('Voer hier uw text opnieuw in: ')


uikomst = bestand.write('{}] {}] {}] {}] {}'.format(naam, bericht, random.choice(station), str(datum), str(currentTime)) + '\n')
bestand.close()


print(naam)
print(bericht)
print(datum, currentTime)
print(random.choice(station))