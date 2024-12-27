"""
PY1010 - Arbeidskrav 2 - oppgave 6

@author: Lars-Erik Karrestad
"""

import numpy as np
import matplotlib.pyplot as plt


# Definerer funksjonen f(x)
def f(x):
    return -x**2 - 5


# Oppretter et array med 200 punkter fordelt på intervallet [-10, 10]
x = np.linspace(-10, 10, 200)
y = f(x)

# Plotter funksjonen
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot av funksjonen $f(x)=-x^2-5$')
plt.grid(True)
plt.show()
