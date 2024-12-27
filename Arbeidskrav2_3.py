"""
PY1010 - Arbeidskrav 2 - oppgave 3

@author: Lars-Erik Karrestad
"""

import numpy as np

v_grad = float(input("Skriv inn gradtallet: "))


def omregning(v_grad):
    return v_grad * (np.pi/180)


v_rad = omregning(v_grad)

print(f"Radiantallet til vinkelen er: {v_rad:.4f}")
