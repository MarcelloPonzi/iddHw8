import pandas as pd
import numpy 

#importa il dataset delle aziende in un dataframe
df = pd.read_csv("../MergedDS/ds_output-filtered.csv")

#estrai dal dataframe solo i nomi delle aziende
companies = df["name"].unique()
print(companies)

numpy.savetxt("../companies.csv", companies, fmt='%s', encoding="utf8", newline=",")