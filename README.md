# 🏥 AI Voice Hospital Appointment Agent

An AI-powered Voice Assistant for Hospital Appointment Management built using **FastAPI**, **SQLAlchemy**, and **Vapi**.

This system allows users to schedule, cancel, and check appointments using natural voice commands connected to a real-time backend database.

---

## 🎥 Live Demo

▶️ **Watch Demo Video:**  
[Click Here to Watch](https://shorturl.at/Q5yg5)

---

## 🚀 Features

- 🎤 Voice-controlled appointment scheduling
- ❌ Cancel appointments using natural speech
- 📋 List appointments by date
- 🔄 Real-time database updates
- 🌐 Public webhook integration using ngrok
- 🧠 Intelligent conversational responses via Vapi
- 🗄️ SQLAlchemy ORM-based database handling
- 🖥️ Streamlit dummy frontend for testing

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| FastAPI | Backend API framework |
| SQLAlchemy | ORM for database operations |
| SQLite | Local database |
| Streamlit | Testing UI |
| Vapi | AI Voice Agent |
| ngrok | Public webhook tunneling |
| Python | Core programming language |

---

## 🏗️ System Architecture

User (Voice Input)  
⬇  
Vapi AI Agent  
⬇  
Webhook → FastAPI Backend  
⬇  
Database (SQLAlchemy + SQLite)  
⬇  
Response returned to Vapi  
⬇  
Voice reply to user  

---

## 📌 API Endpoints

### 1️⃣ Schedule Appointment
`POST /schedule_appointments/`

### 2️⃣ Cancel Appointment
`POST /cancel_appointments/`

### 3️⃣ List Appointments
`GET /list_appointments/?date=YYYY-MM-DD`

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Voice-Hospital-Agent.git
cd AI-Voice-Hospital-Agent
```
### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Backend

```
python backend.py
```

Backend will run on:

```
http://127.0.0.1:4444
```

### 5️⃣ Run Streamlit Frontend (Optional)

```
streamlit run dummy_frontend.py
```

### 6️⃣ Expose Public URL (For Vapi Integration)

```
ngrok http 4444
```

---

## 🧠 How It Works

The Vapi voice agent processes natural language commands and triggers backend endpoints through webhooks.

The FastAPI backend:
- Validates input
- Performs database operations
- Returns structured JSON responses

The AI agent then converts those responses into conversational voice replies.

---

## 🎯 Use Case

This project demonstrates:
- AI + Backend integration
- Voice-driven automation systems
- Real-time API communication
- Production-style architecture
- End-to-end system design

---

## 👨‍💻 Developer

Krishna Yadav
Final Year Computer Engineering Student

Passionate about AI Systems, Backend Engineering, and Building Scalable Applications.
