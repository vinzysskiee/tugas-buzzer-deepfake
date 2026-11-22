# Aplikasi Manajemen Inventaris Laboratorium

## Deskripsi
Aplikasi ini digunakan untuk mengelola data inventaris
barang laboratorium menggunakan Python.

## Fitur
1. Menampilkan seluruh barang.
2. Mencari barang.
3. Memfilter kondisi barang.
4. Menampilkan stok rendah.
5. Menghitung ringkasan inventaris.
6. Mengekspor laporan ke JSON.

## Kebutuhan
- Python versi 3.9 atau lebih baru.
- Tidak membutuhkan library tambahan.

## Cara Menjalankan

Menampilkan seluruh barang:
python main.py list

Mencari barang:
python main.py search laptop

Memfilter barang rusak:
python main.py condition rusak

Menampilkan stok rendah:
python main.py low-stock

Menampilkan ringkasan:
python main.py summary

Mengekspor laporan:
python main.py export

## Pengujian
python -m unittest discover -s tests -v