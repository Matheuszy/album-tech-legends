from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Caminhos absolutos para localizar a pasta de imagens
# independente de onde o servidor for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Serve os arquivos da pasta "figurinhas/" na rota "/imgs"
# Ex: figurinhas/01-alan-turing.jpg → acessível em /imgs/01-alan-turing.jpg
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

EXTENSOES_VALIDAS = {".jpg", ".jpeg", ".png", ".webp"}


def carregar_figurinhas() -> list[dict]:
    """
    Lê os arquivos da pasta de imagens e monta a lista de figurinhas
    automaticamente a partir dos nomes dos arquivos.

    Convenção esperada: "01-alan-turing.jpg"
      - Parte antes do primeiro "-" → id (int)
      - Restante sem extensão, hífens trocados por espaços → nome
    """
    figurinhas = []

    for arquivo in sorted(os.listdir(PASTA_IMAGENS)):
        nome_sem_ext, extensao = os.path.splitext(arquivo)

        if extensao.lower() not in EXTENSOES_VALIDAS:
            continue

        partes = nome_sem_ext.split("-", 1)  # separa só no primeiro hífen
        if len(partes) != 2 or not partes[0].isdigit():
            continue  # ignora arquivos que não seguem o padrão numérico

        id_figurinha = int(partes[0])
        nome = partes[1].replace("-", " ").title()  # "alan-turing" → "Alan Turing"

        figurinhas.append({
            "id": id_figurinha,
            "nome": nome,
            "imagem_url": f"/imgs/{arquivo}"
        })

    return figurinhas


@app.get("/figurinhas")
def listar_figurinhas():
    return carregar_figurinhas()
