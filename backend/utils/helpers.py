"""
Helper utility functions
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

def format_currency(amount: float, currency: str = "TRY") -> str:
    """Format currency amount with proper symbol"""
    symbols = {
        "TRY": "₺",
        "USD": "$",
        "EUR": "€",
        "GBP": "£"
    }
    
    symbol = symbols.get(currency, currency)
    return f"{amount:,.2f} {symbol}"

def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculate percentage change between two values"""
    if old_value == 0:
        return 0.0
    
    return ((new_value - old_value) / old_value) * 100

def get_market_status() -> Dict[str, Any]:
    """Get current market status (open/closed)"""
    now = datetime.now()
    
    # BIST trading hours: 10:00 - 18:00 (Turkey time)
    market_open = now.replace(hour=10, minute=0, second=0, microsecond=0)
    market_close = now.replace(hour=18, minute=0, second=0, microsecond=0)
    
    # Check if it's weekend
    is_weekend = now.weekday() >= 5  # Saturday = 5, Sunday = 6
    
    # Check if market is open
    is_open = not is_weekend and market_open <= now <= market_close
    
    return {
        "is_open": is_open,
        "is_weekend": is_weekend,
        "next_open": market_open + timedelta(days=1) if now > market_close else market_open,
        "next_close": market_close if now < market_close else market_close + timedelta(days=1)
    }

def validate_symbol(symbol: str, symbol_type: str = "stock") -> bool:
    """Validate stock or currency symbol format"""
    if not symbol or not isinstance(symbol, str):
        return False
    
    symbol = symbol.upper().strip()
    
    if symbol_type == "stock":
        # BIST stock symbols: 3-6 characters
        return 3 <= len(symbol) <= 6 and symbol.isalpha()
    elif symbol_type == "currency":
        # Currency pair format: XXX/YYY or XXXYYY
        if "/" in symbol:
            parts = symbol.split("/")
            return len(parts) == 2 and all(len(part) == 3 and part.isalpha() for part in parts)
        else:
            return len(symbol) == 6 and symbol.isalpha()
    
    return False

def get_time_intervals() -> List[Dict[str, str]]:
    """Get available time intervals for data queries"""
    return [
        {"value": "1m", "label": "1 Dakika"},
        {"value": "5m", "label": "5 Dakika"},
        {"value": "15m", "label": "15 Dakika"},
        {"value": "30m", "label": "30 Dakika"},
        {"value": "1h", "label": "1 Saat"},
        {"value": "1d", "label": "1 Gün"},
        {"value": "1w", "label": "1 Hafta"},
        {"value": "1mo", "label": "1 Ay"}
    ]

def sanitize_input(input_str: str, max_length: int = 100) -> str:
    """Sanitize user input"""
    if not input_str:
        return ""
    
    # Remove potentially dangerous characters
    sanitized = input_str.strip()[:max_length]
    
    # Remove SQL injection attempts
    dangerous_chars = ["'", '"', ";", "--", "/*", "*/", "xp_", "sp_"]
    for char in dangerous_chars:
        sanitized = sanitized.replace(char, "")
    
    return sanitized

def log_api_request(endpoint: str, method: str, user_id: Optional[str] = None, 
                   params: Optional[Dict] = None):
    """Log API request for monitoring"""
    log_data = {
        "endpoint": endpoint,
        "method": method,
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "params": params
    }
    
    logger.info(f"API Request: {log_data}")

def format_error_response(error: Exception, request_id: Optional[str] = None) -> Dict[str, Any]:
    """Format error response consistently"""
    return {
        "error": True,
        "message": str(error),
        "type": type(error).__name__,
        "request_id": request_id,
        "timestamp": datetime.now().isoformat()
    } 