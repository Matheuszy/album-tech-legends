from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/imgs/01-alan-turing.jpg"
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/imgs/02-john-mccarthy.jpg"
    },
]


@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas
