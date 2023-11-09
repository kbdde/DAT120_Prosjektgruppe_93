from deloppgave_e import differanse_tall_i_liste
from lister_for_del_1 import temperaturer

temp_endring = differanse_tall_i_liste(temperaturer)

for index, endring in enumerate(temp_endring):
    if endring > 0:
        retning = 'Stigende'
    elif endring < 0:
        retning = 'Synkende'
    else:
        retning = 'Uforandret'
    print(f'{index}: {retning}')
    
