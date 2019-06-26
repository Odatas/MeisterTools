# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:04:15 2019

@author: Odatas
"""


try:
     import Tkinter as tk
except ImportError:
     import tkinter as tk

try:
     import ttk
     py3 = False
except ImportError:
     import tkinter.ttk as ttk
     py3 = True


import sqlite3
import random
import re
     
from . import patrickstools2
from . import odatasfunctions as of
from . import path_db
from tkinter import messagebox
from urllib.request import pathname2url

class Kampftechnik:
    def __init__(self,r = 0,i = 0,j = 0,k = 0):
        self.name = r
        self.leiteigenschaft = i
        self.steigerungsfaktor = j
        self.wert = k
        
        


class PageRandomeNPC(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        
        try:
            dburi = 'file:{}?mode=rw'.format(pathname2url(str(path_db)))
            conn = sqlite3.connect(dburi, uri=True)
        except sqlite3.OperationalError:
            messagebox.showerror("ERROR","Die Datenbank konnte nicht gefunden werden. Stelle sicher dass sich die Datei odatastools im gleichen Ordner wie Das Hauptprogramm befindet.")
        
        
        
        comboBoxFrame=ttk.LabelFrame(self)
        comboBoxFrame.grid(padx=50,pady=50,sticky='w')
        
        mainFrame=ttk.LabelFrame(self)
        mainFrame.grid(padx=50,pady=50,sticky='w')
        
        
        #Erfahrungsstufe
        auswahlErfahrung = ['Unerfahren (900)', 'Durchschnittlich  (1000)','Erfahren (1100) ','Kompetent (1200)','Meisterlich (1400)','Brilliant (1700)','Legendär (2100)']        
        comboErfahrung=ttk.Combobox(comboBoxFrame,values=auswahlErfahrung,state="readonly")
        comboErfahrung.grid(column=2,row=2)  
        comboErfahrung.set('Unerfahren (900)')
        
        ttk.Label(comboBoxFrame,text='Erfahrungsstufe:').grid(sticky='w',column=0,row=2,padx=(0,10))
        
        
        #Rassen. Momentan nur de Spielbaren
        auswahlRasse = ['Zufall', 'Mensch', 'Elf','Zwerg','Halbelf']        
        comboBoxRasse=ttk.Combobox(comboBoxFrame,values=auswahlRasse,state="readonly")
        comboBoxRasse.grid(row=4,column=2)  
        comboBoxRasse.set('Zufall')
        
        ttk.Label(comboBoxFrame,text='Rasse:').grid(sticky='w',column=0,row=4,padx=(0,10))
        
        #Kultur 
        auswahlKultur = ['Rasse zuerst wählen']        
        comboBoxKultur=ttk.Combobox(comboBoxFrame,values=auswahlKultur,state="readonly")
        comboBoxKultur.grid(row=6,column=2)  
        comboBoxKultur.set('Rasse zuerst wählen')
        
        ttk.Label(comboBoxFrame,text='Kultur:').grid(sticky='w',column=0,row=6,padx=(0,10))
        
        #Profession die die Chancen für bestimmte werte Festlegt. 
        auswahlProffession = ['Zufall', 'Söldner']        
        comboBoxProffession=ttk.Combobox(comboBoxFrame,values=auswahlProffession,state="readonly")
        comboBoxProffession.grid(row=8,column=2)  
        comboBoxProffession.set('Zufall')
        
        ttk.Label(comboBoxFrame,text='Proffession:').grid(sticky='w',column=0,row=8,padx=(0,10))
        
    
        
        
        
        #Funktion die die Kulturcombobox bei Auswahl der Rasse auf die Kulturen der Rasse umstellt
        def changeKulturCombobox(event=None):
            
            rasse=comboBoxRasse.get()
                    
            if rasse=='Zufall':
                auswahlKultur=['Rasse zuerst wählen']
                
            if rasse=='Mensch':
                auswahlKultur=['Zufall','Andergaster','Aranier','Bornländer','Fjarninger','Horasier','Maraskaner','Mhanadistani','Mittelreicher','Mohas','Niversen','Norbarden','Nordaventurier','Nostrier','Novadis','Südaventurier','Svelltaler','Thorwaler','Zyklopäer']
            
            if rasse=='Elf':
                auswahlKultur=['Zufall','Aueelfen','Firnelfen','Waldelfen']             
            
            if rasse=='Zwerg':
                auswahlKultur=['Zufall','Ambosszwerge','Brillantzwerge','Erzzwerge','Hügelzwerge']
            
            if rasse=='Halbelf':
                auswahlKultur=['Zufall','Andergaster','Aranier','Aueelfen','Bornländer','Firnelfen','Fjarninger','Horasier','Maraskaner','Mhanadistani','Mittelreicher','Mohas','Niversen','Norbarden','Nordaventurier','Nostrier','Novadis','Südaventurier','Svelltaler','Thorwaler','Waldelfen','Zyklopäer']

            comboBoxKultur.set(auswahlKultur[0])
            comboBoxKultur.config(values=auswahlKultur)
                      
        # Funktion um Zufallswerte zu berechnen
        def generateNew(event=None):  
            
            #Zieht aus dem Erfahrungs String die Zahl raus welche die AP sind.
            anzahlAP=int(re.search(r'\d+', comboErfahrung.get()).group()) 
            #Extrahiert das Level aus dem String
            level=comboErfahrung.get().split(' ', 1)[0]
            #Maximalwert für Heldenerschaffung je nach Level
            if level=='Unerfahren':
               maxEigenschaft=11
               #Max Summe begrenzt da max eigenschaftswert auf Unerfahren 11
               maxsumEigenschaft=88
               maxFertigkeit=10
               maxKampf=8
            if level=='Durchschnittlich':
               maxEigenschaft=13
               maxsumEigenschaft=98
               maxFertigkeit=10
               maxKampf=10
            if level=='Erfahren':
               maxEigenschaft=14
               maxsumEigenschaft=100
               maxFertigkeit=10
               maxKampf=12
            if level=='Kompetent':
               maxEigenschaft=15
               maxsumEigenschaft=102
               maxFertigkeit=13
               maxKampf=14
            if level=='Meisterlich':
               maxEigenschaft=16
               maxsumEigenschaft=105
               maxFertigkeit=16
               maxKampf=16
            if level=='Brilliant':
               maxEigenschaft=17
               maxsumEigenschaft=109
               maxFertigkeit=19
               maxKampf=18
            if level=='Legendär':
               maxEigenschaft=18
               maxsumEigenschaft=114
               maxFertigkeit=20
               maxKampf=20
               
           
            #Rasse
            #Ausgewählte Rasse aus der Combobox auslesen
            rasseString=comboBoxRasse.get()     
            #Momentane Prozentchance welche Rasse wie häufig vorkommt. soll später auf Region bezogen werden. 
            #TODO DATENBANK
            rasseMensch=800
            rasseZwerg=109
            RasseHalbelf=90
            #Wird eigentlich nicht gebraucht da Elf Rest zu 100% ist. 
            rasseElf=1            
            #Wenn Rasse auf Zufall steht wird Zufällige rasse ausgewählt
            if rasseString=='Zufall':
                rasseWert=random.randint(0,1000)
                if rasseWert<=rasseMensch:
                    rasseString='Mensch'                    
                if rasseWert>rasseMensch:
                    rasseString='Zwerg'
                if rasseWert>rasseMensch+rasseZwerg:
                    rasseString='Halbelf'
                if rasseWert>rasseMensch+rasseZwerg+RasseHalbelf:
                    rasseString='Elf'
            if rasseString=='Elf':
                anzahlAP=anzahlAP-18
            if rasseString=='Zwerg':
                anzahlAP=anzahlAP-61
                

                
            #Geschlecht 
            if random.randint(0,100)<80:
                 geschlechtString="Männlich"
            else:
                 geschlechtString="Weiblich"
                 
            #Kultur
            #Kultur wird aus der Kultur Combobox ausgelesen
            kulturString=comboBoxKultur.get()
            #Wenn es keine Kultur gibt dann wird zufällig eine bestimmt
            if kulturString=='Rasse zuerst wählen':
                #Je nach Rasse werden Kulturen aufgelistet
                if rasseString=='Mensch':
                    auswahlKultur=['Zufall','Andergaster','Aranier','Bornländer','Fjarninger','Horasier','Maraskaner','Mhanadistani','Mittelreicher','Mohas','Niversen','Norbarden','Nordaventurier','Nostrier','Novadis','Südaventurier','Svelltaler','Thorwaler','Zyklopäer']
                
                if rasseString=='Elf':
                    auswahlKultur=['Zufall','Aueelfen','Firnelfen','Waldelfen']  
                
                
                if rasseString=='Zwerg':
                    auswahlKultur=['Zufall','Ambosszwerge','Brillantzwerge','Erzzwerge','Hügelzwerge']
                
                if rasseString=='Halbelf':
                    auswahlKultur=['Zufall','Andergaster','Aranier','Aueelfen','Bornländer','Firnelfen','Fjarninger','Horasier','Maraskaner','Mhanadistani','Mittelreicher','Mohas','Niversen','Norbarden','Nordaventurier','Nostrier','Novadis','Südaventurier','Svelltaler','Thorwaler','Waldelfen','Zyklopäer']
                #Aus der Kulturliste wird zufällig eine ausgewählt. Erster wird "Zufall" wird übersprungen.
                kulturString=auswahlKultur[random.randint(1,len(auswahlKultur)-1)]
                
            #Todo Alter
            alterString="20"   
            
            #Eigenschaften
            
            
            eigenschaften={
            "KK": 8,
            "MU": 8,
            "KL": 8,
            "IN": 8,
            "CH": 8,
            "FF": 8,
            "GE": 8,
            "KO": 8
            }
            #Bei Rasse Mensch oder Halbelf Zufälliger Wert+1
            if rasseString=='Mensch' or rasseString=='Halbelf':
                zufall=random.choice(list(eigenschaften.keys()))
                eigenschaften[zufall]=eigenschaften[zufall]+1   
            #Bei Elf IN und GE +1 und Zufällig KL oder KK -2
            if rasseString=='Elf':
                eigenschaften["IN"]=eigenschaften["IN"]+1
                eigenschaften["GE"]=eigenschaften["GE"]+1                
                if random.randint(1,2)==1:
                    eigenschaften["KL"]=eigenschaften["KL"]-2
                else:
                    eigenschaften["KK"]=eigenschaften["KK"]-2
            #Bei Zwerg KO und KK +1 und CH und GE -2
            if rasseString=='Zwerg':
                eigenschaften["KO"]=eigenschaften["KO"]+1
                eigenschaften["KK"]=eigenschaften["KK"]+1                
                if random.randint(1,2)==1:
                    eigenschaften["CH"]=eigenschaften["CH"]-2
                else:
                    eigenschaften["GE"]=eigenschaften["GE"]-2
                
            eigenschaftsSteigerung=['FF','GE','KK','KO','FF','GE','KK','KO','MU','KL','IN','CH']
            
            summeEigenschaften=sum(eigenschaften.values())
            
            while summeEigenschaften<maxsumEigenschaft:
                zufall=random.choice(eigenschaftsSteigerung)
                if eigenschaften[zufall]<maxEigenschaft:
                    eigenschaften[zufall]+=1
                    summeEigenschaften+=1
                    if eigenschaften[zufall]<15:
                        anzahlAP-=15                       
                    else:
                        faktor=eigenschaften[zufall]-13
                        anzahlAP=anzahlAP-(faktor*15)
            #Kampftechnik #TODO
            
            fernkampftechnikliste=[
            #0
            Kampftechnik("Armbrüste","FF","B",6+int((eigenschaften["FF"]-8)/3)),
            #1
            Kampftechnik("Bögen","FF","C",6+int((eigenschaften["FF"]-8)/3)),
            #2
            Kampftechnik("Wurfwaffen","FF","B",6+int((eigenschaften["MU"]-8)/3)),
            ]
               
            nahkampftechnikliste=[
           
            #0
            Kampftechnik("Dolche","GE","B",6+int((eigenschaften["MU"]-8)/3)),
            #1
            Kampftechnik("Fechtwaffen","GE","C",6+int((eigenschaften["MU"]-8)/3)),
            #2
            Kampftechnik("Hiebwaffen","KK","C",6+int((eigenschaften["MU"]-8)/3)),
            #3
            Kampftechnik("Kettenwaffen","KK","C",6+int((eigenschaften["MU"]-8)/3)),
            #4
            Kampftechnik("Lanzen","KK","B",6+int((eigenschaften["MU"]-8)/3)),
            #5            
            Kampftechnik("Schild","KK","C",6+int((eigenschaften["MU"]-8)/3)),
            #6
            Kampftechnik("Zweihandhiebwaffen","KK","C",6+int((eigenschaften["FF"]-8)/3)),
            #7
            Kampftechnik("Zweihandschwert","KK","C",6+int((eigenschaften["MU"]-8)/3))
            ]
            
            
            if eigenschaften["GE"]>eigenschaften["KK"]:
                #8
                x=Kampftechnik("Raufen","GE","B",6+int((eigenschaften["MU"]-8)/3))
                #9
                y=Kampftechnik("Schwerter","GE","C",6+int((eigenschaften["MU"]-8)/3))
                #10
                z=Kampftechnik("Stangenwaffen","GE","C",6+int((eigenschaften["MU"]-8)/3))
            else:
               x=Kampftechnik("Raufen","KK","B",6+int((eigenschaften["MU"]-8)/3))
               y=Kampftechnik("Schwerter","KK","C",6+int((eigenschaften["MU"]-8)/3))
               z=Kampftechnik("Stangenwaffen","KK","C",6+int((eigenschaften["MU"]-8)/3))
            nahkampftechnikliste.append(x)
            nahkampftechnikliste.append(y)
            nahkampftechnikliste.append(z)
            
            maxAngriff=0
            for x in range(len(nahkampftechnikliste)):
                if (nahkampftechnikliste[x].wert)>maxAngriff:
                    if nahkampftechnikliste[x].name!="Schild":
                        maxAngriff=nahkampftechnikliste[x].wert
            angriffstechnik=[]        
            for x in range(len(nahkampftechnikliste)):
                if nahkampftechnikliste[x].wert==maxAngriff:
                    if nahkampftechnikliste[x].name!="Schild":
                        angriffstechnik.append(nahkampftechnikliste[x].name)
                
            primärkampftechnik=random.choice(angriffstechnik)
            
            
            
            
            searchString= "SELECT * FROM waffen WHERE kategorie='"+primärkampftechnik+"' ORDER BY RANDOM() LIMIT 1"     
            c = conn.cursor()
            c.execute(searchString)
            
            for row in c:  
               waffeString=row[0]
               dmgString=row[1]
               leiteigenschaft=row[2]
               schadensschwelle=row[3]
               atmod=row[4]
               pamod=row[5]
               reichweite=row[6]
               preis=row[7]
            
            #Steigerung Angriff TODO
            atkString=maxAngriff+int(random.randint(50,100)*(int(maxKampf)-maxAngriff)/100)
            
            for x in range(len(nahkampftechnikliste)):
                if nahkampftechnikliste[x].name==primärkampftechnik:
                    nahkampftechnikliste[x].wert=atkString
                    
            #Basiswerte Rasse
            if rasseString=='Mensch':
                lepString=5
                seelenkraft=-5
                zaehigkeit=-5
                geschwindigkeit=8
            if rasseString=='Elf':
                lepString=2
                seelenkraft=-4
                zaehigkeit=-6
                geschwindigkeit=8
            if rasseString=='Halbelf':
                lepString=5
                seelenkraft=-4
                zaehigkeit=-6
                geschwindigkeit=8
            if rasseString=='Zwerg':
                lepString=8
                seelenkraft=-4
                zaehigkeit=-4
                geschwindigkeit=6
            #Lebenspunkte 
            lepString=lepString+2*eigenschaften["KO"] 
            
            #Seelenkraft            
            seelenkraft=seelenkraft+(eigenschaften["MU"]+eigenschaften["KL"]+eigenschaften["IN"])/6
            #zähigkeit
            zaehigkeit=zaehigkeit++(eigenschaften["KO"]+eigenschaften["KO"]+eigenschaften["KK"])/6
            #Ausweichen
            ausweichen=eigenschaften["GE"]/2
            #Initative
            initative=(eigenschaften["MU"]+eigenschaften["GE"])/2+random.randint(1,6)
            #Todo Amor
            armorString="Leder"
           
            #Todo DEF
            defString="8"
                    
            #Todo Körperbeherschung
            beherschungString="10"
            #Todo Schmerzstufen
            a1String=round(0.75*lepString)
            a2String=round(0.5*lepString)
            a3String=round(0.25*lepString)
            #Todo Flucht LeP
            fluchtString="5"
          
            
            
            rasseLabel.config(text=rasseString)
            geschlechtLabel.config(text=geschlechtString)
            kulturLabel.config(text=kulturString)
            alterLabel.config(text=alterString)
            lepLabel.config(text=lepString)
            armorLabel.config(text=armorString)
            atkLabel.config(text=atkString)
            defLabel.config(text=defString)
            dmgLabel.config(text=dmgString)
            waffeLabel.config(text=waffeString)
            beherschungLabel.config(text=beherschungString)
            a1Label.config(text=a1String)
            a2Label.config(text=a2String)
            a3Label.config(text=a3String)
            fluchtLabel.config(text=fluchtString)
            
            
            KörperkraftLabel.config(text=eigenschaften["KK"])
            MutLabel.config(text=eigenschaften["MU"])
            KlugheitLabel.config(text=eigenschaften["KL"])
            IntuitionLabel.config(text=eigenschaften["IN"])
            CharismaLabel.config(text=eigenschaften["CH"])
            FingerfertigkeitLabel.config(text=eigenschaften["FF"])
            GewandheitLabel.config(text=eigenschaften["GE"])
            KonstitutionLabel.config(text=eigenschaften["KO"])
            
            ArmbrüsteLabel.config(text=fernkampftechnikliste[0].wert)
            BögenLabel.config(text=fernkampftechnikliste[1].wert)
            WurfwaffenLabel.config(text=fernkampftechnikliste[2].wert)
            
            DolcheLabel.config(text=nahkampftechnikliste[0].wert)
            FechtwaffenLabel.config(text=nahkampftechnikliste[1].wert)
            HiebwaffenLabel.config(text=nahkampftechnikliste[2].wert)
            KettenwaffenLabel.config(text=nahkampftechnikliste[3].wert)
            LanzenLabel.config(text=nahkampftechnikliste[4].wert)            
            SchildLabel.config(text=nahkampftechnikliste[5].wert)
            ZweihandhiebwaffenLabel.config(text=nahkampftechnikliste[6].wert)
            ZweihandschwerterLabel.config(text=nahkampftechnikliste[7].wert)
            RaufenLabel.config(text=nahkampftechnikliste[8].wert)
            SchwerterLabel.config(text=nahkampftechnikliste[9].wert)
            StangenwaffenLabel.config(text=nahkampftechnikliste[10].wert)
            
            
            
            
            
        abstandy=5
        
        #labels  
        #Attribute
        ttk.Label(mainFrame,text="Basiswerte",font="helvetica 10 bold").grid(row=1,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Rasse").grid(row=2,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Geschlecht").grid(row=4,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Kultur").grid(row=3,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Alter").grid(row=5,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Lebenspunkte").grid(row=6,column=1,pady=abstandy,sticky='w')        
        ttk.Label(mainFrame,text="Rüstung").grid(row=7,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Angriffswert").grid(row=8,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Verteidigungswert").grid(row=9,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Waffenschaden").grid(row=10,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Waffe").grid(row=11,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Körperbeherschung").grid(row=12,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schmerzstufe 1").grid(row=13,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schmerzstufe 2").grid(row=14,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schmerzstufe 3").grid(row=15,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Flucht LeP").grid(row=16,column=1,pady=abstandy,sticky='w')
        
        #Eigenschaften 
        ttk.Label(mainFrame,text="Eigenschafte",font="helvetica 10 bold").grid(row=1,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Körperkraft").grid(row=2,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Mut").grid(row=3,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Klugheit").grid(row=4,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Intuition").grid(row=5,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Charisma").grid(row=6,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Fingerfertigkeit").grid(row=7,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Gewandheit").grid(row=8,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Konstitution").grid(row=9,column=3,pady=abstandy,sticky='w')
        
        #Kampftechniken
        ttk.Label(mainFrame,text="Kampfertigkeiten",font="helvetica 10 bold").grid(row=1,column=5,pady=abstandy,sticky='w')        
        ttk.Label(mainFrame,text="Armbrüste").grid(row=2,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Bögen").grid(row=3,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Dolche").grid(row=4,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Fechtwaffen").grid(row=5,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Hiebwaffen").grid(row=6,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Kettenwaffen").grid(row=7,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Lanzen").grid(row=8,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Raufen").grid(row=9,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schild").grid(row=10,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schwerter").grid(row=11,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Stangenwaffen").grid(row=12,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Wurfwaffen").grid(row=13,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Zweihandhiebwaffen").grid(row=14,column=5,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Zweihandschwert").grid(row=15,column=5,pady=abstandy,sticky='w')
        
        #Attribute Labels
        rasseLabel=ttk.Label(mainFrame,text="")
        rasseLabel.grid(row=2,column=2)
        geschlechtLabel=ttk.Label(mainFrame,text="")
        geschlechtLabel.grid(row=4,column=2)        
        kulturLabel=ttk.Label(mainFrame,text="")
        kulturLabel.grid(row=3,column=2)
        alterLabel=ttk.Label(mainFrame,text="")
        alterLabel.grid(row=5,column=2)
        lepLabel=ttk.Label(mainFrame,text="")
        lepLabel.grid(row=6,column=2)
        armorLabel=ttk.Label(mainFrame,text="")
        armorLabel.grid(row=7,column=2)
        atkLabel=ttk.Label(mainFrame,text="")
        atkLabel.grid(row=8,column=2)
        defLabel=ttk.Label(mainFrame,text="")
        defLabel.grid(row=9,column=2)
        dmgLabel=ttk.Label(mainFrame,text="")
        dmgLabel.grid(row=10,column=2)
        waffeLabel=ttk.Label(mainFrame,text="")
        waffeLabel.grid(row=11,column=2)
        beherschungLabel=ttk.Label(mainFrame,text="")
        beherschungLabel.grid(row=12,column=2)
        a1Label=ttk.Label(mainFrame,text="")
        a1Label.grid(row=13,column=2)
        a2Label=ttk.Label(mainFrame,text="")
        a2Label.grid(row=14,column=2)
        a3Label=ttk.Label(mainFrame,text="")
        a3Label.grid(row=15,column=2)
        fluchtLabel=ttk.Label(mainFrame,text="")
        fluchtLabel.grid(row=16,column=2)
        
        #Eigenschaften Label
        KörperkraftLabel=ttk.Label(mainFrame,text="")
        KörperkraftLabel.grid(row=2, column=4)
        MutLabel=ttk.Label(mainFrame,text="")
        MutLabel.grid(row=3, column=4)
        KlugheitLabel=ttk.Label(mainFrame,text="")
        KlugheitLabel.grid(row=4, column=4)
        IntuitionLabel=ttk.Label(mainFrame,text="")
        IntuitionLabel.grid(row=5, column=4)
        CharismaLabel=ttk.Label(mainFrame,text="")
        CharismaLabel.grid(row=6, column=4)
        FingerfertigkeitLabel=ttk.Label(mainFrame,text="")
        FingerfertigkeitLabel.grid(row=7, column=4)
        GewandheitLabel=ttk.Label(mainFrame,text="")
        GewandheitLabel.grid(row=8, column=4)
        KonstitutionLabel=ttk.Label(mainFrame,text="")
        KonstitutionLabel.grid(row=9, column=4)
        
        #Kampfeigenschaften
        ArmbrüsteLabel=ttk.Label(mainFrame,text="")
        ArmbrüsteLabel.grid(row=2, column=6)
        BögenLabel=ttk.Label(mainFrame,text="")
        BögenLabel.grid(row=3, column=6)
        DolcheLabel=ttk.Label(mainFrame,text="")
        DolcheLabel.grid(row=4, column=6)
        FechtwaffenLabel=ttk.Label(mainFrame,text="")
        FechtwaffenLabel.grid(row=5, column=6)
        HiebwaffenLabel=ttk.Label(mainFrame,text="")
        HiebwaffenLabel.grid(row=6, column=6)
        KettenwaffenLabel=ttk.Label(mainFrame,text="")
        KettenwaffenLabel.grid(row=7, column=6)
        LanzenLabel=ttk.Label(mainFrame,text="")
        LanzenLabel.grid(row=8, column=6)
        RaufenLabel=ttk.Label(mainFrame,text="")
        RaufenLabel.grid(row=9, column=6)
        SchildLabel=ttk.Label(mainFrame,text="")
        SchildLabel.grid(row=10, column=6)
        SchwerterLabel=ttk.Label(mainFrame,text="")
        SchwerterLabel.grid(row=11, column=6)
        StangenwaffenLabel=ttk.Label(mainFrame,text="")
        StangenwaffenLabel.grid(row=12, column=6)
        WurfwaffenLabel=ttk.Label(mainFrame,text="")
        WurfwaffenLabel.grid(row=13, column=6)
        ZweihandhiebwaffenLabel=ttk.Label(mainFrame,text="")
        ZweihandhiebwaffenLabel.grid(row=14, column=6)
        ZweihandschwerterLabel=ttk.Label(mainFrame,text="")
        ZweihandschwerterLabel.grid(row=15, column=6)

        
        
        
        
        randomizeButton=ttk.Button(mainFrame,text="Werte Generieren",command=generateNew,width=50)
        randomizeButton.grid(row=50,column=1,columnspan=10)
        
        comboBoxRasse.bind("<<ComboboxSelected>>", changeKulturCombobox)
        