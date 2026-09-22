# -*- coding: utf-8 -*-
"""
Arbeidskrav 1 

Line Larsen (lilar5733@usn.no)

2026 09 25


"""

#%% Data

FE = 5000 # [Forsikring elbil i kr/år]

FB = 7500 # [Forsikring bensinbil i kr/år] 

KM = 10000 # [Km/år]

DE = 0.2 # [Drivstoff forbruk elbil kWt/km]

DB = 1.0 # [Drivstoff forbruk bensinbil kr/km ]

SP = 2.0 # [Strømpris kr/kWh]

ÅR = 365 # [dager]

BE = 0.1 # [Bomavgift elbil kr/km]

BB = 0.3 # [Bomavgift bensinbil kr/km]


#%% Beregning

TA = 8.38 * ÅR # [Trafikkforsikringsavgift per år]

EK = DE * SP # [Pris strøm per km kr/km]


#%% Beregning kostnad per år Elbil

EL = ( KM * EK) + (KM * BE ) + FE + TA # [kr/år]

BI = ( KM * DB) + (KM * BB ) + FE + TA # [kr/år]

#%% Utskrift

print("Kostnad Elbil =", EL , "kr/år") 

print("Kostnad Bensinbil =", BI , "kr/år")





