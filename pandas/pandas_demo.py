import pandas as pd
import numpy as np

# Pandas is Python's core library for working with structured/tabular data (think: Excel sheets, SQL tables, CSV files) — but with the power of Python behind it.

# Why Pandas?
# Handles data of any size (rows × columns) efficiently, built on top of NumPy.
# Reads/writes almost any format: CSV, Excel, JSON, SQL, Parquet, etc.
# Built-in tools for cleaning, filtering, grouping, merging, and analyzing data.
# Industry standard — used in every data science/ML pipeline.


#Core Idea:- 
# Pandas gives you two main data structures:

# Structure	Dimensions	    Analogy
# Series	1D	          A single column / a labeled list
# DataFrame	2D	          A full table (rows + columns)

#2.1 Series - 1D labelled Array
s = pd.Series([10, 20, 30, 40])
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

print(s)                  
marks = pd.Series([80,90,95], index=['Math', 'Science', 'English'])
print(marks)
# Math       80
# Science    90
# English    95
# dtype: int64
print(marks['Science']) #Access by label
print(marks.iloc[1]) #Access by position

population = pd.Series({'Ahemdabad': 8_00_000, 'Mumbai':'20_000_000'})