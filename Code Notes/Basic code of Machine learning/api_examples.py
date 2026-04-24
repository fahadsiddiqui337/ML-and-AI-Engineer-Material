"""
API استعمال کرنے کی مثالیں
Examples of using the Supervised Learning API
"""

import requests
import json
from typing import Dict, Any

# API کا بنیادی URL
API_URL = "http://localhost:8000"

# رنگین پرنٹنگ کے لیے
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text: str):
    """Header پرنٹ کریں"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}{Colors.END}\n")

def print_success(text: str):
    """کامیابی کا پیغام"""
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_info(text: str):
    """معلومات پرنٹ کریں"""
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

def print_error(text: str):
    """خرابی کا پیغام"""
    print(f"{Colors.RED}❌ {text}{Colors.END}")

# ====================== مثالیں ======================

def example_1_health_check():
    """مثال 1: Health Check - API کی جانچ"""
    print_header("مثال 1: API کی صحت کی جانچ")
    
    try:
        response = requests.get(f"{API_URL}/health")
        data = response.json()
        
        print_success(f"Status: {data['status']}")
        print_info(f"Message: {data['message']}")
        print_info(f"Models Loaded: {data['models_loaded']}")
        
        return data
    except Exception as e:
        print_error(f"API سے رابطہ نہیں ہو سکا: {str(e)}")
        return None

def example_2_predict_random_forest():
    """مثال 2: Random Forest سے Prediction"""
    print_header("مثال 2: Random Forest سے پیش گوئی")
    
    # پھول کی معلومات
    flower = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    
    print_info("پھول کی معلومات:")
    print(f"  Sepal Length: {flower['sepal_length']} cm")
    print(f"  Sepal Width: {flower['sepal_width']} cm")
    print(f"  Petal Length: {flower['petal_length']} cm")
    print(f"  Petal Width: {flower['petal_width']} cm")
    
    try:
        response = requests.post(
            f"{API_URL}/predict/random-forest",
            json=flower
        )
        
        if response.status_code == 200:
            data = response.json()
            
            print_success(f"پیش گوئی شدہ قسم: {data['predicted_class']}")
            print_info(f"معاون: {data['confidence']*100:.2f}%")
            print_info("ہر قسم کا امکان:")
            
            for class_name, probability in data['probabilities'].items():
                bar = "█" * int(probability * 20)
                print(f"  {class_name:12} {bar} {probability*100:.2f}%")
            
            return data
        else:
            print_error(f"خرابی: {response.status_code}")
    except Exception as e:
        print_error(f"خرابی: {str(e)}")
    
    return None

def example_3_predict_logistic_regression():
    """مثال 3: Logistic Regression سے Prediction"""
    print_header("مثال 3: Logistic Regression سے پیش گوئی")
    
    # مختلف پھول
    flower = {
        "sepal_length": 6.5,
        "sepal_width": 3.0,
        "petal_length": 5.5,
        "petal_width": 1.8
    }
    
    print_info("پھول کی معلومات:")
    print(f"  Sepal Length: {flower['sepal_length']} cm")
    print(f"  Sepal Width: {flower['sepal_width']} cm")
    print(f"  Petal Length: {flower['petal_length']} cm")
    print(f"  Petal Width: {flower['petal_width']} cm")
    
    try:
        response = requests.post(
            f"{API_URL}/predict/logistic-regression",
            json=flower
        )
        
        if response.status_code == 200:
            data = response.json()
            
            print_success(f"پیش گوئی شدہ قسم: {data['predicted_class']}")
            print_info(f"معاون: {data['confidence']*100:.2f}%")
            print_info("ہر قسم کا امکان:")
            
            for class_name, probability in data['probabilities'].items():
                bar = "█" * int(probability * 20)
                print(f"  {class_name:12} {bar} {probability*100:.2f}%")
            
            return data
        else:
            print_error(f"خرابی: {response.status_code}")
    except Exception as e:
        print_error(f"خرابی: {str(e)}")
    
    return None

def example_4_batch_prediction():
    """مثال 4: متعدد پھولوں کی بیک وقت Prediction"""
    print_header("مثال 4: متعدد پھولوں کی پیش گوئی")
    
    flowers = [
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
        },
        {
            "sepal_length": 7.2,
            "sepal_width": 3.2,
            "petal_length": 6.0,
            "petal_width": 1.8
        }
    ]
    
    print_info(f"کل {len(flowers)} پھولوں کی پیش گوئی کی جا رہی ہے...")
    
    try:
        response = requests.post(
            f"{API_URL}/predict/batch",
            json=flowers
        )
        
        if response.status_code == 200:
            data = response.json()
            
            print_success(f"کل پیش گوئیاں: {data['total_predictions']}")
            
            for i, prediction in enumerate(data['predictions'], 1):
                print(f"\n  پھول #{i}:")
                print(f"    Random Forest: {prediction['random_forest']['predicted_class']} ({prediction['random_forest']['confidence']*100:.2f}%)")
                print(f"    Logistic Regression: {prediction['logistic_regression']['predicted_class']} ({prediction['logistic_regression']['confidence']*100:.2f}%)")
            
            return data
        else:
            print_error(f"خرابی: {response.status_code}")
    except Exception as e:
        print_error(f"خرابی: {str(e)}")
    
    return None

def example_5_get_metrics():
    """مثال 5: ماڈل کی کارکردگی دیکھیں"""
    print_header("مثال 5: ماڈل کی کارکردگی")
    
    try:
        response = requests.get(f"{API_URL}/metrics")
        
        if response.status_code == 200:
            data = response.json()
            
            print_info("Random Forest کی Accuracy:")
            rf_acc = data['random_forest']['accuracy']
            print(f"  {data['random_forest']['accuracy_percentage']} ({rf_acc})")
            
            print_info("\nLogistic Regression کی Accuracy:")
            lr_acc = data['logistic_regression']['accuracy']
            print(f"  {data['logistic_regression']['accuracy_percentage']} ({lr_acc})")
            
            if rf_acc > lr_acc:
                print_success("Random Forest زیادہ بہتر ہے")
            elif lr_acc > rf_acc:
                print_success("Logistic Regression زیادہ بہتر ہے")
            else:
                print_info("دونوں برابر ہیں")
            
            return data
        else:
            print_error(f"خرابی: {response.status_code}")
    except Exception as e:
        print_error(f"خرابی: {str(e)}")
    
    return None

def example_6_feature_importance():
    """مثال 6: خصوصیات کی اہمیت"""
    print_header("مثال 6: خصوصیات کی اہمیت")
    
    try:
        response = requests.get(f"{API_URL}/feature-importance")
        
        if response.status_code == 200:
            data = response.json()
            
            print_info("خصوصیات کی ترتیب (سب سے اہم سے):")
            
            for i, feature in enumerate(data['features'], 1):
                bar = "█" * int(feature['importance'] * 30)
                print(f"  {i}. {feature['feature_name']:20} {bar} {feature['importance_percentage']}")
            
            return data
        else:
            print_error(f"خرابی: {response.status_code}")
    except Exception as e:
        print_error(f"خرابی: {str(e)}")
    
    return None

def example_7_data_info():
    """مثال 7: ڈیٹا کی معلومات"""
    print_header("مثال 7: ڈیٹا کی معلومات")
    
    try:
        response = requests.get(f"{API_URL}/data-info")
        
        if response.status_code == 200:
            data = response.json()
            
            print_info(f"Dataset: {data['dataset_name']}")
            print_info(f"کل ریکارڈز: {data['total_records']}")
            print_info(f"کل خصوصیات: {data['total_features']}")
            print_info(f"Training Samples: {data['training_samples']}")
            print_info(f"Testing Samples: {data['testing_samples']}")
            print_info(f"Split Ratio: {data['train_test_split']}")
            
            print_info("\nخصوصیات:")
            for feature in data['features']:
                print(f"  • {feature}")
            
            print_info("\nTarget Classes:")
            for target in data['target_classes']:
                print(f"  • {target}")
            
            return data
        else:
            print_error(f"خرابی: {response.status_code}")
    except Exception as e:
        print_error(f"خرابی: {str(e)}")
    
    return None

def example_8_retrain_models():
    """مثال 8: ماڈل کو دوبارہ ٹریننگ دیں"""
    print_header("مثال 8: ماڈل کو دوبارہ ٹریننگ دیں")
    
    try:
        response = requests.post(f"{API_URL}/train")
        
        if response.status_code == 200:
            data = response.json()
            
            print_success(f"Status: {data['status']}")
            print_info(f"Message: {data['message']}")
            print_info(f"Models Trained: {', '.join(data['models_trained'])}")
            print_info(f"Training Samples: {data['training_samples']}")
            print_info(f"Testing Samples: {data['testing_samples']}")
            
            return data
        else:
            print_error(f"خرابی: {response.status_code}")
    except Exception as e:
        print_error(f"خرابی: {str(e)}")
    
    return None

# ====================== مرکزی فنکشن ======================

def main():
    """تمام مثالیں چلائیں"""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}")
    print("╔═════════════════════════════════════════════════════════╗")
    print("║  Supervised Learning API - استعمال کی مثالیں           ║")
    print("║  نگرانی سے سیکھنے کا API                              ║")
    print("╚═════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}")
    
    # پہلے health check کریں
    if not example_1_health_check():
        print_error("\n❌ API شروع نہیں ہے!")
        print_info("براہ کرم یہ کمانڈ چلائیں:")
        print_info("  python supervised_learning_api.py")
        return
    
    # باقی مثالیں چلائیں
    example_2_predict_random_forest()
    example_3_predict_logistic_regression()
    example_4_batch_prediction()
    example_5_get_metrics()
    example_6_feature_importance()
    example_7_data_info()
    example_8_retrain_models()
    
    # خلاصہ
    print_header("✨ تمام مثالیں مکمل ہو گئیں!")
    print_success("API صحیح طریقے سے کام کر رہا ہے")
    print_info("\nآپ اب اسے اپنی website یا app میں استعمال کر سکتے ہیں!")
    print_info("مزید معلومات کے لیے API_README.md دیکھیں\n")

if __name__ == "__main__":
    main()
