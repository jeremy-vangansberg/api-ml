from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from app.model import predict_pipeline

app = FastAPI()

class TextIn(BaseModel):
    text: str
    url: str

class PredictionOut(BaseModel):
    category: str

@app.post("/predict", response_model=PredictionOut)
def predict(payload:TextIn):
    category_pred = predict_pipeline(payload.text, payload.url)
    return {'category': category_pred}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)