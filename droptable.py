# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 23:33:14 2019

@author: Paddy
"""

import sqlite3

conn = sqlite3.connect('odatastools.db')
c = conn.cursor()
c.execute('''DROP TABLE ungeheuer ''')
print("Success")