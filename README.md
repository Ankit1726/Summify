<div align="center">

# 🟢 Summify

### 🤖 AI-Powered Text Summarization using Fine-Tuned T5

**Summarize • Understand • Simplify**

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=600&size=24&duration=3500&pause=1000&color=4DA6FF&center=true&vCenter=true&width=900&lines=AI+Powered+Text+Summarizer;Fine-Tuned+T5+Transformer;FastAPI+Backend;Modern+Dark+UI;Docker+%2B+Render+Deployment;Built+by+Ankit+Gupta"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/PyTorch-Deep_Learning-red?style=for-the-badge&logo=pytorch"/>
<img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge&logo=huggingface"/>
<img src="https://img.shields.io/badge/T5-Transformer-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi"/>
<img src="https://img.shields.io/badge/Docker-Deployment-2496ED?style=for-the-badge&logo=docker"/>
<img src="https://img.shields.io/badge/Render-Cloud-46E3B7?style=for-the-badge"/>
</p>

<p align="center">
<a href="YOUR_RENDER_URL">
<img src="https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20Now-success?style=for-the-badge">
</a>
</p>

</div>

---

## 🌟 About

**Summify** is an AI-powered text summarization application built with a **fine-tuned T5 Transformer model**.

It converts long-form text into concise, meaningful summaries through a simple web interface. The project demonstrates an end-to-end NLP workflow from model training and inference to FastAPI, Docker, and cloud deployment.

### ✨ What Summify Offers

- 📝 Long-text summarization
- 🤖 Fine-tuned T5 Transformer model
- 🧠 Sequence-to-sequence NLP inference
- ⚡ FastAPI REST API
- 🎨 Modern dark animated UI
- 🐳 Docker support
- ☁️ Render deployment
- 🔌 Health-check endpoint
- 📱 Responsive frontend

---

## 🚀 Live Demo

🌐 **Application:** `YOUR_RENDER_URL`

> Replace `YOUR_RENDER_URL` with your actual deployed Render URL.

---

## 📸 Preview

Add your screenshot here:

```text
preview/ui.png
```

```html
<img src="./preview/ui.png" width="100%">
```

---

## 🧠 How It Works

```text
                        USER
                         │
                         ▼
                ┌────────────────┐
                │   Summify UI   │
                │  HTML/CSS/JS   │
                └───────┬────────┘
                        │
                        │ HTTP POST
                        ▼
                ┌────────────────┐
                │    FastAPI     │
                │    Backend     │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │    Tokenizer   │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ Fine-Tuned T5  │
                │     Model      │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ Text Generation│
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │    Summary     │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │   Summify UI   │
                └────────────────┘
```

---

# 🔄 Model Workflow

```text
Long Text
    │
    ▼
Preprocessing
    │
    ▼
Tokenization
    │
    ▼
Input IDs
    │
    ▼
Fine-Tuned T5
    │
    ▼
Sequence Generation
    │
    ▼
Output Tokens
    │
    ▼
Detokenization
    │
    ▼
Final Summary
```

---

# 🤖 T5 Transformer

Summify uses a **fine-tuned T5 sequence-to-sequence Transformer**.

T5 approaches NLP problems as **text-to-text** tasks.

```text
Input
  │
  ▼
"summarize: <long text>"
  │
  ▼
T5 Encoder
  │
  ▼
T5 Decoder
  │
  ▼
Generated Tokens
  │
  ▼
Short Summary
```

### T5 can be used for

- Text Summarization
- Translation
- Question Answering
- Text Generation
- Sequence-to-Sequence NLP tasks

---

# 🏋️ Model Training Pipeline

```text
                Dataset
                   │
                   ▼
            Data Cleaning
                   │
                   ▼
          Data Preprocessing
                   │
                   ▼
             Tokenization
                   │
                   ▼
            T5 Fine-Tuning
                   │
                   ▼
              Evaluation
                   │
                   ▼
              Save Model
                   │
                   ▼
             Model Inference
```

---

# 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Programming | Python 3.11 |
| Deep Learning | PyTorch |
| NLP | Hugging Face Transformers |
| Model | T5 |
| Backend | FastAPI |
| Server | Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Containerization | Docker |
| Deployment | Render |
| Development | Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
Summify/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── backend/
│   └── main.py
│
├── model/
│   └── saved_summary_model/
│       ├── config.json
│       ├── tokenizer_config.json
│       ├── tokenizer files
│       └── model weights
│
├── src/
│   ├── data/
│   └── notebook/
│       └── Model_T5.ipynb
│
├── preview/
│   └── ui.png
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Summify.git
cd Summify
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start Backend

Run from the project root:

```bash
uvicorn backend.main:app --reload --port 8000
```

Open:

```text
http://localhost:8000
```

The FastAPI backend serves the frontend, so no separate frontend server is required.

---

# 🐳 Docker Setup

## Build Image

```bash
docker build -t summify .
```

## Run Container

```bash
docker run -p 8000:8000 summify
```

Open:

```text
http://localhost:8000
```

---

# ☁️ Render Deployment

Summify can be deployed as a Docker Web Service on Render.

### Deployment Architecture

```text
GitHub
   │
   ▼
Render
   │
   ▼
Docker Build
   │
   ▼
Install Dependencies
   │
   ▼
Load T5 Model
   │
   ▼
Start FastAPI
   │
   ▼
Live Application
```

### Steps

1. Push the project to GitHub.
2. Create a new Web Service on Render.
3. Connect the GitHub repository.
4. Select Docker deployment.
5. Render detects the `Dockerfile`.
6. Build and deploy the application.
7. Open the generated Render URL.

### Port

Render provides the `PORT` environment variable.

Your application should start Uvicorn using the assigned port.

Example:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

---

# ⚠️ Model Path

The trained model in this project is stored under:

```text
model/saved_summary_model/
```

Make sure the path used in `backend/main.py` matches the location inside the Docker container.

Example:

```python
MODEL_PATH = "model/saved_summary_model"
```

And the Dockerfile should copy the model accordingly:

```dockerfile
COPY model/saved_summary_model /app/model/saved_summary_model
```

The **Python model path and Docker model path must match**.

---

# 🔌 API Documentation

## Health Check

### Endpoint

```http
GET /health
```

### Response

```json
{
  "status": "ok",
  "device": "cpu"
}
```

This endpoint is useful for checking whether the application is running correctly.

---

## Summarization

### Endpoint

```http
POST /summarize/
```

### Request

```json
{
  "dialogue": "Your long text goes here..."
}
```

### Response

```json
{
  "summary": "A shorter version of the input text."
}
```

---

# 🧪 API Example

### Python

```python
import requests

url = "http://localhost:8000/summarize/"

payload = {
    "dialogue": """
    Artificial intelligence is rapidly changing the way organizations
    analyze data, automate processes, and build intelligent applications.
    """
}

response = requests.post(url, json=payload)

print(response.json())
```

---

# 🌐 API Flow

```text
Frontend
   │
   │ POST /summarize/
   ▼
FastAPI
   │
   ▼
Validate Input
   │
   ▼
Tokenizer
   │
   ▼
Fine-Tuned T5
   │
   ▼
Generate Summary
   │
   ▼
JSON Response
   │
   ▼
Frontend
```

---

# 📊 End-to-End ML Pipeline

```text
┌─────────────────────┐
│      Dataset        │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Data Preprocessing  │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│     Tokenization    │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│    T5 Fine-Tuning   │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│      Evaluation     │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│     Save Model      │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│    FastAPI API      │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│       Docker        │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   Render Deployment │
└─────────────────────┘
```

---

# 🎯 Use Cases

Summify can be used for:

- 📚 Research papers
- 📰 News articles
- 📄 Long documents
- 🎓 Educational content
- 📝 Meeting notes
- 🔬 Research assistance
- 📖 Study material
- 💼 Business documents
- ⚡ Productivity workflows

---

# 💡 Key Learning Outcomes

This project demonstrates how to take an NLP model from experimentation to a deployable application.

### Machine Learning

- Dataset preparation
- NLP preprocessing
- Tokenization
- Transformer architecture
- T5 fine-tuning
- Model evaluation
- Model inference

### Software Engineering

- FastAPI REST API
- Frontend integration
- Docker containerization
- Cloud deployment
- API health checks
- Project structure

### Complete Pipeline

```text
Data
 ↓
Preprocessing
 ↓
Tokenization
 ↓
T5 Fine-Tuning
 ↓
Evaluation
 ↓
Model Saving
 ↓
Inference
 ↓
FastAPI
 ↓
Docker
 ↓
Render
 ↓
Live Application
```

---

# 🏆 Project Highlights

| Feature | Implementation |
|---|---|
| NLP Task | Text Summarization |
| Model | Fine-Tuned T5 |
| Deep Learning | PyTorch |
| NLP Framework | Hugging Face Transformers |
| Backend | FastAPI |
| Frontend | HTML / CSS / JavaScript |
| API | REST |
| Containerization | Docker |
| Cloud | Render |
| Training | Jupyter Notebook |

---

# 🎯 Project Goal

The goal of Summify is to demonstrate a complete **NLP model-to-production workflow**.

The project combines:

```text
Machine Learning
       +
Deep Learning
       +
Natural Language Processing
       +
Transformer Models
       +
Backend Development
       +
Frontend Development
       +
Docker
       +
Cloud Deployment
```

---

# 🔮 Future Enhancements

- 📄 PDF summarization
- 📚 Multiple document summarization
- 🔗 URL summarization
- 🎙️ Audio-to-text summarization
- 🌐 Multilingual summarization
- 🧠 RAG-based summarization
- 📊 ROUGE / BERTScore evaluation
- 💾 Summary history
- 🔐 User authentication
- ⚡ GPU inference
- 📱 Improved mobile UI
- 🤖 T5 + LLM hybrid summarization

---

# 🚀 Future Architecture

```text
                         User
                          │
                          ▼
                   ┌─────────────┐
                   │ Summify UI  │
                   └──────┬──────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
         Text Input              Documents
              │                       │
              └───────────┬───────────┘
                          ▼
                   RAG Pipeline
                          │
                          ▼
                  Retrieval System
                          │
                          ▼
                ┌─────────────────┐
                │    T5 / LLM     │
                └────────┬────────┘
                         │
                         ▼
                      Summary
```

---

# 🔐 Environment Variables

For the current version, no API keys are required for the basic summarization workflow.

If additional services are added in the future, configure their credentials through environment variables instead of committing secrets to GitHub.

Example:

```env
MODEL_PATH=model/saved_summary_model
PORT=8000
```

Never commit:

```text
.env
API keys
Passwords
Access tokens
Private credentials
```

---

# 📝 Example Input

```text
Artificial intelligence has become an important technology across
healthcare, finance, education, manufacturing, and many other industries.
Organizations are using machine learning and deep learning systems to
automate repetitive tasks, analyze large datasets, improve decision making,
and create intelligent applications.
```

### Example Output

```text
Artificial intelligence is being used across industries to automate tasks,
analyze data, improve decisions, and build intelligent applications.
```

---

# 🧪 Testing

Start the application:

```bash
uvicorn backend.main:app --reload --port 8000
```

Check health:

```bash
curl http://localhost:8000/health
```

Test summarization:

```bash
curl -X POST http://localhost:8000/summarize/ \
-H "Content-Type: application/json" \
-d "{\"dialogue\":\"Your long text here\"}"
```

---

# 📌 Notes

### Model Size

Transformer model files can be large. If the trained model is too large for normal GitHub repository limits, consider:

- Git LFS
- Hugging Face Hub
- Cloud object storage
- Downloading the model during deployment

Do not commit large model files blindly if they exceed GitHub's file-size limits.

---

# 🤝 Contributing

Contributions are welcome.

### Steps

```bash
git fork
```

Create a feature branch:

```bash
git checkout -b feature/new-feature
```

Make your changes and commit:

```bash
git add .
git commit -m "Add new feature"
```

Push the branch:

```bash
git push origin feature/new-feature
```

Then create a Pull Request.

---

# ⭐ Support

If you find **Summify** useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Report bugs
- 💡 Suggest improvements
- 🤝 Contribute to the project

---

# 👨‍💻 Developer

<div align="center">

## **ANKIT GUPTA 👦**

### AI Engineer • AI Backend Developer • GenAI & Agentic AI Developer

Building intelligent AI systems using:

**Machine Learning • Deep Learning • NLP • Generative AI • Agentic AI**

</div>

---

<div align="center">

# 🟢 Summify

### **Read Less. Understand More.**

**AI-Powered Text Summarization using Fine-Tuned T5**

Made with ❤️ by **Ankit Gupta**

</div>
