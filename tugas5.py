# Function
def greet(nama: str) -> str:
    return f"Halo, {nama}!"
def tambah(a: float, b: float = 0.0) -> float:
    return a + b
def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)

# Class Student
class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []
    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)
    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)
    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"
    def __str__(self):
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"

# Demo
if __name__ == "__main__":
    
    print("=== FUNCTIONS ===")
    print(greet("Rina"))
    print("Tambah 5 + 7 =", tambah(5, 7))
    print("Tambah 10 =", tambah(10))
    print("Rata-rata [80, 90, 100] =", rata_rata([80, 90, 100]))
    print("Rata-rata kosong =", rata_rata([]))

    print("\n=== CLASS STUDENT ===")
    mahasiswa1 = Student("Dina", "231001")
    mahasiswa1.tambah_nilai(85)
    mahasiswa1.tambah_nilai(90)
    mahasiswa1.tambah_nilai(95)
    mahasiswa2 = Student("Fajar", "231002")
    mahasiswa2.tambah_nilai(60)
    mahasiswa2.tambah_nilai(65)
    mahasiswa2.tambah_nilai(70)
    print(mahasiswa1)
    print("Rata-rata:", mahasiswa1.rata_nilai())
    print("Status:", mahasiswa1.status())
    print()
    print(mahasiswa2)
    print("Rata-rata:", mahasiswa2.rata_nilai())
    print("Status:", mahasiswa2.status())