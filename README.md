# Mental Model Hub

A web application that helps you understand complex situations through mental models. The app combines a beautiful frontend with an AI-powered backend using NVIDIA's API.

## Features

- **12 Mental Models** covering Psychology, Business, Economics, and Decision Making
- **Search & Filter** by category or keyword
- **Save Favorites** - bookmark models you want to revisit
- **AI Analysis** - describe any situation and get insights using relevant mental models
- **Beautiful UI** with dark mode support

## Project Structure

```
mental/
├── index.html          # Frontend (HTML, CSS, JavaScript)
├── app.py              # Flask backend with NVIDIA API integration
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API keys)
└── README.md          # This file
```

## Quick Start

### Prerequisites

- Python 3.8+
- NVIDIA API key (from https://integrate.api.nvidia.com)

### 1. Setup Backend

```bash
# Navigate to the project directory
cd c:\Users\Nebin John\Downloads\mental

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key

Edit the `.env` file and add your NVIDIA API key:

```
NVIDIA_API_KEY=your_api_key_here
```

### 3. Run the Backend

```bash
python app.py
```

You should see:

```
🚀 Mental Model Hub Backend
📡 API running on http://localhost:5000
🔑 Using NVIDIA API endpoint
```

### 4. Open the Frontend

- Open `index.html` in your browser (or use a local server)
- The app will connect to the backend at `http://localhost:5000`

## API Endpoints

### POST `/api/analyze`

Analyzes a situation using relevant mental models.

**Request:**

```json
{
  "text": "Why do people keep checking their phone compulsively?"
}
```

**Response:**

```json
{
  "analysis": "<strong>Availability Heuristic</strong><br>People overestimate how likely they are to miss something important because recent notifications are vivid in memory..."
}
```

### GET `/api/health`

Health check endpoint.

**Response:**

```json
{
  "status": "ok"
}
```

## How It Works

1. **Frontend** - User enters a situation in the AI Explain section
2. **Request** - Frontend sends text to backend via `/api/analyze` endpoint
3. **Processing** - Backend uses NVIDIA's GPT model to analyze the situation
4. **AI Response** - AI identifies 2-3 relevant mental models and explains how they apply
5. **Display** - Response is shown in beautiful HTML format in the frontend

## Customization

### Change the Model

Edit `app.py` line with:

```python
model="openai/gpt-oss-120b",  # Change this to another NVIDIA model
```

Available models at: https://integrate.api.nvidia.com/

### Adjust Temperature & Parameters

In `app.py`, modify:

```python
temperature=0.7,  # Lower = more deterministic, Higher = more creative
top_p=0.9,        # Nucleus sampling
max_tokens=1024,  # Max response length
```

### Add More Mental Models

Edit the `MENTAL_MODELS` list in `app.py` to include additional models, or modify the prompt to create new analyses.

## Deployment

### Using Python's built-in server (for testing):

```bash
python app.py
```

### Using Gunicorn (production):

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Troubleshooting

**Q: "Error connecting to server"**

- Make sure the backend is running (`python app.py`)
- Check that it's on `http://localhost:5000`
- Check your firewall settings

**Q: "API key error"**

- Verify your NVIDIA API key in `.env`
- Make sure the key is valid and hasn't expired
- Check https://integrate.api.nvidia.com for your key

**Q: CORS errors**

- The backend has CORS enabled for all origins
- If issues persist, check Flask-CORS is properly installed

**Q: Slow responses**

- NVIDIA API responses can take 5-10 seconds
- This is normal for large language models
- The UI shows a loading state while waiting

## Technologies

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Flask, Python
- **AI Model**: NVIDIA's GPT OSS 120B (via OpenAI client)
- **API Integration**: NVIDIA Inference Endpoints

## License

Open source - feel free to modify and use!

## Support

For issues or questions:

1. Check troubleshooting section above
2. Verify NVIDIA API credentials
3. Check backend logs for errors
4. Review NVIDIA API documentation

---

**Happy learning!** 🧠 Use mental models to think more clearly and make better decisions.
# mental-model-ai
