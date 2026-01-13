# EPL Predictions Tool

A comprehensive full-stack application for predicting English Premier League (EPL) match outcomes using machine learning and data analysis.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Running the Backend](#running-the-backend)
- [Running the Frontend](#running-the-frontend)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

EPL Predictions Tool is a full-stack application that leverages machine learning algorithms and historical EPL data to provide accurate predictions for upcoming matches. The application features a modern web interface for users to view predictions, analyze team statistics, and track prediction accuracy over time.

## ✨ Features

### Core Features
- **Match Predictions**: AI-powered predictions for upcoming EPL matches
- **Team Statistics**: Comprehensive team performance analytics
- **Historical Data**: Access to historical match data and trends
- **Accuracy Tracking**: Monitor prediction accuracy over time
- **Live Updates**: Real-time match results and prediction updates
- **User Dashboard**: Personalized dashboard for prediction tracking

### Technical Features
- RESTful API with comprehensive endpoints
- Machine learning model for prediction accuracy
- Responsive web interface
- User authentication and authorization
- Data caching for optimal performance
- Automated data updates

## 📁 Project Structure

```
epl-predictions-tool/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── team.py
│   │   │   ├── match.py
│   │   │   └── prediction.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── teams.py
│   │   │   ├── matches.py
│   │   │   └── predictions.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── prediction_service.py
│   │   │   ├── data_service.py
│   │   │   └── ml_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── validators.py
│   │   │   └── helpers.py
│   │   └── config.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_predictions.py
│   │   ├── test_teams.py
│   │   └── test_matches.py
│   ├── requirements.txt
│   ├── .env.example
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── MatchCard.jsx
│   │   │   ├── TeamStats.jsx
│   │   │   └── PredictionDetail.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Predictions.jsx
│   │   │   ├── Teams.jsx
│   │   │   ├── Matches.jsx
│   │   │   └── NotFound.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   └── auth.js
│   │   ├── styles/
│   │   │   ├── App.css
│   │   │   ├── components.css
│   │   │   └── pages.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   ├── .env.example
│   └── vite.config.js
├── docs/
│   ├── API.md
│   ├── INSTALLATION.md
│   └── DEPLOYMENT.md
├── .gitignore
└── README.md
```

## 📦 Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **Node.js**: 16.0.0 or higher
- **npm**: 7.0.0 or higher
- **Database**: PostgreSQL 12+ (optional, SQLite for development)

### Required Tools
- Git
- Virtual environment tool (venv or conda)
- Code editor (VS Code, PyCharm, etc.)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mano31-a/epl-predictions-tool.git
cd epl-predictions-tool
```

### 2. Backend Setup

#### Create Virtual Environment

```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
# Required variables:
# - DATABASE_URL
# - SECRET_KEY
# - API_HOST
# - API_PORT
```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
```

#### Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
# Required variables:
# - VITE_API_URL
# - VITE_API_PORT
```

## ⚙️ Setup Instructions

### Backend Database Setup

```bash
cd backend

# Create database migrations (if using SQLAlchemy)
flask db init
flask db migrate
flask db upgrade

# Or if using Django
python manage.py migrate
```

### Load Initial Data

```bash
# Load EPL teams and historical data
python scripts/load_initial_data.py

# Train the prediction model
python scripts/train_model.py
```

### Initialize Configuration

1. Update database connection string in `.env`
2. Set API authentication keys
3. Configure CORS settings for frontend access
4. Set up logging configuration

## 🎮 Running the Backend

### Development Mode

```bash
cd backend

# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Run the development server
python run.py

# The API will be available at http://localhost:5000
```

### Production Mode

```bash
cd backend

# Using Gunicorn (recommended for production)
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app

# Or using a WSGI server of your choice
```

### Common Backend Endpoints

```
GET  /api/teams              - Get all teams
GET  /api/teams/<team_id>    - Get team details
GET  /api/matches            - Get upcoming matches
POST /api/predictions        - Get predictions for matches
GET  /api/predictions/<id>   - Get specific prediction
GET  /api/statistics         - Get accuracy statistics
```

## 🌐 Running the Frontend

### Development Mode

```bash
cd frontend

# Start the development server with Vite
npm run dev

# The application will be available at http://localhost:5173
# (or the port shown in terminal)
```

### Building for Production

```bash
cd frontend

# Create optimized production build
npm run build

# Preview the production build locally
npm run preview
```

### Environment Configuration

Make sure your frontend `.env` file points to the correct backend API:

```
VITE_API_URL=http://localhost
VITE_API_PORT=5000
```

## 📚 API Documentation

For detailed API documentation, including all endpoints, request/response formats, and authentication details, see [API.md](./docs/API.md)

### Quick API Reference

**Authentication**
```bash
POST /api/auth/login       - User login
POST /api/auth/register    - User registration
POST /api/auth/refresh     - Refresh token
```

**Predictions**
```bash
GET  /api/predictions           - Get all predictions
POST /api/predictions          - Create prediction
GET  /api/predictions/<id>     - Get prediction details
PUT  /api/predictions/<id>     - Update prediction
DELETE /api/predictions/<id>   - Delete prediction
```

**Teams**
```bash
GET  /api/teams              - Get all teams
GET  /api/teams/<id>         - Get team details
GET  /api/teams/<id>/stats   - Get team statistics
```

**Matches**
```bash
GET  /api/matches            - Get all matches
GET  /api/matches/<id>       - Get match details
GET  /api/matches/upcoming   - Get upcoming matches
```

## 🛠️ Development

### Running Tests

#### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_predictions.py
```

#### Frontend Tests

```bash
cd frontend

# Run tests
npm test

# Run with coverage
npm test -- --coverage
```

### Code Style and Linting

#### Backend

```bash
# Format code with Black
black app/

# Lint with Flake8
flake8 app/

# Type checking with mypy
mypy app/
```

#### Frontend

```bash
# Lint JavaScript/JSX
npm run lint

# Format code with Prettier
npm run format
```

### Database Migrations

```bash
cd backend

# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Rollback migrations
flask db downgrade
```

## 📝 Configuration Files

### Backend (.env)

```env
# Database
DATABASE_URL=postgresql://user:password@localhost/epl_predictions
# or
DATABASE_URL=sqlite:///./epl_predictions.db

# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# API Configuration
API_HOST=0.0.0.0
API_PORT=5000
API_URL=http://localhost:5000

# Machine Learning
MODEL_PATH=./models/prediction_model.pkl
DATA_PATH=./data/

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/app.log
```

### Frontend (.env)

```env
# API Configuration
VITE_API_URL=http://localhost
VITE_API_PORT=5000
VITE_API_TIMEOUT=30000

# Feature Flags
VITE_ENABLE_ANALYTICS=true
VITE_ENABLE_NOTIFICATIONS=true

# Environment
VITE_ENV=development
```

## 🚢 Deployment

For detailed deployment instructions for various platforms, see [DEPLOYMENT.md](./docs/DEPLOYMENT.md)

### Quick Deployment Checklist

- [ ] Update environment variables for production
- [ ] Run database migrations
- [ ] Build frontend for production
- [ ] Configure HTTPS/SSL certificates
- [ ] Set up proper logging and monitoring
- [ ] Configure backup strategies
- [ ] Test all API endpoints
- [ ] Set up automated updates for data
- [ ] Configure monitoring and alerting

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Write clear, descriptive commit messages
- Include tests for new features
- Update documentation as needed
- Follow the project's code style guidelines
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For issues, questions, or suggestions:

1. Check existing issues in the repository
2. Create a new issue with detailed information
3. Contact the maintainers directly

## 🔗 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Vite Documentation](https://vitejs.dev/)
- [Premier League API](https://www.premierleague.com/api)

## 📊 Project Status

- **Current Version**: 1.0.0
- **Last Updated**: January 2026
- **Status**: Active Development

---

**Made with ❤️ by the EPL Predictions Tool Team**

For the latest updates and releases, visit the [GitHub repository](https://github.com/Mano31-a/epl-predictions-tool)
