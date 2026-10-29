# Pertemuan 11 - Dictionary/Map

**Nama:** Maulyditha Revania A.  
**NIM:** 2225250100  
**Kelas:** 3A

## Tujuan

Mempelajari penggunaan dictionary dalam Python untuk menyimpan, mengakses, mencari, menambahkan, memperbarui, dan menampilkan data menggunakan pasangan key-value.

## Struktur Data

Program menggunakan dictionary dengan NIM sebagai key utama. Setiap value berupa dictionary yang menyimpan nama, kelas, dan nilai mahasiswa.

Contoh:

```python
"A001": {
    "nama": "Ayu",
    "kelas": "A",
    "nilai": 85
}
```

## Daftar File

Folder `latihan/` berisi enam program untuk mempelajari dasar dictionary, akses aman menggunakan `get()`, manipulasi dictionary, iterasi menggunakan `items()`, dictionary bersarang, dan fungsi pencarian.

Folder `praktik/` berisi program `data_mahasiswa.py` untuk mengelola data mahasiswa.

## Cara Menjalankan

Jalankan program melalui terminal VS Code:

```bash
python praktik/data_mahasiswa.py
```

## Test Case

| No. | Input/Aksi | Hasil yang Diharapkan | Status |
|---|---|---|---|
| 1 | Mencari A003 | Data Citra ditampilkan | Berhasil |
| 2 | Mencari A999 | Data tidak ditemukan | Berhasil |
| 3 | Mengubah nilai A002 menjadi 82 | Nilai menjadi 82 | Berhasil |
| 4 | Menambahkan A006 | Data mahasiswa baru tersimpan | Berhasil |
| 5 | Menampilkan rekap menggunakan items() | Seluruh data mahasiswa tampil | Berhasil |

## Refleksi

Salah satu kesalahan yang dapat terjadi ketika menggunakan dictionary adalah mengakses key yang tidak tersedia sehingga menimbulkan `KeyError`. Kesalahan ini dapat dihindari dengan menggunakan metode `get()` untuk mengambil data secara aman. Jika key tidak ditemukan, program dapat menampilkan pesan bahwa data tidak tersedia.

Selain itu, dictionary bersarang memerlukan urutan akses key yang tepat agar data mahasiswa dapat ditampilkan sesuai kebutuhan.