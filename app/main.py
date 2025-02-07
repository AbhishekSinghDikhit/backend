import sys
import os
import uvicorn

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI

from expirydetection import router as expiry_router

app = FastAPI(title="Sharewell API", version="1.0")

# Include routes
app.include_router(expiry_router)

@app.get("/")
def root():
    return {"message": "Welcome to Sharewell API"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080)) 
    uvicorn.run(app, host="0.0.0.0", port=port)