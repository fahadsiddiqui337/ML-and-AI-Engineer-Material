# 🤖 Supervised Learning API
## نگرانی سے سیکھنے کا API

یہ ایک مکمل Machine Learning API ہے جو Supervised Learning کی تمام سہولیات فراہم کرتا ہے۔

---

## 📋 Table of Contents
1. [انسٹال کرنا](#installation)
2. [API شروع کرنا](#running-the-api)
3. [Endpoints کی تفصیل](#api-endpoints)
4. [مثالیں](#examples)
5. [ویب انٹرفیس استعمال کریں](#web-interface)

---

## 🚀 Installation (انسٹال کرنا)

### Step 1: Python انسٹال کریں
یقینی بنائیں کہ Python 3.8+ انسٹال ہے۔

### Step 2: Dependencies انسٹال کریں

```bash
pip install -r requirements.txt
```

یا براہ براہ:

```bash
pip install fastapi uvicorn numpy pandas scikit-learn python-multipart pydantic
```

---

## 🏃 Running the API (API شروع کریں)

### Windows میں:

```bash
python supervised_learning_api.py
```

یا:

```bash
uvicorn supervised_learning_api:app --reload
```

### Linux/Mac میں:

```bash
python3 supervised_learning_api.py
```

یا:

```bash
uvicorn supervised_learning_api:app --reload
```

### Output:
```
🚀 Supervised Learning API شروع ہو رہا ہے...
📍 http://localhost:8000 پر سنو
📚 Documentation: http://localhost:8000/docs
✅ ماڈل تیار ہو گیا!
```

---

## 🔌 API Endpoints (تمام Endpoints)

### 1. Health Check (صحت کی جانچ)
```
GET /health
```
API اچھی طرح کام کر رہا ہے یا نہیں دیکھیں۔

**جواب:**
```json
{
    "status": "کامیاب / Healthy",
    "message": "API صحیح طریقے سے کام کر رہا ہے",
    "models_loaded": true,
    "random_forest_ready": true,
    "logistic_regression_ready": true
}
```

---

### 2. Random Forest سے Prediction
```
POST /predict/random-forest
```

پھول کی قسم کی پیش گوئی کریں (Random Forest ماڈل استعمال کرتے ہوئے)

**Request Body:**
```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

**Response:**
```json
{
    "predicted_class": "Setosa",
    "predicted_class_number": 0,
    "probabilities": {
        "Setosa": 0.95,
        "Versicolor": 0.04,
        "Virginica": 0.01
    },
    "confidence": 0.95
}
```

---

### 3. Logistic Regression سے Prediction
```
POST /predict/logistic-regression
```

پھول کی قسم کی پیش گوئی کریں (Logistic Regression ماڈل استعمال کرتے ہوئے)

**Request Body:**
```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

**Response:** (Random Forest جیسا)

---

### 4. Batch Prediction (متعدد Predictions)
```
POST /predict/batch
```

بیک وقت متعدد پھولوں کی پیش گوئی کریں

**Request Body:**
```json
[
    {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    },
    {
        "sepal_length": 6.2,
        "sepal_width": 2.9,
        "petal_length": 4.3,
        "petal_width": 1.3
    }
]
```

**Response:**
```json
{
    "status": "کامیاب",
    "total_predictions": 2,
    "predictions": [
        {
            "flower_data": {...},
            "random_forest": {
                "predicted_class": "Setosa",
                "confidence": 0.95
            },
            "logistic_regression": {
                "predicted_class": "Setosa",
                "confidence": 0.92
            }
        },
        ...
    ]
}
```

---

### 5. Model Metrics (ماڈل کی کارکردگی)
```
GET /metrics
```

دونوں ماڈل کی Accuracy اور Confusion Matrix دیکھیں

**Response:**
```json
{
    "status": "کامیاب",
    "random_forest": {
        "accuracy": 1.0,
        "accuracy_percentage": "100.00%",
        "confusion_matrix": [[10, 0, 0], [0, 10, 0], [0, 0, 10]]
    },
    "logistic_regression": {
        "accuracy": 1.0,
        "accuracy_percentage": "100.00%",
        "confusion_matrix": [[10, 0, 0], [0, 10, 0], [0, 0, 10]]
    }
}
```

---

### 6. Feature Importance (خصوصیات کی اہمیت)
```
GET /feature-importance
```

کون سی خصوصیت سب سے ضروری ہے؟

**Response:**
```json
{
    "status": "کامیاب",
    "model": "Random Forest",
    "features": [
        {
            "feature_name": "petal width (cm)",
            "importance": 0.45,
            "importance_percentage": "45.23%"
        },
        {
            "feature_name": "petal length (cm)",
            "importance": 0.42,
            "importance_percentage": "42.15%"
        },
        ...
    ]
}
```

---

### 7. Data Information (ڈیٹا کی معلومات)
```
GET /data-info
```

Dataset کے بارے میں معلومات

**Response:**
```json
{
    "status": "کامیاب",
    "dataset_name": "Iris Dataset",
    "total_records": 150,
    "total_features": 4,
    "features": ["sepal length (cm)", "sepal width (cm)", ...],
    "target_classes": ["Setosa", "Versicolor", "Virginica"],
    "training_samples": 120,
    "testing_samples": 30,
    "train_test_split": "80-20"
}
```

---

### 8. Train Models (ماڈل کو دوبارہ ٹریننگ دیں)
```
POST /train
```

ماڈل کو دوبارہ ٹریننگ دیں

**Response:**
```json
{
    "status": "کامیاب / Success",
    "message": "ماڈل کو دوبارہ ٹریننگ دی گئی",
    "models_trained": ["Random Forest", "Logistic Regression"],
    "training_samples": 120,
    "testing_samples": 30
}
```

---

## 💻 Examples (مثالیں)

### Python میں مثال

```python
import requests
import json

API_URL = "http://localhost:8000"

# 1. Health Check
response = requests.get(f"{API_URL}/health")
print(response.json())

# 2. Random Forest سے Prediction
flower_data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

response = requests.post(
    f"{API_URL}/predict/random-forest",
    json=flower_data
)
print(response.json())

# 3. Metrics حاصل کریں
response = requests.get(f"{API_URL}/metrics")
metrics = response.json()
print(f"Random Forest Accuracy: {metrics['random_forest']['accuracy_percentage']}")

# 4. Feature Importance دیکھیں
response = requests.get(f"{API_URL}/feature-importance")
features = response.json()
for feature in features['features']:
    print(f"{feature['feature_name']}: {feature['importance_percentage']}")
```

### JavaScript میں مثال

```javascript
const API_URL = "http://localhost:8000";

// Random Forest Prediction
async function predictFlower() {
    const data = {
        sepal_length: 5.1,
        sepal_width: 3.5,
        petal_length: 1.4,
        petal_width: 0.2
    };
    
    const response = await fetch(`${API_URL}/predict/random-forest`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    
    const result = await response.json();
    console.log(`Predicted: ${result.predicted_class}`);
    console.log(`Confidence: ${result.confidence * 100}%`);
}

predictFlower();
```

### cURL میں مثال

```bash
# Health Check
curl http://localhost:8000/health

# Prediction
curl -X POST http://localhost:8000/predict/random-forest \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }'

# Get Metrics
curl http://localhost:8000/metrics

# Get Feature Importance
curl http://localhost:8000/feature-importance
```

---

## 🌐 Web Interface (ویب انٹرفیس)

### API کے ساتھ ویب انٹرفیس استعمال کریں

1. `api_frontend.html` فائل کو کسی بھی browser میں کھولیں
2. یا یہ کمانڈ چلائیں:

```bash
# Windows
start api_frontend.html

# Linux
xdg-open api_frontend.html

# Mac
open api_frontend.html
```

### ویب انٹرفیس میں کیا کر سکتے ہیں:
✅ Random Forest سے پیش گوئی  
✅ Logistic Regression سے پیش گوئی  
✅ ماڈل کی کارکردگی دیکھیں  
✅ خصوصیات کی اہمیت دیکھیں  
✅ ڈیٹا کی معلومات حاصل کریں  
✅ بہترین urdu انٹرفیس میں  

---

## 📚 API Documentation

جب API چل رہا ہو تو:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🔒 Security (سیکیورٹی)

یہ API test اور development کے لیے ہے۔ Production میں استعمال کرتے وقت:

1. CORS کو محدود کریں
2. API key شامل کریں
3. Rate limiting شامل کریں
4. HTTPS استعمال کریں

---

## 🐛 Troubleshooting (مسائل حل کریں)

### API شروع نہیں ہو رہا؟
```bash
# Port 8000 استعمال میں ہے تو مختلف port استعمال کریں
uvicorn supervised_learning_api:app --port 8001
```

### Dependencies انسٹال نہیں ہو رہی؟
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### CORS خرابی؟
یقینی بنائیں کہ API مکمل طور پر شروع ہو چکا ہے اور لوڈ ہو رہا ہے۔

---

## 📞 Support

کسی مسئلے کے لیے براہ براہ API logs دیکھیں۔

---

## 🎉 خلاصہ

یہ API:
- ✅ Supervised Learning کے لیے مکمل حل ہے
- ✅ متعدد prediction endpoints فراہم کرتا ہے
- ✅ ماڈل کی metrics دیتا ہے
- ✅ Batch predictions کی سہولت دیتا ہے
- ✅ آسان استعمال کے لیے Web Interface ہے
- ✅ Urdu میں مکمل تفصیل کے ساتھ

**آپ اسے اپنی website یا app میں کسی بھی جگہ استعمال کر سکتے ہیں!**

---

Made with ❤️ for Machine Learning learners
