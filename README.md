# Introduction

A Python module to transform a CSV file into an HTML file containing a series of tables, each cell of which represents a gaming card. A template must be supplied that conforms to the Python string template format---this becomes the contents of each cell, with the CSV file filling in the placeholders.

## CSV file

The CSV file must start with a header line that describes the fields. For example:

```
ID,Title,Play,Icon,Level,Effect
1,Handy Rope,Your turn,,1,"Move yourself to any zone on the battlefield, then take your actions"
```

## Template file

This is an HTML fragment containing standard Python template strings. These template strings should match header fields in the CSV file, and are substituted into the template using the standard Python Template functionality. For example:

```
<div class='card'>
    <div class='title'>
        <p>${Title}</p>
    </div>
</div>
```

will create a set of tables, where each cell corresponds to an entry from the CSV file with the `${Title}` identifier replaced by the relevant

## CSS styling

default is cards.css. may want to add more e..g gameicons.css for games icons font. so this is optional arg 

final appearance depends entiorely on the CSS. recommend .card for each as above in template, do not put tabular stuff etc.

will need to set size of card (suggest in mm). have had good results with using flex/grid to arraneg divs inside cards using % of height etc , but may want some kind of explicit measurements in mm

## Output file

Base table structure , .page for paging


## Installation

```
$ pip install gamecards
```

## Usage

```
$ python -m game-cards cards.csv cards.tpl cards.html --css=cards.css
```

