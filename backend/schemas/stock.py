"""
Pydantic schemas for stock-related data
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class StockBase(BaseModel):
    """Base stock schema"""
    symbol: str = Field(..., description="Stock symbol (e.g., THYAO)")
    name: str = Field(..., description="Company name")
    sector: Optional[str] = Field(None, description="Business sector")
    market_cap: Optional[int] = Field(None, description="Market capitalization")

class StockCreate(StockBase):
    """Schema for creating a new stock"""
    pass

class StockUpdate(BaseModel):
    """Schema for updating stock information"""
    name: Optional[str] = None
    sector: Optional[str] = None
    market_cap: Optional[int] = None

class Stock(StockBase):
    """Stock schema with database fields"""
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class StockPriceBase(BaseModel):
    """Base stock price schema"""
    stock_id: str
    price: float = Field(..., description="Current stock price")
    change: float = Field(..., description="Price change")
    change_percent: float = Field(..., description="Percentage change")
    volume: Optional[int] = Field(None, description="Trading volume")
    open_price: Optional[float] = Field(None, description="Opening price")
    high_price: Optional[float] = Field(None, description="Highest price")
    low_price: Optional[float] = Field(None, description="Lowest price")
    close_price: Optional[float] = Field(None, description="Closing price")

class StockPriceCreate(StockPriceBase):
    """Schema for creating stock price record"""
    pass

class StockPrice(StockPriceBase):
    """Stock price schema with database fields"""
    id: str
    timestamp: datetime
    
    class Config:
        from_attributes = True

class StockWithLatestPrice(Stock):
    """Stock with latest price information"""
    latest_price: Optional[StockPrice] = None
    price_history: List[StockPrice] = []

class StockListResponse(BaseModel):
    """Response schema for stock list"""
    stocks: List[StockWithLatestPrice]
    total: int
    page: int
    size: int

class StockDetailResponse(BaseModel):
    """Response schema for stock detail"""
    stock: StockWithLatestPrice
    price_history: List[StockPrice]
    
class StockSearchRequest(BaseModel):
    """Request schema for stock search"""
    query: Optional[str] = None
    sector: Optional[str] = None
    page: int = Field(1, ge=1)
    size: int = Field(20, ge=1, le=100) 