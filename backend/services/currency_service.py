"""
Currency Service
Business logic for currency-related operations
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
import logging
from config.database import get_db_client
from schemas.currency import Currency, CurrencyCreate, CurrencyUpdate
from services.data_collector import DataCollectorService

logger = logging.getLogger(__name__)

class CurrencyService:
    """Service for currency-related business logic"""
    
    def __init__(self):
        self.data_collector = DataCollectorService()
        
    async def get_currencies(
        self, 
        skip: int = 0, 
        limit: int = 100,
        search: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get currencies with pagination and filtering"""
        try:
            db_client = get_db_client()
            
            # Build query
            query = db_client.table('currencies').select('*')
            
            # Apply filters
            if search:
                query = query.or_(f'name.ilike.%{search}%,symbol.ilike.%{search}%')
            
            # Apply pagination
            query = query.range(skip, skip + limit - 1)
            
            # Execute query
            response = query.execute()
            
            # Get total count for pagination
            count_query = db_client.table('currencies').select('*', count='exact')
            if search:
                count_query = count_query.or_(f'name.ilike.%{search}%,symbol.ilike.%{search}%')
            
            count_response = count_query.execute()
            
            return {
                'data': response.data,
                'total': count_response.count,
                'skip': skip,
                'limit': limit
            }
            
        except Exception as e:
            logger.error(f"Error getting currencies: {e}")
            raise
            
    async def get_currency_by_id(self, currency_id: int) -> Optional[Currency]:
        """Get currency by ID"""
        try:
            db_client = get_db_client()
            
            response = db_client.table('currencies').select('*').eq('id', currency_id).execute()
            
            if response.data:
                return Currency(**response.data[0])
            return None
            
        except Exception as e:
            logger.error(f"Error getting currency by ID {currency_id}: {e}")
            raise
            
    async def get_currency_rates(
        self, 
        currency_id: str, 
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[Dict]:
        """Get currency rate history"""
        try:
            db_client = get_db_client()
            
            # Default to last 30 days if no dates provided
            if not start_date:
                start_date = datetime.now() - timedelta(days=30)
            if not end_date:
                end_date = datetime.now()
                
            query = db_client.table('currency_rates')\
                .select('*')\
                .eq('currency_id', currency_id)\
                .gte('timestamp', start_date.isoformat())\
                .lte('timestamp', end_date.isoformat())\
                .order('timestamp', desc=False)
                
            response = await query.execute()
            return response.data if response.data else []
            
        except Exception as e:
            logger.error(f"Error fetching rate history for currency {currency_id}: {e}")
            raise
            
    async def get_latest_rate(self, currency_id: str) -> Optional[Dict]:
        """Get latest rate for a currency"""
        try:
            db_client = get_db_client()
            
            response = await db_client.table('currency_rates')\
                .select('*')\
                .eq('currency_id', currency_id)\
                .order('timestamp', desc=True)\
                .limit(1)\
                .execute()
                
            return response.data[0] if response.data else None
            
        except Exception as e:
            logger.error(f"Error fetching latest rate for currency {currency_id}: {e}")
            raise
            
    async def create_currency(self, currency_data: CurrencyCreate) -> Dict:
        """Create a new currency"""
        try:
            db_client = get_db_client()
            
            currency_dict = currency_data.dict()
            currency_dict['created_at'] = datetime.now().isoformat()
            
            response = await db_client.table('currencies').insert(currency_dict).execute()
            
            return response.data[0] if response.data else None
            
        except Exception as e:
            logger.error(f"Error creating currency: {e}")
            raise
            
    async def update_currency(self, currency_id: str, currency_data: CurrencyUpdate) -> Optional[Dict]:
        """Update an existing currency"""
        try:
            db_client = get_db_client()
            
            update_dict = currency_data.dict(exclude_unset=True)
            update_dict['updated_at'] = datetime.now().isoformat()
            
            response = await db_client.table('currencies')\
                .update(update_dict)\
                .eq('id', currency_id)\
                .execute()
                
            return response.data[0] if response.data else None
            
        except Exception as e:
            logger.error(f"Error updating currency {currency_id}: {e}")
            raise
            
    async def delete_currency(self, currency_id: str) -> bool:
        """Delete a currency"""
        try:
            db_client = get_db_client()
            
            # Delete related rate data first
            await db_client.table('currency_rates').delete().eq('currency_id', currency_id).execute()
            
            # Delete currency
            response = await db_client.table('currencies').delete().eq('id', currency_id).execute()
            
            return True
            
        except Exception as e:
            logger.error(f"Error deleting currency {currency_id}: {e}")
            raise
            
    async def refresh_currency_data(self, currency_id: Optional[str] = None) -> Dict:
        """Refresh currency data from external sources"""
        try:
            if currency_id:
                # Refresh specific currency
                currency = await self.get_currency_by_id(currency_id)
                if not currency:
                    raise ValueError(f"Currency {currency_id} not found")
                    
                data = await self.data_collector.get_currency_data(currency['symbol'])
                return {"status": "success", "message": f"Refreshed data for {currency['symbol']}"}
            else:
                # Refresh all currencies
                await self.data_collector.update_currency_data()
                return {"status": "success", "message": "Refreshed all currency data"}
                
        except Exception as e:
            logger.error(f"Error refreshing currency data: {e}")
            raise 