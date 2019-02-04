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
     
import patrickstools2

import random

class PageRandomeNPC(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        
        
        mainFrame=ttk.Frame(self)
        mainFrame.grid(padx=50,pady=50)
        
        def generateNew(event=None):
            
            #Todo Rasse
            rasseString="Mensch"
            rand=random.randint(0,100)
            if rand>30:
                rasseString="Mensch"
            else:
                if rand>20:
                    rasseString="Zwerg"
                else:
                    if rand>10:
                        rasseString="Elbe"
                        
            #Todo Geschlecht
            geschlechtString="Männlich"
            rand=random.randint(0,100)
            if rand>20:
                geschlechtString="Männlich"
            else:
                geschlechtString="Weiblich"
                
            #Todo Alter
            alterString="20"
            if rasseString=="Mensch":
                alterString=str(random.randint(10,40))
            if rasseString=="Zwerg":
                alterString=str(random.randint(50,400))
            if rasseString=="Elbe":
                alterString=str(random.randint(100,3000))
                
            #Todo LeP
            lepString="20"
            #Todo Amor
            armorString="Leder"
            #Todo ATK
            atkString="10"
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
            
            
            
            
            
        abstandy=5
        
        #labels        
        ttk.Label(mainFrame,text="Rasse").grid(row=2,column=1,pady=abstandy,sticky='w')
        ttk.Label(mainFrame,text="Geschlecht").grid(row=4,column=1,pady=abstandy,sticky='w')
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
        
        rasseLabel=ttk.Label(mainFrame,text="")
        rasseLabel.grid(row=2,column=2)
        geschlechtLabel=ttk.Label(mainFrame,text="")
        geschlechtLabel.grid(row=4,column=2)
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
        
        randomizeButton=ttk.Button(mainFrame,text="Werte Generieren",command=generateNew,width=50)
        randomizeButton.grid(row=30,column=1,columnspan=2)
        
        