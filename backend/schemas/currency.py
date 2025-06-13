"""
Pydantic schemas for currency-related data
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class CurrencyBase(BaseModel):
    """Base currency schema"""
    symbol: str = Field(..., description="Currency pair symbol (e.g., USD/TRY)")
    name: str = Field(..., description="Currency pair name")

class CurrencyCreate(CurrencyBase):
    """Schema for creating a new currency pair"""
    pass

class CurrencyUpdate(BaseModel):
    """Schema for updating currency information"""
    name: Optional[str] = None

class Currency(CurrencyBase):
    """Currency schema with database fields"""
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class CurrencyRateBase(BaseModel):
    """Base currency rate schema"""
    currency_id: str
    rate: float = Field(..., description="Exchange rate")
    change: float = Field(..., description="Rate change")
    change_percent: float = Field(..., description="Percentage change")
    bid: Optional[float] = Field(None, description="Bid price")
    ask: Optional[float] = Field(None, description="Ask price")
    open_rate: Optional[float] = Field(None, description="Opening rate")
    high_rate: Optional[float] = Field(None, description="Highest rate")
    low_rate: Optional[float] = Field(None, description="Lowest rate")
    close_rate: Optional[float] = Field(None, description="Closing rate")

class CurrencyRateCreate(CurrencyRateBase):
    """Schema for creating currency rate record"""
    pass

class CurrencyRate(CurrencyRateBase):
    """Currency rate schema with database fields"""
    id: str
    timestamp: datetime
    
    class Config:
        from_attributes = True

class CurrencyWithLatestRate(Currency):
    """Currency with latest rate information"""
    latest_rate: Optional[CurrencyRate] = None
    rate_history: List[CurrencyRate] = []

class CurrencyListResponse(BaseModel):
    """Response schema for currency list"""
    currencies: List[CurrencyWithLatestRate]
    total: int
    page: int
    size: int

class CurrencyDetailResponse(BaseModel):
    """Response schema for currency detail"""
    currency: CurrencyWithLatestRate
    rate_history: List[CurrencyRate]

class CurrencySearchRequest(BaseModel):
    """Request schema for currency search"""
    query: Optional[str] = None
    page: int = Field(1, ge=1)
    size: int = Field(20, ge=1, le=100) 