## Troubleshoot Perangkat Kantor

### 4.1 Panduan Printer Tidak Terdeteksi

**Deskripsi Masalah:**
Printer tidak muncul pada daftar perangkat, tidak bisa dipilih saat mencetak.

**Langkah Penanganan:**

1. Pastikan printer menyala dan terhubung ke jaringan/laptop.
2. Cek koneksi kabel USB atau Wi-Fi (jika nirkabel).
3. Jalankan perintah `Services.msc` dan restart service “Print Spooler”.
4. Gunakan menu “Add Printer” pada Control Panel untuk menambahkan ulang.
5. Unduh driver printer terbaru dari situs resmi vendor.

---

### 4.2 Setting Ulang Printer Network

**Deskripsi Masalah:**
Printer network tidak terdeteksi atau gagal mencetak melalui jaringan.

**Langkah Penanganan:**

1. Pastikan printer sudah mendapat IP Address dari DHCP (cek di panel printer).
2. Reset setting jaringan printer (factory reset) jika perlu.
3. Akses IP printer via browser dan pastikan printer bisa diakses.
4. Tambahkan printer melalui fitur “Add Printer via IP Address”.
5. Pastikan firewall tidak memblokir port printing (TCP 9100 atau sesuai model).

---

### 4.3 Scanner Tidak Bisa Digunakan

**Deskripsi Masalah:**
Scanner tidak terbaca oleh komputer, tidak bisa menyimpan hasil scan.

**Langkah Penanganan:**

1. Pastikan kabel scanner terhubung dengan baik.
2. Buka Device Manager, pastikan tidak ada warning/error di device scanner.
3. Gunakan aplikasi scanner bawaan vendor, bukan aplikasi Windows Scan.
4. Coba scan via aplikasi Paint atau Acrobat Reader untuk cek koneksi.
5. Update driver scanner dari situs resmi.

---

### 4.4 Webcam atau Audio Tidak Terdeteksi

**Deskripsi Masalah:**
Webcam/mikrofon tidak muncul saat meeting online atau rekaman.

**Langkah Penanganan:**

1. Cek apakah aplikasi memiliki izin akses kamera dan mikrofon.
2. Buka Device Manager → cari Imaging Devices dan Sound, video and game controllers.
3. Jika ada tanda peringatan (kuning), update atau reinstall drivernya.
4. Restart komputer setelah update driver.
5. Coba tes kamera/mikrofon dengan aplikasi lain (misalnya kamera bawaan Windows).

---

🛠️ Jika semua langkah di atas sudah dilakukan namun masalah masih terjadi, silakan hubungi tim IT melalui tiket dukungan atau email resmi.
