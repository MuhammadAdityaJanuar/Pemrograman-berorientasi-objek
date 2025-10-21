# Pemrograman-berorientasi-objek
📚 Aplikasi Manajemen Perpustakaan (Python + MySQL)
📖 Deskripsi

Aplikasi ini merupakan sistem manajemen perpustakaan berbasis Python (Tkinter) dengan koneksi ke MySQL.
Tujuannya adalah untuk mempermudah proses pengelolaan data buku dan anggota secara digital.
Aplikasi ini mendukung fitur login, tampilan statistik, serta manajemen data melalui antarmuka yang ramah pengguna (GUI).

⚙️ Fitur Utama

✅ Login User

Verifikasi username dan password dari database MySQL

Validasi input kosong dan pesan kesalahan otomatis

✅ Dashboard Perpustakaan

Menampilkan total jumlah buku dan anggota

Navigasi menu ke manajemen data

Desain berwarna lembut dan mudah digunakan

✅ Manajemen Buku

Menampilkan seluruh daftar buku dari database

Menggunakan tabel interaktif (Treeview)

✅ Manajemen Anggota

Menampilkan seluruh data anggota

Tampilan rapi dan terstruktur

✅ Logout Aman

Konfirmasi sebelum keluar dari aplikasi

🧰 Teknologi yang Digunakan
Komponen	Teknologi
Bahasa Pemrograman	Python 3.x
GUI Framework	Tkinter
Database	MySQL
Library Tambahan	mysql-connector-python, tkinter, ttk
🗂️ Struktur Database

Database: perpustakaan_db

Tabel users
Kolom	Tipe Data	Keterangan
id	INT (PK, AUTO_INCREMENT)	ID User
username	VARCHAR(50)	Username login
password	VARCHAR(50)	Password login
Tabel buku
Kolom	Tipe Data	Keterangan
id	INT (PK, AUTO_INCREMENT)	ID Buku
judul	VARCHAR(100)	Judul Buku
pengarang	VARCHAR(100)	Nama Pengarang
tahun	INT	Tahun Terbit
Tabel anggota
Kolom	Tipe Data	Keterangan
id	INT (PK, AUTO_INCREMENT)	ID Anggota
nama	VARCHAR(100)	Nama Lengkap
alamat	VARCHAR(200)	Alamat
telepon	VARCHAR(20)	Nomor Telepon
🚀 Cara Menjalankan Program

Pastikan Python 3.x sudah terinstal.

Install library:

pip install mysql-connector-python


Buat database perpustakaan_db di MySQL dan isi dengan tabel seperti di atas.

Jalankan aplikasi:

python app_perpustakaan.py

🎨 Tampilan Aplikasi

Login Page: Form username & password dengan validasi otomatis

Dashboard: Statistik jumlah buku & anggota

Manajemen Buku/Anggota: Tabel daftar data dari database

Logout: Konfirmasi sebelum keluar

🧑‍💻 Pengembang

Nama: Muhammad Aditya Januar
Bahasa Pemrograman: Python
Framework GUI: Tkinter
Database: MySQL
Tujuan: Proyek belajar / implementasi magang
