from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB, Query

app = FastAPI()
# Aqui criamos o arquivo que será o nosso Banco de Dados (DB)
db = TinyDB('banco_de_dados.json')

class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False

@app.get("/")
def home():
    return {"status": "API e Banco de Dados operantes!"}

@app.get("/tarefas")
def listar():
    return db.all()

@app.post("/tarefas")
def criar(tarefa: Tarefa):
    db.insert(tarefa.dict())
    return {"mensagem": "Tarefa salva no Banco de Dados!"}