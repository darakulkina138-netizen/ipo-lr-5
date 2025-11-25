text = input("Введите текст: ")
count = 0
for char in text:
    if char == "и":
        count += 1
print(f"Буква и встречается {count} раз(а)")
