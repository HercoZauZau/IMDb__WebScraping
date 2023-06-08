# IMDb Top 100 Movies - Web Scraping

This is a Python program that web scrapes the IMDb website to get the top 100 highest rated movies of all time. It extracts information such as position, title, score, year and director from each movie and stores this data in an Excel file.

## Prerequisites

Make sure you have Python installed on your system. Additionally, you will need to install the following Python libraries:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

You can install these libraries by running the following command in the terminal:

```
pip install requests beautifulsoup4 pandas openpyxl
```

## How to use

1. Clone this repository or download the `imdb_scraping.py` file.
2. Open a terminal and navigate to the directory where the `imdb_scraping.py` file is located.
3. Run the following command to run the program:

```
python imdb_scraping.py
```

4. Wait for the program to run. It will collect the data from the top 100 IMDb movies and save it in a file named `top_100_filmes_imdb.xlsx`.

## Results

The program will generate an Excel file with the following fields for each movie:

- Id: the position of the movie in the ranking.
- Title: the title of the movie.
- Rating: The movie's IMDb score.
- Year: the year of the movie.
- Director: the director of the movie.

## Note

- This program performs web scraping on the IMDb website (https://www.imdb.com). Check the website usage policy before using it.
- This program is designed for educational and learning purposes only. Please use it responsibly and respect the terms of use of the sites you are collecting data from.
