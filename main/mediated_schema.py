import pandas as pd
import os 
from pathlib import Path

############################
### FUNZIONI DI SUPPORTO ###
############################

# Restituisce un dataframe, qualunque sia il formato,
# aprendolo con la funzione corretta. 
def read_any(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension=='.csv':
        try: 
            df = pd.read_csv(file_path)
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='cp1252')
    elif file_extension=='.json':
        df = pd.read_json(file_path)
    elif file_extension=='.jsonl':
        df = pd.read_json(file_path, lines=True)
    elif file_extension=='.xls':
        df = pd.read_excel(file_path)
    return df

# Clona il dataset nel folderPath in una nuova directory,
# mettendo in lowercase tutte le colonne.
def put_all_columns_in_lowercase(folder_path):
    files = os.listdir(folder_path)
    print(files)
    for file in files:
        print(file)
        df = read_any(folder_path+file)
        df.columns = df.columns.str.lower()

        # Prendi file_name, che contiene tutto il path, e trasformalo
        # per ottenere solo il nome del file senza estensione
        file_name, file_extension = os.path.splitext(folder_path+file)
        file_name_without_extension = Path(file_name).stem
        print(file_name_without_extension)

        # Salva in csv dentro la directory specificata come parametro.
        # Se la directory non esiste, la crea.
        output_directory_path = "./DatasetHW8Lowercase/"
        is_exist = os.path.exists(output_directory_path)
        if not is_exist:
            os.makedirs(output_directory_path)
            print("Directory di output creata!")
        df.to_csv(output_directory_path+file_name_without_extension+".csv")

# Legge i dataset all'interno di una directory, specificata
# con il suo path, e restituisce un array di dataframe.
def dataset_to_dataframe_array(folder_path):
    df_array = []
    for file in os.listdir(folder_path):
        print("Appending "+file+" to the dataframe array")
        df_array.append(read_any(folder_path+file))
    return df_array 

#################################
### FINE FUNZIONI DI SUPPORTO ###
#################################

put_all_columns_in_lowercase('./DatasetHW8Formattato/')

df_array = dataset_to_dataframe_array('./DatasetHW8Lowercase/')
print(df_array)

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