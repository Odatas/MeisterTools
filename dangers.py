# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:00:29 2019

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

import patrickstools2
from tkinter import messagebox


from urllib.request import pathname2url



class PageDangers(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)  
        master.title("Gefahren der Regionen")
        
        
        try:
            dburi = 'file:{}?mode=rw'.format(pathname2url('odatastools.db'))
            conn = sqlite3.connect(dburi, uri=True)
        except sqlite3.OperationalError:
            messagebox.showerror("ERROR","Die Datenbank konnte nicht gefunden werden. Stelle sicher dass sich die Datei odatastools im gleichen Ordner wie Das Hauptprogramm befindet.")
        
        
        #conn = sqlite3.connect('odatastools.db')
        
        hauptFrame=ttk.Frame(self)
        hauptFrame.pack(padx=500)
        
        
        alles=ttk.LabelFrame(self,labelwidget=ttk.Frame(relief='flat'))
        alles.pack(pady=20)
        
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
            ungeheuerString= 'SELECT Name, Quelle FROM ungeheuer WHERE['  +Region+ ']=1 ORDER BY Name'
            
            
            
            c = conn.cursor()
            c.execute(searchString)
            i=3
            
            ttk.Label(alles,text='Wildtier',font='Arial 10 bold').grid(row=1,column=2)
            ttk.Label(alles,text='Quelle',font='Arial 10 bold').grid(row=1,column=4)
            
            ttk.Separator(alles).grid(row=2,columnspan=100,sticky='ew')
            ttk.Separator(alles,orient='vertical').grid(column=5,rowspan=100,sticky='ns')
            for row in c:    
               
                ttk.Label(alles,text=row[0],font='Arial 10').grid(row=i,column=2,sticky='w')
                ttk.Label(alles,text=row[1],font='Arial 10').grid(row=i,column=4,sticky='w')
                i=i+1
                
            i=3
            d=conn.cursor()
            d.execute(ungeheuerString)
            ttk.Label(alles,text='Ungeheuer',font='Arial 10 bold').grid(row=1,column=6)
            ttk.Label(alles,text='Quelle',font='Arial 10 bold').grid(row=1,column=7)
            for row in d:    
               
                ttk.Label(alles,text=row[0],font='Arial 10').grid(row=i,column=6,sticky='w')
                ttk.Label(alles,text=row[1],font='Arial 10').grid(row=i,column=7,sticky='w')
                i=i+1
        
        ButtonShow()
        comboBoxRegionen.bind("<<ComboboxSelected>>", ButtonShow) 
        #showButton = ttk.Button(hauptFrame, text="Anzeigen",command=ButtonShow,width=50)
        #showButton.grid()
        
        mainMenu = ttk.Button(endButton, text="Zurück zum Hauptmenü",
                           command=lambda: master.switch_frame(patrickstools2.StartPage),width=50)
        mainMenu.grid()

