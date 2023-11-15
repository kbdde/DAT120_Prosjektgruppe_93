from deloppgave_2a_ekk import data_parser
from datetime import datetime
import matplotlib.pyplot as plt

def return_longest_annual_rainfree_streaks(text_file):
    vaer_data = data_parser(text_file)
    longest_rainfree_streaks = {}
    annual_streaks = []
    current_streak = 0
    day_counter = 0
    valid_years = set()

    for row in vaer_data:
        date = row['Dato']
        rain = row['Nedbør']

        if (rain == "" or rain == "-") or (date == "" or date == "-"):
            continue
     
        rain = float(rain.replace(",", "."))
        date_parsed = datetime.strptime(date, "%d.%m.%Y")
        year = date_parsed.year
        day_counter += 1

        if year not in longest_rainfree_streaks:
            longest_rainfree_streaks[year] = 0
            if year-1 in longest_rainfree_streaks and day_counter >= 300:
                annual_streaks.append(current_streak)
                longest_rainfree_streaks[year-1] = max(annual_streaks)
                valid_years.add(year-1)
        
            day_counter = 0
            current_streak = 0
            annual_streaks = []
        
        if rain == 0:
            current_streak += 1
        elif current_streak > 0:
            annual_streaks.append(current_streak)
            current_streak = 0

    if day_counter >= 300:
        annual_streaks.append(current_streak)
        longest_rainfree_streaks[year] = max(annual_streaks)

    return {year: streak for year, streak in longest_rainfree_streaks.items() if year in valid_years}


def plot_longest_annual_rainfree_streaks(text_file): 
    year_streaks = return_longest_annual_rainfree_streaks(text_file)

    years = [key for key in year_streaks .keys()]
    streaks = [value for value in year_streaks .values()]
    
    plt.plot(years, streaks, marker='o')
    plt.xlabel('År')
    plt.ylabel('Regnfire Perioder')
    plt.legend()
    plt.show()

plot_longest_annual_rainfree_streaks('snoedybder_vaer_en_stasjon_dogn.csv')


        
