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
         post.grid(padx=10,pady=10)
         
         
         
         
         
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
                
                
             
             
         ttk.Label(post,text='Brief mit Postkutsche. Meilen:').grid(row=1,column=1)
         ttk.Label(post,text='Brief per Beilunk Reiter. Meilen:').grid(row=2,column=1)
         
         postKutscheEntry=ttk.Entry(post)
         postKutscheEntry.grid(row=1,column=2)
         postKutscheEntry.insert(0,"0")
         
         reiterEntry=ttk.Entry(post)
         reiterEntry.grid(row=2,column=2)
         reiterEntry.insert(0,"0")
         
       
         
         postCostLabel=ttk.Label(post,text='0 Dukaten 0 Silber 0 Heller 0 Kreuzer',font='Arial 10 bold')
         postCostLabel.grid(row=3,column=1,columnspan=2)
         
         postBerechnung=ttk.Button(post,text="Berechnen",command=postButton,width=50)
         postBerechnung.grid(row=4,column=1,columnspan=2)
         
         
         
         
         
         
         
         
         
         
         
         #Exit Button
         mainMenu = ttk.Button(self, text="Zurück zum Hauptmenü",
                           command=lambda: master.switch_frame(patrickstools2.StartPage),width=50)
         mainMenu.grid(row=21,column=1)