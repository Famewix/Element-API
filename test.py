import csv

def get_data(symbol):
    with open('table.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = {}
        column_names = []
        for row in csv_reader:
            if line_count == 0:
                for column_name in row:
                    column_names.append(column_name)
                line_count += 1
            else:
                if symbol == row[3]:
                    for index, column_name in enumerate(column_names):
                        data[column_name] = row[index]

    return data

data = get_data('Na')
print(data)