import csv
def main():
    filePath = "./word.csv"
    id_num = 1

    with open(filePath, encoding="utf8", newline="") as f:
        rows = csv.reader(f)
        for row in rows:
            print(id_num,*row)
            id_num=id_num+1
            
if __name__ == "__main__":
    main()