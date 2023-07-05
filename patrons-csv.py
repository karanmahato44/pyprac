import csv

html = ''
names = []
with open('patrons.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # skip header and line below
    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        if line[0] == 'No Reward':
            break
        # print(f'{line[0]} {line[1]}')
        names.append(f'{line[0]} {line[1]}')


html += f'<p>There are currently {len(names)} contributers. Thank you!</p>'

html += '\n<ul>\n'

for name in names:
    html += f'\t<li>{name}</li>\n'

html += '<ul>\n'

with open('patrons.html', 'w') as html_file:
    html_file.write(html)
