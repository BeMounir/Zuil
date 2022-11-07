from datetime import datetime
from datetime import date
import random
from tkinter import *
import psycopg2


def invullen():
    tijdMod = datetime.now()
    datumMod = date.today()
    currentTimeMod = tijdMod.strftime("%H:%M:%S")
    Goedkeuring = '{}] {}] {}] {}] {}] {}'.format(datumMod, currentTimeMod, modNaam, modMail, keuze, eersteLine)
    reviewed.append(Goedkeuring.replace('\n', ' '))
def database():
    connection_string = "host='localhost' dbname='zuil1' user='postgres' password='moumou12'"

    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = """INSERT INTO Moderator (email, naam, tijd, datum)
                           VALUES (%s, %s, %s, %s)"""

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

    conn.commit()
    conn.close()

modNaam = input('Naam: ')
modMail = input('Email: ')
keuze = 'start'
reviewed = []
lijst = []
while keuze != 'stop':
    with open('StationBericht.txt') as f:
        eersteLine = f.readline()
    print(eersteLine)
    if eersteLine == str():
        break
    keuze = input('Goedkeuring bericht: ')
    if keuze == 'ja':
        keuze = True
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