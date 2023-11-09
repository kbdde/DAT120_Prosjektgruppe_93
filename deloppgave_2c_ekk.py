from deloppgave_g import lineaerregresjon
from deloppgave_2b_ekk import annual_ski_days
from datetime import datetime

input_text = annual_ski_days('snoedybder_vaer_en_stasjon_dogn.csv')
y = [value for value in input_text.values()]
x = [key for key in input_text.keys()]

output = lineaerregresjon(x, y)
print(output)