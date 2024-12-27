"""
PY1010 - Arbeidskrav 2 - oppgave 4

@author: Lars-Erik Karrestad
"""

# Oppgave A - Opprettelse av dictionary
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

# Oppgave B - Ber brukeren om å skrive inn et land
land = input("Skriv inn et land: ")

# Henter informasjonen om landet
hovedstad, befolkning = data.get(land, [None, None])

# Sjekker om landet finnes
# Finnes landet skrives det ut informasjon om landet
# Hvis landet ikke finnes blir bruker bedt om å skrive inn hovedstad og innbyggere
if hovedstad:
    print(f"{hovedstad} er hovedstaden i {land} og det er {befolkning} mill. innbyggere i {hovedstad}.")
else:
    print(f"{land} finnes ikke i listen.")
    # Ber brukeren skrive inn hovedstad og befolkning for det nye landet
    ny_hovedstad = input(f"Skriv inn hovedstaden i {land}: ")
    ny_befolkning = float(input(f"Skriv inn antall innbyggere (i mill.) i {ny_hovedstad}: "))
    # Lagrer det nye landet til dictionaryen
    data[land] = [ny_hovedstad, ny_befolkning]
    print("\nOppdatert informasjon i dictionary:")
    for key, value in data.items():
        print(f"{key}: Hovedstad - {value[0]}, Befolkning - {value[1]} mill.")
