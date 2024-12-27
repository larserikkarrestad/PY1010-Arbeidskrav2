"""
PY1010 - Arbeidskrav 2 - oppgave 1

@author: Lars-Erik Karrestad
"""

import datetime
idag = datetime.date.today()
aar = idag.year

alder = int(input('Hvilket år er du født? '))
print("Da blir du", aar-alder, "år i løpet av", aar)
