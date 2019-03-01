# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:43:04 2019

@author: NG7a8f3
"""
import random

#Diese Funktion nimmt einen Int und ein Rundungslevel
#Der Int wird als Kreuzer intepretiert.
#Es wird dann ein String zurück gegeben der die umwandlung in Dukaten Silber
#Heller und Kreuzer unter Berücksichtigung des Rundungslevels beinhaltet
def Geldrechner(money, level,rundungslevel):
    moneystring=''
    money=int(money)
    Kreuzer=money%10
    money=money/10
    Heller=money%10
    money=money/10
    Silber=money%10
    Dukaten=money/10

    if Dukaten>=1:
        if rundungslevel=='Dukaten':
            moneystring= str(int(round(Dukaten,0))) + ' Dukaten '
            return moneystring
        else:
            moneystring=str(int(Dukaten)) + ' Dukaten '
    if Silber>=1:
        if rundungslevel=='Silber' and rundungslevel!='Dukaten':
            moneystring=moneystring+str(int(round(Silber,0))) + ' Silber '
            return moneystring
        else:
            moneystring=moneystring+str(int(Silber)) + ' Silber '
    if Heller>=1 and rundungslevel!='Silber' and rundungslevel!='Dukaten':
        if rundungslevel=='Heller':
            moneystring= moneystring+str(int(round(Heller,0))) + ' Heller '
            return moneystring
        else:
            moneystring=moneystring+str(int(Heller)) + ' Heller '
    if Kreuzer>=1 and rundungslevel!='Silber' and rundungslevel!='Dukaten' and rundungslevel!='Heller':
        moneystring=moneystring+str(int(round(Kreuzer,0)))+ ' Kreuzer '
    return moneystring

# Gleiche Funktion wie Geldrechner. Der String enthält jedoch statt "Dukaten" nur ein D
# Respektiv auch für die anderen Währungen
def GeldrechnerKurz(money, level,rundungslevel):
    moneystring=''
    money=int(money)
    Kreuzer=money%10
    money=money/10
    Heller=money%10
    money=money/10
    Silber=money%10
    Dukaten=money/10

    if Dukaten>=1:
        if rundungslevel=='Dukaten':
            moneystring= str(int(round(Dukaten,0))) + ' D '
            return moneystring
        else:
            moneystring=str(int(Dukaten)) + ' D '
    if Silber>=1:
        if rundungslevel=='Silber' and rundungslevel!='Dukaten':
            moneystring=moneystring+str(int(round(Silber,0))) + ' S '
            return moneystring
        else:
            moneystring=moneystring+str(int(Silber)) + ' S '
    if Heller>=1 and rundungslevel!='Silber' and rundungslevel!='Dukaten':
        if rundungslevel=='Heller':
            moneystring= moneystring+str(int(round(Heller,0))) + ' H '
            return moneystring
        else:
            moneystring=moneystring+str(int(Heller)) + ' H '
    if Kreuzer>=1 and rundungslevel!='Silber' and rundungslevel!='Dukaten' and rundungslevel!='Heller':
        moneystring=moneystring+str(int(round(Kreuzer,0)))+ ' K '
    return moneystring

# Konstanten
#Geschwindigkeit in Meilen pro Tag
speedFuß = 30
speedFlusskahn = 50
speedReiseKutsche = 40
speedShip = 100
speedHorse = 50
#Kosten in Kreuzer
kostenFlusskahn = 25 / 2
kostenReisekutsche = 1200
kostenSeereiseHängematte = 800
kostenSeereiseKabine = 1500
#Proviantkosten pro Tag in Kreuzer
foodPerDay = 50
waterPerDay = 3

def berechne_chance(wegZustand, simulation):
    if simulation:
        if wegZustand=='Perfekt':
            chance=1
        if wegZustand=='Gut':
            chance=0.68
        if wegZustand=='Mittel':
            chance=0.40
        if wegZustand=='Schlecht':
            chance=0.25
    else:
        if wegZustand=='Perfekt':
            chance=1
        if wegZustand=='Gut':
            chance=0.90
        if wegZustand=='Mittel':
            chance=0.74
        if wegZustand=='Schlecht':
            chance=0.65
    return chance

def simuliere_reise(chance, reisewege):
    pferdReise, fußWeg, FlusskahnWeg, reiseKutschenWeg, seeReiseWegM, seeReiseWegK = reisewege
    daysToTravel = 0
    #Jeder Tag wird einzeln simuliert.
    #So lange noch Reiseweg vorhanden ist
    while pferdReise>0:
        #Berechne den Verlangsamungsfaktor
        daySlow = 1/(random.randint(chance*100,100)/100)
        #Zähle Reisetag einen hoch
        daysToTravel += 1
        #Die Distanz ist die Normaldistanz-Distanz*Verlangsamungsfaktor
        pferdReise = pferdReise-(pferdReise*daySlow)
    while fußWeg>0:
        daySlow = (random.randint(chance*100,100)/100)
        daysToTravel += 1
        fußWeg = fußWeg-(speedFuß*daySlow)
    while FlusskahnWeg>0:
        daySlow = (random.randint(chance*100,100)/100)
        daysToTravel += 1
        FlusskahnWeg = FlusskahnWeg-(speedFlusskahn*daySlow)
    while reiseKutschenWeg>0:
        daySlow = (random.randint(chance*100,100)/100)
        daysToTravel += 1
        reiseKutschenWeg = reiseKutschenWeg-(speedReiseKutsche*daySlow)
    while seeReiseWegM>0:
        daySlow = (random.randint(chance*100,100)/100)
        daysToTravel += 1
        seeReiseWegM = seeReiseWegM-(speedShip*daySlow)
    while seeReiseWegK>0:
        daySlow = (random.randint(chance*100,100)/100)
        daysToTravel += 1
        seeReiseWegK = seeReiseWegK-(speedShip*daySlow)
    return daysToTravel

def reisedauerrechnung(reisewege, rundung, gruppengröße, wegZustand, simulation):

    pferdReise, fußWeg, FlusskahnWeg, reiseKutschenWeg, seeReiseWegM, seeReiseWegK = reisewege

    chance = berechne_chance(wegZustand, simulation)

    #Transportkosten Berechnen für das Handeln
    FlusskahnKosten = FlusskahnWeg/100 * kostenFlusskahn * gruppengröße
    ReiseKutscheKosten = reiseKutschenWeg/100 * kostenReisekutsche * gruppengröße
    SeereiseKostenM = seeReiseWegM/100 * kostenSeereiseHängematte * gruppengröße
    SeereiseKostenK = seeReiseWegK/100 * kostenSeereiseKabine * gruppengröße
    transportMittelKosten = (FlusskahnKosten, ReiseKutscheKosten, SeereiseKostenM, SeereiseKostenK)

    #Gesamt Transport Kosten werden nach Distanz und Gruppengröße festgelegt
    transportCost = gruppengröße * (FlusskahnWeg * kostenFlusskahn + reiseKutschenWeg * kostenReisekutsche + seeReiseWegM * kostenSeereiseHängematte + seeReiseWegK * kostenSeereiseKabine)/100
    if simulation and wegZustand != 'Perfekt':
        #Simulation der Reisedistanz.
        daysToTravel = simuliere_reise(chance, reisewege)
    else:
        #Wenn nicht simuliert wird ist es einfach das Level mal der Reisedauer
        daysToTravel = (pferdReise/speedHorse+fußWeg/speedFuß+FlusskahnWeg/speedFlusskahn+reiseKutschenWeg/speedReiseKutsche+seeReiseWegM/speedShip+seeReiseWegK/speedShip)*(1/chance)
    return daysToTravel, transportCost, transportMittelKosten

def berechne_nahrungsbedarf(daysToTravel, gruppengröße, wegZustand, simulation):
    food = 0
    water = 0
    chance = berechne_chance(wegZustand, simulation)
    if simulation and wegZustand != 'Perfekt':
        for x in range(int(daysToTravel)):
            dayHard = 1 / (random.randint(chance*100,100) / 100)
            foodNeed = foodPerDay * gruppengröße * dayHard
            waterNeed = waterPerDay * gruppengröße * dayHard
            food += foodNeed
            water += waterNeed
    else:
        food = foodPerDay * gruppengröße * daysToTravel * (1 / chance)
        water = waterPerDay * gruppengröße * daysToTravel * (1 / chance)
    return food, water


def wuerfeln(wuerfelSeiten,anzahl):
    wurf=0
    for i in range(anzahl):
        wurf=wurf+random.randint(1,wuerfelSeiten)
    return wurf
