# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:06:21 2019

@author: Paddy
"""

import sqlite3

from . import path_db

conn = sqlite3.connect(str(path_db))
c = conn.cursor()
c.execute('select * from bar')
row = cursor.fetchone()
names = row.keys()
