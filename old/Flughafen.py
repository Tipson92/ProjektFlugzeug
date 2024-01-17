import random
from Gebaeude import Gebaeude

class Flughafen(Gebaeude):
    parkpos = ["Terminal 1", "Terminal 2", "Halle 1"]
    
    def __init__(self, _name, _flugzeuge, _personen):
        """
        Initialisiert ein Flughafen-Objekt mit den angegebenen Parametern.

        Args:
            _name (str): Der Name des Flughafens.
            _flugzeuge (list): Eine Liste von Flugzeugen auf dem Flughafen.
            _personen (int): Die Gesamtanzahl der Personen auf dem Flughafen.
        """
        self.name = _name
        self.flugzeuge = _flugzeuge
        self.personen = _personen        
        
    def __str__(self):
        """
        Gibt eine formatierte Zeichenkette mit Informationen über den Flughafen zurück.

        Returns:
            str: Eine formatierte Zeichenkette mit dem Namen, der Anzahl der Flugzeuge, der Anzahl der Personen und den Parkpositionen.
        """
        return f"name: {self.name}\nFlugzeuge: {self.count_flugzeuge()}\nPersonen: {self.count_personen()}\n Parkpositionen:\n{self.get_parkPos()}"
    
    
    def count_personen(self):
        """
        Zählt die Gesamtanzahl der Personen auf dem Flughafen, einschließlich der Passagiere in den Flugzeugen.

        Returns:
            int: Die Gesamtanzahl der Personen auf dem Flughafen.
        """
        personenTemp = self.personen
        for flugzeug in self.flugzeuge:
            personenTemp += flugzeug.passagiere
        return personenTemp

    def count_flugzeuge(self):
        """
        Zählt die Anzahl der Flugzeuge auf dem Flughafen.

        Returns:
            int: Die Anzahl der Flugzeuge auf dem Flughafen.
        """
        return len(self.flugzeuge)

    def get_flugzeuge(self):
        """
        Gibt eine formatierte Zeichenkette mit Informationen über alle Flugzeuge auf dem Flughafen zurück.

        Returns:
            str: Eine formatierte Zeichenkette mit Informationen über alle Flugzeuge auf dem Flughafen.
        """
        result = ""
        for flugzeug in self.flugzeuge:
            result += f"{flugzeug}\n"
        return result  
    

    def get_parkPos(self):
        """
        Gibt Informationen über die Parkpositionen und die zugeordneten Flugzeuge auf dem Flughafen zurück.

        Returns:
            str: Eine formatierte Zeichenkette mit Informationen über die Parkpositionen und zugeordneten Flugzeuge auf dem Flughafen.
        """
        result = ""
        
        for pos in self.parkpos:
            result += f"{pos}:\n"
            for flugzeug in self.flugzeuge:
                if flugzeug.pos == pos:
                    result += f"\t{flugzeug.name}\n"
        return result

        