# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:47:05 2023

@author: Jonas
"""

from deloppgave_2a import csv_til_liste

bananer=csv_til_liste('snoedybder_vaer_en_stasjon_dogn.csv')

sesonger={}

for banan in bananer: 
    
    mnd_tekst=banan[2][3:5]
    aar_tekst=banan[2][6:16]      
    
    mnd_nummer=int(mnd_tekst)
    aar_nummer=int(aar_tekst)
    
    sesong=-1
 
    
    if mnd_nummer>= 10:
        sesong=aar_nummer
    if mnd_nummer<=6:
        sesong=aar_nummer-1
        
    
    print(banan[2],sesong)
    
    if