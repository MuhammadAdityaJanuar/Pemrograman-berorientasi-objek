-- Membuat database
CREATE DATABASE IF NOT EXISTS perpustakaan_db;
USE perpustakaan_db;

-- Membuat tabel users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Membuat tabel buku
CREATE TABLE IF NOT EXISTS buku (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(100) NOT NULL,
    pengarang VARCHAR(100),
    tahun INT
);

-- Membuat tabel anggota
CREATE TABLE IF NOT EXISTS anggota (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    alamat VARCHAR(200),
    telepon VARCHAR(20)
);

-- Tambahkan data awal (opsional)
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
