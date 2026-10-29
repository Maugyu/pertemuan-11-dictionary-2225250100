# Nama: Maulyditha Revania A.
# NIM: 2225250100
# Kelas: 3A
# Mata Kuliah: Algoritma dan Pemrograman
# Pertemuan 11: Dictionary/Map

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")


# Fungsi untuk menghitung rata-rata nilai mahasiswa
def rata_rata_nilai(data):
    if not data:
        return 0

    total_nilai = sum(
        mahasiswa["nilai"]
        for mahasiswa in data.values()
    )

    return total_nilai / len(data)


# Dictionary data mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# 1. Pencarian mahasiswa yang tersedia
print("=== PENCARIAN MAHASISWA ===")

nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil == "Data tidak ditemukan":
    print(hasil)
else:
    print("NIM:", nim_cari)
    print("Nama:", hasil["nama"])
    print("Kelas:", hasil["kelas"])
    print("Nilai:", hasil["nilai"])


# 2. Pencarian mahasiswa yang tidak tersedia
print("\n=== PENCARIAN NIM TIDAK TERSEDIA ===")

nim_cari = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil == "Data tidak ditemukan":
    print(hasil)
else:
    print(hasil)


# 3. Menambahkan mahasiswa baru
print("\n=== MENAMBAHKAN MAHASISWA ===")

data_mahasiswa["A006"] = {
    "nama": "Fani",
    "kelas": "C",
    "nilai": 80
}

print("Mahasiswa A006 berhasil ditambahkan.")


# 4. Memperbarui nilai mahasiswa
print("\n=== MEMPERBARUI NILAI ===")

data_mahasiswa["A002"]["nilai"] = 82

print("Nilai Budi setelah diperbarui:",
      data_mahasiswa["A002"]["nilai"])


# 5. Menampilkan seluruh data mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")

for nim, mahasiswa in data_mahasiswa.items():
    print(
        f"NIM: {nim} | "
        f"Nama: {mahasiswa['nama']} | "
        f"Kelas: {mahasiswa['kelas']} | "
        f"Nilai: {mahasiswa['nilai']}"
    )


# 6. Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")

rata_rata = rata_rata_nilai(data_mahasiswa)

print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")