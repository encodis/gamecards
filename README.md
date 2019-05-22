# Introduction

A Python module to transform a CSV file into an HTML file containing a series of tables, each cell of which represents a gaming card. A template must be supplied that conforms to the Python string template format---this becomes the contents of each cell, with the CSV file filling in the placeholders.

## Installation

```
$ pip install gamecards
```

## Usage

The `gamecards` script simply takes four arguments: the CSV file containing the data, a template HTML file, a CSS specification (a file name, or comma separated list of file names) and the output HTML file name:

```
$ python -m gamecards cards.csv cards.tpl cards.css cards.html
```

The default is for each 'page' of the file to contain 3 rows and 3 columns. This can be changed using the `--rows` and `--cols` arguments:

```
$ python -m gamecards cards.csv cards.tpl cards.css cards.html --rows 2 --cols 4
```

## CSV file

The CSV file must start with a header line that describes the fields. These will be used in the template file. If a field contains a comma it must be enclosed in quotes. For example:

```
ID,Field1,Field2
1,Some text,Some more text
2,Second row,"Text, with a comma"
```

## Template file

This is an HTML fragment containing standard Python template strings. These template strings should match header fields in the CSV file, and are substituted into the template using the Python string Template functionality. For example, the following template file:

```
<div class='card'>
    <div class='title'>
        <p>${Field1}</p>
    </div>
</div>
```

will be repeated for each line of the CSV file, once per table cell in the output file (see below). The template file must use the syntax `${Field1}` to specify the field names and they must be exact (so case is important).

## CSS styling

The styling for the output HTML can be controlled by including the names of CSS files. This becomes a standard "stylesheet" link in the output HTML's `<head>` element. For example, if the usage example above the `cards.css` style argument will become:

```
<link rel="stylesheet" href="cards.css"/>
```

in the output file.

The final appearance of the cards depends entirely on how you arrange the template and the corresponding CSS! It is recommended that each card be contained in a `<div>` element as in the example template above. Styling for this element should specify the card size, probably in 'mm' which will depend on the page size that the HTML will be printed on and the number of rows and columns. Theoretically any HTML constructs can be used but be aware of any browser limitations of *flexbox* and *grid* that might occur *when printing* (they may not show up when previewing in a browser).

## Output file

The output file conforms to the HTML5 specification and consists of a number of `<table>` elements each containing 3 rows with 3 columns (or whatever was specified using the `--rows` and `--cols` arguments). Each `<table>` has the 'page' class which is used to enforce pagination when printed, by the following style automatically included in the output file:

```
@media print {
 .page {
   page-break-after: always;
 }
}
```


entire body enclosed in div with id gamecards

This can be overridden by an included CSS file if required.

It is generally assumed that all styling will be done within each cell, i.e. on the supplied template; the table structure simply provides a framework.
