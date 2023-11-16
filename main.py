import random
from Flughafen import Flughafen
from Flugzeug import Flugzeug
from FlugzeugData import get_flugzeuge


"""
1) Eine Klasse definieren (Klassendiagramm) 2) Implementierung:
 3 Objektattribute und 2 Klassenattribute

 2) Mindestens 2 Operatoren überladen (+, größer)

3) Business erstellen: Objekte erzeugen und "testen".
Muss: gut kommentieren, docstring benutzen, so arbeiten, dass die Codierung weiter verwendet werden kann
"""


def menu():
    result = "--------------------------------------------------\n"
    result += "Was möchtest du tun?\n"
    result += "1. Überschicht Flughafen\n"
    result += "2. Übersicht Flugzeuge\n"
    result += "3. Flugzeug landen\n"
    result += "4. Flugzeug starten\n"
    result += "5. Exit\n"
    result += "--------------------------------------------------\n"
    return result


Flugzeuge = [Flugzeug("Boeing 737-300", 0, 5, 100), Flugzeug("Boeing 737-700", 0, 50, 1000)]
EinFlughafen = Flughafen("IBB", Flugzeuge, ["Terminal 1", "Terminal 2", "Halle 1"], 1)
while True:
    print(menu())
    match input():
        case "1":
            print(EinFlughafen)
        case "2":
            for flugzeug in EinFlughafen.flugzeuge:
                print(flugzeug)
        case "3":
            # Flugzeug("Boeing 737-300", 0, 5, 100)
            neues_flugzeug = Flugzeug(random.choice(list(get_flugzeuge().keys())))
            neues_flugzeug.passagiere_einsteigen(random.randint(0, neues_flugzeug.passagiere_max))
            EinFlughafen.landen(neues_flugzeug)
        case "4":
            pass
        case "5":
            pass
        

'''flieger1 = Flugzeuge[0]
flieger2 = Flugzeuge[1]

print(flieger1)

print(f"### test ###\nbeschleunigen\n{flieger1.speed}")
flieger1.beschleunigen(200)
print(flieger1.speed)

print(f"### test ###\n+ und -")
print(flieger1 + flieger2)
print(flieger1 - flieger2)

print(
    f"### test ###\nist {flieger1.name} besser als {flieger2.name}?\n{flieger1 > flieger2}"
)

print(f"### test ###\nanzahl_flugzeuge: {Flugzeug.anzahl_flugzeuge}")
print(f"### test ###\npassagiere_gesamt: {Flugzeug.anzahl_passagiere_gesamt}")

#flieger1.start()


EinFlughafen = Flughafen("IBB", Flugzeuge, ["Terminal 1", "Terminal 2", "Halle 1"], 1)

print(EinFlughafen)'''
