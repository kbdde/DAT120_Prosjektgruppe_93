def sum_vekstrater(temperatur):
    total_vekst = 0

    for temp in temperatur:
        if temp > 5:
            growth_rate = temp - 5
            total_vekst += growth_rate

    return total_vekst

temperatur = [4, 7, 15]

total = sum_vekstrater(temperatur)

print("Total vekst for planten er:", total)