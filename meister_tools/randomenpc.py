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

import random
import re
     
from . import patrickstools2
from . import odatasfunctions as of


class PageRandomeNPC(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        
        
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
            
           
                   
                         
            
            #Lebenspunkte            
            if rasseString=='Mensch':
                lepString=5
            if rasseString=='Elf':
                lepString=2
            if rasseString=='Halbelf':
                lepString=5
            if rasseString=='Zwerg':
                lepString=8
                
            #Todo Amor
            armorString="Leder"
           
            #Todo DEF
            defString="8"
            #Todo DMG
            dmgString="1W6+2"
            #Todo Waffe
            waffeString="Schwert"
            #Todo Körperbeherschung
            beherschungString="10"
            #Todo Schmerzstufen
            a1String="75%"
            a2String="50%"
            a3String="25%"
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
            
            
            
        abstandy=5
        
        #labels        
        ttk.Label(mainFrame,text="Rasse").grid(row=2,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Geschlecht").grid(row=4,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Kultur").grid(row=3,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Alter").grid(row=6,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Lebenspunkte").grid(row=8,column=1,pady=abstandy,sticky='w')        
        ttk.Label(mainFrame,text="Rüstung").grid(row=10,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Angriffswert").grid(row=12,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Verteidigungswert").grid(row=14,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Waffenschaden").grid(row=16,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Waffentyp").grid(row=18,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Körperbeherschung").grid(row=20,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schmerzstufe 1").grid(row=22,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schmerzstufe 2").grid(row=24,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Schmerzstufe 3").grid(row=26,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Flucht LeP").grid(row=28,column=1,pady=abstandy,sticky='w')
        
        ttk.Label(mainFrame,text="Körperkraft").grid(row=2,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Mut").grid(row=3,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Klugheit").grid(row=4,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Intuition").grid(row=6,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Charisma").grid(row=8,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Fingerfertigkeit").grid(row=10,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Gewandheit").grid(row=12,column=3,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Konstitution").grid(row=14,column=3,pady=abstandy,sticky='w')
        
        rasseLabel=ttk.Label(mainFrame,text="")
        rasseLabel.grid(row=2,column=2)
        geschlechtLabel=ttk.Label(mainFrame,text="")
        geschlechtLabel.grid(row=4,column=2)        
        kulturLabel=ttk.Label(mainFrame,text="")
        kulturLabel.grid(row=3,column=2)
        alterLabel=ttk.Label(mainFrame,text="")
        alterLabel.grid(row=6,column=2)
        lepLabel=ttk.Label(mainFrame,text="")
        lepLabel.grid(row=8,column=2)
        armorLabel=ttk.Label(mainFrame,text="")
        armorLabel.grid(row=10,column=2)
        atkLabel=ttk.Label(mainFrame,text="")
        atkLabel.grid(row=12,column=2)
        defLabel=ttk.Label(mainFrame,text="")
        defLabel.grid(row=14,column=2)
        dmgLabel=ttk.Label(mainFrame,text="")
        dmgLabel.grid(row=16,column=2)
        waffeLabel=ttk.Label(mainFrame,text="")
        waffeLabel.grid(row=18,column=2)
        beherschungLabel=ttk.Label(mainFrame,text="")
        beherschungLabel.grid(row=20,column=2)
        a1Label=ttk.Label(mainFrame,text="")
        a1Label.grid(row=22,column=2)
        a2Label=ttk.Label(mainFrame,text="")
        a2Label.grid(row=24,column=2)
        a3Label=ttk.Label(mainFrame,text="")
        a3Label.grid(row=26,column=2)
        fluchtLabel=ttk.Label(mainFrame,text="")
        fluchtLabel.grid(row=28,column=2)
        
        KörperkraftLabel=ttk.Label(mainFrame,text="")
        KörperkraftLabel.grid(row=2, column=4)
        MutLabel=ttk.Label(mainFrame,text="")
        MutLabel.grid(row=3, column=4)
        KlugheitLabel=ttk.Label(mainFrame,text="")
        KlugheitLabel.grid(row=4, column=4)
        IntuitionLabel=ttk.Label(mainFrame,text="")
        IntuitionLabel.grid(row=6, column=4)
        CharismaLabel=ttk.Label(mainFrame,text="")
        CharismaLabel.grid(row=8, column=4)
        FingerfertigkeitLabel=ttk.Label(mainFrame,text="")
        FingerfertigkeitLabel.grid(row=10, column=4)
        GewandheitLabel=ttk.Label(mainFrame,text="")
        GewandheitLabel.grid(row=12, column=4)
        KonstitutionLabel=ttk.Label(mainFrame,text="")
        KonstitutionLabel.grid(row=14, column=4)
        
        randomizeButton=ttk.Button(mainFrame,text="Werte Generieren",command=generateNew,width=50)
        randomizeButton.grid(row=30,column=1,columnspan=2)
        
        comboBoxRasse.bind("<<ComboboxSelected>>", changeKulturCombobox)
        