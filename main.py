import hashlib

iin = "020103512876"
i = 10

#iin = input("vvedite iin - ")
#i = int(input("vvedite + - "))

while True:
    text = f"{iin}+{i}"
    hash = hashlib.sha256(text.encode()).hexdigest()
    if hash.startswith("00"):
        print("hash - ", text)
        print("2 zeros - ", hash)
        break
    i += 1

while True:
    text = f"{iin}+{i}"
    hash = hashlib.sha256(text.encode()).hexdigest()
    if hash.startswith("000"):
        print("hash - ", text)
        print("3 zeros - ", hash)
        break
    i += 1



