# 🚦 TrafficFlow: Optimasi Transportasi Perkotaan
### Sistem Analisis Beban Lalu Lintas & Prediksi Kepadatan Real-Time Berbasis Machine Learning

TrafficFlow adalah aplikasi cerdas yang dirancang untuk menganalisis beban lalu lintas dan memprediksi tingkat kepadatan secara real-time menggunakan Machine Learning. Sistem ini mendukung upaya mobilitas perkotaan berkelanjutan (SDG 11) dan dikembangkan sebagai bagian dari proyek penelitian di Politeknik Caltex Riau.

---

## ⚙️ Alur Pengembangan (Technical Pipeline)

### 1. Analisis & Pembersihan Data
- Mengolah dataset *Smart Traffic*
- Menangani missing values
- Ekstraksi fitur waktu (hour, day_of_week)

### 2. Feature Engineering
- **One-Hot Encoding** untuk kategori cuaca & status lampu lalu lintas  
- **StandardScaler** untuk normalisasi fitur numerik (jumlah kendaraan, suhu, kecepatan)

### 3. Seleksi Model
Model yang dibandingkan:
- Decision Tree  
- Random Forest  
- K-Nearest Neighbors (KNN)

### 4. Final Model
Model terbaik: **Random Forest Regressor**

Dipilih karena:
- R² Score tertinggi  
- Stabil terhadap overfitting  
- Performa konsisten ketika diuji pada data baru

### 5. Web Deployment
- Backend Flask  
- Integrasi model (.pkl)  
- Frontend dashboard menggunakan Bootstrap 5  

---

## 🚦 Logika Klasifikasi Kepadatan

TrafficFlow menghitung **Traffic Load Score** untuk menentukan status kondisi lalu lintas:

| Status | Deskripsi |
|--------|-----------|
| 🟢 **Lancar** | Beban rendah, arus normal |
| 🟡 **Padat Merayap** | Kendaraan bergerak perlahan tetapi stabil |
| 🔴 **Macet Total** | Beban sangat tinggi, kecepatan hampir berhenti |

---

## 💻 Instalasi dan Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/GhaswulFikriFadhillah/Trafficflow.git
cd Trafficflow
```
### 2. Membuat Virtual Environment
```bash
python -m venv .venv
```
Windows:
```bash
.venv\Scripts\activate
```
Mac/Linux:
```bash
source .venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install flask pandas numpy scikit-learn joblib
```
### 4. Menjalankan Dashboard
Jalankan server:
```bash
python app.py
```
Buka browser ke:
```bash
http://127.0.0.1:5000
```
---
📂 Struktur Direktori
```bash
TrafficFlow/
│
├── app.py                     # Backend Flask + integrasi model ML
├── traffic_model_final.pkl    # Model Random Forest siap digunakan
├── scaler.pkl                 # Normalisasi fitur input
├── templates/
│   └── index.html             # UI dashboard utama
└── .gitignore                 # Ignore file .venv, cache, dll
```
🤝 Kontribusi & Lisensi
Proyek ini bersifat open-source untuk tujuan pembelajaran.
Kontribusi berupa:
- Penambahan fitur
- Perbaikan bug
- Optimasi model
Sangat diapresiasi untuk membantu pengembangan TrafficFlow.

✨ "Data-driven decisions for better urban mobility." — GAZ 2025
