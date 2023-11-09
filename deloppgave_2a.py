# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:56:30 2023

@author: Jonas
"""

import csv

                     

def csv_til_liste(filnavn):
    with open(filnavn) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        resultater = []
    
        for row in csv_reader:   
            dato=row[2]
            if len(dato)==10:
                resultater.append(row)
            
        return resultater
        
