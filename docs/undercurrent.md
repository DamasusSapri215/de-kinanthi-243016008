3b. Identifikasi undercurrents pada pipeline_mini.py

Undercurrent | Bukti penerapan di kode | Kekurangan | Usulan Perbaikan
Security | Kredensial dibaca dari .env lewat load_dotenv() | KPipeline memakai user de_user yang punya hak penuh | Buat user khusus pipeline: hanya baca transaksi, tulis mart_omzet_harian
Data management | Fungsi ingest(engine) mengambil data transaksi, store_raw(data) menyimpan data mentah ke file .csv dan check_quality(data) memeriksa ID transaksi ganda dan nilai total yang kurang dari nol | Mekanisme dalam mengelolah data mentah, backup dan pencatatan metadata | Perbaikan harusnya ketika ada data mentah yang baru bisa dilakukan proses lebih cepat
DataOps | Logging dalam setiap tahap, misalnya Pipeline mulai, kualitas data lolos dan pipeline selesai. | Belum ada pengujian otomatis, notifikasi gagal, pemantauan pipeline atau mekanisme ulang | Tambahkan pengujian otomatis atau menambahkan kalo ada yang sistem gagal
Data architecture | Misahin data sumber dalam PostgreSQL, data mentah ke csv dan hasil pengolahan data dalam mart_omzet_harian | Arsitektur masih sederhana dan belum ada pengaturan skema yang dikelola dalam skala besar | Menambahkan sistem yang lebih besar untuk industri skala besar. Tapi kalo standar umkm ga perlu, tapi udah cukup
Orchestration | Fungsi main() menjalankan proses secara berurutan: ingestion -> Storage -> quality -> check -> transformation -> serving. | Belum ada penjadwalan otomatis, pengaturan dependensi melalui alat orkestrasi seperti Airflow, dan menjalankan ulang pada tahap tertentu | Menambahkan penjadwalan otomatis, dan menambahkan apache Airflow dalam menjalankan tahap tertentu
Software engineering | Memisahkan proses fungsi seperti ingest(), store_raw, transform dan serve(). Logging dan penanganan kesalahan dari ValueError | Belum ada unit test, integration test dengan environment variable, penerapan CI/CD | Membuat Pengujian dalam setiap fungsi, memindahkan username, password dan koneksi database simpan ke .env

Pertanyaan 
1. Mengapa mart_omzet_harian tetap aman saat data rusak masuk? 
2. data/raw/transaksi.csv tetap diperbarui walaupun data rusak. Masalah atau justru berguna? Jelaskan. 

Jawaban:
1. Karena pipeline menerapkan pemeriksaan kualitas data (Quality Check) sebelum melakukan proses transformasi dan menyimpan hasil dalam bentuk tabel mart. hasil yang ditemukan, bahwa data yang tidak valid, misalnya nilai total kurang dari atau sama dengan nol, id transaksi yang duplikat, maka pipeline memberhentikan proses dengan pesan ValueError. Menyebabkan, data yang bermasalah untuk tidak melanjutkan proses yang lebih lanjut dan tidak mengubah isi tabel dari mart_omzet_harian yang udah tersedia.
2. Berguna, karena proses penyimpan data mentah dilakukan pada tahap pemeriksaan kualitas data. hal ini justru lebih berguna untuk file menyimpan data yang diterima dari sumber, termasuk data yang bermasalahan. Data mentah digunakan dalam pemeriksaan apakah ada kesalahan ataupun perbaikan data.