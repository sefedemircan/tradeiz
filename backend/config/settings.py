"""
Configuration settings for TRIZ Trade Backend
"""

import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import validator

class Settings(BaseSettings):
    """Application settings"""
    
    # Basic App Settings
    app_name: str = "TRIZ Trade API"
    version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    # Server Settings
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    
    # Security Settings
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Supabase Settings
    supabase_url: str = os.getenv("SUPABASE_URL", "")
    supabase_key: str = os.getenv("SUPABASE_ANON_KEY", "")  # Unified key name
    supabase_service_role_key: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    
    # Database Settings
    database_url: str = os.getenv("DATABASE_URL", "")
    
    # External API Settings
    alpha_vantage_api_key: str = os.getenv("ALPHA_VANTAGE_API_KEY", "")
    finnhub_api_key: str = os.getenv("FINNHUB_API_KEY", "")
    
    # Redis Settings
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # CORS Settings
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]
    
    # Data Collection Settings
    data_collection_interval: int = 60  # seconds
    data_update_interval: int = int(os.getenv("DATA_UPDATE_INTERVAL", "300"))
    currency_update_interval: int = int(os.getenv("CURRENCY_UPDATE_INTERVAL", "60"))
    
    # Logging Settings
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    stock_symbols: List[str] = [
        "THYAO.IS", "AKBNK.IS", "GARAN.IS", "BIMAS.IS", "SISE.IS",
        "TUPRS.IS", "TCELL.IS", "ARCLK.IS", "KCHOL.IS", "SAHOL.IS"
    ]
    
    currency_pairs: List[str] = [
        "USDTRY=X", "EURTRY=X", "GBPTRY=X", "CHFTRY=X",
        "CADTRY=X", "AUDTRY=X", "JPYTRY=X", "RUBTRY=X"
    ]
    
    @validator('cors_origins', pre=True)
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(',')]
        return v
    
    class Config:
        env_file = "../.env"  # Root .env dosyasını kullan
        case_sensitive = False
        extra = "ignore"  # Frontend değişkenlerini yoksay

# Create settings instance
settings = Settings() 