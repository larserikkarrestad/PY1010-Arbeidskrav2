"""
PY1010 - Arbeidskrav 2 - oppgave 2

@author: Lars-Erik Karrestad
"""

import math
antall_elever = int(input("Skriv inn antall elever: "))
antall_pizza = math.ceil(antall_elever * 0.25)
print("Det må handles inn", antall_pizza, "pizzaer til festen")
