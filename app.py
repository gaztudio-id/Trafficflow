try:
    from flask import Flask, render_template, request
    import pandas as pd
    import numpy as np
    import joblib
    from datetime import datetime
except ImportError:
    import sys
    exit()

app = Flask(__name__)

# --- 1. LOAD MODEL & SCALER ---
try:
    model = joblib.load('traffic_model_final.pkl')
    scaler = joblib.load('scaler.pkl')
    
    model_features = [
        'avg_vehicle_speed', 'vehicle_count_cars', 'vehicle_count_trucks', 
        'vehicle_count_bikes', 'temperature', 'humidity', 'hour', 'day_of_week',
        'weather_condition_Foggy', 'weather_condition_Rainy', 
        'weather_condition_Sunny', 'weather_condition_Windy',
        'signal_status_Red', 'signal_status_Yellow'
    ]
    print("✅ Model & Scaler Berhasil Dimuat!")
except Exception as e:
    print(f"❌ Gagal load model: {e}")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # A. Ambil data dari form
        dt_str = request.form.get('datetime')
        speed = float(request.form.get('speed'))
        temp = float(request.form.get('temp'))
        humidity = float(request.form.get('humidity'))
        cars = int(request.form.get('cars'))
        trucks = int(request.form.get('trucks'))
        bikes = int(request.form.get('bikes'))
        weather = request.form.get('weather')
        signal = request.form.get('signal')

        # B. Fitur Waktu
        dt_obj = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M')
        hour = dt_obj.hour
        day_of_week = dt_obj.weekday()

        # C. Encoding
        w_fog = 1 if weather == 'Foggy' else 0
        w_rain = 1 if weather == 'Rainy' else 0
        w_sun = 1 if weather == 'Sunny' else 0
        w_wind = 1 if weather == 'Windy' else 0
        s_red = 1 if signal == 'Red' else 0
        s_yellow = 1 if signal == 'Yellow' else 0

        # D. DataFrame
        input_dict = {
            'avg_vehicle_speed': speed, 'vehicle_count_cars': cars,
            'vehicle_count_trucks': trucks, 'vehicle_count_bikes': bikes,
            'temperature': temp, 'humidity': humidity, 'hour': hour, 'day_of_week': day_of_week,
            'weather_condition_Foggy': w_fog, 'weather_condition_Rainy': w_rain,
            'weather_condition_Sunny': w_sun, 'weather_condition_Windy': w_wind,
            'signal_status_Red': s_red, 'signal_status_Yellow': s_yellow
        }
        
        input_df = pd.DataFrame([input_dict])[model_features]

        # E. Scaling & Prediksi
        input_scaled = scaler.transform(input_df)
        res = model.predict(input_scaled)[0]
        prediction = int(round(res))

        # F. Penyesuaian Threshold (Sangat Penting)
        # Kita turunkan batas 'Macet Total' menjadi 450 agar input Anda terdeteksi Macet
        if prediction > 450:
            status = "Macet Total"
            color_class = "danger"
        elif prediction > 300:
            status = "Padat Merayap"
            color_class = "warning"
        else:
            status = "Lancar"
            color_class = "success"

        return render_template('index.html', 
                               prediction_text=prediction, 
                               status_text=status,
                               color_class=color_class)

    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)