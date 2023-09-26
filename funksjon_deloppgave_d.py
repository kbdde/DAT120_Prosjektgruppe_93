
# 271408
# Gruppeprosjekt deloppgave d

def tell_storre_eller_lik(liste, verdi):
    # Initialiser en teller for å holde styr på antallet elementer som er større eller lik verdien.
    antall_storre_eller_lik = 0

    # Gå gjennom hvert element i lista.
    for element in liste:
        # Sjekk om elementet er større eller lik den oppgitte verdien.
        if element >= verdi:
            antall_storre_eller_lik += 1

    # Returner antallet elementer som er større eller lik verdien.
    return antall_storre_eller_lik


# Eksempel på bruk:
min_liste = [1.2, 2.5, 3.7, 4.1, 5.0, 6.2]
verdi = 3.0

antall_storre_eller_lik = tell_storre_eller_lik(min_liste, verdi)
print(f"Antall elementer større enn eller lik {verdi}: {antall_storre_eller_lik}")
