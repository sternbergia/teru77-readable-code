import csv
word = "上手"

filename = "word.csv"
with open(filename, encoding="utf8", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(*row)