"""
Supervised Learning Machine Learning API
نگرانی سے سیکھنے کا API
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_squared_error
import json
import joblib
import os

# FastAPI App کو شروع کریں
app = FastAPI(
    title="Supervised Learning API",
    description="Machine Learning API - نگرانی سے سیکھنے کا API",
    version="1.0.0"
)

# CORS کو Enable کریں (تاکہ کوئی بھی website استعمال کر سکے)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # تمام websites کو اجازت دیں
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Variables - مشین لرننگ ماڈل
rf_model = None
lr_model = None
X_train = None
X_test = None
y_train = None
y_test = None
iris_data = None
feature_names = None
target_names = ["Setosa", "Versicolor", "Virginica"]
model_metrics = {}

# ================== Pydantic Models (ڈیٹا کی تعریف) ==================

class FlowerData(BaseModel):
    """نئے پھول کی معلومات"""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    """پیش گوئی کا جواب"""
    predicted_class: str
    predicted_class_number: int
    probabilities: Dict[str, float]
    confidence: float

class ModelMetrics(BaseModel):
    """ماڈل کی کارکردگی"""
    accuracy: float
    model_name: str

class FeatureImportance(BaseModel):
    """خصوصیات کی اہمیت"""
    feature_name: str
    importance: float

# ================== Helper Functions ==================

def load_and_prepare_data():
    """ڈیٹا کو لوڈ اور تیار کریں"""
    global rf_model, lr_model, X_train, X_test, y_train, y_test, iris_data, feature_names
    
    # Iris dataset کو لوڈ کریں
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    iris_data = df
    feature_names = iris.feature_names
    
    # Features اور Target کو الگ کریں
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Training اور Testing میں تقسیم کریں (80-20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Random Forest Model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Logistic Regression Model
    lr_model = LogisticRegression(max_iter=200, random_state=42)
    lr_model.fit(X_train, y_train)
    
    return True

def calculate_metrics():
    """ماڈل کی metrics کا حساب لگائیں"""
    global model_metrics, rf_model, lr_model, X_test, y_test
    
    # Random Forest metrics
    y_pred_rf = rf_model.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    
    # Logistic Regression metrics
    y_pred_lr = lr_model.predict(X_test)
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    
    model_metrics = {
        "random_forest": {
            "accuracy": float(accuracy_rf),
            "confusion_matrix": confusion_matrix(y_test, y_pred_rf).tolist(),
            "predictions": y_pred_rf.tolist(),
            "actual": y_test.tolist()
        },
        "logistic_regression": {
            "accuracy": float(accuracy_lr),
            "confusion_matrix": confusion_matrix(y_test, y_pred_lr).tolist(),
            "predictions": y_pred_lr.tolist(),
            "actual": y_test.tolist()
        }
    }

# ================== API Endpoints ==================

@app.on_event("startup")
async def startup_event():
    """جب API شروع ہو تو ڈیٹا لوڈ کریں"""
    print("🚀 API شروع ہو رہا ہے... Supervised Learning Models لوڈ ہو رہے ہیں...")
    load_and_prepare_data()
    calculate_metrics()
    print("✅ ماڈل تیار ہو گیا!")

# ================ Home Endpoint ================

@app.get("/")
async def root():
    """خوش آمدید - مرحبا"""
    return {
        "message": "خوش آمدید / Welcome to Supervised Learning API",
        "welcome": "نگرانی سے سیکھنے کا API میں آپ کا خوش آمدید",
        "version": "1.0.0",
        "endpoints": {
            "train": "POST /train - ماڈل کو دوبارہ ٹریننگ دیں",
            "predict_rf": "POST /predict/random-forest - Random Forest سے پیش گوئی کریں",
            "predict_lr": "POST /predict/logistic-regression - Logistic Regression سے پیش گوئی کریں",
            "metrics": "GET /metrics - ماڈل کی کارکردگی دیکھیں",
            "feature_importance": "GET /feature-importance - خصوصیات کی اہمیت دیکھیں",
            "data_info": "GET /data-info - ڈیٹا کی معلومات دیکھیں"
        }
    }

# ================ Training Endpoint ================

@app.post("/train")
async def train_model():
    """
    ماڈل کو دوبارہ ٹریننگ دیں
    پہلے سے موجود ماڈل کو دوبارہ تربیت دیں
    """
    try:
        load_and_prepare_data()
        calculate_metrics()
        return {
            "status": "کامیاب / Success",
            "message": "ماڈل کو دوبارہ ٹریننگ دی گئی",
            "models_trained": ["Random Forest", "Logistic Regression"],
            "training_samples": len(X_train),
            "testing_samples": len(X_test)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خرابی: {str(e)}")

# ================ Prediction Endpoints ================

@app.post("/predict/random-forest", response_model=PredictionResponse)
async def predict_random_forest(flower: FlowerData):
    """
    Random Forest سے پیش گوئی کریں
    Iris پھول کی قسم کی پیش گوئی کریں
    
    مثال:
    {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    """
    try:
        # Input data کو Array میں تبدیل کریں
        input_data = np.array([[
            flower.sepal_length,
            flower.sepal_width,
            flower.petal_length,
            flower.petal_width
        ]])
        
        # پیش گوئی کریں
        prediction = rf_model.predict(input_data)[0]
        probabilities = rf_model.predict_proba(input_data)[0]
        
        # نتیجہ تیار کریں
        return PredictionResponse(
            predicted_class=target_names[prediction],
            predicted_class_number=int(prediction),
            probabilities={
                target_names[i]: float(prob)
                for i, prob in enumerate(probabilities)
            },
            confidence=float(probabilities[prediction])
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"پیش گوئی میں خرابی: {str(e)}")

@app.post("/predict/logistic-regression", response_model=PredictionResponse)
async def predict_logistic_regression(flower: FlowerData):
    """
    Logistic Regression سے پیش گوئی کریں
    Iris پھول کی قسم کی پیش گوئی کریں
    """
    try:
        # Input data کو Array میں تبدیل کریں
        input_data = np.array([[
            flower.sepal_length,
            flower.sepal_width,
            flower.petal_length,
            flower.petal_width
        ]])
        
        # پیش گوئی کریں
        prediction = lr_model.predict(input_data)[0]
        probabilities = lr_model.predict_proba(input_data)[0]
        
        # نتیجہ تیار کریں
        return PredictionResponse(
            predicted_class=target_names[prediction],
            predicted_class_number=int(prediction),
            probabilities={
                target_names[i]: float(prob)
                for i, prob in enumerate(probabilities)
            },
            confidence=float(probabilities[prediction])
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"پیش گوئی میں خرابی: {str(e)}")

# ================ Metrics Endpoint ================

@app.get("/metrics")
async def get_metrics():
    """
    ماڈل کی کارکردگی دیکھیں
    دونوں ماڈل کی Accuracy اور Confusion Matrix دیکھیں
    """
    try:
        if not model_metrics:
            calculate_metrics()
        
        return {
            "status": "کامیاب",
            "random_forest": {
                "accuracy": model_metrics["random_forest"]["accuracy"],
                "accuracy_percentage": f"{model_metrics['random_forest']['accuracy']*100:.2f}%",
                "confusion_matrix": model_metrics["random_forest"]["confusion_matrix"]
            },
            "logistic_regression": {
                "accuracy": model_metrics["logistic_regression"]["accuracy"],
                "accuracy_percentage": f"{model_metrics['logistic_regression']['accuracy']*100:.2f}%",
                "confusion_matrix": model_metrics["logistic_regression"]["confusion_matrix"]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خرابی: {str(e)}")

# ================ Feature Importance Endpoint ================

@app.get("/feature-importance")
async def get_feature_importance():
    """
    خصوصیات کی اہمیت دیکھیں
    کون سی خصوصیت سب سے ضروری ہے؟
    """
    try:
        importance = rf_model.feature_importances_
        importance_list = [
            {
                "feature_name": feature_names[i],
                "importance": float(importance[i]),
                "importance_percentage": f"{importance[i]*100:.2f}%"
            }
            for i in range(len(feature_names))
        ]
        
        # اہمیت کے لحاظ سے ترتیب دیں
        importance_list.sort(key=lambda x: x["importance"], reverse=True)
        
        return {
            "status": "کامیاب",
            "model": "Random Forest",
            "features": importance_list,
            "message": "خصوصیات کی اہمیت (سب سے اہم سے سب سے کم اہم)"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خرابی: {str(e)}")

# ================ Data Info Endpoint ================

@app.get("/data-info")
async def get_data_info():
    """
    ڈیٹا کی معلومات دیکھیں
    Dataset کے بارے میں معلومات
    """
    try:
        return {
            "status": "کامیاب",
            "dataset_name": "Iris Dataset",
            "total_records": len(iris_data),
            "total_features": len(feature_names),
            "features": list(feature_names),
            "target_classes": target_names,
            "training_samples": len(X_train),
            "testing_samples": len(X_test),
            "train_test_split": "80-20",
            "data_statistics": {
                "mean": iris_data.drop('target', axis=1).mean().to_dict(),
                "std": iris_data.drop('target', axis=1).std().to_dict(),
                "min": iris_data.drop('target', axis=1).min().to_dict(),
                "max": iris_data.drop('target', axis=1).max().to_dict()
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خرابی: {str(e)}")

# ================ Batch Prediction Endpoint ================

@app.post("/predict/batch")
async def batch_predict(flowers: List[FlowerData]):
    """
    متعدد پھولوں کی بیک وقت پیش گوئی کریں
    Batch Prediction کریں
    """
    try:
        results = []
        
        for flower in flowers:
            input_data = np.array([[
                flower.sepal_length,
                flower.sepal_width,
                flower.petal_length,
                flower.petal_width
            ]])
            
            # Random Forest پیش گوئی
            prediction_rf = rf_model.predict(input_data)[0]
            probs_rf = rf_model.predict_proba(input_data)[0]
            
            # Logistic Regression پیش گوئی
            prediction_lr = lr_model.predict(input_data)[0]
            probs_lr = lr_model.predict_proba(input_data)[0]
            
            results.append({
                "flower_data": {
                    "sepal_length": flower.sepal_length,
                    "sepal_width": flower.sepal_width,
                    "petal_length": flower.petal_length,
                    "petal_width": flower.petal_width
                },
                "random_forest": {
                    "predicted_class": target_names[prediction_rf],
                    "confidence": float(probs_rf[prediction_rf])
                },
                "logistic_regression": {
                    "predicted_class": target_names[prediction_lr],
                    "confidence": float(probs_lr[prediction_lr])
                }
            })
        
        return {
            "status": "کامیاب",
            "total_predictions": len(results),
            "predictions": results
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"پیش گوئی میں خرابی: {str(e)}")

# ================ Health Check ================

@app.get("/health")
async def health_check():
    """API کی صحت جانچیں"""
    return {
        "status": "کامیاب / Healthy",
        "message": "API صحیح طریقے سے کام کر رہا ہے",
        "models_loaded": True,
        "random_forest_ready": rf_model is not None,
        "logistic_regression_ready": lr_model is not None
    }

# ================ Error Handler ================

@app.get("/docs")
async def get_docs():
    """API documentation"""
    return {
        "message": "تمام endpoints کو دیکھنے کے لیے /docs یا /redoc پر جائیں"
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Supervised Learning API شروع ہو رہا ہے...")
    print("📍 http://localhost:8000 پر سنو")
    print("📚 Documentation: http://localhost:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
