def differanse_tall_i_liste(lst):
    output_list = []
    for i in range(len(lst)-1):
        dif = lst[i+1] - lst[i]
        output_list.append(dif)
    return output_list

# Frivillig 1:
def numeriske_derivasjon(x_koordinater, y_koordinater):
    tellere = differanse_tall_i_liste(y_koordinater)
    nevnere = differanse_tall_i_liste(x_koordinater)
    
    derivative = [teller / nevner for teller, nevner in zip(tellere, nevnere)]
    return derivative

# Frivillig 2:
def gjennomsnitt_e_elmenter(lst, e):
    ny_liste = []
    for i in range(len(lst)-e):
        snitt =  sum(lst[i:i+e+1]) / (e+1) 
        ny_liste.append(snitt)
    return ny_liste