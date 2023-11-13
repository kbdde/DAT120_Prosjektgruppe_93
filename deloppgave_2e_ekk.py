from deloppgave_h import vekstrater
from deloppgave_2a_ekk import data_parser
from datetime import datetime
import matplotlib.pyplot as plt

def annual_growth_days(text_file):
    vaer_data = data_parser(text_file)     
    annual_temp_days = {}

    for row in vaer_data:
        date = row['Dato']
        temp = row['Middeltemperatur']

        if (temp == "" or temp == "-") or (date == "" or date == "-"):
            continue

        temp = float(temp.replace(",", "."))
        date_parsed = datetime.strptime(date, "%d.%m.%Y")
        year = date_parsed.year

        if year not in annual_temp_days:
            annual_temp_days[year] = [temp]
        else:
            annual_temp_days[year].append(temp)
        
    date_temp = {key:value for key, value in annual_temp_days.items() if len(value) >= 300}
    return date_temp


def plot_annual_growth(text_file): 
    date_temp = annual_growth_days(text_file)
    annual_growth = {key:vekstrater(value) for key, value in date_temp.items()}

    years = [key for key in annual_growth.keys()]
    growth_rates = [value for value in annual_growth.values()]
    
    plt.plot(years, growth_rates, marker='o')
    plt.xlabel('År')
    plt.ylabel('Vekstrater')
    plt.legend()
    plt.show()

plot_annual_growth('snoedybder_vaer_en_stasjon_dogn.csv')