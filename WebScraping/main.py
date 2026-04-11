import pandas as pd

from conexion import conexion

url = 'https://es.wikipedia.org/wiki/Jesse_Helms'
agente = "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0"
soup = conexion(url,agente)
print(soup.find('span', class_='mw-page-title-main').text)
info_dic = {'Titulo': soup.find('span', class_='mw-page-title-main').text}
print(soup.section.p['id'])
'''for i in soup.section.find_all('p'):
    print(i.text)
    info_dic['Columna'] = i.text

print(info_dic)
import pandas as pd
df = pd.DataFrame([info_dic])
print(df)
df.to_csv('papo.csv', index=False)'''
print(80*'--')
#print(soup.tbody.find_all('tr'))
dict_val = {'Titulo': soup.find('span', class_='mw-page-title-main').text}
for i in soup.tbody.find_all('tr'):
    th = i.find('th')
    td = i.find('td')
    if th is not None and td is not None:
        clave = th.text.strip()
        valor = td.text.strip()
        dict_val[clave] = valor
df = pd.DataFrame([dict_val])
#df.to_csv('final.csv', index=False)
