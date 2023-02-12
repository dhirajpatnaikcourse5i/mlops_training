import boto3
import pandas as pd
import matplotlib.pyplot as plt

client=boto3.client('s3')

## path of s3 bucket expenses.csv needs to be added
## https://course5i-sandbox-bucket.s3.ap-south-1.amazonaws.com/pod3-artifacts/expenses.csv
path="expenses.csv"

df=pd.read_csv(path)
# print(df.head())

#print(df.info())

## EDA
df.smoker.replace(('yes','no'),(1,0),inplace=True)
df.sex.replace(('male','female'),(1,0),inplace=True)
df['region'] = [0 if i == "southwest" else 
                1 if i == "southeast" else
                2 if i == "northwest" else
                3 for i in df['region']]

#print(df.head(),df.info())

print(df.describe().T)

df.to_csv('insurance_course5i.csv',mode='w',index=False)