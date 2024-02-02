# Web Scraping Top 250 Filmy na IMDB a Top 100 Filmy na CSFD

Tento projekt je jednoduchý skript napsaný v jazyce Python, který provádí web scraping na stránkách IMDB (Internet Movie Database) a CSFD (Česko-Slovenská filmová databáze), aby získal informace o nejlépe hodnocených filmech. Skript stáhne seznamy nejlepších 250 filmů na IMDB a 100 filmů na CSFD a zpracuje je pro další analýzu nebo zobrazení.
Data mohou být ukládány do různých datasetů zde byl vybrán nejjednoduší a to csv file.

!TODO nastavit scrapování na každých 10-15 min / uložení do postreSQL database

## Obsah

- `IMDB2.py`: Hlavní skript pro web scraping na IMDB.
- `movies_data.csv`: Soubor CSV obsahující informace o top 250 filmech na IMDB.
- `CSFD2.py`: Hlavní skript pro web scraping na CSFD.
- `filmy_data.csv`: Soubor CSV obsahující informace o top 100 filmech na CSFD.

python IMDB2.py

python CSFD2.py
