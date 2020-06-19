#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:46:22 2020

@author: Automatus

Shows saved data from SQL Table
"""
import sqlite3

db = input("Database name?")
table = input("Table name?")

conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute("SELECT * from " + table)
result = cursor.fetchall()
for row in result:
    print(row)
print("One hour or more:")
cursor.execute("SELECT * from " + table + " WHERE MinutesWorked > 59")
result = cursor.fetchall()
for row in result:
    print(row)

conn.commit()
conn.close()
