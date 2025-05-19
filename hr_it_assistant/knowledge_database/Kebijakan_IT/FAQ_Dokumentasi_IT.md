## 📁 **FAQ & Dokumentasi IT**

---

### 🛠️ **Panduan Instalasi VPN Kantor**

**Deskripsi:**
Panduan ini menjelaskan langkah-langkah untuk menginstal dan mengonfigurasi VPN kantor guna mengakses jaringan internal secara aman dari luar kantor.

**Langkah-langkah Instalasi:**

1. Unduh installer VPN dari portal internal: `vpn.company.local/download`
2. Jalankan installer dan ikuti wizard instalasi.
3. Masukkan server: `vpn.company.local`
4. Login dengan kredensial Active Directory (akun kantor).
5. Klik *Connect* untuk menghubungkan.

**Sistem Operasi yang Didukung:**

* Windows 10/11
* macOS 11 ke atas
* Android/iOS (menggunakan OpenVPN)

**Troubleshooting Umum:**

* 🔌 *Error 789*: Periksa koneksi internet.
* ❌ *Login failed*: Pastikan akun AD aktif dan password benar.
* 🔐 *Certificate not found*: Hubungi tim IT untuk pemasangan sertifikat ulang.

---

### ❓ **FAQ Troubleshooting Aplikasi HRIS**

**Topik Umum:**

1. **🔐 Tidak bisa login ke HRIS?**

   * Pastikan password benar dan akun belum expired.
   * Reset password melalui: `hrisreset.company.local`

2. **📤 Data absen tidak muncul?**

   * Sinkronisasi data membutuhkan waktu 1x24 jam.
   * Hubungi HR jika data tetap tidak tampil.

3. **📱 Aplikasi error di HP Android?**

   * Clear cache aplikasi HRIS.
   * Pastikan versi aplikasi terbaru dari Play Store.

4. **🌐 Akses dari luar kantor gagal?**

   * Gunakan VPN terlebih dahulu sebelum membuka HRIS.

---

### 🔗 **Panduan Koneksi ke Server Internal**

**Server yang Sering Diakses:**

| Server      | IP Address      | Keterangan                |
| ----------- | --------------- | ------------------------- |
| File Server | `192.168.10.12` | Share file divisi         |
| GitLab      | `192.168.10.30` | Repository kode           |
| DB Internal | `192.168.10.40` | Akses terbatas (DBA only) |

**Langkah Akses (Windows):**

1. Buka `File Explorer`, tekan `\\192.168.10.12`
2. Login dengan user domain (format: `COMPANY\username`)
3. Map network drive jika perlu.

**Catatan:**
Gunakan VPN jika berada di luar jaringan kantor.

---

### 💻 **Dokumentasi Onboarding Tools Baru**

**Tools Baru:**

* Slack (Komunikasi internal)
* Notion (Dokumentasi & Wiki)
* Jamboard (Kolaborasi whiteboard)

**Checklist untuk Karyawan Baru:**

| Tools    | Langkah Aktivasi       | Akses Awal              |
| -------- | ---------------------- | ----------------------- |
| Slack    | Undangan via email     | `company.slack.com`     |
| Notion   | Request akses ke IT    | `notion.so/companywiki` |
| Jamboard | Login Google Workspace | `jamboard.google.com`   |

**Tips:**

* 📅 Pastikan mengikuti sesi onboarding IT setiap hari Senin.
* 📧 Kirim tiket ke IT support jika ada masalah akses.
