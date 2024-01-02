# Introduction

Lately it seems that cards have become a popular accessory in tabletop role playing games. These can be used to provide a physical representation of items, spells or other gaming elements. Most decks are produced using image editors like GIMP or Photoshop, which is fine if you have the time, the software and the skills to use it. 

Gamecards tries to automate this process. It takes a CSV file where each row represents an item, spell or other gaming element and each field in the row represents a property or attribute of that item, and converts it into a number of HTML pages. Each page contains a table, and each cell of the table contains a representation of the item, rendered according to a template file.

The resulting HTML file can then be printed and cut up to produce the cards themselves.
 
## Installation

```
$ pip install --upgrade gamecards
```

## Usage

The `gamecards` script simply takes four arguments (in this order): the CSV file containing the data, a template HTML file, a CSS specification (a file name, or comma separated list of file names) and the output HTML file name:

```
$ python -m gamecards cards.csv cards.tpl cards.css cards.html
```

Or use the console script:

```
$ gamecards cards.csv cards.tpl cards.css cards.html
```

The default is for each 'page' of the file to contain 3 rows and 3 columns. This can be changed using the `--rows` and `--cols` arguments:

```
$ gamecards cards.csv cards.tpl cards.css cards.html --rows 2 --cols 4
```

## CSV file

The CSV file must start with a header line that names each of the fields. These will be used in the template file. If a field contains a comma it must be enclosed in quotes. For example:

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

The styling for the output HTML can be controlled by including the names of CSS files. This becomes a standard "stylesheet" link in the output HTML's `<head>` element. For example, in the usage example above the `cards.css` style argument will become:

```
<link rel="stylesheet" href="cards.css"/>
```

in the output file.

The final appearance of the cards depends entirely on how you arrange the template and the corresponding CSS! It is recommended that each card be contained in a `<div>` element as in the example template above. Styling for this element should specify the card size, probably in 'mm' which will depend on the page size that the HTML will be printed on and the number of rows and columns. Theoretically any HTML constructs can be used but be aware of any browser limitations of *flexbox* and *grid* that might occur *when printing* (they may not show up when previewing in a browser).

## Output file

The output file conforms to the HTML5 specification and consists of a number of `<table>` elements each containing 3 rows with 3 columns (or whatever was specified using the `--rows` and `--cols` arguments). The entire body of the output document (i.e. the (only) child of `<body>`) is a `<div>` element with an ID of "gamecards". Each `<table>` element within this `<div>` has the 'page' class which is used to enforce pagination when printed - the following style is automatically included in the output file:

```
@media print {
 .page {
   page-break-after: always;
 }
}
```

This can be overridden by an included CSS file if required. It is generally assumed that all styling will be done within each cell, i.e. on the supplied template; the table structure simply provides a framework.

## Card backs

Use the `--backs` option to reverse the order of each row so that the backs of cards can be printed. The assumptions being made here are that (i) the backs are unique to each card and (ii) the sheet with the backs will be turned over and "glued" onto the back of the main sheet, i.e. they will be joined along the "long edge".

It is recommended that the same CSV file is used (so the order of the cards is the same) but that it contains the information for the back of the card. Different template and stying files will almost certainly be required.

## Development notes

### Unit testing

A small number of tests are included in the `test_gamecards.py` file and can be run using the [pytest](https://pypi.org/project/pytest/) application.

### Packaging a distribution

When ready for a release update the version number, e.g.

```
$ poetry version major
```

This will update the source file and the setup configuration. Then build the distribution:

```
$ poetry build
```

### Testing installation

Testing that the distribution installs correctly can be accomplished using Docker. Use the following command (which will download the "python" Docker image if necessary, so it might take a couple of minutes when first run):

```
$ docker run -it -v "$PWD":/mnt --entrypoint=bash python
```

This will start the "python" Docker image and execute a command prompt. From here install the "gamecards" distribution from the local "dist" folder (mounted in the Docker image under "/mnt"):

```
root@382a37174524:/# pip install gamecards --no-index --find-links /mnt/dist"
root@382a37174524:/# gamecards -h
root@382a37174524:/# python
>>> import gamecards
>>> exit()
```

### Upload to TestPyPi

Upload the distribution to the TestPyPi site:

```
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Then run the "python" Docker image and attempt to install from there:

```
$ docker run -it -v "$PWD":/mnt --entrypoint=bash python
root@382a37174524:/# pip install --index-url https://test.pypi.org/simple/ gamecards
root@382a37174524:/# gamecards -h
```

### Upload to PyPi

Upload to the real package index as follows (or specify the latest distribution):

```
$ twine upload dist/*
```
