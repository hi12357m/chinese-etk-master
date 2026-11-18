import time
import tomllib
from pathlib import Path
from openai import OpenAI

# 1. Read the API key from .streamlit/secrets.toml
secrets_path = Path(".streamlit/secrets.toml")
if not secrets_path.exists():
    print("❌ Could not find .streamlit/secrets.toml. Make sure you are in the main folder.")
    exit()

with open(secrets_path, "rb") as f:
    secrets = tomllib.load(f)
    
api_key = secrets.get("NVIDIA_API_KEY")
if not api_key:
    print("❌ NVIDIA_API_KEY not found in secrets.toml")
    exit()

# 2. Connect to NVIDIA
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

print("Fetching available models...")
# FIX: Removed limit=100, because the list() method doesn't accept it
models = client.models.list()
model_ids = [m.id for m in models.data]

# 3. Filter out image/vision models
chat_models = [m for m in model_ids if not any(x in m.lower() for x in ["vision", "embed", "image", "stable-diffusion"])]

print(f"Found {len(chat_models)} chat models. Testing speed...\n")

# 4. Test a short Chinese prompt
test_prompt = "請用繁體中文回答：什麼是貓？(請簡短回答)"
for model in chat_models:
    try:
        start_time = time.time()
        
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": test_prompt}],
            max_tokens=5,
            stream=True
        )
        
        first_word_time = None
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                first_word_time = time.time() - start_time
                break
                
        if first_word_time:
            print(f"✅ {model}: {first_word_time:.2f} seconds (First word)")
        else:
            print(f"⚠️ {model}: Connected, but returned no text.")
            
    except Exception as e:
        print(f"❌ {model}: Failed - {str(e)[:50]}...")