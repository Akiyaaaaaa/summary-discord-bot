import os
from google import genai
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY tidak ditemukan. Pastikan file .env sudah benar.")
    exit()

# Inisialisasi Gemini Client
client = genai.Client(api_key=api_key)

print("🔍 Sedang mengambil daftar model yang tersedia...")
print("-" * 40)

try:
    # Langsung print nama modelnya
    for model in client.models.list():
        print(f"✅ {model.name}")
            
    print("-" * 40)
    print("Selesai! Silakan cari model yang mengandung kata 'flash'.")
    
except Exception as e:
    print(f"❌ Terjadi kesalahan saat mengambil model: {e}")