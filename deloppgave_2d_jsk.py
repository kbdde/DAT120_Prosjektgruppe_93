from deloppgave_2a_ekk import data_parser
from deloppgave_g import lineaerregresjon
from datetime import datetime
import matplotlib.pyplot as plt

def annual_ski_days(text_file):
    vaer_data = data_parser(text_file)     
    start_of_season = {10, 11, 12}
    end_of_season = {1, 2, 3, 4, 5, 6}
    annual_ski_days = {}
    annual_days_with_data = {}
    
    
    for row in vaer_data:
        date = row['Dato']
        dybde = row['Snødybde']

        if (dybde == "" or dybde == "-") or (date == "" or date == "-"):
            continue

        date_parsed = datetime.strptime(date, "%d.%m.%Y")
        year = date_parsed.year
        month = date_parsed.month

        if year not in annual_ski_days:
            annual_ski_days[year] = 0
        if year not in annual_days_with_data:
            annual_days_with_data[year] = 0

        if month in start_of_season and float(dybde) >= 20:
            annual_ski_days[year] += 1
        elif month in end_of_season and float(dybde) >= 20:
            annual_ski_days[year-1] += 1
        if month in start_of_season:
            annual_days_with_data[year] += 1
        elif month in end_of_season:
            annual_days_with_data[year-1] += 1
            
    for year in annual_days_with_data:
        days= annual_days_with_data[year]
        
        if days < 200:
            del annual_ski_days[year]


    return annual_ski_days


output = annual_ski_days('snoedybder_vaer_en_stasjon_dogn.csv')

y = [value for value in output.values()]
x = [key for key in output.keys()]

output2 = lineaerregresjon(x, y)


first_year = x[0]
last_year = x[len(x)-1]

Dager_med_sno_first_year = first_year*output2[0]+output2[1]
Dager_med_sno_last_year = last_year*output2[0]+output2[1]
trendx = [first_year, last_year]
trendy = [Dager_med_sno_first_year, Dager_med_sno_last_year]
    
plt.plot(x, y, marker='o')
plt.plot(trendx, trendy, marker='x')
plt.xlabel('År')
plt.ylabel('Vekstrater')
plt.legend()
plt.show()



