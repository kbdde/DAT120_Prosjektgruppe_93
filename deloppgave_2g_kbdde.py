
# 271408

from datetime import datetime

file_path = 'snoedybder_vaer_en_stasjon_dogn.csv'
with open(file_path, 'r') as file:
    # Leser linjer fra filen
    lines = file.readlines()

lines = [line.strip() for line in lines]

invalid_values = []

header = lines[0].split(';')
data_lines = lines[1:]

data = []
for line in data_lines:
    values = line.split(';')
    data.append(values)

valid_period_start = None
valid_period_count = 0

for row in data:
    temp = row[5].replace(',', '.')
    date = row[2]

    if temp == "" or temp == "-" or date == "" or date == "-":
        # Ugyldig måling, nullstill telleren
        valid_period_start = None
        valid_period_count = 0
        continue

    try:
        sky_coverage = float(row[6].replace(',', '.'))
    except ValueError as e:
        invalid_values.append({'row': row, 'error': str(e)})
    if sky_coverage <= 3:
        if valid_period_start is None:
            valid_period_start = datetime.strptime(date, "%d.%m.%Y")
        valid_period_count += 1
    else:
        # Skydekket er over 3, nullstill telleren
        valid_period_start = None
        valid_period_count = 0

    if valid_period_count >= 300:
        end_date = datetime.strptime(date, "%d.%m.%Y")
        print(f"Gyldig periode fra {valid_period_start} til {end_date}")
        valid_period_start = None
        valid_period_count = 0

