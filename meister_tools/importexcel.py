# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 21:22:23 2019

@author: Paddy
"""

import os
import sqlite3
from win32com.client import constants, Dispatch

from . import path_db

try:
    
    #----------------------------------------
    # get data from excel file
    #----------------------------------------
    XLS_FILE = os.getcwd() + "\\ungeheuer.xlsx"
    ROW_SPAN = (2, 61)
    COL_SPAN = (1, 24)
    app = Dispatch("Excel.Application")
    app.Visible = True
    ws = app.Workbooks.Open(XLS_FILE).Sheets(1)
    exceldata = [[ws.Cells(row, col).Value 
                  for col in range(COL_SPAN[0], COL_SPAN[1])] 
                 for row in range(ROW_SPAN[0], ROW_SPAN[1])]
    
    #----------------------------------------
    # create SQL table and fill it with data
    #----------------------------------------
    conn = sqlite3.connect(str(path_db))
    c = conn.cursor()
    c.execute('''CREATE TABLE ungeheuer (
       Name TEXT,
       Mittelreich INTEGER,
       Orkland INTEGER,
       Thorwal	INTEGER,
       Nostria	INTEGER,
       Andergast INTEGER,
       Horasreich INTEGER,
       Zyklopeninseln	INTEGER,
       Alanfa	INTEGER,
       'Dschungel des Südens'	INTEGER,
       Südmeer	INTEGER,
       Kalifat	INTEGER,
       'Länder der Tulamiden'	INTEGER,
       Aranien	INTEGER,
       Maraskan	INTEGER,
       Schattenlande	INTEGER,
       Salamandersteine	INTEGER,
       Svelltal	INTEGER,
       Bornland	INTEGER,
       'Hoher Norden'	INTEGER,
       Mhanadistan	INTEGER,
       'Wüste Khom'	INTEGER,
       Quelle TEXT
    )''')
    for row in exceldata:
        c.execute('INSERT INTO ungeheuer VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
    conn.commit()
    
    #----------------------------------------
    # display SQL data
    #----------------------------------------
    c.execute('SELECT * FROM ungeheuer')
    for row in c:
        print (row)
        
    #c.execute('''DROP TABLE animals ''')
except Exception as e:
    print(e)
    #c.execute('''DROP TABLE animals ''')
    
