#!/usr/bin/env python

""" gamecards.py


"""

import csv
import argparse
from string import Template


def gamecards(input, template, output, styles='cards.css', rows=3, cols=3):

    # set up header and footer
    header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="generator" content="gamecards" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <title>Game Cards</title>
    %s
</head>
<body>
    <div id="cards">
"""

    footer = """
    </div>
</body>
</html>
"""

    # make stylesheet markup from styles parameter
    style_list = [ '<link rel="stylesheet" href="' + s + '">' for s in styles.split(',') ]

    header = header % ('\n').join(style_list)

    with open(template, 'r', encoding="utf8") as t:
        cell = t.read()

    output_file = open(output, "w", encoding="utf8")

    # process CSV file

    count = 1

    output_file.write(header)

    with open(input, "r", encoding="utf8") as c:
        reader = csv.DictReader(c)

        for line in reader:

            if count == 1:
                output_file.write('<table class="page">')

            if count % cols == 1:
                output_file.write('<tr>')

            output_file.write('<td>')

            output_file.write(str(Template(cell).safe_substitute(line)))

            output_file.write('</td>')

            if count % cols == 0:
                output_file.write('</tr>')

            if count == rows * cols:
                output_file.write('</table>')
                count = 0

            count = count + 1

        # ended last row early
        if (count - 1) % cols != 0:
            output_file.write('</tr>')

        if (count - 1) != rows * cols:
            output_file.write('</table>')

    output_file.write(footer)


### MAIN ###

__version__ = '0.1.0'

# execute if main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV file into game cards using a template")
    parser.add_argument("input", help="Input file (CSV)")
    parser.add_argument("template", help="Template file (HTML fragment)")
    parser.add_argument("output", help="Output file (HTML)")
    parser.add_argument("--css", default="cards.css", help="List of CSS style files (default: cards.css)", action="store")
    parser.add_argument("--rows", default="3", help="Rows per page (default: 3)", type=int, action="store")
    parser.add_argument("--cols", default="3", help="Columns per page (default: 3)", type=int, action="store")
    args = parser.parse_args()

    gamecards(args.input, args.template, args.output, styles=args.css, rows=args.rows, cols=args.cols)

