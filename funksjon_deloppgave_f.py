
# 271408
# Gruppeprosjekt deloppgave f

def lengste_nullsekvens(tallliste):
    maks_lengde = 0
    gjeldende_lengde = 0

    for tall in tallliste:
        if tall == 0:
            gjeldende_lengde += 1
        else:
            gjeldende_lengde = 0
        maks_lengde = max(maks_lengde, gjeldende_lengde)
    return maks_lengde

# Eksempel på bruk:
tallliste = [0, 1, 0, 0, 0, 2, 0, 3, 0, 0, 0, 4, 0, 0]

lengde = lengste_nullsekvens(tallliste)
print(f"Lengden på den lengste sammenhengende nullsekvensen er: {lengde}")
