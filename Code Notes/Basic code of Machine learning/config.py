# Configuration file for Supervised Learning API
# API کی ترتیب کے لیے configuration فائل

# ===== API SETTINGS =====
# API کی ترتیبات

# API کا نام
API_NAME = "Supervised Learning Machine Learning API"
API_TITLE_URDU = "نگرانی سے سیکھنے کا API"

# API Version
API_VERSION = "1.0.0"

# API Host اور Port
API_HOST = "0.0.0.0"
API_PORT = 8000

# API Reload (development میں true، production میں false)
API_RELOAD = True

# ===== CORS SETTINGS =====
# Cross-Origin Resource Sharing کی ترتیبات

# CORS Allowed Origins (تمام sites کے لیے "*")
# Production میں specific origins استعمال کریں
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",      # Local React app
    "http://localhost:8080",      # Local Vue app
    "http://127.0.0.1:3000",      # Local development
    "https://yourdomain.com",     # Production domain
    "http://localhost:5500",      # Live Server extension
]

# CORS Allow Credentials
CORS_ALLOW_CREDENTIALS = True

# CORS Allow Methods
CORS_ALLOW_METHODS = ["*"]

# CORS Allow Headers
CORS_ALLOW_HEADERS = ["*"]

# ===== MODEL SETTINGS =====
# مشین لرننگ ماڈل کی ترتیبات

# Random Forest Parameters
RANDOM_FOREST_N_ESTIMATORS = 100
RANDOM_FOREST_RANDOM_STATE = 42
RANDOM_FOREST_MAX_DEPTH = None

# Logistic Regression Parameters
LOGISTIC_REGRESSION_MAX_ITER = 200
LOGISTIC_REGRESSION_RANDOM_STATE = 42

# ===== DATA SETTINGS =====
# ڈیٹا کی ترتیبات

# Training Test Split Ratio (80-20 means 80% training, 20% testing)
TRAIN_TEST_SPLIT_RATIO = 0.2

# Random State for reproducibility
RANDOM_STATE = 42

# Dataset Name
DATASET_NAME = "Iris Dataset"

# ===== LOGGING SETTINGS =====
# لاگنگ کی ترتیبات

# Log Level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL = "INFO"

# Enable Request Logging
ENABLE_REQUEST_LOGGING = True

# Enable Response Logging
ENABLE_RESPONSE_LOGGING = True

# ===== SECURITY SETTINGS =====
# سیکیورٹی کی ترتیبات

# Enable HTTPS (production میں true)
ENABLE_HTTPS = False

# API Key (اگر API key استعمال کریں تو)
API_KEY_ENABLED = False
API_KEY = "your-secret-api-key-here"

# Rate Limiting (requests per minute)
RATE_LIMIT_ENABLED = False
RATE_LIMIT_REQUESTS_PER_MINUTE = 60

# ===== DOCUMENTATION SETTINGS =====
# دستاویزات کی ترتیبات

# Enable Swagger UI
ENABLE_SWAGGER = True

# Enable ReDoc
ENABLE_REDOC = True

# Documentation Title
DOC_TITLE = "Supervised Learning API"

# Documentation Description
DOC_DESCRIPTION = "Machine Learning API برائے نگرانی سے سیکھنے کی پیش گوئی"

# ===== PERFORMANCE SETTINGS =====
# کارکردگی کی ترتیبات

# Workers (0 = auto)
WORKERS = 1

# Request Timeout (seconds)
REQUEST_TIMEOUT = 30

# Keep Alive Timeout
KEEP_ALIVE_TIMEOUT = 5

# ===== DATABASE SETTINGS =====
# ڈیٹابیس کی ترتیبات (اگر ضروری ہو تو)

DATABASE_URL = "sqlite:///./ml_api.db"
DATABASE_ECHO = False

# ===== MODEL PATHS =====
# ماڈل کے paths

# Path to save trained models
MODELS_SAVE_PATH = "./models"
RANDOM_FOREST_MODEL_PATH = "./models/random_forest_model.pkl"
LOGISTIC_REGRESSION_MODEL_PATH = "./models/logistic_regression_model.pkl"

# ===== CACHE SETTINGS =====
# کیش کی ترتیبات

ENABLE_CACHING = True
CACHE_TTL_SECONDS = 3600  # 1 hour

# ===== NOTIFICATION SETTINGS =====
# اطلاع کی ترتیبات

ENABLE_NOTIFICATIONS = False
NOTIFICATION_EMAIL = "admin@example.com"

# ===== FILE UPLOAD SETTINGS =====
# فائل upload کی ترتیبات

MAX_UPLOAD_SIZE_MB = 100
ALLOWED_FILE_TYPES = ["csv", "xlsx", "json"]

# ===== EXTERNAL API SETTINGS =====
# بیرونی API کی ترتیبات

# Webhook URL (اگر کوئی external service notify کریں تو)
WEBHOOK_URL = "https://example.com/webhook"
WEBHOOK_ENABLED = False

# ===== EMAIL SETTINGS =====
# ای میل کی ترتیبات

EMAIL_ENABLED = False
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your-email@gmail.com"
EMAIL_PASSWORD = "your-password"
EMAIL_FROM = "noreply@example.com"

# ===== ENVIRONMENT =====
# ماحول (development/production)

ENVIRONMENT = "development"  # یا "production"

# Debug Mode (development میں True, production میں False)
DEBUG_MODE = True

# ===== DEFAULT VALUES =====
# ڈیفالٹ اقدار

DEFAULT_SEPAL_LENGTH = 5.1
DEFAULT_SEPAL_WIDTH = 3.5
DEFAULT_PETAL_LENGTH = 1.4
DEFAULT_PETAL_WIDTH = 0.2

# ===== FEATURE NAMES =====
# خصوصیات کے نام

FEATURE_NAMES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

# ===== TARGET NAMES =====
# ہدف کے نام

TARGET_NAMES = [
    "Setosa",
    "Versicolor",
    "Virginica"
]

# ===== METRIC THRESHOLDS =====
# کارکردگی کی حدود

GOOD_ACCURACY_THRESHOLD = 0.85
EXCELLENT_ACCURACY_THRESHOLD = 0.95

# ===== BATCH PREDICTION SETTINGS =====
# متعدد پیش گوئی کی ترتیبات

MAX_BATCH_SIZE = 1000
MIN_BATCH_SIZE = 1

# ===== PREDICTION CONFIDENCE THRESHOLD =====
# پیش گوئی کے اعتماد کی حد

MIN_CONFIDENCE_THRESHOLD = 0.5

# ===== API VERSIONING =====
# API کی versioning

CURRENT_API_VERSION = "v1"
SUPPORTED_API_VERSIONS = ["v1"]

# ===== RESPONSE SETTINGS =====
# جواب کی ترتیبات

INCLUDE_TIMESTAMP_IN_RESPONSE = True
INCLUDE_REQUEST_ID_IN_RESPONSE = True
INCLUDE_PROCESSING_TIME_IN_RESPONSE = True
