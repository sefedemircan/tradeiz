import asyncio
from typing import Optional
from supabase import create_client, Client
from config.settings import settings

class DatabaseManager:
    """Database connection manager for Supabase"""
    
    def __init__(self):
        self._client: Optional[Client] = None
    
    @property
    def client(self) -> Client:
        """Get Supabase client instance"""
        if self._client is None:
            self._client = create_client(
                settings.supabase_url,
                settings.supabase_key
            )
        return self._client
    
    async def test_connection(self) -> bool:
        """Test database connection"""
        try:
            # Simple connection test - just create client
            client = create_client(settings.supabase_url, settings.supabase_key)
            # Try a basic query to test connection
            result = client.table("stocks").select("count", count="exact").execute()
            print(f"✅ Database connection successful! Found {result.count} stocks.")
            return True
        except Exception as e:
            print(f"Database connection test failed: {e}")
            return False
    
    async def close(self):
        """Close database connection"""
        if self._client:
            # Supabase client doesn't require explicit closing
            # but we can reset the instance
            self._client = None

# Global database manager instance
db_manager = DatabaseManager()

async def init_db():
    """Initialize database connection"""
    print("🔌 Initializing database connection...")
    
    if await db_manager.test_connection():
        print("✅ Database connection successful!")
    else:
        print("❌ Database connection failed!")
        raise Exception("Failed to connect to Supabase database")

def get_db_client() -> Client:
    """Dependency to get database client"""
    return db_manager.client 