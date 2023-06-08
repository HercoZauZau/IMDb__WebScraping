*Leia em outros idiomas: [English](https://github.com/HercoZauZau/IMDb__WebScraping/blob/main/README-en.md)*

# IMDb Top 100 Filmes - Web Scraping

Este é um programa Python que realiza web scraping no site IMDb para obter os 100 filmes com as maiores pontuações de todos os tempos. Ele extrai informações como posição, título, pontuação, ano e diretor de cada filme e armazena esses dados em um arquivo Excel.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Além disso, você precisará instalar as seguintes bibliotecas Python:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

Você pode instalar essas bibliotecas executando o seguinte comando no terminal:

```
pip install requests beautifulsoup4 pandas openpyxl
```

## Como usar

1. Clone este repositório ou faça o download do arquivo `imdb_scraping.py`.
2. Abra um terminal e navegue até o diretório em que o arquivo `imdb_scraping.py` está localizado.
3. Execute o seguinte comando para executar o programa:

```
python imdb_scraping.py
```

4. Aguarde até que o programa seja executado. Ele coletará os dados dos 100 filmes do IMDb com as maiores pontuações e salvará em um arquivo chamado `top_100_filmes_imdb.xlsx`.

## Resultados

O programa irá gerar um arquivo Excel com os seguintes campos para cada filme:

- Id: a posição do filme no ranking.
- Title: o título do filme.
- Rating: a pontuação do filme no IMDb.
- Year: o ano do filme.
- Director: o diretor do filme.

## Notas

- Este programa realiza web scraping no site IMDb (https://www.imdb.com). Verifique a política de uso do site antes de utilizá-lo.
- Este programa foi desenvolvido apenas para fins educacionais e de aprendizado. Use-o de forma responsável e respeite os termos de uso dos sites que você está coletando dados.
