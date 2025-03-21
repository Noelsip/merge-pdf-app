# Merge PDF App

## Deskripsi
Program ini adalah sebuah aplikasi Python sederhana yang memungkinkan pengguna untuk menggabungkan beberapa file PDF menjadi satu file PDF. Program ini menggunakan pustaka `PyPDF2` untuk melakukan penggabungan file PDF secara otomatis berdasarkan input dari pengguna.

## Fitur
- Menggabungkan beberapa file PDF menjadi satu.
- Input nama file secara dinamis oleh pengguna.
- Menampilkan pesan jika ada file yang tidak ditemukan.

## Persyaratan
Sebelum menjalankan program, pastikan Anda telah menginstal dependensi yang diperlukan dengan menggunakan `pip` dan file `requirements.txt`.

### Dependensi
- Python 3.x
- PyPDF2

## Cara Instalasi dan Penggunaan

### 1. Clone Repository (Opsional jika belum didownload)
Jika proyek ini ada di GitHub dan belum Anda download, clone repositori dengan perintah:
```sh
git clone https://github.com/Noelsip/merge-pdf-app.git
cd merge-pdf-app
```

### 2. Instal Dependensi
Pastikan Anda berada di dalam direktori proyek, lalu jalankan perintah berikut:
```sh
pip install -r requirements.txt
```

### 3. Jalankan Program
Jalankan program menggunakan Python:
```sh
python mergePDF.py
```

### 4. Masukkan Nama File PDF
Saat program berjalan, Anda akan diminta untuk memasukkan nama file PDF yang ingin digabungkan:
```
Masukkan nama file PDF yang ingin digabungkan (ketik 'selesai' untuk mengakhiri):
Masukkan nama file: file1.pdf
Masukkan nama file: file2.pdf
Masukkan nama file: selesai
Masukkan nama output file (contoh: hasil_gabungan.pdf): gabungan.pdf
```
Setelah itu, program akan menggabungkan file dan menyimpan hasilnya dengan nama yang Anda tentukan.

## Catatan Tambahan
- Pastikan file PDF yang ingin digabungkan berada dalam direktori yang sama dengan skrip Python ini.
- Jika ada file yang tidak ditemukan, program akan memberikan notifikasi.
- Nama file yang dimasukkan harus sesuai dengan yang ada di sistem.

## Lisensi
Proyek ini bersifat open-source dan dapat digunakan untuk keperluan pribadi maupun komersial.

