from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

MODEL_FILE = "kmeans_model.pkl"
SCALER_FILE = "scaler.pkl"
DATA_FILE = "Online Retail.xlsx"

# ------------------ Helper: Train Model if Missing ------------------ #
def train_model():
    df = pd.read_excel(DATA_FILE)
    df.dropna(subset=['CustomerID'], inplace=True)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    customer_df = df.groupby('CustomerID').agg({
        'InvoiceNo': 'nunique',
        'Quantity': 'sum',
        'TotalPrice': 'sum',
        'StockCode': 'nunique',
        'InvoiceDate': 'max'
    }).rename(columns={
        'InvoiceNo': 'Frequency',
        'Quantity': 'TotalQuantity',
        'StockCode': 'Variety',
        'TotalPrice': 'TotalSpending'
    })

    latest_date = df['InvoiceDate'].max()
    customer_df['Recency'] = (latest_date - customer_df['InvoiceDate']).dt.days
    customer_df.drop(columns='InvoiceDate', inplace=True)

    features = ['Frequency', 'TotalQuantity', 'Variety', 'TotalSpending', 'Recency']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(customer_df[features])

    kmeans = KMeans(n_clusters=4, random_state=42)
    customer_df['Cluster'] = kmeans.fit_predict(scaled_features)

    # Save model and scaler
    joblib.dump(kmeans, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)

    # Save clustered data for reference
    customer_df.to_csv("customer_segments.csv", index=True)
    print("✅ Model retrained and saved successfully!")

# ------------------ Load or Train Model ------------------ #
if not os.path.exists(MODEL_FILE) or not os.path.exists(SCALER_FILE):
    print("⚠️ Model or Scaler not found. Training new model...")
    train_model()

kmeans = joblib.load(MODEL_FILE)
scaler = joblib.load(SCALER_FILE)

# ------------------ Routes ------------------ #
@app.route('/')
def home():
    return send_from_directory('.', 'frontend.html')

@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        Frequency = data['Frequency']
        TotalQuantity = data['TotalQuantity']
        Variety = data['Variety']
        TotalSpending = data['TotalSpending']
        Recency = data['Recency']

        features = np.array([[Frequency, TotalQuantity, Variety, TotalSpending, Recency]])
        features_scaled = scaler.transform(features)
        cluster = int(kmeans.predict(features_scaled)[0])

        # Map cluster numbers to names
        cluster_names = {
            0: "VIP Customer 👑",
            1: "Regular Buyer 🛒",
            2: "Bargain Hunter 💰",
            3: "New/Inactive Customer 🌱"
        }
        cluster_label = cluster_names.get(cluster, "Unknown")

        return jsonify({"cluster": cluster, "label": cluster_label})

    except Exception as e:
        return jsonify({"error": str(e)})

# ------------------ Main ------------------ #
if __name__ == '__main__':
    app.run(debug=True)
