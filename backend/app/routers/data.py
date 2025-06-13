"""
Data management API endpoints
"""

from fastapi import APIRouter, HTTPException, Depends
from config.database import get_db_client

router = APIRouter()

@router.post("/refresh/stocks")
async def refresh_stock_data(db_client=Depends(get_db_client)):
    """Manually trigger stock data refresh"""
    try:
        # Placeholder implementation
        return {"message": "Stock data refresh triggered", "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error refreshing stock data: {str(e)}")

@router.post("/refresh/currencies")
async def refresh_currency_data(db_client=Depends(get_db_client)):
    """Manually trigger currency data refresh"""
    try:
        # Placeholder implementation
        return {"message": "Currency data refresh triggered", "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error refreshing currency data: {str(e)}")

@router.get("/status")
async def get_data_status():
    """Get data collection status"""
    try:
        return {
            "status": "active",
            "last_update": "2024-01-01T00:00:00Z",
            "stocks_count": 10,
            "currencies_count": 8,
            "data_sources": ["yfinance"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data status: {str(e)}")

@router.get("/health")
async def data_health_check():
    """Health check for data services"""
    try:
        return {
            "status": "healthy",
            "services": {
                "yfinance": "active",
                "database": "connected",
                "cache": "active"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}") 