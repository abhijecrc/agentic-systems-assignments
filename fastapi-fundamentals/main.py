from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/search")
def search(name: Optional[str] = None, age: Optional[int] = None):
    """
    Search endpoint that accepts optional query parameters:
    - name: string (optional)
    - age: integer (optional)
    
    Returns the received parameters as JSON.
    """
    result = {}
    if name is not None:
        result["name"] = name
    if age is not None:
        result["age"] = age
    
    return result