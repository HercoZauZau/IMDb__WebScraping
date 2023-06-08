import requests
from bs4 import BeautifulSoup
import pandas as pd

# Faz a requisição HTTP para a página com os filmes do IMDB
url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)

# Faz o parsing do HTML da página usando o BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra a tabela com os filmes
table = soup.find('tbody', class_='lister-list')

# Encontra todas as linhas da tabela (filmes)
rows = table.find_all('tr')

# Cria listas para armazenar os dados
id = []
title = []
year = []
rating = []
director = []

# Itera pelas linhas para extrair as informações de cada filme
for row in rows[:100]:

    # Extrai as informações do filme
    title_column = row.find('td', class_='titleColumn')
    
    # id
    txt = title_column.text
    txt = txt.split()[0][:-1]
    id.append(txt)
    
    # título
    title.append(title_column.a.text)

    # ano
    year.append(title_column.span.text[1:-1])
    
    # pontuação
    rating_column = row.find('td', class_='ratingColumn')
    rating.append(rating_column.strong.text)

    # diretor
    director_column = row.find('td', class_='titleColumn').a['title']
    dirct = director_column.split('(dir.),')[0].strip()
    director.append(dirct)


# Cria um DataFrame com os dados
data = {'Id': id, 'Title': title, 'Year': year, 'Director': director, 'Rating': rating}
df = pd.DataFrame(data)

# Salva o DataFrame em um arquivo Excel
df.to_excel('top_100_filmes_imdb.xlsx', index=False)
