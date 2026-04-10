from bs4 import BeautifulSoup
import requests

url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#porting-code-to-bs4'
path = requests.get(url)
html_doc = path
soup = BeautifulSoup(html_doc.text, 'html.parser')

#print(soup.prettify())
print(80*'-')
#print(soup.h1.text)
print(soup.title.string)
print(80*'-')
print(soup.title.name)
print(80*'-')
print(soup.title.parent.name)
print(80*'-')
print(soup.p.parent.name)
print(80*'-')
print(soup.a['class'])
print(80*'-')
#print(soup.find_all('p'))
print(80*'-')
print(soup.find(id = 'id15'))
print(80*'-')
#for i in soup.find_all('a'):
    #print(i.get('href'))
print(80*'-')
#print(soup.get_text())
print(80*'-')
soup2 = BeautifulSoup('<b id="klk te duele"> class="boldest">Extremely bold</b>', 'html.parser')
tag = soup2.b
print(tag)
print(type(tag))
print(80*'-')
print(tag.name)
print(80*'-')
tag.name = 'mmg'
print(tag.name)
print(80*'-')
print(tag['id'])
print(80*'-')
print(tag.attrs)
print(tag.attrs.keys())
print(tag.attrs.values())
print(80*'-')
tag['id'] = 'Nine'
print(tag['id'])
print(80*'-')
tag['atributo-newman'] = 'veo goldon y ahi tan lo galletone'
print(tag['atributo-newman'])
print(tag['id'])
print(80*'-')
#del tag['id']
#del tag['atributo-newman']
print(tag)
print(tag.get('id'))

print(80*'-')
print(tag.attrs.pop('id', None))
print(tag)
print(80*'-')
print(soup.a['class'])
print(80*'-')
print(soup('span',attrs={'id': 'id15'}))
print(80*'-')
'''for i in soup.find_all('a'):
    print(i.get(''))'''
print(soup.find_all('a', attrs={'class': 'headerlink'}))
print(80*'-')
print(soup.find_all('a', class_='headerlink'))
soup3 = BeautifulSoup('<p class="mango"></p>', 'html.parser')
print(soup3.p['class'])
print(80*'-')
soup3 = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(soup3.p['class'])