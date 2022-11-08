import requests
import json
import psycopg2
from tkinter import *
from functools import partial

#tkinter scherm
ws = Tk()
ws.geometry('400x300')
ws.title('NS Scherm')
ws['bg'] = '#Dcd730'
f = ("Times bold", 14)

#functie dat de weer van de api pakt en ook de weer van de gekozen stad
def weer():
    apiKey = 'f76b7f74cd6c4f49f1a361da0df8c21b'
    city = entry.get()
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    completeURL = baseURL + "lang=nl&appid=" + apiKey + "&q=" + city + "&units=metric"
    response = requests.get(completeURL)

    #hier stuurt hij alle gegevens van de weer api naar de json file en dan gaat hij naar de volgende pagina
    with open("package.json", "w") as outfile:
        json.dump(response.json(), outfile, indent=4)
    ws.destroy()

    import page2

#dit allemaal is opmaak voor de tkinter scherm
Label(
    ws,
    text="Vul je stad in",
    padx=20,
    pady=20,
    bg='#Dcd730',
    font=f
).pack(expand=True, fill=BOTH)

#invul bar voor tkinter scherm
entry = Entry(master=ws)
entry.pack(padx=10, pady=10)

#enter knop voor tk enter scherm
Button(
    ws,
    text="Enter",
    font=f,
    command=weer
).pack(fill=X, expand=TRUE, side=LEFT)
ws.mainloop()
