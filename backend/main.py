"""
TRIZ Trade Backend API
FastAPI backend for financial data platform
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routers
from app.routers import stocks, currencies, auth, data

# Import services
from services.data_collector import DataCollectorService
from config.database import init_db
from config.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle management for FastAPI app"""
    # Startup
    print("🚀 Starting TRIZ Trade Backend...")
    
    # Initialize database
    await init_db()
    
    # Initialize data collector service
    data_collector = DataCollectorService()
    app.state.data_collector = data_collector
    
    # Start background tasks for data collection
    await data_collector.start_background_tasks()
    
    print("✅ Backend started successfully!")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down TRIZ Trade Backend...")
    if hasattr(app.state, 'data_collector'):
        await app.state.data_collector.stop_background_tasks()
    print("✅ Backend shutdown complete!")

# Create FastAPI application
app = FastAPI(
    title="TRIZ Trade API",
    description="Financial data platform backend for BIST stocks and currency rates",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# Add security middleware
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=["localhost", "127.0.0.1", "*.vercel.app"]
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(stocks.router, prefix="/api/v1/stocks", tags=["Stocks"])
app.include_router(currencies.router, prefix="/api/v1/currencies", tags=["Currencies"])
app.include_router(data.router, prefix="/api/v1/data", tags=["Data Management"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "TRIZ Trade API",
        "version": "1.0.0",
        "status": "active",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "triz-trade-backend",
        "version": "1.0.0"
    }

@app.get("/api/v1/info")
async def api_info():
    """API information endpoint"""
    return {
        "api_name": "TRIZ Trade API",
        "version": "1.0.0",
        "endpoints": {
            "stocks": "/api/v1/stocks",
            "currencies": "/api/v1/currencies",
            "auth": "/api/v1/auth",
            "data": "/api/v1/data"
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info"
    ) 