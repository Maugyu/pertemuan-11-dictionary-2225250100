# Latihan 3: Manipulasi Dictionary

data = {
    "nama": "Maulyditha Revania Aprilliyanti",
    "nilai": 100
}

# Menambahkan data kelas
data["kelas"] = "A"

# Memperbarui nilai
data["nilai"] = 90

print("Data setelah ditambahkan dan diperbarui:")
print(data)

# Menghapus data kelas
data.pop("kelas")

print("Data setelah kelas dihapus:")
print(data)