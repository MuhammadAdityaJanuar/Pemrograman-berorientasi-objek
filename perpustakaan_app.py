import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# =======================
# KONEKSI DATABASE
# =======================
def connect_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpustakaan_db"
        )
        return db
    except mysql.connector.Error as err:
        messagebox.showerror("Koneksi Gagal", f"Gagal konek ke database:\n{err}")
        return None


# =======================
# LOGIN FORM
# =======================
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Peringatan", "Username dan password tidak boleh kosong!")
        return

    db = connect_db()
    if db is None:
        return

    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
        login_window.destroy()
        open_dashboard(username)
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")
    db.close()


# =======================
# DASHBOARD
# =======================
def open_dashboard(username):
    db = connect_db()
    if db is None:
        return

    dashboard = tk.Tk()
    dashboard.title("📚 Dashboard Perpustakaan")
    dashboard.geometry("650x400")
    dashboard.config(bg="#e8f5e9")

    tk.Label(dashboard, text=f"👋 Selamat Datang, {username}", font=("Arial", 14, "bold"), bg="#e8f5e9", fg="#2e7d32").pack(pady=10)

    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM buku")
    total_buku = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM anggota")
    total_anggota = cursor.fetchone()[0]

    frame_stat = tk.Frame(dashboard, bg="#c8e6c9", pady=10, padx=20, relief="groove", bd=2)
    frame_stat.pack(pady=10)
    tk.Label(frame_stat, text=f"📚 Jumlah Buku: {total_buku}", font=("Arial", 12), bg="#c8e6c9").pack()
    tk.Label(frame_stat, text=f"👥 Jumlah Anggota: {total_anggota}", font=("Arial", 12), bg="#c8e6c9").pack()

    # Tombol menu
    frame_btn = tk.Frame(dashboard, bg="#e8f5e9")
    frame_btn.pack(pady=20)

    tk.Button(frame_btn, text="📖 Manajemen Buku", command=lambda: manajemen_buku(), width=20, bg="#66bb6a", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(frame_btn, text="👤 Manajemen Anggota", command=lambda: manajemen_anggota(), width=20, bg="#42a5f5", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(frame_btn, text="🚪 Logout", command=lambda: logout(dashboard), width=20, bg="#ef5350", fg="white", font=("Arial", 11, "bold")).grid(row=1, column=0, columnspan=2, pady=10)

    db.close()
    dashboard.mainloop()


# =======================
# LOGOUT
# =======================
def logout(window):
    if messagebox.askyesno("Konfirmasi", "Yakin ingin logout?"):
        window.destroy()
        main()


# =======================
# MANEJEMEN BUKU
# =======================
def manajemen_buku():
    db = connect_db()
    if db is None:
        return

    window = tk.Toplevel()
    window.title("📚 Manajemen Buku")
    window.geometry("700x400")
    window.config(bg="#f1f8e9")

    tk.Label(window, text="Daftar Buku", font=("Arial", 14, "bold"), bg="#f1f8e9", fg="#33691e").pack(pady=10)

    table = ttk.Treeview(window, columns=("ID", "Judul", "Pengarang", "Tahun"), show="headings")
    table.heading("ID", text="ID")
    table.heading("Judul", text="Judul Buku")
    table.heading("Pengarang", text="Pengarang")
    table.heading("Tahun", text="Tahun Terbit")
    table.pack(fill=tk.BOTH, expand=True)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM buku")
    for row in cursor.fetchall():
        table.insert("", tk.END, values=row)
    db.close()


# =======================
# MANEJEMEN ANGGOTA
# =======================
def manajemen_anggota():
    db = connect_db()
    if db is None:
        return

    window = tk.Toplevel()
    window.title("👥 Manajemen Anggota")
    window.geometry("700x400")
    window.config(bg="#e3f2fd")

    tk.Label(window, text="Daftar Anggota", font=("Arial", 14, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=10)

    table = ttk.Treeview(window, columns=("ID", "Nama", "Alamat", "Telepon"), show="headings")
    table.heading("ID", text="ID")
    table.heading("Nama", text="Nama")
    table.heading("Alamat", text="Alamat")
    table.heading("Telepon", text="No. Telepon")
    table.pack(fill=tk.BOTH, expand=True)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM anggota")
    for row in cursor.fetchall():
        table.insert("", tk.END, values=row)
    db.close()


# =======================
# FORM LOGIN (UTAMA)
# =======================
def main():
    global entry_username, entry_password, login_window
    login_window = tk.Tk()
    login_window.title("Login Perpustakaan")
    login_window.geometry("400x300")
    login_window.config(bg="#e3f2fd")

    tk.Label(login_window, text="📚 Sistem Login Perpustakaan", font=("Arial", 14, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=15)
    tk.Label(login_window, text="Username:", bg="#e3f2fd", font=("Arial", 11)).pack()
    entry_username = tk.Entry(login_window, width=30)
    entry_username.pack(pady=5)

    tk.Label(login_window, text="Password:", bg="#e3f2fd", font=("Arial", 11)).pack()
    entry_password = tk.Entry(login_window, width=30, show="•")
    entry_password.pack(pady=5)

    tk.Button(login_window, text="Login", command=login, bg="#64b5f6", fg="white", width=15, font=("Arial", 11, "bold")).pack(pady=15)

    login_window.mainloop()


# =======================
# JALANKAN PROGRAM
# =======================
if __name__ == "__main__":
    main()
