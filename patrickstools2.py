# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:27:25 2019

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


# page classes import   
import travel 
import contact
import dangers 
import sonstiges
import randomenpc



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

class StartPage(ttk.Frame):

    def __init__(self, master):        
        
        #Theme für Programm wird gesetzt
        s=ttk.Style()
        s.theme_use('winnative')
        
        ttk.Frame.__init__(self, master)
        master.title("Hauptmenu")
        #Frames werden geöffnet.
        alles=ttk.Frame(self)
        alles.pack(padx=100)
        version=ttk.Frame(self)
        version.pack(anchor='e')
        #Ein paar Buttons               
        self.Name=ttk.Label(alles,text="Odatas Meistertools", font='Arial 18 bold')
        self.Name.pack(pady=30)
        
        self.Hilfe=ttk.Label(alles,text="Er haut die Alpha Versionen raus wie andere Leute die Fuffies in den Club")
        self.Hilfe.pack(pady=20)
        
        self.button1 =ttk.Button(alles, text ="Reisehelfer",command=lambda: master.switch_frame(travel.PageTravel),width=50) #command linked
        self.button1.pack()
                
        
        self.button2=ttk.Button(alles, text ="Monster und Wildtiere",command=lambda: master.switch_frame(dangers.PageDangers),width=50)
        self.button2.pack()
        
        #self.button5=ttk.Button(alles, text ="NPC Generator",command=lambda:master.switch_frame(randomenpc.PageRandomeNPC),width=50)
        #self.button5.pack()
        
        self.button5=ttk.Button(alles, text ="NPC Generator (In the works)",width=50)
        self.button5.pack()
        
        self.button3=ttk.Button(alles, text ="Verschiedenes",command=lambda: master.switch_frame(sonstiges.StuffPage),width=50)
        self.button3.pack()
        
        self.button4=ttk.Button(alles, text ="Kontakt",command=lambda: master.switch_frame(contact.PageContact),width=50)
        self.button4.pack()
        
       
        ttk.Button(alles, text="Quit", command=self.master.destroy,width=50).pack(pady=30)
        
        self.version=ttk.Label(version,text="Version Alpha 0.21")
        self.version.pack(anchor='se')

        

if __name__ == "__main__":
    app = PTools()
    app.mainloop()
        
