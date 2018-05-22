# Introduction

A Python module to transform a CSV file into an HTML file containing a series of tables, each cell of which represents a gaming card. A template must be supplied that conforms to the Python string template format---this becomes the contents of each cell, with the CSV file filling in the placeholders.

## Installation

```
$ pip install gamecards
```

## Usage

```
$ python -m gamecards cards.csv cards.tpl cards.html --css=cards.css
```

## CSV file

The CSV file must start with a header line that describes the fields. For example:

```
ID,Title,Play,Icon,Level,Effect
1,Handy Rope,Your turn,,1,"Move yourself to any zone on the battlefield, then take your actions"
```

## Template file

This is an HTML fragment containing standard Python template strings. These template strings should match header fields in the CSV file, and are substituted into the template using the standard Python string Template functionality. For example:

```
<div class='card'>
    <div class='title'>
        <p>${Title}</p>
    </div>
</div>
```

will create a set of tables, where each cell corresponds to an entry from the CSV file with the `${Title}` identifier replaced by the relevant field. Note that case is important.

## CSS styling

The styling for the output HTML is controlled by one or more CSS files. By default 'cards.css' is used, but this can be changed using the `--css` flag, which takes a comma separated list of CSS files, e.g. `--css=cards.css,game-icons.css`.

Note that the final appearance of the cards depends entirely on the CSS! It is recommended that each card be contained in a `<div>` element as in the example template above. This element should specify the card size, probably in 'mm'. I have had good results using *flexbox* and *grid* styling for the contents of the "card" `<div>` but you may want to use some absolute positioning within it.

## Output file

The output file is HTML5. Each page is an HTML table with 3 rows and 3 columns (by default, change these with the `--rows` and `--cols` flags). Each `<table>` has the 'page' class which can be used to enforce pagination when printed, e.g.:

```
@media print {
 .page {
   page-break-after: always;
 }
}
```


