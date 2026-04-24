# 🚀 Quick Start Guide - فوری شروعات کی رہنمائی

## 5 منٹ میں API چلا دیں!

### Step 1️⃣ : Requirements انسٹال کریں

```bash
pip install -r requirements.txt
```

### Step 2️⃣ : API شروع کریں

```bash
python supervised_learning_api.py
```

آپ کو یہ نظر آئے گا:
```
🚀 Supervised Learning API شروع ہو رہا ہے...
📍 http://localhost:8000 پر سنو
📚 Documentation: http://localhost:8000/docs
✅ ماڈل تیار ہو گیا!
```

### Step 3️⃣ : API کو ٹیسٹ کریں

#### آپشن A: ویب انٹرفیس استعمال کریں

`api_frontend.html` فائل کو browser میں کھولیں۔ یہ بہت آسان ہے!

#### آپشن B: Python میں ٹیسٹ کریں

نئی ٹرمینل کھولیں اور چلائیں:

```bash
python api_examples.py
```

#### آپشن C: cURL استعمال کریں

```bash
# Test کریں
curl http://localhost:8000/health

# Prediction کریں
curl -X POST http://localhost:8000/predict/random-forest \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

---

## 📌 تمام Endpoints کا مختصر ریفرنس

| Endpoint | طریقہ | مقصد |
|----------|------|------|
| `/health` | GET | API کی جانچ |
| `/predict/random-forest` | POST | Random Forest سے پیش گوئی |
| `/predict/logistic-regression` | POST | Logistic Regression سے پیش گوئی |
| `/predict/batch` | POST | متعدد predictions |
| `/metrics` | GET | ماڈل کی کارکردگی |
| `/feature-importance` | GET | خصوصیات کی اہمیت |
| `/data-info` | GET | ڈیٹا کی معلومات |
| `/train` | POST | ماڈل کو دوبارہ ٹریننگ دیں |

---

## 💡 بہترین مثالیں

### مثال 1: Python میں

```python
import requests

# API کو کال کریں
response = requests.post(
    'http://localhost:8000/predict/random-forest',
    json={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
)

# نتیجہ دیکھیں
result = response.json()
print(f"پیش گوئی: {result['predicted_class']}")
print(f"معاون: {result['confidence']*100:.2f}%")
```

### مثال 2: JavaScript میں

```javascript
// API کو کال کریں
fetch('http://localhost:8000/predict/random-forest', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        sepal_length: 5.1,
        sepal_width: 3.5,
        petal_length: 1.4,
        petal_width: 0.2
    })
})
.then(response => response.json())
.then(data => {
    console.log(`پیش گوئی: ${data.predicted_class}`);
    console.log(`معاون: ${(data.confidence*100).toFixed(2)}%`);
});
```

---

## 🐛 عام مسائل

### مسئلہ 1: "Connection refused"
**حل:** یقینی بنائیں کہ API چل رہا ہے
```bash
python supervised_learning_api.py
```

### مسئلہ 2: "Port 8000 already in use"
**حل:** مختلف port استعمال کریں
```bash
uvicorn supervised_learning_api:app --port 8001
```

### مسئلہ 3: ImportError
**حل:** Dependencies دوبارہ انسٹال کریں
```bash
pip install -r requirements.txt --force-reinstall
```

---

## 📚 مزید معلومات

- **مکمل API Reference**: `API_README.md` دیکھیں
- **Notebook میں code**: `Supervised_Learning_Project.ipynb`
- **مثالیں**: `api_examples.py` چلائیں

---

## ✅ اگلے قدم

1. ✅ API چلا دیا
2. ✅ ویب انٹرفیس کھول دیا
3. ✅ پہلی prediction کر دی
4. 🎯 اب اسے اپنی website/app میں لگائیں!

---

## 🎉 مبارک ہو!

آپ نے اپنا پہلا Machine Learning API بنا لیا! 🚀

اب آپ اسے:
- 🌐 Website میں embed کر سکتے ہیں
- 📱 Mobile App میں استعمال کر سکتے ہیں
- ☁️ Cloud میں deploy کر سکتے ہیں
- 🔧 اپنی ضروریات کے مطابق modify کر سکتے ہیں

**خوش رہیں اور سیکھتے رہیں! 📖**
