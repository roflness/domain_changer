# domain_changer

import sys
import csv
import pandas as pd
import numpy as np
import re

df = pd.read_csv(sys.argv[1])

df = df.drop_duplicates(keep='first')

df['email'] = df.email.replace(r"^(?:http)s?://", "", regex=True) # Remove http/s from start of string
df['email'] = df.email.replace(r"^(?:www)\.?", "", regex=True) # Remove www. from start of string
df['email'] = df.email.replace(r"(/).*", "", regex=True) # Remove everything after first '/'

# df = re.sub(r"(/).*", "", df)

def domain_it(df):
  return re.split('@', df)[-1]
  
def domain_type(df):
  return re.split('\.', df)[-1]
  
func = lambda x: 100*x.count()/df.shape[0] # Used for calculating percentages for count2
  
# df['domain'] = df['email'].apply(domain_it)

df['domain_type'] = df['email'].apply(domain_type)

count = df.pivot_table(index=['domain_type'], aggfunc='count', margins=True)
count2 = pd.pivot_table(df, index=['domain_type'], aggfunc=func)

print(count)
print(count2)
df.columns = ["email", "domain"]
# print(df)

df.to_csv('output.csv', index=False, columns=["email"], header =True)
