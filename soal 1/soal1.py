file_pertama = open('text1.txt')
file_kedua = open('text2.txt')

baris1 = file_pertama.readlines()
baris2 = file_kedua.readlines()

for b1, b2 in zip(baris1, baris2):
    if b1 != b2:
        print("Baris beda!")
        print("File1:", b1.strip())
        print("File2:", b2.strip())

file_pertama.close()
file_kedua.close()