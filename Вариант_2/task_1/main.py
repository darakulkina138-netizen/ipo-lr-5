#darakulkina138-netizen
text = input("Введите 10 слов: ")
words = text.split()
if len(words) < 10:
    text = "один два три четыре пять шесть семь восемь девять десять"
elif len(words) > 10:
    words = words[:10]
    text = " ".join(words)
uppercase_text = text.upper()
print(uppercase_text)
