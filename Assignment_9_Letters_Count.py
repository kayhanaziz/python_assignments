cumle = input("Please enter a sentence")

sozluk = {}

for i in cumle:

    keys = sozluk.keys()

    if i in keys:

        sozluk[i] += 1

    else:

        sozluk[i] = 1

print(sozluk)
