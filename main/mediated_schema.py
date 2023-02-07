import pandas as pd
import os 

# FUNZIONI DI SUPPORTO

def readAny(filePath):
    file_name, file_extension = os.path.splitext(filePath)
    if file_extension=='.csv':
        try: 
            df = pd.read_csv(filePath)
        except UnicodeDecodeError:
            df = pd.read_csv(filePath, encoding='cp1252')
    elif file_extension=='.json':
        df = pd.read_json(filePath)
    elif file_extension=='.jsonl':
        df = pd.read_json(filePath, lines=True)
    elif file_extension=='.xls':
        df = pd.read_excel(filePath)
    return df

def putAllColumnsInLowercase(folderPath):
    files = os.listdir(folderPath)
    print(files)
    for file in files:
        print('./DatasetHW8/'+file)
        df = readAny('./DatasetHW8/'+file)
        df.columns = df.columns.str.lower()
        df.to_csv("./DatasetHW8Lowercase/"+file)

#################################
### FINE FUNZIONI DI SUPPORTO ###
#################################

# putAllColumnsInLowercase('./DatasetHW8')

'''
path1 = './DatasetHW8/avengers-companiesmarketcap.jsonl'
path2 = './DatasetHW8/GioPonSpiz-companiesmarketcap.com.json'

df1 = readAny(path1)
df2 = readAny(path2)

print(df1)
print(df2)

# Unisci i DataFrames in base alle colonne "colonna_x" e "colonna_y"
df_merged = pd.merge(df1, df2, left_on='Name', right_on='name', how='outer')

print(df_merged)

# Salva i risultati in un file CSV
df_merged.to_csv("risultatiMergeTest.csv", index=False)
'''