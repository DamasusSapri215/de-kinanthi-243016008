3: Pemetaan Peran dan Identifikasi Undercurrent

3a. Pemetaan Peran
No | Kebutuhan pemilik Batik Kinanthi | Peran utama | Alasan singkat | Tahap lifecycle
1 | Data penjualan dari toko, web, dan marketplace dikumpulkan ke satu tempat setiap malam | Data Engineer | Memindahkan dan menyatukan data dari banyak sumber secara otomatis | Ingestion
2 | Dashboard omzet harian per kanal | Data Analyst | Menganalisis data untuk menghitung data pemasukkan yang produk terlaku atau laris | Transformation
3 | Prediksi kebutuhan stok kain bulan depan | Data Analyst | Menganalisis data Riwayat penjualan dalam memprediksi stok pada bulan berikutnya | Transformation
4 | Tabel pelanggan tidak boleh berisi data ganda | Data Engineer | Menjaga integritas data agar aturan unique constraint, validasi atau proses duplikasi | Transformation
5 | Laporan motif terlaris per kota untuk rapat bulanan | Data Analyst | Menganalisis data penjualan berdasarkan produk dan kota, lalu menyajikan dalam bentuk laporan produk yang paling banyak terjual di setiap kota | Serving
6 | Rekomendasi produk untuk pelanggan di situs web | Data Scientist | Membangun sistem rekomendasi berdasarkan hasil Riwayat pencarian, atau preferensi dari pelanggan. | Storage
7 | Data transaksi lama tetap tersimpan aman dan hemat biaya | Data Arsitect| Merancang sistem agar penyimpanan data tetap terjaga dan efisiensi biaya penyimpanan. | Storage
8 | Analisis penyebab penurunan penjualan marketplace bulan lalu | Data Analyst | Menganalisis data penjualan, dengan membandingkan tren, dan mencari faktor yang menyebabkan penurunan penjualan | Serving

(a) mengapa kebutuhan 3 dan 6 tidak bisa dikerjakan sebelum kebutuhan 1 dan 4 selesai,
(b) risiko satu orang merangkap tiga peran di UMKM dan bagian yang sebaiknya diotomatisasi lebih dulu

Jawaban:
(a) Kebutuhan 3, yaitu prediksi kebutuhan stok kain bulan depan, bergantung pada kebutuhan 1, yaitu pengumpulan data penjualan dari toko, web dan marketplace ke satu tempat. Data penjualan yang terpadu dan konsisten agar memerlukan prediksi dapat digambarkan permintaan secara lebih lengkap. Jika data belum terkumpul, maka prediksi berisiko data tidak akurat karena sebagian transaksi tidak dapat diperhitungkan.
Kebutuhan 6, yaitu rekomendasi produk untuk pelanggan di situs web, bergantung pada kebutuhan 4, karena memastikan tabel pelanggan tidak memiliki data yang duplikat/ganda. Jadi, pembersihan data duplikat dapat membantu sistem dalam riwayat pembelian dengan pelanggan yang tetap. Tanpa proses ini, riwayat pelanggam bisa terpecahkan dan rekomendasi yang dihasilkan kurang relevan.
Dengan seperti ini, maka kebutuhan 1 dan 4 itu perlu diprioritaskan sebagai fondasi data sebelum melanjutkan ke kebutuhan ke 3 dan 6 diterapkan secara handal.
(b) Pada UMKM, keterbatasan tenaga kerja memungkinkan satu orang merangkap sebagai Data Engineer, Data Science, dan Data Analyst. Risiko yang muncul meliputi beban kerja berlebihan, kesalahan pengolahan data, kurangnya pemeriksaan independen, ketergantungan pada satu orang, serta berkurangnya waktu untuk melakukan analisis bisnis.
Bagian yang sebaiknya diotomatisasi terlebih dahulu adalah pengumpulan dan integrasi data penjualan dari berbagai kanal, dilanjutkan dengan pemeriksaan kualitas data. Setelah itu, transformasi data dan pembaruan dashboard omzet dapat diotomatisasi. Prediksi stok dan rekomendasi produk dilakukan setelah data yang diperlukan tersedia dan cukup berkualitas.
