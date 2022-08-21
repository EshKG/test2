import pandas as pd
#from openpyxl import load_workbook
#import numpy as np
#import types



file_path = "ООО МКК Фастмани ру_2022_06_15.csv"


df = pd.read_csv(file_path,delimiter=";",decimal=",",na_filter=False)#,index_col=None)
cols = df.columns.to_list()
#df.columns = cols
cols[1] = "Мобильный"
cols.append("Название")
df['Название'] = df['Фамилия'] + " " + df['Имя'] + " " + df['Отчество']
cols.append("Часовой пояс")
df['Часовой пояс'] = "GMT+03:00"
df.columns = cols
#print(cols)
#df1 = df.copy()
#df.reset_index()


for i in range(len(df)):
    #Все номера найденные в строке добавляем в лист
    nomera = []
    if len(str(df['Контактное лицо 1 номер телефона'][i])) != 0:
        nomera.append(df['Контактное лицо 1 номер телефона'][i])
    if len(str(df['Контактное лицо 2 номер телефона'][i])) != 0:
         nomera.append(df['Контактное лицо 2 номер телефона'][i])
    if len(str(df['Контактное лицо 3 номер телефона'][i])) != 0:
         nomera.append((df['Контактное лицо 3 номер телефона'][i]))
    if len(str(df['Контактное лицо 4 номер телефона'][i])) != 0:
         nomera.append((df['Контактное лицо 4 номер телефона'][i]))
    #По длине листа понимаем сколько контактов
    if len(nomera) == 2:
        df.loc[df['Мобильный'].index == i, 'Мобильный'] = str(df['Мобильный'][i]) + "," + str(df['Контактное лицо 1 номер телефона'][i])+ "," + str(df['Контактное лицо 2 номер телефона'][i])
    elif len(nomera) == 1:
        df.loc[df['Мобильный'].index == i, 'Мобильный'] = str(df['Мобильный'][i]) + "," + str(df['Контактное лицо 1 номер телефона'][i])
    elif len(nomera) == 3:
        df.loc[df['Мобильный'].index == i, 'Мобильный'] = str(df['Мобильный'][i]) + "," + str(df['Контактное лицо 1 номер телефона'][i]) + "," + str(df['Контактное лицо 2 номер телефона'][i]) + "," + str(df['Контактное лицо 3 номер телефона'][i])
    elif len(nomera) == 4:
        df.loc[df['Мобильный'].index == i, 'Мобильный'] = str(df['Мобильный'][i]) + "," + str(
          df['Контактное лицо 1 номер телефона'][i]) + "," + str(df['Контактное лицо 2 номер телефона'][i]) + "," + str(df['Контактное лицо 3 номер телефона'][i]) + "," + str(df['Контактное лицо 4 номер телефона'][i])


df.to_excel("new.xlsx")
