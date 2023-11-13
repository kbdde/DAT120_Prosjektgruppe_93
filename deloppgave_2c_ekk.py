from deloppgave_g import lineaerregresjon
from deloppgave_2b_ekk import annual_ski_days
from datetime import datetime

input_text = annual_ski_days('snoedybder_vaer_en_stasjon_dogn.csv')
y = [value for value in input_text.values()]
x = [key for key in input_text.keys()]

output = lineaerregresjon(x, y)
print(output)



        annual_growth[key] = round(vekstrater(value), 10)

    x_values = annual_growth.keys()
    y_values = annual_growth.values()

    for x, y in zip(x_values, y_values):
        plt.plot(x, y, label=x)
        plt.show()