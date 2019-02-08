# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:43:04 2019

@author: NG7a8f3
"""

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