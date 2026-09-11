# 1. Deklarasi Variabel dan Tipe Data
nama = "Rina"              # string
umur = 21                 # integer
tinggi = 167.5             # float
mahasiswa = True           # boolean
hobi = ["nonton drakor sad", "baking", "musik"]  # list

print("=== VARIABEL ===")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", mahasiswa)
print("Hobi:", hobi)

# 2. Manipulasi String
print("\n=== MANIPULASI STRING ===")
kalimat = "Belajar Python"
print("Teks:", kalimat)
print("Panjang teks:", len(kalimat))
print("Huruf besar:", kalimat.upper())
print("Huruf kecil:", kalimat.lower())
gabung = nama + " sedang belajar Python"
print("Gabungan string:", gabung)

# 3. Operasi Matematika
print("\n=== OPERASI MATEMATIKA ===")
a = 10
b = 3
print("Tambah:", a + b)
print("Kurang:", a - b)
print("Kali:", a * b)
print("Bagi:", a / b)
print("Pembagian bulat:", a // b)
print("Sisa bagi:", a % b)

# 4. List dan Akses Elemen
print("\n=== LIST ===")
hewan = ["kucing", "anjing", "ikan", "burung", "kelinci"]
print("List awal:", hewan)
print("Elemen pertama:", hewan[0])
hewan.append("hamster")
print("Setelah append:", hewan)
hewan.remove("ikan")
print("Setelah remove:", hewan)
hewan.pop()
print("Setelah pop:", hewan)

# 5. Input User
print("\n=== INPUT USER ===")
nama_user = input("Masukkan nama kamu: ")
umur_user = input("Masukkan umur kamu: ")
print("Halo, nama saya", nama_user, "dan umur saya", umur_user, "tahun.")