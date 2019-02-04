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

import odatasfunctions as of
import patrickstools2

class StuffPage(ttk.Frame):
    def __init__(self, master):
         ttk.Frame.__init__(self, master)
         master.title("Verschiedene Tools")
         
         #Frames
         post=tk.LabelFrame(self,text="Postversand")
         post.grid(padx=10,pady=10,row=1,column=1)
         
         geldumrechner=tk.LabelFrame(self,text="Geldumrechner")
         geldumrechner.grid(padx=10,pady=10,row=2,column=1)
         
         
         
         def geldButton(event=None):
             try:                
                dukaten=int(dukatenEntry.get())
             except:
                dukaten=0
                messagebox.showerror("Dukaten","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                dukatenEntry.delete(0,'end')
                dukatenEntry.insert(0,"0")
                
             try:                
                silber=int(silberEntry.get())
             except:
                silber=0
                messagebox.showerror("Silber","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                silberEntry.delete(0,'end')
                silberEntry.insert(0,"0")  
             
             try:                
                heller=int(hellerEntry.get())
             except:
                heller=0
                messagebox.showerror("Heller","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                hellerEntry.delete(0,'end')
                hellerEntry.insert(0,"0")    
                
             try:                
                kreuzer=int(kreuzerEntry.get())
             except:
                kreuzer=0
                messagebox.showerror("Kreuzer","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                kreuzerEntry.delete(0,'end')
                kreuzerEntry.insert(0,"0") 
             
             
             
             gesamt=dukaten*1000+silber*100+heller*10+kreuzer
             geldAnzeige.config(text=of.Geldrechner(gesamt,'Silber','Kreuzer'))
            
            
         def postButton(event=None):             
             try:                
                postKutsche=int(postKutscheEntry.get())
             except:
                postKutsche=0
                messagebox.showerror("Postkutsche","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                postKutscheEntry.delete(0,'end')
                postKutscheEntry.insert(0,"0")
             try:                
                reiter=int(reiterEntry.get())
             except:
                reiter=0
                messagebox.showerror("ZPostkutsche","Falsche eingabe. Nur ganze Zahlen erlaubt. Wert wird auf 0 gesetz.")
                reiterEntry.delete(0,'end')
                reiterEntry.insert(0,"0")
             #Obacht bei der Berechnung. Hier wird Meilen in Kreuzer Gerechnet. 
             # Eine Meilen Einheit bei 1 Silber pro 100 Meilen wird deswegen /100*100 gerechnet
             #Das ergibt nach Adam Riesen 1
             postCost=postKutsche+reiter*12
             postCostLabel.config(text=of.Geldrechner(postCost,'Kreuzer','Kreuzer'))
                
                
             
         #Post: labels und Entrys und ein Button zum Berechnen 
         ttk.Label(post,text='Brief mit Postkutsche. Meilen:').grid(row=1,column=1)
         ttk.Label(post,text='Brief per Beilunk Reiter. Meilen:').grid(row=2,column=1)
         
         postKutscheEntry=ttk.Entry(post)
         postKutscheEntry.grid(row=1,column=2)
         postKutscheEntry.insert(0,"0")
         
         reiterEntry=ttk.Entry(post)
         reiterEntry.grid(row=2,column=2)
         reiterEntry     
       
         
         postCostLabel=ttk.Label(post,text='0 Dukaten 0 Silber 0 Heller 0 Kreuzer',font='Arial 10 bold')
         postCostLabel.grid(row=3,column=1,columnspan=2)
         
         postBerechnung=ttk.Button(post,text="Berechnen",command=postButton,width=50)
         postBerechnung.grid(row=4,column=1,columnspan=2)
         
         
         
         
         #Geldumrechner: labels und Entrys und ein Button zum Berechnen
         ttk.Label(geldumrechner,text="Dukaten").grid(row=1,column=1)
         ttk.Label(geldumrechner,text="Silber").grid(row=2,column=1)
         ttk.Label(geldumrechner,text="Heller").grid(row=3,column=1)
         ttk.Label(geldumrechner,text="Kreuzer").grid(row=4,column=1)
         
         dukatenEntry=ttk.Entry(geldumrechner)         
         silberEntry=ttk.Entry(geldumrechner)         
         hellerEntry=ttk.Entry(geldumrechner)         
         kreuzerEntry=ttk.Entry(geldumrechner)
         
         
         dukatenEntry.grid(row=1,column=2)
         silberEntry.grid(row=2,column=2)
         hellerEntry.grid(row=3,column=2)
         kreuzerEntry.grid(row=4,column=2)
         
         dukatenEntry.insert(0,"0")  
         silberEntry.insert(0,"0")  
         hellerEntry.insert(0,"0")  
         kreuzerEntry.insert(0,"0")  
         
         
         geldAnzeige=ttk.Label(geldumrechner,text='0 Dukaten 0 Silber 0 Heller 0 Kreuzer',font='Arial 10 bold')
         geldAnzeige.grid(row=5,column=1,columnspan=2)
         
         geldumrechnungButton=ttk.Button(geldumrechner,text="Berechnen",command=geldButton,width=50)
         geldumrechnungButton.grid(row=6,column=1,columnspan=2)
         
         
         
         
         
         
         #Exit Button
         mainMenu = ttk.Button(self, text="Zurück zum Hauptmenü",
                           command=lambda: master.switch_frame(patrickstools2.StartPage),width=50)
         mainMenu.grid(row=21,column=1,columnspan=2)