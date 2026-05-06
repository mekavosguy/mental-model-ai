"""
Configuration settings for Mental Model Hub Backend
"""
import os
from dotenv import load_dotenv

load_dotenv()

# NVIDIA API Configuration
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_MODEL = "openai/gpt-oss-120b"  # Change this to use different NVIDIA models

# AI Parameters
AI_TEMPERATURE = 0.7  # 0-2, higher = more creative
AI_TOP_P = 0.9  # Nucleus sampling parameter
AI_MAX_TOKENS = 2048  # Maximum response length (increased for comprehensive analysis)

# Flask Configuration
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
HOST = "0.0.0.0"
PORT = 5000

# CORS Configuration
CORS_ORIGINS = ["*"]  # Allow all origins for development

# System Prompt for AI
SYSTEM_PROMPT_TEMPLATE = """You are a mental models expert. Given a situation, analyze it comprehensively using ALL relevant mental models that apply.

Available mental models:
{models}

Instructions:
1. Review all available mental models carefully
2. Identify EVERY model that applies to this situation (could be 3-8+ models)
3. Prioritize the most relevant ones first
4. For each relevant model, explain how it applies

Format your response as clear HTML. For each model used, show:
<strong>Model Name</strong><br>How it applies to this situation (2-3 sentences). Use <br> for line breaks between models.

Be comprehensive, practical and insightful. Cover all angles of the situation.
No markdown, only HTML tags."""

# Mental Models Database
MENTAL_MODELS = [
    "Social Proof: People copy others when uncertain to reduce risk and effort",
    "First Principles Thinking: Break a problem down to fundamental truths, then reason up",
    "Loss Aversion: Losses hurt roughly twice as much as equivalent gains feel good",
    "Second-Order Thinking: Think past immediate consequences to the consequences of consequences",
    "Confirmation Bias: We seek, notice, and remember information that confirms existing beliefs",
    "Inversion: Instead of asking how to succeed, ask how to avoid failing",
    "Circle of Competence: Know what you know and stay inside it when stakes are high",
    "Availability Heuristic: We judge likelihood by how easily examples come to mind",
    "Sunk Cost Fallacy: Past spending has no bearing on future decisions",
    "Network Effects: The product becomes more valuable as more people use it",
    "Pareto Principle: Roughly 80% of effects come from 20% of causes",
    "Mental Accounting: We treat money differently depending on where it came from"
]

def get_system_prompt():
    """Generate the system prompt with mental models"""
    models_str = '\n'.join([f'- {model}' for model in MENTAL_MODELS])
    return SYSTEM_PROMPT_TEMPLATE.format(models=models_str)
