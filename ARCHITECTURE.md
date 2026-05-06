```
╔════════════════════════════════════════════════════════════════════╗
║     Mental Model Hub - Architecture Overview                       ║
║     Full-Stack Application with NVIDIA AI Integration              ║
╚════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────┐
│                         USER BROWSER (Frontend)                       │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ index.html (HTML + CSS + JavaScript)                        │   │
│  │ ═════════════════════════════════════════════════════════════  │
│  │                                                               │   │
│  │  [Navigation]  Explore | AI Explain | Saved                 │   │
│  │  ─────────────────────────────────────────────────────────── │   │
│  │                                                               │   │
│  │  Pages:                                                      │   │
│  │  1. Home/Explore  - Browse 12 mental models                 │   │
│  │  2. AI Explain    - Get AI analysis of situations           │   │
│  │  3. Detail Page   - View full model details                 │   │
│  │  4. Favorites     - View saved models                        │   │
│  │                                                               │   │
│  │  Features:                                                   │   │
│  │  ✓ Search by keyword                                        │   │
│  │  ✓ Filter by category (Psychology, Business, etc.)         │   │
│  │  ✓ Save favorite models (localStorage)                      │   │
│  │  ✓ Dark/Light mode support                                  │   │
│  │  ✓ Responsive design (mobile-friendly)                      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                         [User Input]                                │
│                              │                                      │
│                   JavaScript Fetch API                              │
│                              │                                      │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                    HTTP POST to localhost:5000
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│              Backend Server (Python/Flask)                            │
│                     [Port 5000]                                       │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ Flask Application (app.py)                                  │   │
│  │ ═════════════════════════════════════════════════════════════  │
│  │                                                               │   │
│  │  Routes:                                                     │   │
│  │  POST /api/analyze      → Process AI request                │   │
│  │  GET  /api/health       → Health check                      │   │
│  │                                                               │   │
│  │  Features:                                                   │   │
│  │  ✓ CORS enabled (allow browser requests)                   │   │
│  │  ✓ JSON request/response                                    │   │
│  │  ✓ Streaming from API                                       │   │
│  │  ✓ Error handling                                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ Configuration (config.py)                                   │   │
│  │ ═════════════════════════════════════════════════════════════  │
│  │                                                               │   │
│  │  - NVIDIA API credentials                                   │   │
│  │  - AI model selection                                       │   │
│  │  - Temperature & parameters                                 │   │
│  │  - Mental models database                                   │   │
│  │  - System prompts                                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                      [Build System Prompt]                          │
│                              │                                      │
│              OpenAI Client Library (openai package)                  │
│                              │                                      │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                    HTTPS to NVIDIA API
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│         NVIDIA API Integration Platform                              │
│         https://integrate.api.nvidia.com/v1                          │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ AI Model: openai/gpt-oss-120b (Open Source 120B)            │   │
│  │                                                               │   │
│  │  Input:                                                      │   │
│  │  - System prompt with mental models list                    │   │
│  │  - User's situation/question                                │   │
│  │                                                               │   │
│  │  Processing:                                                │   │
│  │  - Analyzes the situation                                   │   │
│  │  - Identifies relevant mental models (2-3)                  │   │
│  │  - Generates explanation with HTML formatting               │   │
│  │                                                               │   │
│  │  Output: (Streaming)                                        │   │
│  │  <strong>Model Name</strong><br>                            │   │
│  │  How it applies... (2-3 sentences)                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                    Streaming Response (chunks)
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│              Backend Processes Response                               │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ Streaming Handler                                           │   │
│  │ - Collect chunks into full_response                         │   │
│  │ - Skip reasoning content                                    │   │
│  │ - Keep regular content                                      │   │
│  │ - Return as JSON: {"analysis": "..."}                       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                    HTTP Response (JSON)
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                         Browser (Frontend)                            │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ JavaScript Handler                                          │   │
│  │ - Parse JSON response                                       │   │
│  │ - Extract analysis HTML                                     │   │
│  │ - Display in result box                                     │   │
│  │ - Format with CSS styles                                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                      [Display to User]                               │
│                              │                                      │
│  Analysis with mental models appears on screen                      │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘


╔════════════════════════════════════════════════════════════════════╗
║                      Data Flow Summary                             ║
╚════════════════════════════════════════════════════════════════════╝

1. USER → Browser        "Why do people procrastinate?"
2. Browser → JavaScript   Create fetch request
3. JavaScript → HTTP      POST to /api/analyze
4. HTTP → Flask Server    Receives request
5. Flask → Config         Load mental models & prompt
6. Flask → OpenAI Client  Create API request
7. OpenAI Client → NVIDIA streaming chunks
8. NVIDIA → Flask        Process and collect response
9. Flask → JSON          Send response to browser
10. JSON → JavaScript    Parse and render
11. JavaScript → DOM     Display in HTML
12. DOM → User          See the analysis!


╔════════════════════════════════════════════════════════════════════╗
║                    File Responsibilities                           ║
╚════════════════════════════════════════════════════════════════════╝

Frontend Layer:
  index.html
  └─ Entire user interface
     ├─ HTML structure
     ├─ CSS styling (light/dark mode)
     └─ JavaScript logic (client-side)

Backend Layer:
  app.py
  └─ Flask server & routes
     ├─ /api/analyze endpoint
     ├─ /api/health endpoint
     ├─ CORS handling
     └─ OpenAI client initialization

  config.py
  └─ Configuration management
     ├─ API credentials
     ├─ Model parameters
     ├─ Mental models list
     └─ System prompts

Support Files:
  requirements.txt    → Python dependencies
  .env               → Environment variables (secrets)
  .gitignore         → Git configuration
  test_api.py        → Testing utility
  run.bat/.ps1       → Startup scripts
  README.md          → Full documentation
  QUICKSTART.md      → Quick start guide


╔════════════════════════════════════════════════════════════════════╗
║                   Deployment Architecture                          ║
╚════════════════════════════════════════════════════════════════════╝

Development (Current Setup):
  Browser → Flask (localhost:5000) → NVIDIA API

Production (Example):
  CDN (index.html) → Load Balancer → Flask (Gunicorn) → NVIDIA API

  With Database:
  CDN → Load Balancer → Flask → Database (user data) → NVIDIA API

  Containerized:
  Docker → Docker Registry → Kubernetes → Flask Pods → NVIDIA API


╔════════════════════════════════════════════════════════════════════╗
║                     Key Integration Points                         ║
╚════════════════════════════════════════════════════════════════════╝

1. Browser ↔ Server
   Protocol: HTTP/REST
   Format: JSON
   Auth: CORS headers

2. Server ↔ NVIDIA API
   Protocol: HTTPS
   Auth: API key in header
   Format: OpenAI format
   Streaming: Yes (chunks)

3. Frontend ↔ Storage
   Protocol: LocalStorage API
   Data: Favorites (IDs)
   Scope: Per-browser


╔════════════════════════════════════════════════════════════════════╗
║                      Mental Models Database                        ║
╚════════════════════════════════════════════════════════════════════╝

Stored in: Frontend (index.html) + Config (config.py)

Structure:
  - id: unique identifier
  - name: display name
  - category: Psychology/Business/Economics/Decision Making
  - tagline: short description
  - what: explanation of the model
  - why: why it works
  - how: how it manifests
  - examples: real-world applications
  - application: how to use it
  - failure: when it doesn't work
  - visual: diagram data
  - featured: boolean for showcase

Total: 12 models
Access: Browser search/filter


╔════════════════════════════════════════════════════════════════════╗
║                      System Requirements                           ║
╚════════════════════════════════════════════════════════════════════╝

Client (Browser):
  - Modern browser (Chrome, Firefox, Safari, Edge)
  - JavaScript enabled
  - LocalStorage enabled
  - No plugins required

Server (Local):
  - Python 3.8+
  - Flask 3.0.0+
  - ~100MB disk space
  - Port 5000 available
  - Internet connection (for NVIDIA API)

NVIDIA API:
  - Active account
  - Valid API key
  - Credit/quota available
  - Internet connection
```

---

## 🎯 Usage Flow Diagram

```
START
  ↓
[User opens index.html]
  ↓
[Choose section: Explore/AI Explain/Saved]
  ↓
Explore Tab?                     AI Explain Tab?                Saved Tab?
  ↓                                ↓                               ↓
View 12 models            User types scenario                  View bookmarks
Browse by category        Click "Analyze"                      Manage favorites
Search by keyword         ↓
Save favorites            [Frontend sends]
↓                         POST /api/analyze
Back Button               ↓
  ↓                       [Backend processes]
[Return to home]          Load config
  ↓                       Build prompt
DONE                      Call NVIDIA API
                          ↓
                          [API responds with analysis]
                          ↓
                          [Display results]
                          ↓
                          User reads analysis
                          ↓
                          Done or try another
```

---

**Architecture Last Updated**: 2026-05-06
**Version**: 1.0
**Status**: Production Ready ✅
