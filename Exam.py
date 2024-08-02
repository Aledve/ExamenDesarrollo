from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app=FastAPI()
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class TextInput(BaseModel):
    codigo: int
    valor: str

@app.post("/clasificar/")
def clasificar(text_input: TextInput):
    labels = ["politica", "religion", "cine"]
    result = classifier(text_input.valor, labels)
    if not result['labels']:
        return {"codigo": text_input.codigo, "respuesta": "No puedo generar una etiqueta, porque solo tengo el entrenamiento en política, religión y cine."}
    
    label = result['labels'][0]
    return {"codigo": text_input.codigo, "respuesta": label}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)

