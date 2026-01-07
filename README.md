# 🚦 TrafficFlow: Optimasi Transportasi Perkotaan dengan AI

### Sistem Analisis Beban Lalu Lintas & Prediksi Kepadatan Real-Time

**TrafficFlow** adalah aplikasi berbasis web yang dirancang untuk memprediksi tingkat kepadatan lalu lintas secara real-time menggunakan Machine Learning. Proyek ini bertujuan untuk mendukung mobilitas perkotaan yang berkelanjutan (SDG 11) dengan memberikan wawasan berbasis data mengenai kondisi jalan raya.

Dikembangkan sebagai bagian dari proyek penelitian (Politeknik Caltex Riau), sistem ini mengevaluasi faktor-faktor seperti waktu, cuaca, volume kendaraan, dan status lampu lalu lintas untuk menentukan kelancaran arus.

## 🚀 Fitur Utama

-   **Prediksi Real-Time**: Memproses input pengguna melalui model Machine Learning terlatih untuk memprediksi volume dan status lalu lintas.
-   **Logika Klasifikasi Cerdas**: Memberikan status visual yang mudah dipahami:
    -   🟢 **Lancar**: Beban rendah, arus normal.
    -   🟡 **Padat Merayap**: Kendaraan bergerak perlahan namun stabil.
    -   🔴 **Macet Total**: Beban sangat tinggi, arus hampir berhenti.
-   **Panduan Interaktif**: Halaman khusus "Panduan Pengisian" dengan tips mendetail untuk membantu pengguna memasukkan data yang akurat.
-   **Simulasi Skenario**: Kartu visual yang menampilkan contoh input (Skenario Macet, Lancar, dll) untuk pengujian model.
-   **Antarmuka Modern**: Dibangun dengan Bootstrap 5 dan Google Fonts (Plus Jakarta Sans) untuk pengalaman pengguna yang responsif.

## 🛠️ Teknologi yang Digunakan (Tech Stack)

### Backend & Machine Learning
-   **Python**: Bahasa pemrograman utama.
-   **Flask**: Framework web ringan untuk API dan routing.
-   **Scikit-learn**: Implementasi algoritma Machine Learning (Random Forest).
-   **Pandas & NumPy**: Manipulasi dan analisis data numerik.
-   **Joblib**: Serialisasi model (menyimpan/memuat model .pkl).

### Frontend
-   **HTML5 & CSS3**: Struktur dan gaya halaman.
-   **Bootstrap 5.3**: Framework CSS untuk desain responsif.
-   **FontAwesome**: Ikon antarmuka.

## ⚙️ Alur Pengembangan AI (Machine Learning Pipeline)

Sistem kecerdasan buatan ini dibangun melalui beberapa tahapan ketat:

1.  **Analisis & Pembersihan Data**
    -   Pengolahan dataset Smart Traffic.
    -   Penanganan missing values.
    -   Ekstraksi fitur waktu (jam, hari dalam seminggu).

2.  **Feature Engineering**
    -   **One-Hot Encoding**: Mengubah data kategori (Cuaca, Status Lampu) menjadi format numerik.
    -   **StandardScaler**: Normalisasi fitur numerik (Jumlah kendaraan, Suhu, Kecepatan) agar skala data seragam.

3.  **Seleksi Model**
    -   Kami membandingkan beberapa algoritma: Decision Tree, Random Forest, dan K-Nearest Neighbors (KNN).

4.  **Final Model: Random Forest Regressor**
    -   Dipilih karena:
        -   Memiliki R² Score tertinggi.
        -   Stabil terhadap overfitting.
        -   Performa konsisten saat diuji dengan data baru.

## 📂 Struktur Proyek

Berikut adalah susunan folder dan file dalam proyek ini:

```bash
Traffic_App/
├── app.py                  # Aplikasi utama Flask (Backend & Route)
├── requirements.txt        # Daftar dependensi Python

├── traffic_model_final.pkl # Model Random Forest yang sudah dilatih
├── scaler.pkl              # Scaler untuk normalisasi data input
├── templates/              # Folder file HTML
│   ├── index.html          # Dashboard Utama / Form Prediksi
│   └── guide.html          # Halaman Panduan & Skenario
└── README.md               # Dokumentasi Proyek
```

## 💻 Instalasi dan Cara Penggunaan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer lokal Anda:

### 1. Clone Repository
Unduh kode sumber proyek ini:
```bash
git clone https://github.com/username-anda/Traffic_App.git
cd Traffic_App
```

### 2. Buat Virtual Environment (Disarankan)
Isolasi dependensi proyek agar tidak bentrok dengan sistem utama.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install semua pustaka yang diperlukan:
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
Mulai server Flask:
```bash
python app.py
```

### 5. Akses Dashboard
Buka browser Anda dan kunjungi alamat berikut:
`http://127.0.0.1:5001/` atau `http://127.0.0.1:5000/` (sesuai output di terminal).

## 📖 Cara Menggunakan Panduan (Guide)

Untuk hasil prediksi yang akurat, pengguna disarankan memahami variabel input:

1.  Klik tombol **"Panduan"** di navigasi atas.
2.  Pelajari 5 kategori input (Waktu, Kecepatan, Cuaca, Volume, Sinyal).
3.  Gulir ke bawah ke bagian **"Contoh Skenario Lengkap"**.
4.  Gunakan nilai contoh tersebut untuk menguji model (misalnya: Masukkan nilai skenario "Macet Total" ke form utama untuk melihat hasil indikator Merah).



---

**Kredit**

Dibuat untuk Proyek Optimasi Alur Lalu Lintas
GAZ 2025 - *Data-driven decisions for better urban mobility.*
