nama_file = r'd:\Babam\Kuliah\PrakAlpro\Laprak Alpro Minggu 10\soal 2\soal.txt'
print(f"nama file1: {nama_file}")

with open(nama_file, 'r') as file:
    for baris in file:
        bagian = baris.strip().split('||')
        if len(bagian) == 2:
            soal = bagian[0].strip()
            jawaban_benar = bagian[1].strip().lower()
            
            print(soal)
            jawaban_user = input("Jawab: ").strip().lower()
            
            if jawaban_user == jawaban_benar:
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")