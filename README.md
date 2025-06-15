# LifeTriage Project Development Plan (Revised)

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
- **SQLAlchemy** for database ORM
- **Flask-CORS** for cross-origin requests
- **Python 3.9+** runtime
- **spaCy** for NLP processing (added in Phase 3)

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
│   │   │   └── task_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── database.py
│   │   └── config.py
│   ├── requirements.txt
│   ├── app.py
│   ├── Procfile
│   └── .env
├── docs/
│   ├── api.md
│   └── deployment.md
├── .gitignore
└── README.md
```

## 🚀 Development Phases

### Phase 1: Foundation Setup (Week 1)
**Goal**: Set up basic project structure and core functionality with SIMPLE categorization

#### Backend Setup
- [ ] Initialize Flask application with blueprint structure
- [ ] Set up Supabase PostgreSQL database connection
- [ ] Create Task model with SQLAlchemy
- [ ] Implement basic CRUD operations for tasks
- [ ] Set up Flask-CORS for frontend communication
- [ ] Create simple keyword-based categorization (no spaCy yet)
- [ ] Add health check endpoint

#### Frontend Setup
- [ ] Initialize React + Vite project
- [ ] Set up basic UI components (VoiceInput, TaskList, TaskCard)
- [ ] Implement Web Speech API integration
- [ ] Create basic API service for backend communication
- [ ] Style basic interface with simple CSS/Tailwind
- [ ] Add error handling for API calls

#### Database Schema
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    category VARCHAR(50) DEFAULT 'general',
    priority_score INTEGER DEFAULT 5,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    color VARCHAR(7) DEFAULT '#6B7280'
);

-- Insert default categories
INSERT INTO categories (name, description, color) VALUES 
('work', 'Work-related tasks', '#3B82F6'),
('health', 'Health and fitness', '#10B981'),
('personal', 'Personal tasks', '#8B5CF6'),
('home', 'Household tasks', '#F59E0B'),
('finance', 'Financial tasks', '#EF4444'),
('general', 'Uncategorized tasks', '#6B7280');
```

#### Simple Categorization Logic (Phase 1)
```python
# Simple keyword-based categorization for Phase 1
SIMPLE_CATEGORIES = {
    'work': ['work', 'job', 'meeting', 'project', 'client', 'boss', 'office', 'email'],
    'health': ['doctor', 'gym', 'exercise', 'medicine', 'appointment', 'workout'],
    'home': ['clean', 'house', 'home', 'kitchen', 'bedroom', 'repair', 'grocery'],
    'finance': ['bill', 'pay', 'money', 'bank', 'budget', 'tax', 'purchase'],
    'personal': ['learn', 'read', 'hobby', 'friend', 'family', 'call', 'visit']
}

def simple_categorize(text):
    text_lower = text.lower()
    for category, keywords in SIMPLE_CATEGORIES.items():
        if any(keyword in text_lower for keyword in keywords):
            return category
    return 'general'
```

#### API Endpoints (Phase 1)
- [ ] `GET /health` - Health check
- [ ] `POST /api/tasks` - Create new task with simple categorization
- [ ] `GET /api/tasks` - Retrieve all tasks
- [ ] `PUT /api/tasks/:id` - Update task
- [ ] `DELETE /api/tasks/:id` - Delete task
- [ ] `GET /api/categories` - Get all categories

### Phase 2: Deployment & Testing (Week 2)
**Goal**: Deploy application and ensure reliability - CRITICAL PHASE

#### Pre-Deployment Checklist
- [ ] Verify all environment variables are properly configured
- [ ] Test database connection locally with Supabase
- [ ] Ensure Flask app runs with production settings
- [ ] Test API endpoints with production-like data
- [ ] Verify CORS settings work across domains
- [ ] Test voice recognition in different browsers

#### Backend Deployment (Railway)
- [ ] Create Railway account and link GitHub repository
- [ ] Configure Railway environment variables:
  - `SUPABASE_URL`
  - `SUPABASE_KEY`
  - `FLASK_ENV=production`
  - `SECRET_KEY`
- [ ] Add Procfile for Railway deployment
- [ ] Deploy backend and verify health endpoint
- [ ] Test all API endpoints in production
- [ ] Set up Railway custom domain (optional)

#### Frontend Deployment (Vercel)
- [ ] Create Vercel account and link GitHub repository
- [ ] Configure build settings for Vite
- [ ] Set up environment variables:
  - `VITE_API_URL` (Railway backend URL)
- [ ] Deploy frontend and test voice recognition
- [ ] Verify API communication between frontend and backend
- [ ] Test on mobile devices

#### Production Testing
- [ ] End-to-end testing: voice → task creation → storage
- [ ] Cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsiveness and voice recognition
- [ ] Network error handling and retry logic
- [ ] Database connection stability under load
- [ ] SSL certificate and HTTPS enforcement

#### Deployment Files

##### Backend Procfile
```
web: gunicorn app:app
```

##### Backend requirements.txt (minimal for Phase 2)
```txt
Flask==2.3.3
Flask-CORS==4.0.0
Flask-SQLAlchemy==3.0.5
psycopg2-binary==2.9.7
python-dotenv==1.0.0
gunicorn==21.2.0
```

##### Frontend package.json
```json
{
  "name": "lifetriage-frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.15",
    "@types/react-dom": "^18.2.7",
    "@vitejs/plugin-react": "^4.0.3",
    "vite": "^4.4.5"
  }
}
```

#### Deployment Validation
- [ ] Verify app loads correctly on production URLs
- [ ] Test voice input works on HTTPS
- [ ] Confirm task creation, retrieval, and deletion
- [ ] Validate database persistence across sessions
- [ ] Monitor application logs for errors
- [ ] Test error handling and recovery

### Phase 3: NLP Integration (Week 3)
**Goal**: Add intelligent categorization and prioritization

#### NLP Service Development
- [ ] Add spaCy to backend requirements
- [ ] Install and configure spaCy with English model
- [ ] Create advanced categorization service
- [ ] Implement priority scoring algorithm
- [ ] Add text preprocessing and cleaning
- [ ] Create fallback categorization logic
- [ ] **REDEPLOY and test NLP features in production**

#### Enhanced Category Domains
```python
LIFE_DOMAINS = {
    'health': ['doctor', 'exercise', 'gym', 'medicine', 'therapy', 'wellness', 'fitness'],
    'work': ['meeting', 'project', 'deadline', 'client', 'email', 'presentation', 'conference'],
    'relationships': ['family', 'friend', 'date', 'call', 'visit', 'anniversary', 'birthday'],
    'finance': ['bill', 'payment', 'budget', 'tax', 'investment', 'savings', 'insurance'],
    'personal': ['hobby', 'learning', 'book', 'course', 'skill', 'development', 'growth'],
    'home': ['clean', 'repair', 'grocery', 'maintenance', 'organize', 'decorate', 'garden']
}
```

#### Priority Scoring Algorithm
```python
def calculate_priority(text: str) -> int:
    """Calculate priority score 1-10 based on urgency indicators"""
    urgency_indicators = {
        'urgent': 3,
        'asap': 3,
        'immediately': 3,
        'deadline': 2,
        'important': 2,
        'soon': 1,
        'today': 2,
        'tomorrow': 1
    }
    
    base_priority = 5
    priority_adjustment = 0
    
    text_lower = text.lower()
    for indicator, weight in urgency_indicators.items():
        if indicator in text_lower:
            priority_adjustment += weight
    
    return min(10, max(1, base_priority + priority_adjustment))
```

### Phase 4: Enhanced Features (Week 4)
**Goal**: Add advanced functionality and improve UX

#### Frontend Enhancements
- [ ] Implement task filtering by category
- [ ] Add priority-based task sorting
- [ ] Create task completion interface
- [ ] Add voice feedback and confirmation
- [ ] Implement task editing capabilities
- [ ] Add loading states and better error handling

#### Backend Improvements
- [ ] Add task search functionality
- [ ] Implement batch operations
- [ ] Add task analytics/insights
- [ ] Create data export functionality
- [ ] Add comprehensive error handling and logging
- [ ] **REDEPLOY with enhanced features**

#### UX/UI Polish
- [ ] Responsive design improvements
- [ ] Accessibility enhancements (ARIA labels, keyboard navigation)
- [ ] Visual feedback for voice recognition
- [ ] Progressive web app features (offline support)
- [ ] Performance optimization

## 🛠 Technical Implementation Details

### Voice Recognition Implementation
```javascript
// useSpeechRecognition.js
const useSpeechRecognition = () => {
  const [transcript, setTranscript] = useState('');
  const [isListening, setIsListening] = useState(false);
  const [error, setError] = useState(null);
  
  const startListening = () => {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
      setError('Speech recognition not supported in this browser');
      return;
    }
    
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = 'en-US';
    
    recognition.onstart = () => {
      setIsListening(true);
      setError(null);
    };
    
    recognition.onresult = (event) => {
      const transcript = Array.from(event.results)
        .map(result => result[0].transcript)
        .join('');
      setTranscript(transcript);
    };
    
    recognition.onerror = (event) => {
      setError(`Speech recognition error: ${event.error}`);
      setIsListening(false);
    };
    
    recognition.onend = () => {
      setIsListening(false);
    };
    
    recognition.start();
  };
  
  return { transcript, isListening, error, startListening };
};
```

### Simple Task Service (Phase 1)
```python
# services/task_service.py
class TaskService:
    def __init__(self):
        self.categories = {
            'work': ['work', 'job', 'meeting', 'project', 'client', 'boss', 'office', 'email'],
            'health': ['doctor', 'gym', 'exercise', 'medicine', 'appointment', 'workout'],
            'home': ['clean', 'house', 'home', 'kitchen', 'bedroom', 'repair', 'grocery'],
            'finance': ['bill', 'pay', 'money', 'bank', 'budget', 'tax', 'purchase'],
            'personal': ['learn', 'read', 'hobby', 'friend', 'family', 'call', 'visit']
        }
    
    def categorize_task(self, text: str) -> str:
        """Simple keyword-based categorization"""
        text_lower = text.lower()
        for category, keywords in self.categories.items():
            if any(keyword in text_lower for keyword in keywords):
                return category
        return 'general'
    
    def calculate_priority(self, text: str) -> int:
        """Simple priority calculation"""
        urgent_words = ['urgent', 'asap', 'important', 'deadline']
        text_lower = text.lower()
        if any(word in text_lower for word in urgent_words):
            return 8
        return 5
```

### Database Configuration
```python
# config.py
import os
from urllib.parse import urlparse

class Config:
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    if SUPABASE_URL:
        # Parse Supabase URL for SQLAlchemy
        url = urlparse(SUPABASE_URL)
        SQLALCHEMY_DATABASE_URI = f"postgresql://{url.username}:{url.password}@{url.hostname}:{url.port}{url.path}"
    else:
        # Fallback for local development
        SQLALCHEMY_DATABASE_URI = 'sqlite:///lifetriage.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

## 🚀 Deployment Commands

### Local Development
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

# Frontend
cd frontend
npm install
npm run dev
```

### Production Deployment

#### Railway Backend Deployment
```bash
# Connect to Railway
railway login
railway init
railway link [your-project-id]

# Set environment variables
railway variables set SUPABASE_URL=your_supabase_url
railway variables set SUPABASE_KEY=your_supabase_anon_key
railway variables set FLASK_ENV=production
railway variables set SECRET_KEY=your_secret_key

# Deploy
git add .
git commit -m "Deploy to Railway"
git push origin main
```

#### Vercel Frontend Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd frontend
vercel

# Set environment variables in Vercel dashboard:
# VITE_API_URL=https://your-railway-app.up.railway.app
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
```

### Production Environment Variables

#### Railway (Backend)
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `FLASK_ENV=production`
- `SECRET_KEY`

#### Vercel (Frontend)
- `VITE_API_URL` (Railway backend URL)

## 📈 Success Metrics

### Phase 1 Success Criteria
- [ ] Voice recognition works in local development
- [ ] Tasks can be created, read, updated, deleted locally
- [ ] Simple categorization assigns correct categories
- [ ] Database connection is stable

### Phase 2 Success Criteria (CRITICAL)
- [ ] Application deploys successfully to production
- [ ] Voice recognition works on HTTPS in production
- [ ] API endpoints respond correctly in production
- [ ] Database operations work in production environment
- [ ] App is accessible on mobile devices
- [ ] No console errors in production

### Phase 3 Success Criteria
- [ ] NLP categorization accuracy > 80%
- [ ] Priority scoring works correctly
- [ ] Production deployment still stable after NLP integration

### Phase 4 Success Criteria
- [ ] All advanced features work in production
- [ ] App load time < 3 seconds
- [ ] Mobile responsiveness across devices
- [ ] Accessibility compliance
- [ ] 99% uptime metrics

## 🔄 Rollback Strategy

### Deployment Issues
- Keep previous working version tagged in Git
- Railway allows instant rollbacks to previous deployments
- Vercel has automatic rollback capabilities
- Database migrations should be reversible

### Testing Strategy
- Test each phase thoroughly in production before moving to next phase
- Use feature flags for gradual rollouts
- Monitor application logs and performance metrics
- Have rollback plan ready for each deployment

## 🚨 Common Deployment Pitfalls to Avoid

### Backend Issues
- [ ] CORS misconfiguration for production domains
- [ ] Environment variables not set correctly
- [ ] Database connection string formatting errors
- [ ] Missing production dependencies in requirements.txt
- [ ] Gunicorn configuration issues

### Frontend Issues
- [ ] API URL not updated for production
- [ ] Build process failures due to missing dependencies
- [ ] Voice recognition not working on HTTP (needs HTTPS)
- [ ] Environment variables not prefixed with VITE_

### Database Issues
- [ ] Supabase connection limits exceeded
- [ ] SSL connection requirements in production
- [ ] Database migration scripts not run
- [ ] Connection pooling not configured

---

This revised plan prioritizes deployment stability by tackling infrastructure challenges early, ensuring you have a solid foundation before adding complex features. The key change is moving deployment to Phase 2, right after basic functionality is established, which will help you identify and resolve any architectural issues before investing time in advanced features.
