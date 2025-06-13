import yfinance as yf
import requests
from datetime import datetime
import time

def test_internet_connection():
    """Test internet connection"""
    try:
        response = requests.get("https://www.google.com", timeout=5)
        print("✅ Internet connection OK")
        return True
    except:
        print("❌ Internet connection failed")
        return False

def test_yahoo_finance_access():
    """Test Yahoo Finance access"""
    try:
        response = requests.get("https://finance.yahoo.com", timeout=10)
        print(f"✅ Yahoo Finance accessible (Status: {response.status_code})")
        return True
    except Exception as e:
        print(f"❌ Yahoo Finance access failed: {e}")
        return False

def test_with_different_periods(symbol):
    """Test different periods for a symbol"""
    periods = ["1d", "5d", "1mo", "3mo"]
    
    for period in periods:
        try:
            print(f"  Testing {symbol} with period={period}...")
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period)
            
            if not data.empty:
                print(f"    ✅ Success with {period}: {len(data)} records")
                print(f"    Latest close: {data['Close'].iloc[-1]:.4f}")
                return data
            else:
                print(f"    ❌ No data with {period}")
        except Exception as e:
            print(f"    ❌ Error with {period}: {e}")
    
    return None

def test_alternative_symbols():
    """Test alternative symbol formats"""
    
    # BIST alternatives
    bist_alternatives = [
        "THYAO.IS",
        "THYAO.IST", 
        "THYAO",
        "IST:THYAO"
    ]
    
    print("=== BIST Symbol Alternatives ===")
    for symbol in bist_alternatives:
        print(f"Testing {symbol}...")
        result = test_with_different_periods(symbol)
        if result is not None:
            print(f"✅ {symbol} WORKS!")
            break
        print()
    
    # Currency alternatives
    currency_alternatives = [
        "USDTRY=X",
        "USD/TRY",
        "USDTRY",
        "TRY=X",
        "TRYUSD=X"
    ]
    
    print("\n=== Currency Symbol Alternatives ===")
    for symbol in currency_alternatives:
        print(f"Testing {symbol}...")
        result = test_with_different_periods(symbol)
        if result is not None:
            print(f"✅ {symbol} WORKS!")
            break
        print()

def test_with_headers():
    """Test with custom headers"""
    print("\n=== Testing with custom headers ===")
    
    # Set custom headers
    import yfinance as yf
    
    # Try with user agent
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    try:
        ticker = yf.Ticker("AAPL", session=session)  # Test with a known working symbol
        data = ticker.history(period="1d")
        
        if not data.empty:
            print("✅ Custom headers work with AAPL")
            
            # Now try BIST
            ticker_bist = yf.Ticker("THYAO.IS", session=session)
            data_bist = ticker_bist.history(period="1d")
            
            if not data_bist.empty:
                print("✅ Custom headers work with THYAO.IS")
            else:
                print("❌ Custom headers don't work with THYAO.IS")
        else:
            print("❌ Custom headers don't work")
            
    except Exception as e:
        print(f"❌ Custom headers failed: {e}")

if __name__ == "__main__":
    print("=== yfinance Diagnostic Test ===")
    print(f"yfinance version: {yf.__version__}")
    print()
    
    # Test basic connectivity
    if not test_internet_connection():
        exit(1)
    
    if not test_yahoo_finance_access():
        print("⚠️  Yahoo Finance access issues detected")
    
    print()
    
    # Test alternative symbols
    test_alternative_symbols()
    
    # Test with headers
    test_with_headers()
    
    print("\n=== Test completed ===") 