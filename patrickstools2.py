#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19 #  in conjunction with Tcl version 8.6 
# Jan 18, 2019 08:39:17 PM CET  platform: Windows NT


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
from tkinter import messagebox

import random

import sqlite3


#print(s.theme_names())

    
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
    


#Main Window wird gestartet.
class PTools(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #self.geometry("%dx%d"%(self.winfo_screenwidth()-200,self.winfo_screenheight()-200))
        self._frame = None
        
        self.title("Odatas Meister Tools")
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(anchor='center')    

#Das Start Fenster was nach dem Starten des Tools gezeigt wird
#Hier wird auch das Theme für die App gesetzt.
class StartPage(ttk.Frame):

    def __init__(self, master):        
        
        s=ttk.Style()
        s.theme_use('winnative')
        
        ttk.Frame.__init__(self, master)
        
        alles=ttk.Frame(self)
        alles.pack(padx=100)
        version=ttk.Frame(self)
        version.pack(anchor='e')
    
                       
        self.Name=ttk.Label(alles,text="Odatas Meistertools", font='Arial 18 bold')
        self.Name.pack(pady=30)
        
        self.Hilfe=ttk.Label(alles,text="Diese Alpha Version ist noch ziemlich kacke. Mal schauen ob es besser wird.\n Feedback an Odatas auf Reddit")
        self.Hilfe.pack(pady=20)
        
        self.button1 =ttk.Button(alles, text ="Reisehelfer",command=lambda: master.switch_frame(PageTravel),width=50) #command linked
        self.button1.pack()
        
        self.button2=ttk.Button(alles, text ="Hier kommt noch was (NPC Randomizer)",width=50)
        self.button2.pack()
        
        self.button3=ttk.Button(alles, text ="Hier auch (Gefahrenübersicht)",command=lambda: master.switch_frame(PageDangers),width=50)
        self.button3.pack()
        
        self.button4=ttk.Button(alles, text ="Kontakt",command=lambda: master.switch_frame(PageContact),width=50)
        self.button4.pack()
        
       
        ttk.Button(alles, text="Quit", command=self.master.destroy,width=50).pack(pady=30)
        
        self.version=ttk.Label(version,text="Version Alpha 0.11")
        self.version.pack(anchor='se')

        

#Das Fenster Reisehilfen
class PageTravel(ttk.Frame):
    #Die Verschiedenen Frames für die Unterkategorien
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        
        eingaben=tk.Frame(self)
        eingaben.grid(row=0,column=0,pady=50,padx=(100,0),sticky='w')
        
        anzeigen=tk.Frame(self)
        anzeigen.grid(row=0,column=1,pady=50,sticky='nw')
        
        tabelle=tk.Frame(self)
        tabelle.grid(row=1,column=0,pady=10,padx=100,columnspan=2,sticky='w')
        
        listbox=tk.Frame(self)
        listbox.grid(row=2,column=0,sticky='w',padx=100)
        
        berechnungsbutton=tk.Frame(self)
        berechnungsbutton.grid(row=3,column=0,pady=10,padx=100)
        
        knöpfe=tk.Frame(self)
        knöpfe.grid(row=3,column=1,pady=10,padx=100)
        
        #Die Funktion was passiert wenn man auf "Berrechnen" drückt.
        def ButtonPress(event=None):
            #Zuerst werden alle Eingaben geprüft und ausgelesen
            try:                
                #Gruppengröße
                gruppengröße=int(eingabe1.get())
            except:
                messagebox.showerror("Idiot", "Nur ganze Zahlen erlaubt. Keine Buchstaben. Keine Komma Zahlen und auch keine Sonderzeichen")
                eingabe1.delete(0,'end')
                eingabe1.insert(0,"1")
            #Zu Fuß
            try:                
                fußWeg=int(self.eingabe2.get())
            except:
                fußWeg=0
                messagebox.showerror("Zu Fuß","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                self.eingabe2.delete(0,'end')
                self.eingabe2.insert(0,"0")
            #Flusskahn
            try:
                FlusskahnWeg=int(self.eingabe3.get())
            except: 
                FlusskahnWeg=0
                messagebox.showerror("Flusskahn","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                self.eingabe3.delete(0,'end')
                self.eingabe3.insert(0,"0")
                #Reisekutsche
            try:
                reiseKutschenWeg=int(self.eingabe4.get())
            except: 
                reiseKutschenWeg=0
                messagebox.showerror("Reisekutsche","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                self.eingabe4.delete(0,'end')
                self.eingabe4.insert(0,"0")
                #Seereise Hängematte
            try:
                seeReiseWegM=int(self.eingabe5.get())
            except:
                seeReiseWegM=0
                messagebox.showerror("Seereise Hängematte","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                self.eingabe5.delete(0,'end')
                self.eingabe5.insert(0,"0")
                #Seereise Kabine
            try:
                seeReiseWegK=int(self.eingabe6.get())
            except:
                messagebox.showerror("Seereise Kabine","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                self.eingabe6.delete(0,'end')
                self.eingabe6.insert(0,"0")
                seeReiseWegK=0
                
            try:
                pferdReise=int(self.eingabe7.get())
            except:
                messagebox.showerror("Pferd Reiten","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                self.eingabe7.delete(0,'end')
                self.eingabe7.insert(0,"0")
                pferdReise=0
            #Das Rundungslevel wird bestimmt
            rundung=comboBoxRundung.get()
            #Die Reiseschwierigkeit wird bestimmt
            wegZustand=comboBoxWege.get()
            
            #Je nach Rundungslevel wird der Prozentwert festgelegt
            simulation=comboBoxSimulation.get()
            if simulation == 'Simulation':            
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
           
            
            daysToTravel=0
            
            
            #Festlegen ob Wert berechnet oder Simuliert werden soll
            
            #Transportkosten Berechnen für das Handeln
            FlusskahnKosten=FlusskahnWeg/100*kostenFlusskahn*gruppengröße
            ReiseKutscheKosten=reiseKutschenWeg/100*kostenReisekutsche*gruppengröße
            SeereiseKostenM=seeReiseWegM/100*kostenSeereiseHängematte*gruppengröße
            SeereiseKostenK=seeReiseWegK/100*kostenSeereiseKabine*gruppengröße
            
            #Gesamt Transport Kosten werden nach Distanz und Gruppengröße festgelegt
            transportCost=gruppengröße*(FlusskahnWeg*kostenFlusskahn+reiseKutschenWeg*kostenReisekutsche+seeReiseWegM*kostenSeereiseHängematte+seeReiseWegK*kostenSeereiseKabine)/100
            #Simulation der Reisedistanz. 
            if simulation=='Simulation' and wegZustand != 'Perfekt':
                #Jeder Tag wird einzelnd Simuliert.
                #So lange noch Reisweg vorhanden ist
                while pferdReise>0:
                    #Berechne den Verlangsamungsfaktor
                    daySlow=1/(random.randint(chance*100,100)/100)
                    #Zähle Reisetag einen hoch
                    daysToTravel=daysToTravel+1
                    #Die Distanz ist die Normaldistanz-Distanz*Verlangsamungsfaktor
                    pferdReise=pferdReise-(pferdReise*daySlow)
                    
                while fußWeg>0:
                    daySlow=(random.randint(chance*100,100)/100)
                    daysToTravel=daysToTravel+1
                    fußWeg=fußWeg-(speedFuß*daySlow)
                    
                while FlusskahnWeg>0:
                    daySlow=(random.randint(chance*100,100)/100)
                    daysToTravel=daysToTravel+1
                    FlusskahnWeg=FlusskahnWeg-(speedFlusskahn*daySlow)
                    
                while reiseKutschenWeg>0:
                    daySlow=(random.randint(chance*100,100)/100)
                    daysToTravel=daysToTravel+1
                    reiseKutschenWeg=reiseKutschenWeg-(speedReiseKutsche*daySlow)
                    
                while seeReiseWegM>0:
                    daySlow=(random.randint(chance*100,100)/100)
                    daysToTravel=daysToTravel+1
                    seeReiseWegM=seeReiseWegM-(speedShip*daySlow)
                    
                while seeReiseWegK>0:
                    daySlow=(random.randint(chance*100,100)/100)
                    daysToTravel=daysToTravel+1
                    seeReiseWegK=seeReiseWegK-(speedShip*daySlow)
                
            #Wenn nicht simuliert wird ist es einfach das Level mal der Reisedauer   
            else:
                daysToTravel=(pferdReise/speedHorse+fußWeg/speedFuß+FlusskahnWeg/speedFlusskahn+reiseKutschenWeg/speedReiseKutsche+seeReiseWegM/speedShip+seeReiseWegK/speedShip)*(1/chance)
                
            
            
            #Darstellung von Tagen und Transporkosten
            self.travelDays.config(text=str(int(daysToTravel))+ " Tage") 
            
            self.transportKosten.config(text=Geldrechner(transportCost,'Silber',rundung))
            
            
            food=0
            water=0
            #travelersCount=int(gruppengröße)
            if simulation=='Simulation' and wegZustand != 'Perfekt':
                for x in range(int(daysToTravel)):
                    dayHard=1/((random.randint(chance*100,100)/100))
                    
                        
                    foodNeed=foodPerDay*gruppengröße*dayHard
                    waterNeed=waterPerDay*gruppengröße*dayHard
                    food=food+foodNeed
                    water=water+waterNeed
            else:
                food=foodPerDay*gruppengröße*daysToTravel*(1/(chance))
                water=waterPerDay*gruppengröße*daysToTravel*(1/(chance))
                
               
                
            
            costs=Geldrechner(food,'Silber',rundung)
            self.foodCost.config(text=costs)   
            travelcostAll=Geldrechner(food+transportCost,'Silber',rundung)
            self.travelAll.config(text= travelcostAll)
            
            
            
       
            
            tabelle01.config(text="Fertigkeitsprobe: Handeln")
            #tabelle02.config(text="Für wenn die Spieler auf Handeln würfeln wollen")
            tabelle11.config(text="Fehlschlag")
            tabelle21.config(text="Normalpreis")
            tabelle31.config(text="QS 1: FP 0-3")
            tabelle41.config(text="QS 2: FP 4-6")
            tabelle51.config(text="QS 3: FP 7-9")
            tabelle61.config(text="QS 4: FP 10-12")
            tabelle71.config(text="QS 5: FP 13-15")
            tabelle81.config(text="QS 6: FP 16+")

            
            #Tabelle Füllen
            if food>0:
                
                tabelle12.config(text="Proviant")
                tabelle22.config(text=GeldrechnerKurz(food*1.3,'Silber',rundung))
                tabelle32.config(text=GeldrechnerKurz(food*1,'Silber',rundung))
                tabelle42.config(text=GeldrechnerKurz(food*0.95,'Silber',rundung))
                tabelle52.config(text=GeldrechnerKurz(food*0.92,'Silber',rundung))
                tabelle62.config(text=GeldrechnerKurz(food*0.9,'Silber',rundung))
                tabelle72.config(text=GeldrechnerKurz(food*0.89,'Silber',rundung))
                tabelle82.config(text=GeldrechnerKurz(food*0.87,'Silber',rundung))
                tabelle92.config(text=GeldrechnerKurz(food*0.80,'Silber',rundung))
            else:
                tabelle12.config(text="")
                tabelle22.config(text="")
                tabelle32.config(text="")
                tabelle42.config(text="")
                tabelle52.config(text="")
                tabelle62.config(text="")
                tabelle72.config(text="")
                tabelle82.config(text="")
                tabelle92.config(text="")
                
            
                
            if FlusskahnKosten>0:
                
                tabelle13.config(text="Flusskahn")
                tabelle23.config(text=GeldrechnerKurz(FlusskahnKosten*1.3,'Silber',rundung))
                tabelle33.config(text=GeldrechnerKurz(FlusskahnKosten,'Silber',rundung))
                tabelle43.config(text=GeldrechnerKurz(FlusskahnKosten*0.95,'Silber',rundung))
                tabelle53.config(text=GeldrechnerKurz(FlusskahnKosten*0.92,'Silber',rundung))
                tabelle63.config(text=GeldrechnerKurz(FlusskahnKosten*0.9,'Silber',rundung))
                tabelle73.config(text=GeldrechnerKurz(FlusskahnKosten*0.89,'Silber',rundung))
                tabelle83.config(text=GeldrechnerKurz(FlusskahnKosten*0.87,'Silber',rundung))
                tabelle93.config(text=GeldrechnerKurz(FlusskahnKosten*0.80,'Silber',rundung))
            else:
                tabelle13.config(text="")
                tabelle23.config(text="")
                tabelle33.config(text="")
                tabelle43.config(text="")
                tabelle53.config(text="")
                tabelle63.config(text="")
                tabelle73.config(text="")
                tabelle83.config(text="")
                tabelle93.config(text="")
            
            
            if ReiseKutscheKosten>0:
                
                tabelle14.config(text="Reisekutschen")
                tabelle24.config(text=GeldrechnerKurz(ReiseKutscheKosten*1.3,'Silber',rundung))
                tabelle34.config(text=GeldrechnerKurz(ReiseKutscheKosten,'Silber',rundung))
                tabelle44.config(text=GeldrechnerKurz(ReiseKutscheKosten*0.95,'Silber',rundung))
                tabelle54.config(text=GeldrechnerKurz(ReiseKutscheKosten*0.92,'Silber',rundung))
                tabelle64.config(text=GeldrechnerKurz(ReiseKutscheKosten*0.9,'Silber',rundung))
                tabelle74.config(text=GeldrechnerKurz(ReiseKutscheKosten*0.89,'Silber',rundung))
                tabelle84.config(text=GeldrechnerKurz(ReiseKutscheKosten*0.87,'Silber',rundung))
                tabelle94.config(text=GeldrechnerKurz(ReiseKutscheKosten*0.80,'Silber',rundung))
            else:
                tabelle14.config(text="")
                tabelle24.config(text="")
                tabelle34.config(text="")
                tabelle44.config(text="")
                tabelle54.config(text="")
                tabelle64.config(text="")
                tabelle74.config(text="")
                tabelle84.config(text="")
                tabelle94.config(text="")
            
            
            if SeereiseKostenM>0:
                
                tabelle15.config(text="Seereise Hängematte")
                tabelle25.config(text=GeldrechnerKurz(SeereiseKostenM*1.3,'Silber',rundung))
                tabelle35.config(text=GeldrechnerKurz(SeereiseKostenM,'Silber',rundung))
                tabelle45.config(text=GeldrechnerKurz(SeereiseKostenM*0.95,'Silber',rundung))
                tabelle55.config(text=GeldrechnerKurz(SeereiseKostenM*0.92,'Silber',rundung))
                tabelle65.config(text=GeldrechnerKurz(SeereiseKostenM*0.9,'Silber',rundung))
                tabelle75.config(text=GeldrechnerKurz(SeereiseKostenM*0.89,'Silber',rundung))
                tabelle85.config(text=GeldrechnerKurz(SeereiseKostenM*0.87,'Silber',rundung))
                tabelle95.config(text=GeldrechnerKurz(SeereiseKostenM*0.80,'Silber',rundung))
            else:
                tabelle15.config(text="")
                tabelle25.config(text="")
                tabelle35.config(text="")
                tabelle45.config(text="")
                tabelle55.config(text="")
                tabelle65.config(text="")
                tabelle75.config(text="")
                tabelle85.config(text="")
                tabelle95.config(text="")
                
            
            if SeereiseKostenK>0:
                
                tabelle16.config(text="Seereise Kabine")
                tabelle26.config(text=GeldrechnerKurz(SeereiseKostenK*1.3,'Silber',rundung))
                tabelle36.config(text=GeldrechnerKurz(SeereiseKostenK,'Silber',rundung))
                tabelle46.config(text=GeldrechnerKurz(SeereiseKostenK*0.95,'Silber',rundung))
                tabelle56.config(text=GeldrechnerKurz(SeereiseKostenK*0.92,'Silber',rundung))
                tabelle66.config(text=GeldrechnerKurz(SeereiseKostenK*0.9,'Silber',rundung))
                tabelle76.config(text=GeldrechnerKurz(SeereiseKostenK*0.89,'Silber',rundung))
                tabelle86.config(text=GeldrechnerKurz(SeereiseKostenK*0.87,'Silber',rundung))
                tabelle96.config(text=GeldrechnerKurz(SeereiseKostenK*0.80,'Silber',rundung))
            else:
                tabelle16.config(text="")
                tabelle26.config(text="")
                tabelle36.config(text="")
                tabelle46.config(text="")
                tabelle56.config(text="")
                tabelle66.config(text="")
                tabelle76.config(text="")
                tabelle86.config(text="")
                tabelle96.config(text="")
            
        
        #Gewicht in Steine
        foodPerDay=50
        waterPerDay=3
        
        #Geschwindigkeit in Meilen pro Tag
        speedFuß=30
        
        speedFlusskahn=50
        
        #Kosten in Kreuzer
        kostenFlusskahn=25/2
        
        speedReiseKutsche=40
        kostenReisekutsche=1200
        
        speedShip=100
        kostenSeereiseHängematte=800
        kostenSeereiseKabine=15000     
            
        speedHorse=50       
        
        
        #eingaben
        numberLabel1=ttk.Label(eingaben,text="Gruppengröße",font='Arial 14')
        numberLabel1.grid(row=1,column=1,sticky='w',pady=10)         
        eingabe1=ttk.Entry(eingaben)
        eingabe1.insert(0,"1")
        eingabe1.grid(row=1,column=2,sticky='w',pady=10)
        
        self.distanz=ttk.Label(eingaben,text="Distanzen in ganzen Meilen:",font='Arial 12 bold')
        self.distanz.grid(row=2,column=1,sticky='w')
         
        self.numberLabel2=ttk.Label(eingaben,text="Zu Fuß",font='Arial 10')
        self.numberLabel2.grid(row=3,column=1,sticky='w')
        self.eingabe2=ttk.Entry(eingaben)
        #Testwert
        self.eingabe2.insert(0,"1000")
        self.eingabe2.grid(row=3,column=2,sticky='w')
         
        self.numberLabel3=ttk.Label(eingaben,text="Flusskahn",font='Arial 10')
        self.numberLabel3.grid(row=4,column=1,sticky='w')
        self.eingabe3=ttk.Entry(eingaben)
        self.eingabe3.insert(3,"1000")
        self.eingabe3.grid(row=4,column=2,sticky='w')
         
        self.numberLabel4=ttk.Label(eingaben,text="Reisekutsche",font='Arial 10')
        self.numberLabel4.grid(row=5,column=1,sticky='w')
        self.eingabe4=ttk.Entry(eingaben)
        self.eingabe4.insert(0,"1000")
        self.eingabe4.grid(row=5,column=2,sticky='w')
         
        self.numberLabel5=ttk.Label(eingaben,text="Seereise, Hängematte",font='Arial 10')
        self.numberLabel5.grid(row=6,column=1,sticky='w')   
        self.eingabe5=ttk.Entry(eingaben)
        self.eingabe5.insert(0,"1000")
        self.eingabe5.grid(row=6,column=2,sticky='w')
        
        self.numberLabel6=ttk.Label(eingaben,text="Seereise, Kabine",font='Arial 10')
        self.numberLabel6.grid(row=7,column=1,sticky='w')   
        self.eingabe6=ttk.Entry(eingaben)
        self.eingabe6.insert(0,"1000")
        self.eingabe6.grid(row=7,column=2,sticky='w')
        
        self.numberLabel7=ttk.Label(eingaben,text="Pferd Reitend",font='Arial 10')
        self.numberLabel7.grid(row=8,column=1,sticky='w')   
        self.eingabe7=ttk.Entry(eingaben)
        self.eingabe7.insert(0,"1000")
        self.eingabe7.grid(row=8,column=2,sticky='w')
        
        auswahlWege = ['Perfekt', 'Gut', 'Mittel','Schlecht']
        
        ttk.Label(eingaben,text="").grid(row=9,columns=2)

        
        
        ttk.Label(eingaben,text="Geschwindigkeit durch\nWegbeschaffenheit \nund Umwelteinflüsse").grid(row=10,column=1,sticky='w')
        comboBoxWege=ttk.Combobox(eingaben,values=auswahlWege,state="readonly")
        comboBoxWege.grid(row=10,column=2)  
        comboBoxWege.set('Gut')
        
        ttk.Label(eingaben,text="Berechnungsmethode Proviant").grid(row=11,column=1,sticky='w')
        simulationAuswahl=['Simulation','Einfach']
        comboBoxSimulation=ttk.Combobox(eingaben,values=simulationAuswahl,state="readonly")
        comboBoxSimulation.grid(row=11,column=2)
        comboBoxSimulation.set('Simulation')
        
        #berechnungsbutton
        self.calculation=ttk.Button(berechnungsbutton,text="Berechnen",command=ButtonPress,width=50)
        self.calculation.grid(row=20,column=1,pady=10,sticky='w') 
        
        
        #anzeigen
        self.travelDayslabel=ttk.Label(anzeigen,text="Reisedauer:",font='Arial 10 bold')
        self.travelDayslabel.grid(row=1,column=1,sticky='w')
        self.travelDays=ttk.Label(anzeigen,text="0 Tage",font='Arial 10 bold')
        self.travelDays.grid(row=1,column=2,sticky='w')
        
        self.foodCostlabel=ttk.Label(anzeigen,text="Kosten für Proviant:",font='Arial 10 bold')
        self.foodCostlabel.grid(row=2,column=1,sticky='w')
        self.foodCost=ttk.Label(anzeigen,text="0 Dukaten 0 Silber 0 Heller 0 Kreuzer",font='Arial 10 bold')
        self.foodCost.grid(row=2,column=2,sticky='w')

        
        self.transportKostenlabel=ttk.Label(anzeigen,text="Kosten für Transport:",font='Arial 10 bold')
        self.transportKostenlabel.grid(row=3,column=1,sticky='w')
        self.transportKosten=ttk.Label(anzeigen,text="0 Dukaten 0 Silber 0 Heller 0 Kreuzer",font='Arial 10 bold')
        self.transportKosten.grid(row=3,column=2,sticky='w')
        
        self.travelAlllabel=ttk.Label(anzeigen,text="Kosten Gesamt: ",font='Arial 10 bold')
        self.travelAlllabel.grid(row=4,column=1,sticky='w')
        self.travelAll=ttk.Label(anzeigen,text="0 Dukaten 0 Silber 0 Heller 0 Kreuzer",font='Arial 10 bold')
        self.travelAll.grid(row=4,column=2,sticky='w')
        
        
        
        #TABELLE        
        #COLUMN 1 Beschriftung
        tabelle01=ttk.Label(tabelle,text="",font='Arial 14 bold')
        tabelle01.grid(row=1,column=1,pady=(0,20),sticky='w')
        
        tabelle02=ttk.Label(tabelle,text="",font='Arial 10 ')
        tabelle02.grid(row=1,column=2,pady=(0,20),sticky='w',columnspan=5)
        
        tabelle11=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle11.grid(row=3,column=1,sticky='w')
        
        tabelle21=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle21.grid(row=4,column=1,sticky='w')
        
        tabelle31=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle31.grid(row=5,column=1,sticky='w')
        
        tabelle41=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle41.grid(row=6,column=1,sticky='w')
        
        tabelle51=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle51.grid(row=7,column=1,sticky='w')
        
        tabelle61=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle61.grid(row=8,column=1,sticky='w')
        
        tabelle71=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle71.grid(row=9,column=1,sticky='w')
        
        tabelle81=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle81.grid(row=10,column=1,sticky='w')
        
        
        
            
        #COLUMN 2 Proviant
        tabelle12=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle12.grid(row=2,column=2,sticky='e')
        
        
        tabelle22=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle22.grid(row=3,column=2,sticky='e')
        
        tabelle32=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle32.grid(row=4,column=2,sticky='e')
        
        tabelle42=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle42.grid(row=5,column=2,sticky='e')
        
        tabelle52=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle52.grid(row=6,column=2,sticky='e')
        
        tabelle62=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle62.grid(row=7,column=2,sticky='e')
        
        tabelle72=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle72.grid(row=8,column=2,sticky='e')
        
        tabelle82=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle82.grid(row=9,column=2,sticky='e')
        
        tabelle92=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle92.grid(row=10,column=2,sticky='e')
        
        #COLUMN 3 Flusskahn
        tabelle13=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle13.grid(row=2,column=3,sticky='e')
        
        
        tabelle23=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle23.grid(row=3,column=3,sticky='e')
        
        tabelle33=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle33.grid(row=4,column=3,sticky='e')
        
        tabelle43=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle43.grid(row=5,column=3,sticky='e')
        
        tabelle53=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle53.grid(row=6,column=3,sticky='e')
        
        tabelle63=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle63.grid(row=7,column=3,sticky='e')
        
        tabelle73=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle73.grid(row=8,column=3,sticky='e')
        
        tabelle83=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle83.grid(row=9,column=3,sticky='e')
        
        tabelle93=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle93.grid(row=10,column=3,sticky='e')
        
         #COLUMN 4 Reisekutsche
        tabelle14=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle14.grid(row=2,column=4,sticky='e')
        
        
        tabelle24=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle24.grid(row=3,column=4,sticky='e')
        
        tabelle34=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle34.grid(row=4,column=4,sticky='e')
        
        tabelle44=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle44.grid(row=5,column=4,sticky='e')
        
        tabelle54=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle54.grid(row=6,column=4,sticky='e')
        
        tabelle64=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle64.grid(row=7,column=4,sticky='e')
        
        tabelle74=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle74.grid(row=8,column=4,sticky='e')
        
        tabelle84=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle84.grid(row=9,column=4,sticky='e')
        
        tabelle94=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle94.grid(row=10,column=4,sticky='e')
        
        #COLUMN 5 Seereise Hängematte
        tabelle15=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle15.grid(row=2,column=5,sticky='e')
        
        
        tabelle25=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle25.grid(row=3,column=5,sticky='e')
        
        tabelle35=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle35.grid(row=4,column=5,sticky='e')
        
        tabelle45=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle45.grid(row=5,column=5,sticky='e')
        
        tabelle55=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle55.grid(row=6,column=5,sticky='e')
        
        tabelle65=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle65.grid(row=7,column=5,sticky='e')
        
        tabelle75=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle75.grid(row=8,column=5,sticky='e')
        
        tabelle85=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle85.grid(row=9,column=5,sticky='e')
        
        tabelle95=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle95.grid(row=10,column=5,sticky='e')
        
        #COLUMN 6 Seereise Kabine
        tabelle16=ttk.Label(tabelle,text="",font='Arial 10 bold')
        tabelle16.grid(row=2,column=6,sticky='e')
        
        
        tabelle26=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle26.grid(row=3,column=6,sticky='e')
        
        tabelle36=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle36.grid(row=4,column=6,sticky='e')
        
        tabelle46=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle46.grid(row=5,column=6,sticky='e')
        
        tabelle56=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle56.grid(row=6,column=6,sticky='e')
        
        tabelle66=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle66.grid(row=7,column=6,sticky='e')
        
        tabelle76=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle76.grid(row=8,column=6,sticky='e')
        
        tabelle86=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle86.grid(row=9,column=6,sticky='e')
        
        tabelle96=ttk.Label(tabelle,text="",font='Arial 10')
        tabelle96.grid(row=10,column=6,sticky='e')
        
        
        
        ttk.Label(listbox,text="Rundung auf volle:",font='Arial 10').grid(sticky='w')
        
            
        auswahlRundung = ['Dukaten', 'Silber', 'Heller','Kreuzer']
        
        comboBoxRundung=ttk.Combobox(listbox,values=auswahlRundung,state="readonly")
        comboBoxRundung.grid()  
        comboBoxRundung.set('Kreuzer')
                

        #masterframe
               
        
        #self.caluclationQS=ttk.Button(knöpfe,text="QS Stufen Berechnen")
        #self.caluclationQS.grid(row=20,column=3)
        
        self.mainMenu = ttk.Button(knöpfe, text="Zurück zum Hauptmenü",
                           command=lambda: master.switch_frame(StartPage),width=50)
        self.mainMenu.grid(row=21,column=1)
        
class PageDangers(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)  
        
        
        hauptFrame=ttk.Frame(self)
        hauptFrame.pack()
        
        alles=ttk.Frame(self)
        alles.pack()
        
        endButton=ttk.Frame(self)
        endButton.pack()
        
        
        auswahlRegionen = ['Mittelreich' ,'Orkland' ,'Thorwal' ,'Nostria' , 'Andergast' , 'Horasreich' , 'Zyklopeninseln' ,'Alanfa' ,'Dschungel des Südens'	,'Südmeer'	,'Kalifat', 'Länder der Tulamiden'	,'Aranien'	,'Maraskan'	,'Schattenlande'	,'Salamandersteine'	,'Svelltal'	,'Bornland'	,'Hoher Norden'	,'Mhanadistan'	,'Wüste Khom']
        comboBoxRegionen=ttk.Combobox(hauptFrame,values=auswahlRegionen,state="readonly")
        comboBoxRegionen.grid()  
        comboBoxRegionen.set('Mittelreich')
        
        
        def ButtonShow(event=None):
           
                
                
            
            for widget in alles.winfo_children():
                widget.destroy()
            Region=comboBoxRegionen.get()
            
            searchString= 'SELECT Name, Quelle FROM animals WHERE['  +Region+ ']=1 ORDER BY Name'
            
            conn = sqlite3.connect('odatastools.db')
            c = conn.cursor()
            c.execute(searchString)
            i=2
            
            ttk.Label(alles,text='Name',font='Arial 10 bold').grid(row=1,column=2,sticky='w')
            ttk.Label(alles,text='Quelle',font='Arial 10 bold').grid(row=1,column=3,sticky='w')
            for row in c:    
               
                ttk.Label(alles,text=row[0],font='Arial 10').grid(row=i,column=2,sticky='w')
                ttk.Label(alles,text=row[1],font='Arial 10').grid(row=i,column=3,sticky='w')
                i=i+1
        
        showButton = ttk.Button(hauptFrame, text="Anzeigen",command=ButtonShow,width=50)
        showButton.grid()
        
        mainMenu = ttk.Button(endButton, text="Zurück zum Hauptmenü",
                           command=lambda: master.switch_frame(StartPage),width=50)
        mainMenu.grid()

class PageContact(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        #label = ttk.Label(self, text="Fragen, Anregungen, Bugs?\n Per Mail bin ich unter ")
        #label.pack(side="top", fill="x", pady=10)
        kontakt=tk.Text(self,font='Arial')
        kontakt.pack()
        contactInformation = """
        Lieber User: Vielen Dank für dein Testen.
        Feedback, Wünsche und Bugs nehem ich gerne entgegen.
        Auf Reddit bin ich als User Odatas bekannt.
        Du kannst mir aber auch gern eine direkte Mail an odatas@posteo.eu schreiben.
        Danke für dein Input."""
        kontakt.insert("end",contactInformation)
        button = ttk.Button(self, text="Zurück zum Hauptmenü",
                           command=lambda: master.switch_frame(StartPage))
        button.pack()


if __name__ == "__main__":
    app = PTools()
    app.mainloop()