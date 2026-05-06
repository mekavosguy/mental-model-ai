# Quick Start Guide - Mental Model Hub

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```powershell
cd c:\Users\Nebin John\Downloads\mental
pip install -r requirements.txt
```

### Step 2: Start the Backend

**Option A - Double-click (Windows):**

- Double-click `run.bat` or `run.ps1`

**Option B - Manual (PowerShell/CMD):**

```powershell
python app.py
```

You should see:

```
🚀 Mental Model Hub Backend
📡 API running on http://0.0.0.0:5000
🔑 Using NVIDIA API endpoint
🤖 Model: openai/gpt-oss-120b
```

### Step 3: Open the App

- Open `index.html` in your web browser
- Or navigate to: `file:///c:/Users/Nebin%20John/Downloads/mental/index.html`

## ✅ Testing It Works

1. Go to "AI Explain" tab
2. Type: "Why do people procrastinate?"
3. Click "Analyze with models ↗"
4. Wait 5-10 seconds for response
5. See mental models analysis!

## 📁 What Each File Does

| File                  | Purpose                                       |
| --------------------- | --------------------------------------------- |
| `index.html`          | Frontend - beautiful UI for the app           |
| `app.py`              | Backend - Flask server handling API requests  |
| `config.py`           | Configuration - API settings, prompts, models |
| `requirements.txt`    | Python dependencies to install                |
| `.env`                | API key storage (keep this secret!)           |
| `run.bat` / `run.ps1` | Quick start scripts for Windows               |
| `README.md`           | Full documentation                            |

## 🔧 Customize

### Change the AI Model

Edit `config.py`:

```python
NVIDIA_MODEL = "openai/gpt-oss-120b"  # Change this line
```

Available models: https://integrate.api.nvidia.com/

### Adjust AI Behavior

Edit `config.py`:

```python
AI_TEMPERATURE = 0.7  # Lower = deterministic, Higher = creative
AI_TOP_P = 0.9        # Diversity of output
AI_MAX_TOKENS = 1024  # Length of response
```

### Add/Edit Mental Models

Edit `config.py` - MENTAL_MODELS list:

```python
MENTAL_MODELS = [
    "Your Model: Description here",
    # ... more models
]
```

## 🐛 Troubleshooting

**Backend won't start?**

```powershell
# Make sure you're in the right directory
cd c:\Users\Nebin John\Downloads\mental

# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Run with Python explicitly
python app.py
```

**"Cannot connect to server" error?**

- Check backend is running (you should see the startup message)
- Make sure you're using http://localhost:5000 (not https)
- Check Windows firewall allows Python

**API key error?**

- Verify your NVIDIA API key in `.env`
- It should start with `nvapi-`
- Get one from: https://integrate.api.nvidia.com

**Slow responses?**

- NVIDIA API takes 5-10 seconds - this is normal
- The UI shows loading dots while waiting
- First request might be slower due to model loading

## 📊 How It Works

```
Frontend (Browser)
       ↓
   User types
       ↓
JavaScript fetch()
       ↓
Backend (Flask)
       ↓
NVIDIA API Request
       ↓
GPT-OSS-120B Model
       ↓
Analysis Response
       ↓
Backend returns JSON
       ↓
Frontend displays HTML
```

## 🎯 Next Steps

1. **Explore** - Try different mental models in the explore tab
2. **Experiment** - Test AI analysis with different scenarios
3. **Customize** - Add your own mental models to the list
4. **Deploy** - Use Gunicorn/Docker for production

## 📚 Learn More

- **NVIDIA API Docs**: https://integrate.api.nvidia.com/
- **Flask Docs**: https://flask.palletsprojects.com/
- **Mental Models**: https://www.mentalmodeldepot.com/

---

**Enjoy thinking through mental models!** 🧠
