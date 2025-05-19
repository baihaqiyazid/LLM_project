## Permintaan Reset Email & Storage

### 1. Reset Quota Email

**ID Kebijakan:** IT-RST-EMAIL-001
**Deskripsi:**
Pengguna yang mengalami kendala pengiriman atau penerimaan email akibat batas kuota dapat mengajukan permintaan reset quota.

**Langkah Penanganan:**

* Verifikasi akun pengguna aktif di sistem internal.
* Lakukan pengecekan sisa kuota melalui dashboard admin email (contoh: Google Workspace).
* Jika penggunaan >90%, lakukan clear email folder *Spam*, *Trash*, dan *Promotions*.
* Jika masih tidak cukup, reset kuota atau berikan notifikasi upgrade paket.

**SLA Penanganan:** Maksimal 2x24 jam sejak permintaan diterima.

**Catatan Khusus:**
Reset kuota hanya dapat dilakukan 1x per bulan per akun. Permintaan kedua wajib melalui persetujuan Manajer Departemen.

---

### 2. Permintaan Upgrade Kapasitas Google Drive Internal

**ID Kebijakan:** IT-GDRIVE-UPG-002
**Deskripsi:**
Permintaan peningkatan kapasitas penyimpanan Google Drive internal untuk mendukung operasional divisi.

**Kriteria Pengguna yang Berhak:**

* Karyawan tetap dengan email perusahaan.
* Memiliki penggunaan drive di atas 85%.
* Telah mencoba membersihkan file duplikat dan tidak aktif.

**Langkah Penanganan:**

* Validasi penggunaan ruang drive lewat Admin Console.
* Konsultasikan dengan Kepala Divisi terkait urgensi penyimpanan.
* Jika disetujui, ajukan ke Finance untuk biaya tambahan lisensi.
* Upgrade dilakukan oleh Admin IT dalam 1 hari kerja.

**Batas Maksimal:**
Upgrade maksimum hingga 2TB per akun. Jika lebih, dibutuhkan justifikasi tertulis.

---

### 3. Clear Cache / Temporary Files Remotely

**ID Kebijakan:** IT-CLR-CACHE-003
**Deskripsi:**
Permintaan untuk membersihkan cache dan temporary files secara remote, terutama untuk perangkat yang mengalami lag atau masalah performa.

**Syarat:**

* Perangkat aktif dan terhubung ke jaringan internal VPN.
* Telah mendapat persetujuan dari atasan langsung pengguna.
* Akses remote (misal: TeamViewer, AnyDesk, Google Admin Remote) telah dikonfigurasi sebelumnya.

**Langkah Penanganan:**

* Jadwalkan sesi remote dengan pengguna.
* Gunakan script atau tools seperti CCleaner, Disk Cleanup (Windows), atau `rm -rf ~/Library/Caches` (macOS).
* Pastikan tidak ada data penting yang terhapus.

**Risiko:**
Proses ini tidak menghapus file personal, namun tetap perlu backup sistem untuk jaga-jaga.