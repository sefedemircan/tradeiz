import yfinance as yf
from datetime import datetime

def test_bist_stock(ticker):
    print(f"Testing {ticker}.IS...")
    stock = yf.Ticker(ticker + ".IS")
    data = stock.history(period="1d")
    
    if data.empty:
        print(f"❌ No data found for {ticker}.IS")
        return None
    else:
        print(f"✅ Data found for {ticker}.IS")
        print(f"   Close: {data['Close'].iloc[-1]:.2f}")
        print(f"   Volume: {data['Volume'].iloc[-1]}")
        return data

def test_currency(symbol):
    print(f"Testing {symbol}...")
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    
    if data.empty:
        print(f"❌ No data found for {symbol}")
        return None
    else:
        print(f"✅ Data found for {symbol}")
        print(f"   Close: {data['Close'].iloc[-1]:.4f}")
        return data

if __name__ == "__main__":
    print("=== BIST Stock Tests ===")
    test_bist_stock("THYAO")
    test_bist_stock("AKBNK")
    test_bist_stock("GARAN")
    
    print("\n=== Currency Tests ===")
    test_currency("USDTRY=X")
    test_currency("EURTRY=X")
    test_currency("TRYUSD=X")  # Alternatif format
    
    print("\n=== Alternative Currency Formats ===")
    test_currency("TRY=X")
    test_currency("USD=X") 