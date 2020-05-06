from fuzzywuzzy import fuzz, process
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/rahulsharma/Desktop/internship/Mapped-sku-Sheet1.csv')

df.head()
fuzz.ratio(df['Distributor Item code'].str[-1:' '].all(), df['Company Dscription'].str[' ':' '].all())
df.dtypes
df = df.dropna()
df = df.astype(str)
l = df['Distributor Item code'].str.split(' ', n=2, expand=True)
df['DIC dimensions'] = l[2]
l = df['Company Dscription'].str.split(' ', n=2, expand=True)
df['CD dimensions'] = l[1]

df['CD dimensions'] = df['CD dimensions'].str.split('-',n=1, expand=True)

DIC = df['Distributor Item code'].str.split(' ', n=1, expand=True)

df['DIC name'] = DIC[0]

CD = df['Company Dscription'].str.split(' ', n=2, expand=True)
df['CD code'] = CD[0]

df['CD color'] = CD[2].str.split('-', n = 2, expand=True)

df = df.dropna()
choices = [df['Distributor Item code'].all(), df['Company Dscription'].all()]
process.extract(str(df['DIC dimensions'].all()), choices, limit=2)

choices1 = [df['Distributor Item code'].all(), df['Company Dscription'].all()]
process.extract(str(df['CD dimensions'].all()), choices1, limit=2)

choices2 = [df['Distributor Item code'].all(), df['Company Dscription'].all()]
process.extract(str(df['DIC name'].all()), choices2, limit=2)

choices3 = [df['Distributor Item code'].all(), df['Company Dscription'].all()]
process.extract(str(df['CD code'].all()), choices3, limit=2)

choices4 = [df['Distributor Item code'].all(), df['Company Dscription'].all()]
process.extract(str(df['CD color'].all()), choices4, limit=2)


"""
So, we can see that only the comparison between "Distribution Item code",
 "Company Dscription" and "DIC dimensions" gives us the appropriate result
  of 90 and 77 respectively.

Also the comparison between the "Distributor Item code", "Comparison Dscription"
 and "CD code" gives us the appropriate result of 90 and 18 respectively.
"""
