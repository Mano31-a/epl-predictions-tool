# EPL Predictions Tool

A comprehensive web application for predicting English Premier League (EPL) match outcomes using machine learning and statistical analysis.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Predictions
- **Machine Learning Models**: Leverages multiple ML algorithms to predict match outcomes
- **Statistical Analysis**: Analyzes historical EPL data for pattern recognition
- **Real-time Updates**: Updates predictions as new match data becomes available
- **Confidence Scoring**: Provides confidence metrics for each prediction

### User Interface
- **Interactive Dashboard**: Browse predictions across all EPL fixtures
- **Match Details**: View in-depth analysis for individual matches
- **Historical Data**: Access past predictions and actual results
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

### Data Management
- **Automated Data Sync**: Regularly updates with latest EPL data
- **Team Statistics**: Tracks team performance metrics
- **Player Analysis**: Individual player performance insights
- **Trend Analysis**: Identifies team form and momentum

## Project Structure

```
epl-predictions-tool/
├── backend/
│   ├── app.py                 # Flask application entry point
│   ├── config.py              # Configuration settings
│   ├── requirements.txt        # Python dependencies
│   ├── models/
│   │   ├── prediction_model.py # ML prediction logic
│   │   └── data_processor.py   # Data processing utilities
│   ├── routes/
│   │   ├── predictions.py      # Prediction API endpoints
│   │   ├── matches.py          # Match data endpoints
│   │   └── teams.py            # Team data endpoints
│   ├── utils/
│   │   ├── database.py         # Database utilities
│   │   ├── api_client.py       # External API integration
│   │   └── helpers.py          # Helper functions
│   └── database/
│       └── models.py           # Database models
│
├── frontend/
│   ├── public/
│   │   ├── index.html          # Main HTML file
│   │   └── favicon.ico         # App icon
│   ├── src/
│   │   ├── App.js              # Main App component
│   │   ├── index.js            # React entry point
│   │   ├── components/
│   │   │   ├── Dashboard.js     # Main dashboard
│   │   │   ├── MatchCard.js     # Individual match card
│   │   │   ├── PredictionDetails.js
│   │   │   └── Navbar.js        # Navigation bar
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── Predictions.js
│   │   │   └── Statistics.js
│   │   ├── services/
│   │   │   └── api.js          # API communication
│   │   ├── styles/
│   │   │   └── App.css         # Global styles
│   │   └── utils/
│   │       └── helpers.js      # Utility functions
│   ├── package.json            # Node dependencies
│   └── .env.example            # Environment variables template
│
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml      # Multi-container setup
│
├── .gitignore
├── README.md                   # This file
└── LICENSE
```

## Prerequisites

### Required Software
- **Python 3.8+** - For backend development
- **Node.js 14+** and **npm 6+** - For frontend development
- **PostgreSQL 12+** or **SQLite** - Database
- **Git** - Version control

### Recommended Tools
- **Docker** and **Docker Compose** - For containerized deployment
- **Virtual Environment** (venv or conda) - Python environment isolation
- **VS Code** or **PyCharm** - Code editor/IDE

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mano31-a/epl-predictions-tool.git
cd epl-predictions-tool
```

### 2. Backend Setup

#### Create and Activate Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

#### Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Frontend Setup

#### Install Node Dependencies

```bash
cd ../frontend
npm install
```

#### Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
# REACT_APP_API_URL=http://localhost:5000
# REACT_APP_API_TIMEOUT=5000
```

## Setup Instructions

### Backend Configuration

1. **Create `.env` file in the backend directory:**

```bash
cd backend
touch .env
```

2. **Add the following environment variables:**

```env
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Database Configuration
DATABASE_URL=sqlite:///epl_predictions.db
# or for PostgreSQL
# DATABASE_URL=postgresql://username:password@localhost:5432/epl_predictions

# API Configuration
EXTERNAL_API_KEY=your-api-key
EXTERNAL_API_URL=https://api.example.com

# Prediction Settings
MODEL_PATH=./models/trained_model.pkl
CONFIDENCE_THRESHOLD=0.65

# Server Configuration
PORT=5000
DEBUG=True
```

3. **Initialize the Database:**

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Frontend Configuration

The frontend configuration is managed through environment variables in the `.env` file (copied from `.env.example`).

Key variables:
- `REACT_APP_API_URL` - Backend API base URL
- `REACT_APP_API_TIMEOUT` - API request timeout in milliseconds

## Running the Application

### Option 1: Local Development (Recommended for Development)

#### Terminal 1 - Start Backend Server

```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

The backend will start on `http://localhost:5000`

#### Terminal 2 - Start Frontend Development Server

```bash
cd frontend
npm start
```

The frontend will start on `http://localhost:3000` and open automatically in your browser.

### Option 2: Docker Deployment (Recommended for Production)

#### Build and Run with Docker Compose

```bash
# Build images
docker-compose build

# Start containers
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

The application will be available at:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5000`

#### Individual Docker Commands

```bash
# Build backend image
docker build -f docker/Dockerfile.backend -t epl-backend .

# Run backend container
docker run -p 5000:5000 --env-file backend/.env epl-backend

# Build frontend image
docker build -f docker/Dockerfile.frontend -t epl-frontend .

# Run frontend container
docker run -p 3000:3000 epl-frontend
```

### Running Tests

#### Backend Tests

```bash
cd backend
pytest -v
pytest --cov=.  # Generate coverage report
```

#### Frontend Tests

```bash
cd frontend
npm test
npm run build  # Build for production
```

## Configuration

### Backend Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | development | Environment mode (development/production) |
| `SECRET_KEY` | None | Flask secret key for sessions |
| `DATABASE_URL` | sqlite:///epl.db | Database connection string |
| `DEBUG` | False | Enable/disable debug mode |
| `PORT` | 5000 | Server port |
| `EXTERNAL_API_KEY` | None | API key for external data sources |

### Frontend Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `REACT_APP_API_URL` | http://localhost:5000 | Backend API base URL |
| `REACT_APP_API_TIMEOUT` | 5000 | Request timeout in ms |
| `REACT_APP_DEBUG` | false | Enable/disable debug logging |

## API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### Get All Predictions
```
GET /api/predictions
```

#### Get Prediction by ID
```
GET /api/predictions/{id}
```

#### Get Matches
```
GET /api/matches?date=2026-01-13&team=Arsenal
```

#### Get Team Statistics
```
GET /api/teams/{team_name}/stats
```

For detailed API documentation, see [API.md](./API.md) or access the interactive Swagger documentation at `http://localhost:5000/api/docs`.

## Development Workflow

### Creating a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### Making Changes

1. Make your changes
2. Test your changes locally
3. Commit with descriptive messages

```bash
git add .
git commit -m "feat: add new prediction algorithm"
```

### Submitting a Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Troubleshooting

### Backend Issues

**ModuleNotFoundError: No module named 'flask'**
- Solution: Ensure virtual environment is activated and dependencies are installed
  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

**Database Connection Error**
- Solution: Check `DATABASE_URL` in `.env` and ensure database is running

**Port Already in Use**
- Solution: Change port in `.env` or kill the process using the port
  ```bash
  # macOS/Linux
  lsof -i :5000 | grep LISTEN | awk '{print $2}' | xargs kill -9
  ```

### Frontend Issues

**npm ERR! Cannot find module**
- Solution: Clear node_modules and reinstall
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

**CORS Errors**
- Solution: Ensure backend `.env` has correct `CORS_ORIGINS`
  ```env
  CORS_ORIGINS=http://localhost:3000
  ```

## Performance Optimization

- **Caching**: Implement Redis for caching frequently accessed data
- **Database Indexing**: Optimize database queries with proper indexes
- **Frontend Lazy Loading**: Implement code splitting for React components
- **API Rate Limiting**: Implement rate limiting to protect the backend

## Security Considerations

- Never commit `.env` files to version control
- Use strong, unique secret keys in production
- Implement HTTPS in production
- Sanitize user inputs on both frontend and backend
- Keep dependencies updated: `npm audit` and `pip audit`

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Last Updated**: January 13, 2026

For issues, questions, or suggestions, please open an [issue](https://github.com/Mano31-a/epl-predictions-tool/issues) on GitHub.
