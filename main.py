import csv


def main():
    filePath = "./words.csv"
    input_name = input("名前を入力してください：")
    input_num = input("数字を入力してください：")
    with open(filePath, encoding="utf8", newline="") as f:
        print("ユーザ名:", input_name)
        words_road = csv.reader(f)
        if not input_num:
            for i, word in enumerate(words_road):
                print(f"{i+1}:", word[0], word[1])
        else:
            for i, word in enumerate(words_road):
                if i + 1 == int(input_num):
                    print(f"{i+1}:", word[0], word[1])
                    break


if __name__ == "__main__":
    main()
