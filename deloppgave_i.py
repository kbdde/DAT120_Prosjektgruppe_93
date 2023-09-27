from deloppgave_d import tell_antall_storre_eller_lik
from lister_for_del_1 import temperaturer

antall_sommerdager = tell_antall_storre_eller_lik(temperaturer, 20)
antall_hoysommerdager = tell_antall_storre_eller_lik(temperaturer, 25)
antall_tropedager = tell_antall_storre_eller_lik(temperaturer, 30)

print(f'antall sommerdager: {antall_sommerdager}')
print(f'antall høysommerdager: {antall_hoysommerdager}')
print(f'antall tropedager: {antall_tropedager}')


