import pandas as pd
import os

folder_path = 'C:\\Users\\NAA\\Desktop\\DAILY'

#list all the files the folder

files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

#Now read and concatenate the files
all_data = pd.DataFrame()

for file in files:
    df = pd.read_excel(os.path.join(folder_path, file))
    all_data = pd.concat([all_data,df], ignore_index=True)
#Now save the consolidated data
all_data.to_excel('C:\\Users\\NAA\\Desktop\\DAILY\\consolidate_data.xlsx')   