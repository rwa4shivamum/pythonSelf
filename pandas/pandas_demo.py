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

# Series from a dictionary (keys become index)
population = pd.Series({'Ahmedabad': 8_000_000, 'Mumbai': 20_000_000, 'Delhi': 19_000_000})
print(population)

#Data Frame
data = {
    'Name': ['Shivam', 'Kajal', 'Aman'],
    'Age': [24, 22, 26],
    'City': ['Ahmedabad', 'Mumbai', 'Delhi']
}
# Name  Age       City
# 0  Shivam   24  Ahmedabad
# 1   Kajal   22     Mumbai
# 2    Aman   26      Delhi
df = pd.DataFrame(data)
print(type(df['Name']))   # <class 'pandas.core.series.Series'>
print(df)



#3.1 Ways to Create Data Frame
# From a dictionary of lists (most common)
df1 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [55000, 500, 1200],
    'Stock': [10, 150, 80]
})

# From a list of dictionaries (row-wise)
df2 = pd.DataFrame([
    {'Name': 'A', 'Score': 90},
    {'Name': 'B', 'Score': 85}
])

# From a NumPy array
df3 = pd.DataFrame(np.random.randint(1, 100, (4, 3)), columns=['A', 'B', 'C'])

# From a CSV file (most common in real projects)
df4 = pd.read_csv('data.csv')

# From Excel
df5 = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# From a SQL query (needs a DB connection object `conn`)
# df6 = pd.read_sql('SELECT * FROM users', conn)



#3.2

s = pd.Series([12, 45, 7, 23, 56, 89, 3])

s.head(3)      # first 3 elements
s.tail(2)      # last 2 elements
s.sort_values()          # sort by value
s.sort_index()           # sort by index
s.unique()                # array of unique values
s.value_counts()          # frequency of each value
s.isin([7, 23])           # boolean mask for membership


#3.3
df = pd.DataFrame({
    'Name': ['Shivam', 'Kajal', 'Aman', 'Riya', 'Neha'],
    'Age': [24, 22, 26, np.nan, 29],
    'Department': ['Dev', 'HR', 'Dev', 'Sales', 'HR'],
    'Salary': [45000, 30000, 52000, 28000, 31000]
})

df.head()          # first 5 rows (default)
df.tail(2)          # last 2 rows
df.shape            # (rows, cols)
df.info()           # column names, non-null counts, dtypes, memory usage
df.describe()       # summary statistics for numeric columns
df.columns           # list of column names
df.dtypes            # dtype of each column
df.index              # row index range
df.nunique()          # unique value count per column
df.isnull().sum()     # missing values per column
df.sample(2)           # random sample of rows

df['Name']              # single column -> Series
df[['Name', 'Age']]     # multiple columns -> DataFrame

df.loc[0]                # row by label
df.iloc[0]                # row by position
df.loc[0:2, 'Name':'Age']  # slice by label (inclusive)
df.iloc[0:2, 0:2]           # slice by position (exclusive of end)

df[df['Age'] > 24]           # boolean filtering
df[(df['Age'] > 22) & (df['Department'] == 'Dev')]   # multiple conditions


#4.OPeration on Data Frames
#4.1 Adding / modifying / dropping columns
df['Bonus'] = df['Salary'] * 0.10                     # new column from existing one
df['Total'] = df['Salary'] + df['Bonus']                # arithmetic across columns
df['Senior'] = df['Age'] > 25                            # boolean column

df.rename(columns={'Salary': 'Base_Salary'}, inplace=True)  # rename column
df.drop('Bonus', axis=1, inplace=True)                       # drop a column
df.drop(0, axis=0)                                              # drop a row (by index)

#4.2 Applying on function
df['Age_in_5yrs'] = df['Age'].apply(lambda x: x + 5)

def salary_band(sal):
    if sal < 30000: return 'Low'
    elif sal < 50000: return 'Mid'
    else: return 'High'

df['Band'] = df['Base_Salary'].apply(salary_band)

# applymap-style operation on entire numeric DataFrame (elementwise)
numeric_df = df[['Age', 'Base_Salary']]
numeric_df.map(lambda x: x)   # (pandas 2.1+: DataFrame.map replaces applymap)


#4.3 Sorting
df.sort_values('Base_Salary')                       # ascending
df.sort_values('Base_Salary', ascending=False)        # descending
df.sort_values(['Department', 'Base_Salary'])          # multi-column sort