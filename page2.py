import tkinter
from tkinter import *
from PIL import Image, ImageTk
import json
import psycopg2

#tkinter scherm
ws = Tk()
ws.geometry('400x300')
ws.title('NS Scherm')
ws['bg'] = '#Dcd730'
f = ("Times bold", 14)

#connection naar de database
connection_string = "host='localhost' dbname='zuil1' user='postgres' password='moumou12'"

conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

#de gebruikte query
query = "SELECT naam, bericht, datum, station, tijd FROM bericht WHERE goedkeuring = TRUE ORDER BY berichtid DESC LIMIT 5"

cursor.execute(query)
results = cursor.fetchall()

query2 = "SELECT station_city, ov_bike, elevator, toilet, park_and_ride FROM station_service"

cursor.execute(query2)
results2 = cursor.fetchall()

#hier opent hij de json file met de weer api informatie
with open('package.json', 'r') as openfile:
    json_object = json.load(openfile)

#hier pakt hij alleen de temperatuur van de json folder
weatherJson = json_object["main"]['temp']
cityJson = json_object['name']
for row in results2:
    if row[0] == cityJson:
        if row[1]:
            ov_bike = 'ov bike '
        else:
            ov_bike = ''
        if row[2]:
            elevator = ' elevator '
        else:
            elevator = ''
        if row[3]:
            toilet = ' toilet '
        else:
            toilet = ''
        if row[4]:
            parkAndRide = ' park and ride'
        else:
            parkAndRide = ''

#tk opmaak voor de faciliteit
Label(
    ws,
    text=(ov_bike + elevator + toilet + parkAndRide),
    padx=30,
    pady=20,
    bg='#Dcd730',
    font=f
).pack(expand=True, fill=BOTH)

#tkinter label
Label(
    ws,
    text=(weatherJson, 'C.'),
    padx=30,
    pady=20,
    bg='#Dcd730',
    font=f
).pack(expand=True, fill=BOTH)

for row in results:
    variable = str(row[0]) + '\n' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3])
    print(variable)
    Bericht = Label(
        ws,
        text=variable,
        padx=20,
        pady=20,
        bg='#Dcd730',
        font=f
    ).pack(expand=True, fill=BOTH)

cursor.close()
conn.close()

ws.mainloop()