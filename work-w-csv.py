import csv
string_email = ''
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # next(csv_reader) # skip first row val.

    with open('tabbed_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
