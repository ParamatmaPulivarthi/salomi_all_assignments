# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:40:51 2026

@author: hp
"""

import pandas as pd

# 1
friends = pd.read_excel(r"C:\Users\hp\salomi\friend_names.xls file.xlsx")
print("\nFriends:\n", friends)

# 2
family = pd.read_excel(r"C:\Users\hp\salomi\family_members.xls file.xlsx")
print("\nFamily:\n", family)

# 3
veg = pd.read_excel(r"C:\Users\hp\salomi\vegfood_items.xlsx file.xlsx")
print("\nVeg Food:\n", veg)

# 4
nonveg = pd.read_excel(r"C:\Users\hp\salomi\nonvegfood_items.xlsx file.xlsx")
print("\nNon-Veg Food:\n", nonveg)

# 5
months = pd.read_excel(r"C:\Users\hp\salomi\month_names.xlsx file.xlsx")
print("\nMonths:\n", months)

# 6
colours = pd.read_excel(r"C:\Users\hp\salomi\colours_names.xlsx file.xlsx")
print("\nColours:\n", colours)