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
import webbrowser

class PageContact(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Kontaktinfomrationen")
        #label = ttk.Label(self, text="Fragen, Anregungen, Bugs?\n Per Mail bin ich unter ")
        #label.pack(side="top", fill="x", pady=10)
        mainFrame=ttk.Frame(self)
        mainFrame.pack(padx=50,pady=50)
        
        
        contactInformation = """
        Hallo!\n
        Willkommen in meiner kleinen App.\n
        Ich bin Patrick, 29 Jahre jung, Ingenieur aus Hamburg und leidenschaftlicher DSA Spieler.\n
        Eines Tages dachte ich mir: "Patrick, Reisen sind zu langweilig. Programmier dochmal was".\n
        Es vergingen nochmal 2 Jahre bis ich dann am 14.01.2019 größe Töne spuckend den ersten Faden im Reddit DSA Unterlases machte.
        Eine Woche später gab es die erste Alpha dieses Tools.\n
        Da ich alles in meiner Freizeit entwickle kann es schonmal etwas länger dauern bis was passiert. Danke für dein Verstädniss.\n\n
        Wenn du Ideen hast, Bugs findest oder einfach so mal hallo sagen willst findest du unten ein paar Kontaktmöglichkeiten\n
        Frei nach dem Motto: "Erwarte nichts". """
        kontaktText=ttk.Label(mainFrame,text=contactInformation)
        kontaktText.pack()
        
        
        button = ttk.Button(mainFrame, text="Finde mich auf Reddit",
                           command=lambda: webbrowser.open_new(r"https://www.reddit.com/user/odatas"), width=50)
        button.pack(pady=10)
        
        button = ttk.Button(mainFrame, text="Schreib mir eine Mail",
                           command=lambda: webbrowser.open('mailto:odatas@posteo.eu', new=1), width=50)
        button.pack(pady=10)
        
        button = ttk.Button(mainFrame, text="Join meinen Discord",
                           command=lambda: webbrowser.open('https://discord.gg/VFjp58y', new=1), width=50)
        button.pack(pady=10)
        
        
        button = ttk.Button(mainFrame, text="Zurück zum Hauptmenü",
                           command=lambda: master.switch_frame(patrickstools2.StartPage),width=50)
        button.pack(pady=30)
        
        


