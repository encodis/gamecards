import os

from gamecards import gamecards


def test_gamecards(tmpdir):

    csv_file = tmpdir.join('cards.csv')
    csv_file.write(f'''ID,Field1
1,Field 1 text line 1
2,Field 1 text line 2
3,Field 1 text line 3
4,Field 1 text line 4
5,Field 1 text line 5
''')

    tpl_file = tmpdir.join('cards.tpl')
    tpl_file.write('''<div class='card'>
        <div class='field1'>
            <p>${Field1}</p>
        </div>
        <div class='id1'>
            <p>${ID}</p>
        </div>
    </div>
''')

    out_file = tmpdir.join('cards.html')

    gamecards(csv_file, tpl_file, 'cards.css', out_file, rows=2, cols=2)

    # assert correct output files exist
    assert os.path.exists(out_file)

    # assert contents of page_one.md have a link to page_two.md
    expect = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="generator" content="gamecards" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <title>Game Cards</title>
    <link rel="stylesheet" href="cards.css"/>
</head>
<body>
    <div id="cards">
<table class="page"><tr><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text line 1</p>
        </div>
        <div class='id1'>
            <p>1</p>
        </div>
    </div>
</td><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text line 2</p>
        </div>
        <div class='id1'>
            <p>2</p>
        </div>
    </div>
</td></tr><tr><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text line 3</p>
        </div>
        <div class='id1'>
            <p>3</p>
        </div>
    </div>
</td><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text line 4</p>
        </div>
        <div class='id1'>
            <p>4</p>
        </div>
    </div>
</td></tr></table><table class="page"><tr><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text line 5</p>
        </div>
        <div class='id1'>
            <p>5</p>
        </div>
    </div>
</td></tr></table>
    </div>
</body>
</html>
'''

    with open(out_file, 'r', encoding='utf8') as fh:
        actual = fh.read()

    assert expect == actual


def test_gamecards_single(tmpdir):

    csv_file = tmpdir.join('cards.csv')
    csv_file.write(f'''ID,Field1,Field2
1,Field 1 text,"Field 2, with comma"
''')

    tpl_file = tmpdir.join('cards.tpl')
    tpl_file.write('''<div class='card'>
        <div class='field1'>
            <p>${Field1}</p>
        </div>
        <div class='field2'>
            <p>${Field2}</p>
        </div>
        <div class='id1'>
            <p>${ID}</p>
        </div>
    </div>
''')

    out_file = tmpdir.join('cards.html')

    gamecards(csv_file, tpl_file, 'cards.css', out_file)

    # assert correct output files exist
    assert os.path.exists(out_file)

    # assert contents of page_one.md have a link to page_two.md
    expect = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="generator" content="gamecards" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <title>Game Cards</title>
    <link rel="stylesheet" href="cards.css"/>
</head>
<body>
    <div id="cards">
<table class="page"><tr><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text</p>
        </div>
        <div class='field2'>
            <p>Field 2, with comma</p>
        </div>
        <div class='id1'>
            <p>1</p>
        </div>
    </div>
</td></tr></table>
    </div>
</body>
</html>
'''

    with open(out_file, 'r', encoding='utf8') as fh:
        actual = fh.read()

    assert expect == actual


def test_gamecards_multiple_styles(tmpdir):

    csv_file = tmpdir.join('cards.csv')
    csv_file.write(f'''ID,Field1,Field2
1,Field 1 text,"Field 2, with comma"
''')

    tpl_file = tmpdir.join('cards.tpl')
    tpl_file.write('''<div class='card'>
        <div class='field1'>
            <p>${Field1}</p>
        </div>
        <div class='field2'>
            <p>${Field2}</p>
        </div>
        <div class='id1'>
            <p>${ID}</p>
        </div>
    </div>
''')

    out_file = tmpdir.join('cards.html')

    gamecards(csv_file, tpl_file, 'cards1.css,cards2.css', out_file)

    # assert correct output files exist
    assert os.path.exists(out_file)

    # assert contents of page_one.md have a link to page_two.md
    expect = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="generator" content="gamecards" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <title>Game Cards</title>
    <link rel="stylesheet" href="cards1.css"/>
<link rel="stylesheet" href="cards2.css"/>
</head>
<body>
    <div id="cards">
<table class="page"><tr><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text</p>
        </div>
        <div class='field2'>
            <p>Field 2, with comma</p>
        </div>
        <div class='id1'>
            <p>1</p>
        </div>
    </div>
</td></tr></table>
    </div>
</body>
</html>
'''

    with open(out_file, 'r', encoding='utf8') as fh:
        actual = fh.read()

    assert expect == actual


def test_gamecards_no_styles(tmpdir):

    csv_file = tmpdir.join('cards.csv')
    csv_file.write(f'''ID,Field1,Field2
1,Field 1 text,"Field 2, with comma"
''')

    tpl_file = tmpdir.join('cards.tpl')
    tpl_file.write('''<div class='card'>
        <div class='field1'>
            <p>${Field1}</p>
        </div>
        <div class='field2'>
            <p>${Field2}</p>
        </div>
        <div class='id1'>
            <p>${ID}</p>
        </div>
    </div>
''')

    out_file = tmpdir.join('cards.html')

    gamecards(csv_file, tpl_file, '', out_file)

    # assert correct output files exist
    assert os.path.exists(out_file)

    # assert contents of page_one.md have a link to page_two.md
    expect = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="generator" content="gamecards" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
    <title>Game Cards</title>
    
</head>
<body>
    <div id="cards">
<table class="page"><tr><td><div class='card'>
        <div class='field1'>
            <p>Field 1 text</p>
        </div>
        <div class='field2'>
            <p>Field 2, with comma</p>
        </div>
        <div class='id1'>
            <p>1</p>
        </div>
    </div>
</td></tr></table>
    </div>
</body>
</html>
'''

    with open(out_file, 'r', encoding='utf8') as fh:
        actual = fh.read()

    assert expect == actual