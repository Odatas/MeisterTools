# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:54:19 2019

@author: NG7a8f3
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

from travel import PageTravel
from contact import PageContact
from dangers import PageDangers
     
class StartPage(ttk.Frame):

    def __init__(self, master):        
        
        #Theme für Programm wird gesetzt
        s=ttk.Style()
        s.theme_use('winnative')
        
        ttk.Frame.__init__(self, master)
        
        #Frames werden geöffnet.
        alles=ttk.Frame(self)
        alles.pack(padx=100)
        version=ttk.Frame(self)
        version.pack(anchor='e')
    
        #Ein paar Buttons               
        self.Name=ttk.Label(alles,text="Odatas Meistertools", font='Arial 18 bold')
        self.Name.pack(pady=30)
        
        self.Hilfe=ttk.Label(alles,text="Diese Alpha Version ist noch ziemlich kacke. Mal schauen ob es besser wird.\n Feedback an Odatas auf Reddit")
        self.Hilfe.pack(pady=20)
        
        self.button1 =ttk.Button(alles, text ="Reisehelfer",command=lambda: master.switch_frame(PageTravel),width=50) #command linked
        self.button1.pack()
                
        
        self.button2=ttk.Button(alles, text ="Monster und Wildtiere",command=lambda: master.switch_frame(PageDangers),width=50)
        self.button2.pack()
        
        self.button3=ttk.Button(alles, text ="Verschiedenes",width=50)
        self.button3.pack()
        
        self.button4=ttk.Button(alles, text ="Kontakt",command=lambda: master.switch_frame(PageContact),width=50)
        self.button4.pack()
        
       
        ttk.Button(alles, text="Quit", command=self.master.destroy,width=50).pack(pady=30)
        
        self.version=ttk.Label(version,text="Version Alpha 0.21")
        self.version.pack(anchor='se')