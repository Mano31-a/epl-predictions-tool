# EPL Predictions Tool

A comprehensive machine learning tool for predicting English Premier League (EPL) match outcomes using historical data, team statistics, and advanced predictive models.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Overview

The EPL Predictions Tool leverages machine learning algorithms and historical EPL data to generate accurate predictions for upcoming matches. It analyzes team performance metrics, head-to-head records, player statistics, and various other factors to provide probability-based match outcome predictions.

## Features

- **Match Outcome Predictions**: Predicts win/draw/loss probabilities for upcoming matches
- **Historical Data Analysis**: Processes historical EPL match data for model training
- **Team Statistics**: Tracks and analyzes team performance metrics
- **Multiple ML Models**: Implements various machine learning algorithms for ensemble predictions
- **Data Visualization**: Generates charts and reports of predictions and historical trends
- **Real-time Updates**: Fetches and processes latest EPL data
- **Confidence Scores**: Provides confidence metrics for each prediction

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **Git**: For cloning the repository
- **Virtual Environment**: Python venv or conda

### System Requirements

- **Disk Space**: At least 2GB for data and dependencies
- **RAM**: Minimum 4GB recommended
- **Internet Connection**: Required for fetching live EPL data and updates

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mano31-a/epl-predictions-tool.git
cd epl-predictions-tool
```

### 2. Create a Virtual Environment

#### Using venv:

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### Using conda:

```bash
conda create -n epl-predictions python=3.8
conda activate epl-predictions
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install essential packages:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn requests beautifulsoup4 jupyter
```

### 4. Verify Installation

```bash
python -c "import pandas; import sklearn; print('Installation successful!')"
```

## Configuration

### 1. Environment Variables

Create a `.env` file in the project root directory:

```env
# API Configuration
EPL_API_KEY=your_api_key_here
EPL_API_BASE_URL=https://api.example.com

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=epl_predictions
DB_USER=your_username
DB_PASSWORD=your_password

# Model Configuration
MODEL_TYPE=gradient_boosting
CONFIDENCE_THRESHOLD=0.65

# Data Configuration
DATA_DIR=./data
RESULTS_DIR=./results
```

### 2. Download Historical Data

```bash
python scripts/download_historical_data.py
```

This script downloads historical EPL match data for training the models.

### 3. Configure API Keys (Optional)

If using external APIs for real-time data:

1. Sign up for an EPL data provider (e.g., RapidAPI, ESPN)
2. Add your API key to the `.env` file
3. Update the configuration in `config/api_config.json`

## Usage

### Quick Start

```bash
# Run predictions for upcoming matches
python predict.py

# Generate predictions with verbose output
python predict.py --verbose

# Predict for a specific date range
python predict.py --start-date 2026-01-15 --end-date 2026-01-31
```

### Running the Complete Pipeline

```bash
# 1. Fetch latest data
python scripts/fetch_data.py

# 2. Preprocess and clean data
python scripts/preprocess_data.py

# 3. Train models
python scripts/train_models.py

# 4. Generate predictions
python scripts/generate_predictions.py

# 5. Generate report
python scripts/generate_report.py
```

### Interactive Jupyter Notebook

```bash
jupyter notebook
# Open 'notebooks/predictions_analysis.ipynb' for interactive analysis
```

### Command-line Options

```bash
usage: predict.py [-h] [--verbose] [--model MODEL] [--output OUTPUT]
                   [--start-date START_DATE] [--end-date END_DATE]

optional arguments:
  -h, --help            Show help message
  --verbose             Enable verbose output
  --model MODEL         Specify model type (default: ensemble)
  --output OUTPUT       Output file path for results
  --start-date START_DATE   Start date for predictions (YYYY-MM-DD)
  --end-date END_DATE       End date for predictions (YYYY-MM-DD)
```

## Project Structure

```
epl-predictions-tool/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── .env.example                   # Example environment variables
├── .gitignore                     # Git ignore rules
│
├── src/
│   ├── __init__.py
│   ├── models/                    # ML models
│   │   ├── __init__.py
│   │   ├── ensemble_model.py
│   │   ├── gradient_boosting.py
│   │   └── neural_network.py
│   │
│   ├── data/                      # Data processing
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── preprocessor.py
│   │   └── fetcher.py
│   │
│   ├── utils/                     # Utility functions
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── visualization.py
│   │   └── config.py
│   │
│   └── api/                       # API integrations
│       ├── __init__.py
│       ├── epl_api.py
│       └── data_provider.py
│
├── scripts/
│   ├── download_historical_data.py
│   ├── fetch_data.py
│   ├── preprocess_data.py
│   ├── train_models.py
│   ├── generate_predictions.py
│   └── generate_report.py
│
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── model_evaluation.ipynb
│   └── predictions_analysis.ipynb
│
├── data/
│   ├── raw/                       # Raw EPL data
│   ├── processed/                 # Processed data for models
│   └── predictions/               # Generated predictions
│
├── models/
│   ├── trained_models/            # Saved trained models
│   └── scaler_objects/            # Preprocessing scalers
│
├── results/
│   ├── predictions.csv
│   ├── report.html
│   └── metrics.json
│
├── config/
│   ├── api_config.json
│   ├── model_config.json
│   └── feature_config.json
│
└── tests/
    ├── __init__.py
    ├── test_models.py
    ├── test_data.py
    └── test_predictions.py
```

## API Reference

### Making Predictions

```python
from src.models import EnsembleModel
from src.data import DataLoader

# Load and prepare data
loader = DataLoader()
X_test = loader.load_upcoming_matches()

# Load pre-trained model
model = EnsembleModel.load('models/trained_models/ensemble_model.pkl')

# Generate predictions
predictions = model.predict(X_test)

# Get probability scores
probabilities = model.predict_proba(X_test)
```

### Training a New Model

```python
from src.models import GradientBoostingModel
from src.data import DataLoader

# Load historical data
loader = DataLoader()
X_train, y_train = loader.load_training_data()

# Train model
model = GradientBoostingModel(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)

# Save model
model.save('models/trained_models/gb_model.pkl')
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_models.py -v

# Run with coverage
pytest tests/ --cov=src
```

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'src'`
```bash
# Solution: Add project root to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Issue**: API key not recognized
```bash
# Solution: Verify .env file exists and contains correct key
cat .env | grep EPL_API_KEY
```

**Issue**: Insufficient memory for model training
```bash
# Solution: Use data batching
python scripts/train_models.py --batch-size 1000
```

**Issue**: Data download fails
```bash
# Solution: Check internet connection and API availability
python scripts/fetch_data.py --verbose
```

## Performance Metrics

The tool tracks several key metrics:

- **Accuracy**: Overall prediction correctness
- **Precision/Recall**: Per-class prediction quality
- **ROC-AUC**: Model discrimination ability
- **Calibration**: Prediction confidence reliability
- **Mean Absolute Error**: Prediction deviation magnitude

View detailed metrics:

```bash
python scripts/evaluate_models.py
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

Please ensure:
- Code follows PEP 8 style guidelines
- All tests pass
- New features include unit tests
- Documentation is updated

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:

1. Check existing [GitHub Issues](https://github.com/Mano31-a/epl-predictions-tool/issues)
2. Create a new issue with detailed description
3. Include error messages, Python version, and OS information

## Disclaimer

These predictions are generated based on statistical models and historical data. They are not guaranteed to be accurate and should not be used as the sole basis for betting or financial decisions. Use at your own risk.

## Acknowledgments

- English Premier League for providing match data
- Data science community for open-source libraries
- Contributors and testers

---

**Last Updated**: January 2026

For the latest version and updates, visit the [GitHub repository](https://github.com/Mano31-a/epl-predictions-tool).
