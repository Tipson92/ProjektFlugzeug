import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_flugzeuge():
    return {
        "Boeing 737-100": {
            "leerGewicht": 41_145,
            "maximalGewicht": 77_565,
            "passagiere": 85,
            "speed": 988,
            "tank": 20_370,
            "reichweite": 2500,
        },
        "Boeing 737-200": {
            "leerGewicht": 42_080,
            "maximalGewicht": 84_000,
            "passagiere": 115,
            "speed": 988,
            "tank": 20_370,
            "reichweite": 2800,
        },
        "Boeing 737-300": {
            "leerGewicht": 45_230,
            "maximalGewicht": 82_080,
            "passagiere": 149,
            "speed": 983,
            "tank": 19_150,
            "reichweite": 4200,
        },
        "Boeing 737-400": {
            "leerGewicht": 49_800,
            "maximalGewicht": 82_080,
            "passagiere": 168,
            "speed": 977,
            "tank": 19_150,
            "reichweite": 3800,
        },
        "Boeing 737-500": {
            "leerGewicht": 56_400,
            "maximalGewicht": 68_000,
            "passagiere": 132,
            "speed": 982,
            "tank": 18_490,
            "reichweite": 4500,
        },
        "Boeing 737-600": {
            "leerGewicht": 60_830,
            "maximalGewicht": 68_000,
            "passagiere": 132,
            "speed": 950,
            "tank": 20_940,
            "reichweite": 5300,
        },
        "Boeing 737-700": {
            "leerGewicht": 62_820,
            "maximalGewicht": 85_100,
            "passagiere": 149,
            "speed": 914,
            "tank": 26_020,
            "reichweite": 6050,
        },
        "Boeing 737-800": {
            "leerGewicht": 70_440,
            "maximalGewicht": 79_015,
            "passagiere": 189,
            "speed": 839,
            "tank": 26_020,
            "reichweite": 5450,
        },
        "Boeing 737-900": {
            "leerGewicht": 70_430,
            "maximalGewicht": 88_265,
            "passagiere": 213,
            "speed": 839,
            "tank": 26_020,
            "reichweite": 5300,
        },
        "Boeing 737 MAX": {
            "leerGewicht": 72_500,
            "maximalGewicht": 88_300,
            "passagiere": 230,
            "speed": 839,
            "tank": 28_820,
            "reichweite": 6510,
        },
        "Boeing 747-100": {
            "leerGewicht": 162_400,
            "maximalGewicht": 378_840,
            "passagiere": 660,
            "speed": 933,
            "tank": 183_380,
            "reichweite": 5600,
        },
        "Boeing 747-200": {
            "leerGewicht": 168_380,
            "maximalGewicht": 833_000,
            "passagiere": 524,
            "speed": 988,
            "tank": 200_320,
            "reichweite": 7300,
        },
        "Boeing 747-300": {
            "leerGewicht": 178_756,
            "maximalGewicht": 833_000,
            "passagiere": 660,
            "speed": 988,
            "tank": 183_380,
            "reichweite": 7200,
        },
        "Boeing 747-400": {
            "leerGewicht": 178_756,
            "maximalGewicht": 987_000,
            "passagiere": 624,
            "speed": 988,
            "tank": 216_840,
            "reichweite": 7700,
        },
        "boeing 767-200": {
            "leerGewicht": 90_001,
            "maximalGewicht": 179_170,
            "passagiere": 181,
            "speed": 870,
            "tank": 91_200,
            "reichweite": 6030,
        },
        "boeing 767-300": {
            "leerGewicht": 91_636,
            "maximalGewicht": 181_610,
            "passagiere": 218,
            "speed": 870,
            "tank": 91_200,
            "reichweite": 6100,
        },
        "boeing 767-400": {
            "leerGewicht": 91_999,
            "maximalGewicht": 187_700,
            "passagiere": 245,
            "speed": 870,
            "tank": 91_200,
            "reichweite": 5150,
        },
        "Boeing 777-200": {
            "leerGewicht": 132_200,
            "maximalGewicht": 263_610,
            "passagiere": 317,
            "speed": 950,
            "tank": 171_170,
            "reichweite": 14_260,
        },
        "Boeing 777-300": {
            "leerGewicht": 166_930,
            "maximalGewicht": 347_810,
            "passagiere": 396,
            "speed": 950,
            "tank": 171_170,
            "reichweite": 11_165,
        },
        "Boeing 787-8": {
            "leerGewicht": 119_500,
            "maximalGewicht": 227_930,
            "passagiere": 242,
            "speed": 954,
            "tank": 138_699,
            "reichweite": 13_620,
        },
        "Boeing 787-9": {
            "leerGewicht": 127_900,
            "maximalGewicht": 254_011,
            "passagiere": 290,
            "speed": 954,
            "tank": 138_699,
            "reichweite": 13_530,
        },
    }


# Daten in JSON-Datei speichern
#with open(f"{dir_path}flugzeugdaten.json", "w") as json_datei:
#    json.dump(get_flugzeuge(), json_datei, indent=2)
