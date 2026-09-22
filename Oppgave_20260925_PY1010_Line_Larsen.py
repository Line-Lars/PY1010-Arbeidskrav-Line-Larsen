# -*- coding: utf-8 -*-
"""
Arbeidskrav 1 

Line Larsen (lilar5733@usn.no)

Innlevering 2026 09 25


"""

#%% Data

FB = 7500 # [Forsikring bensinbil i kr/år] 

FE = 5000 # [Forsikring elbil i kr/år]

DB = 1.0 # [Drivstoff forbruk bensinbil kr/km ]

DE = 0.2 # [Drivstoff forbruk elbil kWt/km]

BB = 0.3 # [Bomavgift bensinbil kr/km]

BE = 0.1 # [Bomavgift elbil kr/km]

SP = 2.0 # [Strømpris kr/kWh]

ÅR = 365 # [dager]

KM = 10000 # [km/år]


#%% Beregning

TA = 8.38 * ÅR # [Trafikkforsikringsavgift per år]

EK = DE * SP # [Pris strøm per km kr/km]


#%% Beregning kostnad per år

BI = ( KM * DB) + (KM * BB ) + FB + TA # [kr/år]

EL = ( KM * EK) + (KM * BE ) + FE + TA # [kr/år]

Diffbensinel = BI - EL


#%% Utskrift

print("Kostnad Elbil =", EL , "kr/år") 

print("Kostnad Bensinbil =", BI , "kr/år")

print("Prisdifferanse Bensinbil vs Elbil =", Diffbensinel , "kr/år")



