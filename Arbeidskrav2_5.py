"""
PY1010 - Arbeidskrav 2 - oppgave 5

@author: Lars-Erik Karrestad
"""

import math


def beregn_figur(a, b):
    # Areal av rettvinklet trekant
    areal_trekant = (a * b) / 2

    # Areal av halvsirkel
    radius = a / 2
    areal_halvsirkel = (math.pi * radius**2) / 2

    # Totalt areal
    total_areal = areal_trekant + areal_halvsirkel

    # Ytre omkrets
    c = a + b + math.sqrt(a**2 + b**2)  # Finner lengden på den ukjente siden i trekanten
    omkrets_trekant = b + c  # Tar ikke med a i ytre omkrets
    omkrets_halvsirkel = 2 * (math.pi * radius) / 2
    ytre_omkrets = omkrets_trekant + omkrets_halvsirkel

    return total_areal, ytre_omkrets


# Input fra bruker
a = float(input("Oppgi lengden av a: "))
b = float(input("Oppgi lengden av b: "))

# Bruk av funksjonen
areal, omkrets = beregn_figur(a, b)

# Skriver resultatene til skjermen
print(f"Arealet av figuren er: {areal:.2f}")
print(f"Ytre omkrets av figuren er: {omkrets:.2f}")
