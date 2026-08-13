# 🤖 AI FAQ Chatbot

An AI-powered FAQ chatbot built with **Python, Flask, and Sentence Transformers**. The chatbot understands the meaning of a user's question and finds the most relevant answer from a predefined FAQ database.

Unlike a traditional keyword-based chatbot, this project uses **semantic similarity** to understand different ways of asking the same question.

---

## 📌 Features

* 🤖 AI-powered FAQ question answering
* 🧠 Semantic question matching using Sentence Transformers
* 👋 Greeting detection
* ❓ Intelligent fallback response for unknown questions
* 💬 Modern chatbot-style web interface
* ⏳ "Thinking..." indicator
* 🗑️ Clear Chat functionality
* 🔒 Safe rendering of user messages
* 📱 Responsive interface
* 📚 30 predefined FAQs
* ⚡ Flask-based backend API

---

## 🛠️ Technologies Used

### Backend

* **Python** — Core programming language
* **Flask** — Web framework used to create the backend and API
* **Sentence Transformers** — Converts questions into numerical embeddings
* **all-MiniLM-L6-v2** — Pre-trained sentence embedding model
* **PyTorch** — Used internally by Sentence Transformers

### Frontend

* **HTML5** — Webpage structure
* **CSS3** — Styling and responsive layout
* **JavaScript** — User interaction and communication with the Flask API

### Data

* **JSON** — Stores the FAQ questions and answers

---

## 📂 Project Structure

```text
AI_FAQ_chatbot/
│
├── app.py
├── chatbot.py
├── faq_data.json
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── venv/
```

### File Description

| File                   | Purpose                                |
| ---------------------- | -------------------------------------- |
| `app.py`               | Flask application and API routes       |
| `chatbot.py`           | AI chatbot logic and semantic matching |
| `faq_data.json`        | FAQ questions and answers              |
| `requirements.txt`     | Python dependencies                    |
| `templates/index.html` | Frontend chatbot interface             |
| `README.md`            | Project documentation                  |
| `venv/`                | Python virtual environment             |

---

# 🧠 How the AI Matching Works

The main AI functionality is implemented using **Sentence Transformers**.

The project uses:

```text
all-MiniLM-L6-v2
```

This model converts sentences into **embeddings** — numerical representations of their meaning.

### Example

Suppose the FAQ database contains:

```text
What are your working hours?
```

A user might ask:

```text
When are you open?
```

Although the two questions use different words, they have a similar meaning.

The Sentence Transformer converts both into embeddings and compares them using **cosine similarity**.

Conceptually:

```text
FAQ Question
     ↓
Sentence Transformer
     ↓
Embedding
     ↓
             Compare
     ↑
User Question
     ↑
Sentence Transformer
     ↑
Embedding
```

The chatbot selects the FAQ with the highest similarity score.

---

## 🔍 Semantic Similarity

The chatbot uses:

```python
util.cos_sim()
```

to calculate the cosine similarity between the user's question and all stored FAQ questions.

The highest-scoring FAQ becomes the candidate answer.

A similarity threshold is also used:

```python
if best_score < 0.40:
    return "I'm currently designed to answer questions about our services, orders, payments, accounts, and support. Please try asking a related question."
```

This prevents the chatbot from confidently returning an unrelated FAQ when the user's question is outside the supported topics.

---

# 👋 Greeting Detection

Common greetings are handled separately before semantic matching:

```python
greetings = ["hi", "hello", "hey", "hii", "hola"]

if user_question in greetings:
    return "Hello! 👋 How can I help you today?"
```

This provides a more natural conversational experience.

---

# 🌐 Application Flow

The overall application works like this:

```text
User enters question
        ↓
Frontend JavaScript
        ↓
POST request to /ask
        ↓
Flask backend
        ↓
FAQChatbot
        ↓
Sentence Transformer
        ↓
Generate question embedding
        ↓
Compare with FAQ embeddings
        ↓
Find highest similarity
        ↓
Check similarity threshold
        ↓
Return answer
        ↓
Display answer in chatbot UI
```

---

# ⚙️ Installation

## 1. Clone or download the project

Place the project on your computer.

Example:

```text
C:\Users\YourName\AI_FAQ_chatbot
```

---

## 2. Open Command Prompt

Navigate to the project directory:

```cmd
cd AI_FAQ_chatbot
```

---

## 3. Create a virtual environment

```cmd
python -m venv venv
```

---

## 4. Activate the virtual environment

### Windows

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your Command Prompt.

---

## 5. Install dependencies

Run:

```cmd
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Flask application:

```cmd
python app.py
```

After the server starts, open your browser and visit:

```text
http://127.0.0.1:5000
```

The chatbot should now be available in your browser.

---

# 📦 Requirements

The project requires Python packages including:

```text
Flask
sentence-transformers
torch
```

The exact installed dependencies should be maintained in:

```text
requirements.txt
```

You can generate the file from your active virtual environment using:

```cmd
pip freeze > requirements.txt
```

---

# 💬 Example Questions

The chatbot can answer questions such as:

```text
What are your working hours?
```

```text
When are you open?
```

```text
How do I reset my password?
```

```text
How can I change my login password?
```

```text
How can I track my order?
```

```text
Where is my package?
```

```text
How can I return a product?
```

```text
What payment methods do you accept?
```

It can understand different wording because it uses semantic similarity rather than relying only on exact keywords.

---

# ❓ Unsupported Questions

If a question is unrelated to the available FAQ topics, the chatbot provides a fallback response instead of returning a potentially incorrect FAQ answer.

For example:

```text
What is the weather today?
```

The chatbot responds that it is currently designed to answer questions related to its supported services.

---

# 🔒 Security Consideration

User messages and chatbot responses are inserted into the webpage using JavaScript's:

```javascript
textContent
```

rather than directly injecting user input into HTML with `innerHTML`.

This helps prevent user-provided text from being interpreted as executable HTML or JavaScript.

---

# 🚀 Future Improvements

Possible future improvements include:

* 💾 Conversation history
* 🎯 Improved confidence scoring
* 📊 Analytics for frequently asked questions
* 🗂️ FAQ categories
* 🔐 User authentication
* 🗄️ Database integration
* 🌐 Deployment to a cloud platform
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 Integration with a generative AI model
* 📱 Improved mobile interface
* 🌍 Multi-language support

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python
* Flask
* REST-style API communication
* HTML/CSS/JavaScript
* JSON data handling
* Natural Language Processing
* Sentence embeddings
* Cosine similarity
* Semantic search
* Frontend-backend integration
* Basic web security
* Virtual environments
* AI model integration

---

# 👨‍💻 Project Purpose

This project was created as a beginner-friendly introduction to **AI/NLP application development**.

It demonstrates how a pre-trained language model can be integrated into a web application to build a useful AI-powered question-answering system without training a machine-learning model from scratch.

---

## ⭐ Project Highlights

> **AI FAQ Chatbot — Semantic Search Based Question Answering**

**Technologies:** Python • Flask • Sentence Transformers • HTML • CSS • JavaScript • JSON

**Core AI technique:** Sentence embeddings + cosine similarity

**Model:** `all-MiniLM-L6-v2`

**Application type:** AI/NLP Web Application
