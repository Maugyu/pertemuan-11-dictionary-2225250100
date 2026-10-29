# Latihan 6: Fungsi Pencarian

def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")


mahasiswa = {
    "A001": {"nama": "Maulyditha Revania Aprilliyanti", "nilai": 85},
    "A002": {"nama": "Asep", "nilai": 78}
}

print("Pencarian A002:", cari(mahasiswa, "A002"))
print("Pencarian A003:", cari(mahasiswa, "A003"))