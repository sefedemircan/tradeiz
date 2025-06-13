"""
Data Collector Service
Handles data collection from external sources like yfinance
"""

import asyncio
import yfinance as yf
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import logging
from config.database import get_db_client
from config.settings import settings

logger = logging.getLogger(__name__)

class DataCollectorService:
    """Service for collecting financial data from external sources"""
    
    def __init__(self):
        self.is_running = False
        self.tasks = []
        
    async def start_background_tasks(self):
        """Start background data collection tasks"""
        if self.is_running:
            return
            
        self.is_running = True
        logger.info("Starting data collection background tasks...")
        
        # Start periodic tasks
        self.tasks.append(asyncio.create_task(self._periodic_stock_update()))
        self.tasks.append(asyncio.create_task(self._periodic_currency_update()))
        
    async def stop_background_tasks(self):
        """Stop background data collection tasks"""
        if not self.is_running:
            return
            
        self.is_running = False
        logger.info("Stopping data collection background tasks...")
        
        # Cancel all tasks
        for task in self.tasks:
            task.cancel()
            
        # Wait for tasks to complete
        await asyncio.gather(*self.tasks, return_exceptions=True)
        self.tasks.clear()
        
    async def _periodic_stock_update(self):
        """Periodic stock data update task"""
        while self.is_running:
            try:
                await self.update_stock_data()
                # Update every 5 minutes during market hours
                await asyncio.sleep(300)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in periodic stock update: {e}")
                await asyncio.sleep(60)  # Wait 1 minute on error
                
    async def _periodic_currency_update(self):
        """Periodic currency data update task"""
        while self.is_running:
            try:
                await self.update_currency_data()
                # Update every 1 minute
                await asyncio.sleep(60)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in periodic currency update: {e}")
                await asyncio.sleep(60)  # Wait 1 minute on error
                
    async def update_stock_data(self):
        """Update stock data from yfinance"""
        try:
            logger.info("Updating stock data...")
            
            # Get BIST stocks from database
            db_client = get_db_client()
            
            # Fetch stocks from database
            stocks_response = db_client.table('stocks').select('*').execute()
            stocks = stocks_response.data
            
            for stock in stocks:
                try:
                    # Fetch data from yfinance with BIST suffix
                    symbol_with_suffix = f"{stock['symbol']}.IS"
                    logger.info(f"Fetching data for {symbol_with_suffix}")
                    
                    ticker = yf.Ticker(symbol_with_suffix)
                    hist = ticker.history(period="5d", interval="1d")  # 5 günlük veri, günlük interval
                    
                    if not hist.empty:
                        latest = hist.iloc[-1]
                        
                        # Insert latest price data
                        price_data = {
                            'stock_id': stock['id'],
                            'timestamp': datetime.now().isoformat(),
                            'open': float(latest['Open']),
                            'high': float(latest['High']),
                            'low': float(latest['Low']),
                            'close': float(latest['Close']),
                            'volume': int(latest['Volume'])
                        }
                        
                        db_client.table('stock_prices').insert(price_data).execute()
                        logger.info(f"Successfully updated {symbol_with_suffix}: Close={latest['Close']}")
                        
                    else:
                        logger.warning(f"No data found for {symbol_with_suffix}")
                        
                except Exception as e:
                    logger.error(f"Error updating stock {stock['symbol']}: {e}")
                    continue
                    
            logger.info("Stock data update completed")
            
        except Exception as e:
            logger.error(f"Error in update_stock_data: {e}")
            
    async def update_currency_data(self):
        """Update currency data from yfinance"""
        try:
            logger.info("Updating currency data...")
            
            db_client = get_db_client()
            
            # Fetch currencies from database
            currencies_response = db_client.table('currencies').select('*').execute()
            currencies = currencies_response.data
            
            for currency in currencies:
                try:
                    # Fetch data from yfinance
                    logger.info(f"Fetching data for {currency['symbol']}")
                    
                    ticker = yf.Ticker(currency['symbol'])
                    hist = ticker.history(period="5d", interval="1d")  # 5 günlük veri, günlük interval
                    
                    if not hist.empty:
                        latest = hist.iloc[-1]
                        
                        # Insert latest rate data
                        rate_data = {
                            'currency_id': currency['id'],
                            'timestamp': datetime.now().isoformat(),
                            'rate': float(latest['Close']),
                            'high': float(latest['High']),
                            'low': float(latest['Low'])
                        }
                        
                        db_client.table('currency_rates').insert(rate_data).execute()
                        logger.info(f"Successfully updated {currency['symbol']}: Rate={latest['Close']}")
                        
                    else:
                        logger.warning(f"No data found for {currency['symbol']}")
                        
                except Exception as e:
                    logger.error(f"Error updating currency {currency['symbol']}: {e}")
                    continue
                    
            logger.info("Currency data update completed")
            
        except Exception as e:
            logger.error(f"Error in update_currency_data: {e}")
            
    async def get_stock_data(self, symbol: str, period: str = "1d") -> Optional[Dict]:
        """Get stock data for a specific symbol"""
        try:
            ticker = yf.Ticker(f"{symbol}.IS")
            hist = ticker.history(period=period)
            
            if hist.empty:
                return None
                
            return {
                'symbol': symbol,
                'data': hist.to_dict('records'),
                'info': ticker.info
            }
            
        except Exception as e:
            logger.error(f"Error fetching stock data for {symbol}: {e}")
            return None
            
    async def get_currency_data(self, symbol: str, period: str = "1d") -> Optional[Dict]:
        """Get currency data for a specific symbol"""
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period)
            
            if hist.empty:
                return None
                
            return {
                'symbol': symbol,
                'data': hist.to_dict('records'),
                'info': ticker.info
            }
            
        except Exception as e:
            logger.error(f"Error fetching currency data for {symbol}: {e}")
            return None 