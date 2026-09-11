# 1. List – akses & manipulasi
# LIST
print("=== LIST ===")
data = ["Rina", 21, True, 167.5, "Batam", "Python"]
print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing:", data[1:5:2])
# append
data.append("Coding")
print("Setelah append:", data)
# insert
data.insert(1, "Mahasiswa")
print("Setelah insert:", data)
# extend
data.extend(["SQL", "Git"])
print("Setelah extend:", data)
# pop
data.pop()
print("Setelah pop:", data)
# remove
data.remove(True)
print("Setelah remove:", data)

# 2. Tuple –  immutability & unpacking
print("\n=== TUPLE ===")
mahasiswa = ("Rina", 21, "Sistem Informasi", "ITEBA", "Batam")
print("Tuple:", mahasiswa)
print("Panjang tuple:", len(mahasiswa))
print("Index ke-2:", mahasiswa[2])
nama, umur, jurusan, *lainnya = mahasiswa
print("Nama:", nama)
print("Umur:", umur)
print("Jurusan:", jurusan)
print("Lainnya:", lainnya)

# 3. Set – keunikan & operasi himpunan
print("\n=== SET ===")
set1 = {"Python", "Java", "HTML", "CSS"}
set2 = {"Python", "SQL", "CSS", "Git"}
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# 4. Dictionary – key/value dasar
print("\n=== DICTIONARY ===")
student = {
    "nama": "Rina",
    "nim": "12345",
    "angkatan": 2024,
    "kota": "Batam"
}
print(student)
student["email"] = "rina@email.com"
student["kota"] = "Batam"
del student["angkatan"]
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
for key, value in student.items():
    print(key, ":", value)

# 5. Nested structures
print("\n=== NESTED STRUCTURE ===")
buku = [
    {"judul": "The Love Hypothesis","penulis": "Ali Hazelwood","tahun": 2021},
    { "judul": "Better Than The Movies", "penulis": "Lynn Painter","tahun": 2021},
    {"judul": "To All The Boys I've Loved Before","penulis": "Jenny Han","tahun": 2014},
    {"judul": "The Unhoneymooners","penulis": "Christina Lauren","tahun": 2019 }
]
for item in buku:
    print(item["judul"])
filter_buku = [
    b for b in buku 
    if b["tahun"] >= 2020
]
print("Buku terbaru:", filter_buku)

# 6. Comprehension & utilitas
print("\n=== COMPREHENSION ===")
angka = list(range(1,21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x*x for x in angka]
print("Genap:", genap)
print("Kuadrat:", kuadrat)
dict_angka = {
    x: "genap" if x % 2 == 0 else "ganjil"
    for x in range(1,11)
}
print(dict_angka)
huruf = {x.lower() for x in "Python Programming"}
print("Huruf unik:", huruf)

# 7. Keanggotaan & pencarian sederhana
print("\n=== SEARCH ===")
warna = ["merah", "biru", "hijau"]

print("Apakah biru ada?",
      "biru" in warna)

print("Index merah:",
      warna.index("merah"))