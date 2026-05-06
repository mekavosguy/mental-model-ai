from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from config import (
    NVIDIA_BASE_URL, NVIDIA_API_KEY, NVIDIA_MODEL,
    AI_TEMPERATURE, AI_TOP_P, AI_MAX_TOKENS,
    DEBUG, HOST, PORT, CORS_ORIGINS, MENTAL_MODELS, get_system_prompt
)

app = Flask(__name__)
CORS(app, origins=CORS_ORIGINS)

# Initialize NVIDIA API client
client = OpenAI(
    base_url=NVIDIA_BASE_URL,
    api_key=NVIDIA_API_KEY
)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Analyze a situation using mental models via NVIDIA API"""
    try:
        data = request.json
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Get system prompt with mental models
        system_prompt = get_system_prompt()

        # Call NVIDIA API with streaming
        completion = client.chat.completions.create(
            model=NVIDIA_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f'You are a mental‑model analyst. After the user provides a situation, search your knowledge (including up‑to‑date internet sources) and select exactly three mental models that best explain or address it; for each model give the name, a one‑sentence definition, and a one‑sentence reason why it applies, then list the three models only.\n\n"{text}"'}
            ],
            temperature=AI_TEMPERATURE,
            top_p=AI_TOP_P,
            max_tokens=AI_MAX_TOKENS,
            stream=True
        )
        
        # Collect streaming response
        full_response = ""
        for chunk in completion:
            if not getattr(chunk, "choices", None):
                continue
            
            # Get reasoning content if available
            reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
            if reasoning:
                pass  # We'll skip reasoning in the response
            
            # Get regular content
            if chunk.choices and chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
        
        if not full_response:
            return jsonify({'error': 'No response from API'}), 500
        
        return jsonify({'analysis': full_response})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("🚀 Mental Model Hub Backend")
    print(f"📡 API running on http://{HOST}:{PORT}")
    print("🔑 Using NVIDIA API endpoint")
    print(f"🤖 Model: {NVIDIA_MODEL}")
    print("")
    app.run(debug=DEBUG, port=PORT, host=HOST)
