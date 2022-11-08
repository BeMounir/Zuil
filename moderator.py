#het importe van alles dat ik nodig heb
from datetime import datetime
from datetime import date
import random
from tkinter import *
import psycopg2

#function voor het invullen van het bericht met de moderator informatie + het bericht zelf
def invullen():
    tijdMod = datetime.now()
    datumMod = date.today()
    currentTimeMod = tijdMod.strftime("%H:%M:%S")
    Goedkeuring = '{}] {}] {}] {}] {}] {}'.format(datumMod, currentTimeMod, modNaam, modMail, keuze, eersteLine)
    reviewed.append(Goedkeuring.replace('\n', ' '))

#functie voor het bericht sturen naar het database
def database():
    #connectie naar mijn prosgres database
    connection_string = "host='localhost' dbname='zuil1' user='postgres' password='moumou12'"

    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    #de query voor het invullen van de moderator berichten naar het database
    query = """INSERT INTO Moderator (email, naam, tijd, datum)
                           VALUES (%s, %s, %s, %s)"""

    #dit zijn de specifieke plekken van het lijst in de code hieronder nadat in stukken wordt gehakken. het wordt dan hier verdeeld
    data = (lijst[3], lijst[2], lijst[1], lijst[0])
    cursor.execute(query, data)

    query3 = """INSERT INTO Station (stationScherm, faciliteit)
                                   VALUES (%s, %s)"""

    data3 = ('test', True)
    cursor.execute(query3, data3)

    query2 = """INSERT INTO Bericht (naam, bericht, tijd, datum, station, goedkeuring)
                           VALUES (%s, %s, %s, %s, %s, %s)"""

    data2 = (lijst[5], lijst[6], lijst[9], lijst[8], lijst[7], lijst[4])
    cursor.execute(query2, data2)

    #hier stuurt hij het naar de database
    conn.commit()
    conn.close()

#de moderator naam en email invullen
modNaam = input('Naam: ')
modMail = input('Email: ')
#dit is voor het whileloop, als je stop schrijft dan stopt het progamma
keuze = 'start'
#lege lijsten waar ik strings van de bericht kan invullen
reviewed = []
lijst = []
#whileloop voor goedkeuring
while keuze != 'stop':
    with open('StationBericht.txt') as f:
        eersteLine = f.readline()
    print(eersteLine)
    if eersteLine == str():
        break
    keuze = input('Goedkeuring bericht: ')
    #als de keuze ja is dan wordt keuze True zodat het in de database kan bij goedkeuring
    if keuze == 'ja':
        keuze = True
        #de functie van boven wordt hier gebruikt
        invullen()
        #for loop waar hij de bericht in stukken hakt en in een string zet
        for x in reviewed:
            lijst.extend(x.split('] '))
            print(lijst)
            database()
            lijst.clear()
            reviewed.clear()
            print(lijst)
        #hier verwijdert hij het gebruikte line in het text document zodat het niet dubbel wordt gebruikt
        with open('StationBericht.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('StationBericht.txt', 'w') as fout:
            fout.writelines(data[1:])

# hier gebeurt er hetzelfde, maar dan is keuze False inplaats van True, dit wordt ook naar het database verstuurt
    elif keuze == 'nee':
        keuze = False
        invullen()
        for x in reviewed:
            lijst.extend(x.split('] '))
            print(lijst)
            database()
            lijst.clear()
            reviewed.clear()
            print(lijst)
        with open('StationBericht.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('StationBericht.txt', 'w') as fout:
            fout.writelines(data[1:])