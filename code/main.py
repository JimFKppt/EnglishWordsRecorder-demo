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
select=input("Please select mode(record/print): ")
if select=='record':
    record()
elif select=='print':
    print_words()