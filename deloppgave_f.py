
def lengste_nullsekvens(tallliste):
    maks_lengde = 0
    gjeldende_lengde = 0

    for tall in tallliste:
        if tall == 0:
            gjeldende_lengde += 1
        else:
            gjeldende_lengde = 0
        maks_lengde = max(maks_lengde, gjeldende_lengde)
    return maks_lengde

# a. Frivillig, avansert
def longest_sequence(ints):
    if len(ints) == 1:
        return 1, ints[0]
    
    output_int = 0
    longest_seq = 0
    count = 1

    for i in range(1, len(ints)):
        if ints[i] == ints[i-1]:
            count += 1
            if count > longest_seq:
                longest_seq = count
                output_int = ints[i]
        else:
            count = 1
    
    return longest_seq, output_int

# b. Frivillig, avansert: Det samme for flyttall, men med en oppgitt toleranse.
# def longest_sequence_of_floats(floats, tolerance):
#     if len(floats) == 1:
#         return 1, floats[0]
    
#     output_float = -1
#     longest_seq = 0
#     count = 1
    
#     for i in range(1,len(floats)):
#         for j in range(i+1,len(floats)):
#             if floats[i] >= floats[j] - tolerance and floats[i] <= floats[j] + tolerance:
#                 count += 1

#                 if count > longest_seq:
#                     longest_seq = count
#                     output_float = floats[i]
            
#             else:
#                 break

#         for k in range(i-1,len(floats)-1,-1):
#             if floats[i] >= floats[k] - tolerance and floats[i] <= floats[k] + tolerance:
#                 count += 1

#                 if count > longest_seq:
#                     longest_seq = count
#                     output_float = floats[i]
            
#             else:
#                 count = 1
#                 break
        
#     return longest_seq, output_float



def longest_sequence_of_floats(floats, toleranse):
    if len(floats) == 1:
        return 1, floats[0]
    count = 0
    output_float = -1
    longest_seq = 1

    for i in range(1, len(floats)):

        for j in range(i, len(floats)):
            if floats[j] >= floats[i] - toleranse and floats[j] <= floats[i] + toleranse:
                count += 1
                if count > longest_seq:
                    longest_seq = count
                    output_float = floats[i]
            else:
                print(output_float, longest_seq)
                print(f"floats[i]: {floats[i]} ")
                print(f"floats[j]: {floats[j]} ")
                count = 0
                break

        # for k in range(i-1,-1,-1):
        #     if floats[k] >= floats[i] - toleranse and floats[k] <= floats[i] + toleranse:
        #         count += 1
        #         if count > longest_seq:
        #             longest_seq = count
        #             output_float = floats[i]
        #     else:
        #         print(output_float, longest_seq)
        #         print(f"floats[k]: {floats[k]} ")
        #         break
    
    return longest_seq, output_float

tolerance = 0.2
floats = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
print(longest_sequence_of_floats(floats, tolerance))
# print(longest_sequence(ints))
