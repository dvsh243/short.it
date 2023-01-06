import uvicorn
from core.urls import app


if __name__ == "__main__":
    
    uvicorn.run(
        app, 
        port = 8000
    )

# uvicorn main:app --port 8000 --reload