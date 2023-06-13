# moviebot
Telegram bot to search for films in Krakow cinemas.

## Project data flow

![Project diagram flow.](https://raw.githubusercontent.com/zaebee/moviebot/main/diagram.svg)
As datasource as suggest to use https://kino.krakow.pl/. We need to get movies and theatres from that and probably save into our DB (postgres, sqlite, or elastic).
As intent parser I suggest to use [dateparser](https://dateparser.readthedocs.io/en/latest/) and [spacy](https://spacy.io/usage/linguistic-features#named-entities).

## Installation

To set up a development environment, run:

```
poetry shell    # any time you want to run code or tests
poetry install  # install and update dependencies in your environment, the first time
```


## Run bot

```
python bot.py
```
