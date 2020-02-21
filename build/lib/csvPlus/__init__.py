import csv

def read(file, headers=False):
    """file: A open file in mode 'r'
    headers: Whether this CSV has headers or not.
    Do not use 'headers' if rows are not the same length."""
    reader = csv.reader(file)
    if headers:
        head = reader.__next__()
        data = []
        for i in reader:
            tmp = {}
            for j in range(len(i)):
                tmp[head[j]] = i[j]
            data.append(tmp)
    else:
        data = list(reader)
    return data

def write(file, data):
    """file: A open file in mode 'r'
    data: A list of rows, possibly including a header."""
    csvwriter = csv.writer(file)
    csvwriter.writerows(data)
