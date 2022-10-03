from datetime import datetime
from datetime import date
import random

bestand = open("StationBericht.txt", "w")

naam = input('Voer je naam in: ')
test = input()
tijd = datetime.now()
datum = date.today()
currentTime = tijd.strftime("%H:%M:%S")
station = ['Arnhem', 'Almere', 'Amersfoort']

if len(naam) == 0:
    naam = 'Anoniem'

if len(test) > 140:
    print('Te veel letters.')

else:
    print(naam)
    print(test)
    print(datum, currentTime)
    print(random.choice(station))

bestand.write('naam: ' + naam + '\n')
bestand.write('text: ' + test + '\n')
bestand.write(str(datum) + str(currentTime) + '\n')
bestand.write(random.choice(station) + '\n')
