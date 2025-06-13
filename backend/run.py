#!/usr/bin/env python3
"""
Simple runner script for TRIZ Trade Backend
"""

import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get configuration from environment or use defaults
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    debug = os.getenv("DEBUG", "true").lower() == "true"
    
    print("🚀 Starting TRIZ Trade Backend...")
    print(f"📍 Host: {host}")
    print(f"🔢 Port: {port}")
    print(f"🐛 Debug: {debug}")
    print(f"📖 API Docs: http://{host}:{port}/docs")
    print("=" * 50)
    
    # Run the application
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info"
    ) 