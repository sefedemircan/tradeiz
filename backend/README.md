# TRIZ Trade Backend

Python FastAPI backend for TRIZ Trade financial platform.

## Features

- **Real-time Data Collection**: Automatic data collection from yfinance
- **RESTful API**: Comprehensive REST API for stocks and currencies
- **Database Integration**: Supabase PostgreSQL integration
- **Background Tasks**: Automated data updates
- **Error Handling**: Comprehensive error handling and logging
- **API Documentation**: Auto-generated OpenAPI/Swagger docs

## Tech Stack

- **Framework**: FastAPI
- **Database**: Supabase (PostgreSQL)
- **Data Source**: yfinance
- **Authentication**: Supabase Auth (planned)
- **Deployment**: Python 3.9+

## Project Structure

```
backend/
├── app/
│   ├── routers/          # API route handlers
│   │   ├── stocks.py     # Stock endpoints
│   │   ├── currencies.py # Currency endpoints
│   │   ├── auth.py       # Authentication
│   │   └── data.py       # Data management
│   └── __init__.py
├── config/
│   ├── database.py       # Database configuration
│   └── settings.py       # App settings
├── schemas/
│   ├── stock.py          # Stock data models
│   └── currency.py       # Currency data models
├── services/
│   ├── stock_service.py      # Stock business logic
│   ├── currency_service.py   # Currency business logic
│   └── data_collector.py     # Data collection service
├── utils/
│   └── helpers.py        # Utility functions
├── tests/
│   └── test_api.py       # API tests
├── main.py               # FastAPI application
├── run.py                # Development server
└── requirements.txt      # Python dependencies
```

## API Endpoints

### Stocks
- `GET /api/v1/stocks/` - List stocks with pagination
- `GET /api/v1/stocks/{id}` - Get stock details
- `GET /api/v1/stocks/{id}/prices` - Get price history
- `GET /api/v1/stocks/{id}/latest` - Get latest price
- `GET /api/v1/stocks/sectors/list` - List sectors

### Currencies
- `GET /api/v1/currencies/` - List currencies
- `GET /api/v1/currencies/{id}` - Get currency details
- `GET /api/v1/currencies/{id}/rates` - Get rate history
- `GET /api/v1/currencies/{id}/latest` - Get latest rate

### Data Management
- `POST /api/v1/data/refresh/stocks` - Refresh stock data
- `POST /api/v1/data/refresh/currencies` - Refresh currency data
- `GET /api/v1/data/status` - Get data status
- `GET /api/v1/data/health` - Health check

### Authentication (Planned)
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/logout` - User logout
- `GET /api/v1/auth/me` - Get current user

## Setup

### 1. Environment Setup

Create `.env` file in backend directory:

```env
# Application Settings
DEBUG=True
HOST=127.0.0.1
PORT=8000

# Supabase Configuration
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key

# CORS Settings
CORS_ORIGINS=["http://localhost:3000"]

# Data Collection Settings
DATA_UPDATE_INTERVAL=300
CURRENCY_UPDATE_INTERVAL=60

# Logging
LOG_LEVEL=INFO
```

### 2. Install Dependencies

```bash
# From project root
npm run backend:install

# Or directly in backend folder
cd backend
pip install -r requirements.txt
```

### 3. Run Development Server

```bash
# From project root
npm run backend:dev

# Or directly in backend folder
cd backend
python run.py
```

### 4. Run with Frontend

```bash
# From project root
npm run dev:all
```

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Data Collection

The backend automatically collects data from yfinance:

- **Stocks**: Updates every 5 minutes during market hours
- **Currencies**: Updates every 1 minute
- **Background Tasks**: Automatic data collection service

## Database Schema

### Tables
- `stocks` - Stock information
- `stock_prices` - Historical stock prices
- `currencies` - Currency pairs
- `currency_rates` - Historical exchange rates
- `user_watchlists` - User favorites (planned)

## Testing

```bash
cd backend
python -m pytest tests/
```

## Deployment

### Production Setup

1. Set production environment variables
2. Use production WSGI server (gunicorn)
3. Configure reverse proxy (nginx)
4. Set up SSL certificates

### Docker (Planned)

```bash
docker build -t triz-trade-backend .
docker run -p 8000:8000 triz-trade-backend
```

## Contributing

1. Follow PEP 8 style guide
2. Add type hints
3. Write tests for new features
4. Update documentation

## License

Private project - All rights reserved. 