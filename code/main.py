def record():
    word = input("Save WORD: ")
    paraphrase = input("Paraphrase: ")

    with open("words.txt", mode="at", encoding="utf-8") as f:
        f.write(f"{word} {paraphrase}\n")

def print_words():
    print()
    with open("words.txt", mode="rt", encoding="utf-8") as f:
        data = f.read()
        print(data)

# 程序入口
while True:
    select=input("Please select mode:\n---r(record)\n---p(print)\n---e(exit)\n: ")
    if select=='record' or select=='r':
        record()
    elif select=='print' or select=='p':
        print_words()
    else:
        break