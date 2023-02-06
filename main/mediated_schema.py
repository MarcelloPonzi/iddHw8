import pandas as pd

df1 = pd.read_csv("Resource/forbes.csv")
df2 = pd.read_json("Resource/forbes.com.json")

# Unisci i DataFrames in base alle colonne "colonna_x" e "colonna_y"
df_merged = pd.merge(df1, df2, on=["industry", "revenue", "name"])

# Salva i risultati in un file CSV
df_merged.to_csv("risultati.csv", index=False)