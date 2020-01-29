import pandas as pd
import numpy as np
import os


# print(os.getcwd())
# print(pd)
df = pd.read_csv('student.txt')

df.columns=[column.replace("<", "") for column in df.columns] 
df.columns=[column.replace(">", "") for column in df.columns] 
print(df)
student1=df.query('Rollno==101',inplace=False)
# print(df.describe())
print(student1)
student2=df.query('Rollno==102',inplace=False)
# print(df.describe())
print(student2,student2.shape)
print(student2.iloc[[0],[3]])