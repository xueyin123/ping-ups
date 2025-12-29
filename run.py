import uvicorn
import os
import sys
from main import app
from config import settings

def run_server():
    """
    运行FastAPI服务器
    """
    port = settings.port
    host = settings.host
    reload = settings.debug
    
    print(f"Starting server on {host}:{port}")
    print(f"API documentation available at http://{host}:{port}/docs")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        debug=settings.debug
    )

if __name__ == "__main__":
    run_server()