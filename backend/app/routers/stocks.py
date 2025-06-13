"""
Stock-related API endpoints
"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from datetime import datetime, timedelta

from config.database import get_db_client
from schemas.stock import (
    Stock, StockCreate, StockUpdate, StockListResponse,
    StockDetailResponse, StockSearchRequest, StockWithLatestPrice
)
from services.stock_service import StockService

router = APIRouter()
stock_service = StockService()

@router.get("/", response_model=StockListResponse)
async def get_stocks(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    sector: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db_client=Depends(get_db_client)
):
    """Get list of stocks with pagination and filtering"""
    try:
        stock_service = StockService(db_client)
        
        stocks = await stock_service.get_stocks_with_pagination(
            page=page,
            size=size,
            sector=sector,
            search_query=search
        )
        
        total = await stock_service.get_total_count(sector=sector, search_query=search)
        
        return StockListResponse(
            stocks=stocks,
            total=total,
            page=page,
            size=size
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stocks: {str(e)}")

@router.get("/{stock_id}", response_model=StockDetailResponse)
async def get_stock_detail(
    stock_id: str,
    days: int = Query(30, ge=1, le=365),
    db_client=Depends(get_db_client)
):
    """Get detailed stock information with price history"""
    try:
        stock_service = StockService(db_client)
        
        stock = await stock_service.get_stock_by_id(stock_id)
        if not stock:
            raise HTTPException(status_code=404, detail="Stock not found")
        
        # Get price history for specified days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        price_history = await stock_service.get_price_history(
            stock_id=stock_id,
            start_date=start_date,
            end_date=end_date
        )
        
        return StockDetailResponse(
            stock=stock,
            price_history=price_history
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stock detail: {str(e)}")

@router.get("/{stock_id}/prices")
async def get_stock_prices(
    stock_id: str,
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    interval: str = Query("1d", regex="^(1m|5m|15m|30m|1h|1d)$"),
    db_client=Depends(get_db_client)
):
    """Get stock price history with different intervals"""
    try:
        stock_service = StockService(db_client)
        
        # Set default date range if not provided
        if not end_date:
            end_date = datetime.now()
        if not start_date:
            start_date = end_date - timedelta(days=30)
        
        prices = await stock_service.get_price_history_with_interval(
            stock_id=stock_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval
        )
        
        return {
            "stock_id": stock_id,
            "start_date": start_date,
            "end_date": end_date,
            "interval": interval,
            "prices": prices
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching price history: {str(e)}")

@router.get("/{stock_id}/latest")
async def get_latest_stock_price(
    stock_id: str,
    db_client=Depends(get_db_client)
):
    """Get latest stock price"""
    try:
        stock_service = StockService(db_client)
        
        latest_price = await stock_service.get_latest_price(stock_id)
        if not latest_price:
            raise HTTPException(status_code=404, detail="No price data found for this stock")
        
        return latest_price
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching latest price: {str(e)}")

@router.get("/sectors/list")
async def get_sectors(db_client=Depends(get_db_client)):
    """Get list of all sectors"""
    try:
        stock_service = StockService(db_client)
        sectors = await stock_service.get_all_sectors()
        
        return {
            "sectors": sectors
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching sectors: {str(e)}")

@router.post("/", response_model=Stock)
async def create_stock(
    stock: StockCreate,
    db_client=Depends(get_db_client)
):
    """Create a new stock (Admin only)"""
    try:
        stock_service = StockService(db_client)
        
        # Check if stock already exists
        existing_stock = await stock_service.get_stock_by_symbol(stock.symbol)
        if existing_stock:
            raise HTTPException(status_code=400, detail="Stock with this symbol already exists")
        
        new_stock = await stock_service.create_stock(stock)
        return new_stock
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating stock: {str(e)}")

@router.put("/{stock_id}", response_model=Stock)
async def update_stock(
    stock_id: str,
    stock_update: StockUpdate,
    db_client=Depends(get_db_client)
):
    """Update stock information (Admin only)"""
    try:
        stock_service = StockService(db_client)
        
        updated_stock = await stock_service.update_stock(stock_id, stock_update)
        if not updated_stock:
            raise HTTPException(status_code=404, detail="Stock not found")
        
        return updated_stock
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating stock: {str(e)}")

@router.delete("/{stock_id}")
async def delete_stock(
    stock_id: str,
    db_client=Depends(get_db_client)
):
    """Delete a stock (Admin only)"""
    try:
        stock_service = StockService(db_client)
        
        success = await stock_service.delete_stock(stock_id)
        if not success:
            raise HTTPException(status_code=404, detail="Stock not found")
        
        return {"message": "Stock deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting stock: {str(e)}") 