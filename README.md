# Introduction

A Python module to transform a CSV file into an HTML file containing a series of tables, each cell of which represents a gaming card. A template must be supplied that conforms to the Python string template format---this becomes the contents of each cell, with the CSV file filling in the placeholders.

## Usage

```
$ python -s game-cards.py cards.csv cards.tpl cards.html --css=cards.css
```

or if installed via Pip:

```
$ python -m game-cards cards.csv cards.tpl cards.html --css=cards.css
```

