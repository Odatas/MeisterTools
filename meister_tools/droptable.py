# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 23:33:14 2019

@author: Paddy
"""

import sqlite3

from . import path_db

conn = sqlite3.connect(str(path_db))
c = conn.cursor()
c.execute('''DROP TABLE ungeheuer ''')
print("Success")