import pandas as pd

from conexion import conexion

listas_urls = ['https://es.wikipedia.org/wiki/Jesse_Helms',
               'https://es.wikipedia.org/wiki/Charles_Bukowski',
               'https://es.wikipedia.org/wiki/Giovanni_Battista_Lombardi',
               'https://es.wikipedia.org/wiki/Igal_Al%C3%B3n',
               'https://es.wikipedia.org/wiki/Jorge_Montenegro_(escritor)']
listas_personas = []
for i in listas_urls:
    dict_values = {}

    soup = conexion(i, 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0')
    dict_values['Titulo'] = soup.title.string
    for z in soup.tbody.find_all('tr'):
        th = z.find('th')
        td = z.find('td')
        if th is not None and td is not None:

            if 'Nacimiento' in th.text:
                dict_values['Nacimiento'] = td.text.strip()

            elif 'Fallecimiento' in th.text:
                dict_values['Fallecimiento'] = td.text.strip()

            elif 'Causa de muerte' in th.text:
                dict_values['Causa de muerte'] = td.text.strip()

        else:
            print('No contiene el atributo td o th')
    listas_personas.append(dict_values)
df = pd.DataFrame(listas_personas)
df.to_csv('5_urls.csv', index=False)