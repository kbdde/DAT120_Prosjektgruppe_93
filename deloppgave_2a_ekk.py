import csv
import datetime as dt

def data_parser(filnavn):
    with open(filnavn) as input_file:
        data = csv.reader(input_file, delimiter=';')
        parsed_data = []

        for row in data:
            data_in_row = {
                'Navn': row[0],
                'Stasjon': row[1],
                'Dato': row[2], 
                'Snødybde': row[3],
                'Nedbør': row[4],
                'Middeltemperatur': row[5],
                'Gj_skydekke': row[6],
                'Max_middelvind': row[7],
            }
            parsed_data.append(data_in_row)
            
        parsed_data.pop(0) # removes the headings
        return parsed_data
    
# output = data_parser('snoedybder_vaer_en_stasjon_dogn.csv')     
# print(output)
