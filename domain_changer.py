# domain_changer

import csv
import pandas as pd
import numpy as np
import re

df = pd.read_csv('test.csv')

df = df.drop_duplicates(keep='first')

df['email'] = df.email.replace(r"^(?:http)s?://", "", regex=True)

df['email'] = df.email.replace(r"(/).*", "", regex=True)


# df = re.sub(r"(/).*", "", df)

def domain_it(df):
  return re.split('@', df)[-1]
  
def domain_type(df):
  return re.split('\.', df)[-1]
  
func = lambda x: 100*x.count()/df.shape[0]
  
# df['domain'] = df['email'].apply(domain_it)

df['domain_type'] = df['email'].apply(domain_type)

count = df.pivot_table(index=['domain_type'], aggfunc='count', margins=True)
count2 = pd.pivot_table(df, index=['domain_type'], aggfunc=func)

print(count)
print(count2)

# print(df)