import hashlib

#iin = "020103512347"
#i = 1

iin = input("vvedite iin - ")
i = int(input("vvedite + - "))

while True:
    text = f"{iin}+{i}"
    hash = hashlib.sha256(text.encode()).hexdigest()

    if hash.startswith("00"):
        print(text)
        print(hash)
        break
    i += 1
