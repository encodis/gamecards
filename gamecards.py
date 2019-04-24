#!/usr/bin/env python

""" gamecards.py


"""

import csv
import argparse
from string import Template
from itertools import zip_longest


def gamecards(source, template, styles, output, rows=3, cols=3):

    # make stylesheet markup from styles parameter
    style_list = '\n'.join([f'<link rel="stylesheet" href="{s}"/>' for s in styles.split(',')])

    # set up header and footer
    header = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="generator" content="gamecards" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <title>Game Cards</title>
    {style_list}
</head>
<body>
    <div id="cards">
"""

    footer = """
    </div>
</body>
</html>
"""

    # read template file
    with open(template, 'r', encoding="utf8") as template_file:
        cell_template = template_file.read()

    # process CSV file
    with open(output, "w", encoding="utf8") as output_file, open(source, "r", encoding="utf8") as csv_file:

        csv_reader = csv.DictReader(csv_file)
        output_file.write(header)

        while True:
            table_group = list(zip(range(rows * cols), csv_reader))

            if len(table_group) == 0:
                break

            output_file.write('<table class="page">')

            row_group = list(zip_longest(*(iter(table_group),) * rows))

            for row in row_group:
                output_file.write('<tr>')

                for cell in list(row):
                    if cell is not None:
                        output_file.write('<td>')
                        output_file.write(str(Template(cell_template).safe_substitute(cell[1])))
                        output_file.write('</td>')

                output_file.write('</tr>')

            output_file.write('</table>')

        output_file.write(footer)

# MAIN #


__version__ = '0.1.0'

# execute if main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV file or folder of Markdown files into game cards using a template")
    parser.add_argument("source", help="Source file (CSV) or folder ()")
    parser.add_argument("template", help="Template file (HTML fragment)")
    parser.add_argument("styles", help="List of CSS style files (relative to output file)", action="store")
    parser.add_argument("output", help="Output file (HTML)")
    parser.add_argument("--rows", default="3", help="Rows per page (default: 3)", type=int, action="store")
    parser.add_argument("--cols", default="3", help="Columns per page (default: 3)", type=int, action="store")
    args = parser.parse_args()

    gamecards(args.source, args.template, args.styles, args.output, rows=args.rows, cols=args.cols)
