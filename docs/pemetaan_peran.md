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
(a)

(b)