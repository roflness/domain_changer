# domain_changer (testing on second computer, now on first computer)

import sys
import csv
import pandas as pd
import numpy as np
import re


if len(sys.argv) > 2:
    filename = sys.argv[1]
    output_file = sys.argv[2]
else:
    print("Error: %s needs to include name of csv file" % (sys.argv[0],))
    sys.exit()

df = pd.read_csv(filename)

df = df.drop_duplicates(keep='first')
df = df.apply(lambda x: x.astype(str).str.lower())

df = df[df["email"].str.contains('\.') == True]

df['email'] = df.email.replace(r"^(?:http)s?://", "", regex=True) # Remove http/s from start of string
df['email'] = df.email.replace(r"^(?:www)\.?", "", regex=True) # Remove www. from start of string
df['email'] = df.email.replace(r"^@", "", regex=True) # Remove @ symbol
df['email'] = df.email.replace(r"(/).*", "", regex=True) # Remove everything after first '/'
df = df.drop_duplicates(keep='first') # Delete duplicates again
# df = re.sub(r"(/).*", "", df)

def domain_it(df):
  return re.split('@', df)[-1]

def domain_type(df):
  return re.split('\.', df)[-1]

func = lambda x: 100*x.count()/df.shape[0] # Used for calculating percentages for count2

# df['domain'] = df['email'].apply(domain_it)

df['domain_type'] = df['email'].apply(domain_type)

count = df.pivot_table(index=['domain_type'], aggfunc='count', margins=True)
count2 = pd.pivot_table(df, index=['domain_type'], aggfunc=func).sort_values(by=['email'], ascending=False)

print(count)
print(count2)
# df.columns = ["email", "domain"]
# print(df)

df.to_csv(output_file+'.csv', index=False, columns=["email"], header =True)

count2.to_csv('percentage.csv', index=True, columns=["email"], header=["percentage"])
#print(df)