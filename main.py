import csv
import argparse

def Parse():
    parser = argparse.ArgumentParser(description='辞書管理プログラム')
    parser.add_argument('filePath', type=str, help='単語データのファイルのパス')
    args = parser.parse_args()
    return args

def main():
    # 引数の設定
    args = Parse()

    filePath = args.filePath
    with open(filePath, encoding="utf8", newline="") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            print(*row)

if __name__ == '__main__':
    main()