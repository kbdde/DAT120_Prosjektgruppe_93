from deloppgave_e import differanse_tall_i_liste
from lister_for_del_1 import temperaturer

temp_endring = differanse_tall_i_liste(temperaturer)
print(temperaturer)
print(temp_endring)

for index, endring in enumerate(temp_endring):
    if endring > 0:
        retning = 'Stigende'
    elif endring < 0:
        retning = 'Synkende'
    else:
        retning = 'Uforandret'
    print(f'{index}: {retning}')

# j) Bruk funksjonen fra oppgave e) til å finne ut om temperaturen er stigende eller synkende for hvert tidspunkt. 
# Gå gjennom lista som dere får når dere kaller funksjonen fra oppgave e) på temperaturlista. 
# For hvert element skriv ut indeksen og skriv ut «stigende» om differansen er over 0, 
# «synkende» om den er negativ eller «uforandret» om den er 0.

