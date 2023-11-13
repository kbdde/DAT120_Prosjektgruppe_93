from deloppgave_2a_ekk import data_parser
from datetime import datetime

def annual_ski_days(text_file):
    vaer_data = data_parser(text_file)     
    start_of_season = {10, 11, 12}
    end_of_season = {1, 2, 3, 4, 5, 6}
    annual_ski_days = {}

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

        if month in start_of_season and float(dybde) >= 20:
            annual_ski_days[year] += 1
        elif month in end_of_season and float(dybde) >= 20:
            annual_ski_days[year-1] += 1

    return annual_ski_days

output = annual_ski_days('snoedybder_vaer_en_stasjon_dogn.csv')
print(output)
