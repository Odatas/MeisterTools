# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:35:00 2019

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
                           command=lambda: master.switch_frame(patrickstools2.StartPage))
        button.pack()


