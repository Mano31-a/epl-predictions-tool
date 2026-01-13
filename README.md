# EPL Predictions Tool

A comprehensive tool for predicting English Premier League (EPL) match outcomes using machine learning and statistical analysis.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Backend Setup](#backend-setup)
  - [Installation](#backend-installation)
  - [Configuration](#backend-configuration)
  - [Running the Backend](#running-the-backend)
- [Frontend Setup](#frontend-setup)
  - [Installation](#frontend-installation)
  - [Configuration](#frontend-configuration)
  - [Running the Frontend](#running-the-frontend)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The EPL Predictions Tool is designed to:
- Analyze historical EPL match data
- Generate predictions for upcoming matches
- Provide detailed statistics and insights
- Visualize predictions and team performance metrics
- Deliver results through both a REST API and web interface

---

## Prerequisites

Before you begin, ensure you have the following installed:

### General Requirements
- **Git**: For version control ([Download](https://git-scm.com/))
- **Python 3.8+**: Required for the backend
- **Node.js 14+**: Required for the frontend
- **npm or yarn**: Package managers for Node.js

### Verify Installations
```bash
python --version
node --version
npm --version
```

---

## Backend Setup

### Backend Installation

1. **Clone the Repository** (if not already done)
   ```bash
   git clone https://github.com/Mano31-a/epl-predictions-tool.git
   cd epl-predictions-tool
   ```

2. **Navigate to Backend Directory**
   ```bash
   cd backend
   ```

3. **Create a Virtual Environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Backend Configuration

1. **Environment Variables**
   Create a `.env` file in the `backend` directory:
   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file with your configuration:
   ```
   FLASK_ENV=development
   FLASK_DEBUG=True
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=sqlite:///predictions.db
   API_PORT=5000
   LOG_LEVEL=INFO
   ```

2. **Database Setup** (if applicable)
   ```bash
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

### Running the Backend

1. **Activate Virtual Environment** (if not already activated)
   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

2. **Start the Backend Server**
   ```bash
   python app.py
   ```
   or
   ```bash
   flask run
   ```

3. **Verify Backend is Running**
   - Open your browser and navigate to: `http://localhost:5000`
   - You should see the API running or a confirmation message

4. **Access API Documentation** (if Swagger/OpenAPI is configured)
   - Navigate to: `http://localhost:5000/api/docs`

---

## Frontend Setup

### Frontend Installation

1. **Navigate to Frontend Directory**
   ```bash
   cd frontend
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```
   or if using yarn:
   ```bash
   yarn install
   ```

### Frontend Configuration

1. **Environment Variables**
   Create a `.env` file in the `frontend` directory:
   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file with your configuration:
   ```
   REACT_APP_API_URL=http://localhost:5000/api
   REACT_APP_API_TIMEOUT=30000
   NODE_ENV=development
   ```

2. **Update API Base URL** (if using a different backend address)
   - Edit `src/config/api.js` or relevant configuration file
   - Update the `API_BASE_URL` to match your backend URL

### Running the Frontend

1. **Start the Development Server**
   ```bash
   npm start
   ```
   or with yarn:
   ```bash
   yarn start
   ```

2. **Access the Application**
   - The application will automatically open in your browser
   - If not, navigate to: `http://localhost:3000`

3. **Build for Production** (when ready to deploy)
   ```bash
   npm run build
   ```
   or
   ```bash
   yarn build
   ```

---

## Project Structure

```
epl-predictions-tool/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example            # Example environment variables
│   ├── config/                 # Configuration files
│   ├── models/                 # Machine learning models
│   ├── routes/                 # API routes/endpoints
│   ├── utils/                  # Utility functions
│   └── data/                   # Data storage and processing
├── frontend/
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   ├── services/           # API service calls
│   │   ├── App.js              # Main App component
│   │   └── index.js            # React entry point
│   ├── public/                 # Static assets
│   ├── package.json            # Node.js dependencies
│   ├── .env.example            # Example environment variables
│   └── package-lock.json       # Dependency lock file
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
└── LICENSE                     # License file
```

---

## API Documentation

### Base URL
```
http://localhost:5000/api
```

### Available Endpoints

#### Predictions
- `GET /predictions` - Get all predictions
- `GET /predictions/<id>` - Get a specific prediction
- `POST /predictions` - Create a new prediction
- `PUT /predictions/<id>` - Update a prediction
- `DELETE /predictions/<id>` - Delete a prediction

#### Teams
- `GET /teams` - Get all teams
- `GET /teams/<id>` - Get team details
- `GET /teams/<id>/stats` - Get team statistics

#### Matches
- `GET /matches` - Get all matches
- `GET /matches/<id>` - Get match details
- `GET /matches/upcoming` - Get upcoming matches

#### Statistics
- `GET /stats/league` - Get league statistics
- `GET /stats/team/<team_id>` - Get team statistics

For detailed API documentation, refer to the backend's API docs endpoint once the server is running.

---

## Troubleshooting

### Backend Issues

**Port Already in Use**
```bash
# Find and kill the process using port 5000
# On Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On macOS/Linux
lsof -i :5000
kill -9 <PID>
```

**Module Import Errors**
```bash
# Ensure virtual environment is activated and run
pip install -r requirements.txt
```

### Frontend Issues

**Port Already in Use**
```bash
# Specify a different port
PORT=3001 npm start
```

**Dependencies Installation Failed**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Cannot Connect to Backend**
- Ensure backend is running on the configured port
- Check the `REACT_APP_API_URL` environment variable
- Verify firewall settings allow the connection

---

## Development Workflow

### Making Changes

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Backend: Modify files in the `backend/` directory
   - Frontend: Modify files in the `frontend/` directory

3. **Test Your Changes**
   - Run the application and test functionality
   - Ensure no errors in browser console or terminal

4. **Commit and Push**
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Go to GitHub and create a pull request
   - Provide a clear description of your changes

---

## Running Both Services Simultaneously

For development, you may want to run both services in parallel:

### Option 1: Two Terminal Windows
**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

### Option 2: Using Concurrently (from project root)
If you have `concurrently` installed:
```bash
npm install -g concurrently
concurrently "cd backend && python app.py" "cd frontend && npm start"
```

---

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write or update tests as needed
5. Ensure code follows project style guidelines
6. Submit a pull request with a clear description

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team

---

**Last Updated:** January 13, 2026
