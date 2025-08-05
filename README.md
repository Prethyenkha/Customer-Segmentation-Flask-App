# 🛍️ Customer Segmentation Flask App

## 🚀 Overview
This project is a **Machine Learning-powered Customer Segmentation Application** built using **Flask** and **K-Means Clustering**. It segments customers into distinct groups based on their purchasing behavior, allowing businesses to target marketing campaigns more effectively.  

Clusters include:
- 👑 **VIP Customer**
- 🛒 **Regular Buyer**
- 💰 **Bargain Hunter**
- 🌱 **New/Inactive Customer**

---

## ✨ Features
✅ Flask web application with interactive frontend  
✅ Automated K-Means clustering model  
✅ Optimal cluster selection using Elbow Method  
✅ Outlier handling with log transformation  
✅ Real-time prediction via REST API  
✅ Styled responsive UI with custom colors  
✅ Export of segmented customers to CSV  
✅ Easy deployment to GitHub/Heroku  

---

## 🛠️ Tech Stack
- **Python, Flask** (Backend)
- **Scikit-learn, Pandas, NumPy** (ML)
- **HTML, CSS, JavaScript** (Frontend)
- **Matplotlib** (Visualization)

---

## 📂 Project Structure
```
Customer Segmentation/
│── app.py                 # Flask backend
│── train_model.py          # Training script
│── style.css               # UI styling
│── frontend.html           # Web interface
│── requirements.txt        # Dependencies
│── test_app.py             # API tests
│── customer_segments.csv   # Segmented output
│── kmeans_model.pkl        # Saved model
│── scaler.pkl              # Saved scaler
```

---

## ⚡ How to Run

1️⃣ Clone the repository:
```bash
git clone https://github.com/Prethyenkha/Customer-Segmentation-Flask-App.git
cd Customer-Segmentation-Flask-App
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Train the model:
```bash
python train_model.py
```

4️⃣ Start Flask server:
```bash
python app.py
```

5️⃣ Open in browser:
```
http://127.0.0.1:5000
```

---

## 🧪 Test the API
Run automated tests:
```bash
pytest test_app.py
```

---

## 📊 Output Example
- VIP Customers 👑: 25%
- Regular Buyers 🛒: 40%
- Bargain Hunters 💰: 20%
- New/Inactive 🌱: 15%

---

## 🖼️ App Preview

<img width="1364" height="624" alt="Screenshot 2025-08-05 143638" src="https://github.com/user-attachments/assets/6d2ce837-48dd-4b13-a5c2-07fdf1db575a" />


---

### 👩‍💻 Author
Developed with ❤️ by [Prethyenkha](https://github.com/Prethyenkha)
