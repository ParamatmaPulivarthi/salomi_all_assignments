# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:26:03 2026

@author: hp
"""

import pandas as pd

friends = pd.read_csv(r"C:\Users\hp\salomi\friend_names.csv file.txt")
print(friends)

family = pd.read_csv(r"C:\Users\hp\salomi\family_members.txt file.txt", delimiter="*")
print(family)

veg = pd.read_csv(r"C:\Users\hp\salomi\vegfood_items.txt file.txt", delimiter="|")
print(veg)

nonveg = pd.read_csv(r"C:\Users\hp\salomi\nonvegfood_items.txt file.txt", delimiter="|")
print(nonveg)

months = pd.read_csv(r"C:\Users\hp\salomi\month_names.txt file.txt", delimiter="&")
print(months)

colours = pd.read_csv(r"C:\Users\hp\salomi\colours_names.txt file.txt", delimiter="^")
print(colours)