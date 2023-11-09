from deloppgave_g import lineaerregresjon
from lister_for_del_1 import temperaturer   
from lister_for_del_1 import temperaturer_tidspunkter   

a,b=lineaerregresjon(temperaturer_tidspunkter, temperaturer)
print(a,b)

if a > 0 :
    print('trenden på temperaturen er stigende')
elif a < 0 :
    print('trenden på temperaturen er synkende')
else:
    print('Temperaturen trender ikke i disse tider')
