"""
Stock Service
Business logic for stock-related operations
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
import logging
from config.database import get_db_client
from schemas.stock import Stock, StockCreate, StockUpdate, StockPrice
from services.data_collector import DataCollectorService

logger = logging.getLogger(__name__)

class StockService:
    """Service for stock-related business logic"""
    
    def __init__(self):
        self.data_collector = DataCollectorService()
        
    async def get_stocks(
        self, 
        skip: int = 0, 
        limit: int = 100,
        search: Optional[str] = None,
        sector: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get stocks with pagination and filtering"""
        try:
            db_client = get_db_client()
            
            # Build query
            query = db_client.table('stocks').select('*')
            
            # Apply filters
            if search:
                query = query.ilike('name', f'%{search}%')
            
            if sector:
                query = query.eq('sector', sector)
            
            # Apply pagination
            query = query.range(skip, skip + limit - 1)
            
            # Execute query
            response = query.execute()
            
            # Get total count for pagination
            count_query = db_client.table('stocks').select('*', count='exact')
            if search:
                count_query = count_query.ilike('name', f'%{search}%')
            if sector:
                count_query = count_query.eq('sector', sector)
            
            count_response = count_query.execute()
            
            return {
                'data': response.data,
                'total': count_response.count,
                'skip': skip,
                'limit': limit
            }
            
        except Exception as e:
            logger.error(f"Error getting stocks: {e}")
            raise
            
    async def get_stock_by_id(self, stock_id: int) -> Optional[Stock]:
        """Get stock by ID"""
        try:
            db_client = get_db_client()
            
            response = db_client.table('stocks').select('*').eq('id', stock_id).execute()
            
            if response.data:
                return Stock(**response.data[0])
            return None
            
        except Exception as e:
            logger.error(f"Error getting stock by ID {stock_id}: {e}")
            raise
            
    async def get_stock_prices(
        self, 
        stock_id: str, 
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        interval: str = '1h'
    ) -> List[Dict]:
        """Get stock price history"""
        try:
            db_client = get_db_client()
            
            # Default to last 30 days if no dates provided
            if not start_date:
                start_date = datetime.now() - timedelta(days=30)
            if not end_date:
                end_date = datetime.now()
                
            query = db_client.table('stock_prices')\
                .select('*')\
                .eq('stock_id', stock_id)\
                .gte('timestamp', start_date.isoformat())\
                .lte('timestamp', end_date.isoformat())\
                .order('timestamp', desc=False)
                
            response = await query.execute()
            return response.data if response.data else []
            
        except Exception as e:
            logger.error(f"Error fetching price history for stock {stock_id}: {e}")
            raise
            
    async def get_latest_price(self, stock_id: str) -> Optional[Dict]:
        """Get latest price for a stock"""
        try:
            db_client = get_db_client()
            
            response = await db_client.table('stock_prices')\
                .select('*')\
                .eq('stock_id', stock_id)\
                .order('timestamp', desc=True)\
                .limit(1)\
                .execute()
                
            return response.data[0] if response.data else None
            
        except Exception as e:
            logger.error(f"Error fetching latest price for stock {stock_id}: {e}")
            raise
            
    async def get_sectors(self) -> List[str]:
        """Get list of available sectors"""
        try:
            db_client = get_db_client()
            
            response = await db_client.table('stocks')\
                .select('sector')\
                .execute()
                
            if not response.data:
                return []
                
            # Extract unique sectors
            sectors = list(set([stock['sector'] for stock in response.data if stock['sector']]))
            return sorted(sectors)
            
        except Exception as e:
            logger.error(f"Error fetching sectors: {e}")
            raise
            
    async def create_stock(self, stock_data: StockCreate) -> Dict:
        """Create a new stock"""
        try:
            db_client = get_db_client()
            
            stock_dict = stock_data.dict()
            stock_dict['created_at'] = datetime.now().isoformat()
            
            response = await db_client.table('stocks').insert(stock_dict).execute()
            
            return response.data[0] if response.data else None
            
        except Exception as e:
            logger.error(f"Error creating stock: {e}")
            raise
            
    async def update_stock(self, stock_id: str, stock_data: StockUpdate) -> Optional[Dict]:
        """Update an existing stock"""
        try:
            db_client = get_db_client()
            
            update_dict = stock_data.dict(exclude_unset=True)
            update_dict['updated_at'] = datetime.now().isoformat()
            
            response = await db_client.table('stocks')\
                .update(update_dict)\
                .eq('id', stock_id)\
                .execute()
                
            return response.data[0] if response.data else None
            
        except Exception as e:
            logger.error(f"Error updating stock {stock_id}: {e}")
            raise
            
    async def delete_stock(self, stock_id: str) -> bool:
        """Delete a stock"""
        try:
            db_client = get_db_client()
            
            # Delete related price data first
            await db_client.table('stock_prices').delete().eq('stock_id', stock_id).execute()
            
            # Delete stock
            response = await db_client.table('stocks').delete().eq('id', stock_id).execute()
            
            return True
            
        except Exception as e:
            logger.error(f"Error deleting stock {stock_id}: {e}")
            raise
            
    async def refresh_stock_data(self, stock_id: Optional[str] = None) -> Dict:
        """Refresh stock data from external sources"""
        try:
            if stock_id:
                # Refresh specific stock
                stock = await self.get_stock_by_id(stock_id)
                if not stock:
                    raise ValueError(f"Stock {stock_id} not found")
                    
                data = await self.data_collector.get_stock_data(stock['symbol'])
                return {"status": "success", "message": f"Refreshed data for {stock['symbol']}"}
            else:
                # Refresh all stocks
                await self.data_collector.update_stock_data()
                return {"status": "success", "message": "Refreshed all stock data"}
                
        except Exception as e:
            logger.error(f"Error refreshing stock data: {e}")
            raise 