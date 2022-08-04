import csv

def main():

    filePath = './word.csv'
    
    with open(filePath, encoding="utf8", newline="") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            print(*row)

if __name__ == '__main__':
    main()