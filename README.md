# LifeTriage Project Development Plan

## 📋 Project Overview

**LifeTriage** is a voice-first task management application that automatically categorizes and prioritizes tasks using natural language processing. Users speak tasks aloud, and the app intelligently organizes them by life domains (health, work, relationships, etc.) with smart prioritization.

## 🎯 Core Features

- 🎙 **Voice-to-text task capture** using Web Speech API  
- 📂 **Automatic task categorization** by life domain
- 📈 **Smart prioritization** based on importance scoring
- 💾 **Persistent storage** with Supabase PostgreSQL
- 🌐 **Cloud deployment** via Railway
- 🔒 **Modular backend architecture** for extensibility

## 🏗 Technical Architecture

### Frontend Stack
- **React 18** with Vite for fast development
- **Modern CSS** or Tailwind for styling
- **Web Speech API** for voice recognition
- **Fetch API** for backend communication

### Backend Stack
- **Flask** with modular blueprint architecture
- **spaCy** for NLP processing and categorization
- **SQLAlchemy** for database ORM
- **Flask-CORS** for cross-origin requests
- **Python 3.9+** runtime

### Database & Deployment
- **Supabase PostgreSQL** for data persistence
- **Railway** for backend deployment
- **Vercel** for frontend deployment (or Railway for full-stack)

## 📁 Project Structure

```
LifeTriage/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── VoiceInput.jsx
│   │   │   ├── TaskList.jsx
│   │   │   ├── TaskCard.jsx
│   │   │   └── CategoryFilter.jsx
│   │   ├── hooks/
│   │   │   ├── useSpeechRecognition.js
│   │   │   └── useTaskManager.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── utils/
│   │   │   └── constants.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── task.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── tasks.py
│   │   │   └── health.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── nlp_service.py
│   │   │   └── categorization_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── database.py
│   │   └── config.py
│   ├── requirements.txt
│   ├── app.py
│   └── .env
├── docs/
│   ├── api.md
│   └── deployment.md
├── .gitignore
└── README.md
```

## 🚀 Development Phases

### Phase 1: Foundation Setup (Week 1)
**Goal**: Set up basic project structure and core functionality

#### Backend Setup
- [ ] Initialize Flask application with blueprint structure
- [ ] Set up Supabase PostgreSQL database
- [ ] Create Task model with SQLAlchemy
- [ ] Implement basic CRUD operations for tasks
- [ ] Set up Flask-CORS for frontend communication

#### Frontend Setup
- [ ] Initialize React + Vite project
- [ ] Set up basic UI components (VoiceInput, TaskList)
- [ ] Implement Web Speech API integration
- [ ] Create basic API service for backend communication
- [ ] Style basic interface

#### Database Schema
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    category VARCHAR(50),
    priority_score INTEGER DEFAULT 0,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    color VARCHAR(7) -- hex color
);
```

### Phase 2: NLP Integration (Week 2)
**Goal**: Add intelligent categorization and prioritization

#### NLP Service Development
- [ ] Install and configure spaCy with English model
- [ ] Create categorization service with domain keywords
- [ ] Implement priority scoring algorithm
- [ ] Add text preprocessing and cleaning
- [ ] Create fallback categorization logic

#### Category Domains
```python
LIFE_DOMAINS = {
    'health': ['doctor', 'exercise', 'gym', 'medicine', 'therapy'],
    'work': ['meeting', 'project', 'deadline', 'client', 'email'],
    'relationships': ['family', 'friend', 'date', 'call', 'visit'],
    'finance': ['bill', 'payment', 'budget', 'tax', 'investment'],
    'personal': ['hobby', 'learning', 'book', 'course', 'skill'],
    'home': ['clean', 'repair', 'grocery', 'maintenance', 'organize']
}
```

#### API Endpoints
- [ ] `POST /api/tasks` - Create and categorize new task
- [ ] `GET /api/tasks` - Retrieve all tasks with filters
- [ ] `PUT /api/tasks/:id` - Update task status/priority
- [ ] `DELETE /api/tasks/:id` - Delete task
- [ ] `GET /api/categories` - Get all categories

### Phase 3: Enhanced Features (Week 3)
**Goal**: Add advanced functionality and improve UX

#### Frontend Enhancements
- [ ] Implement task filtering by category
- [ ] Add priority-based task sorting
- [ ] Create task completion interface
- [ ] Add voice feedback and confirmation
- [ ] Implement task editing capabilities

#### Backend Improvements
- [ ] Add task search functionality
- [ ] Implement batch operations
- [ ] Add task analytics/insights
- [ ] Create data export functionality
- [ ] Add error handling and logging

#### UX/UI Polish
- [ ] Responsive design for mobile devices
- [ ] Loading states and error handling
- [ ] Accessibility improvements
- [ ] Visual feedback for voice recognition

### Phase 4: Deployment & Testing (Week 4)
**Goal**: Deploy application and ensure reliability

#### Deployment Setup
- [ ] Configure Railway for backend deployment
- [ ] Set up environment variables and secrets
- [ ] Configure Supabase connection strings
- [ ] Deploy frontend to Vercel (or Railway)
- [ ] Set up custom domain (optional)

#### Testing & Quality Assurance
- [ ] Test voice recognition across browsers
- [ ] Validate NLP categorization accuracy
- [ ] Test API endpoints thoroughly
- [ ] Cross-browser compatibility testing
- [ ] Mobile responsiveness testing

#### Documentation
- [ ] API documentation
- [ ] Deployment guide
- [ ] User manual
- [ ] Developer setup instructions

## 🛠 Technical Implementation Details

### Voice Recognition Implementation
```javascript
// useSpeechRecognition.js
const useSpeechRecognition = () => {
  const [transcript, setTranscript] = useState('');
  const [isListening, setIsListening] = useState(false);
  
  const startListening = () => {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = 'en-US';
    
    recognition.onresult = (event) => {
      const transcript = Array.from(event.results)
        .map(result => result[0].transcript)
        .join('');
      setTranscript(transcript);
    };
    
    recognition.start();
    setIsListening(true);
  };
  
  return { transcript, isListening, startListening };
};
```

### NLP Service Structure
```python
# services/nlp_service.py
import spacy
from typing import Tuple, Dict

class NLPService:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.categories = self._load_categories()
    
    def categorize_task(self, text: str) -> Tuple[str, float]:
        """Categorize task and return confidence score"""
        doc = self.nlp(text.lower())
        scores = self._calculate_category_scores(doc)
        return max(scores.items(), key=lambda x: x[1])
    
    def calculate_priority(self, text: str) -> int:
        """Calculate priority score 1-10 based on urgency indicators"""
        urgency_words = ['urgent', 'asap', 'immediately', 'deadline', 'important']
        doc = self.nlp(text.lower())
        # Implementation logic here
        return priority_score
```

### Database Configuration
```python
# config.py
import os
from urllib.parse import urlparse

class Config:
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
    # Parse Supabase URL for SQLAlchemy
    url = urlparse(SUPABASE_URL)
    SQLALCHEMY_DATABASE_URI = f"postgresql://{url.username}:{url.password}@{url.hostname}:{url.port}{url.path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 📦 Dependencies

### Frontend Dependencies
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.3",
    "vite": "^4.4.5"
  }
}
```

### Backend Dependencies
```txt
Flask==2.3.3
Flask-CORS==4.0.0
Flask-SQLAlchemy==3.0.5
psycopg2-binary==2.9.7
spacy==3.6.1
python-dotenv==1.0.0
gunicorn==21.2.0
```

## 🚀 Deployment Commands

### Local Development
```bash
# Backend
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
flask run

# Frontend
cd frontend
npm install
npm run dev
```

### Production Deployment
```bash
# Railway deployment
railway login
railway init
railway add
railway deploy

# Environment variables to set:
# SUPABASE_URL
# SUPABASE_KEY
# FLASK_ENV=production
```

## 🔧 Environment Variables

### Backend (.env)
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

### Frontend (.env)
```env
VITE_API_URL=http://localhost:5000
VITE_API_URL_PROD=https://your-railway-app.railway.app
```

## 📈 Success Metrics

- [ ] Voice recognition accuracy > 90%
- [ ] Task categorization accuracy > 85%
- [ ] App load time < 3 seconds
- [ ] Mobile responsiveness across devices
- [ ] Zero data loss in production
- [ ] 99% uptime after deployment

## 🔄 Future Enhancements

### Phase 5: Advanced Features
- Task scheduling and reminders
- Integration with calendar apps
- Team collaboration features
- Advanced analytics dashboard
- Mobile app development (React Native)
- AI-powered task suggestions

### Phase 6: Scaling
- Multi-language support
- Advanced NLP models
- Real-time collaboration
- Offline functionality
- API rate limiting
- Performance optimization

---

This plan provides a comprehensive roadmap for building LifeTriage from conception to deployment. Each phase builds upon the previous one, ensuring a solid foundation while gradually adding complexity and features.
