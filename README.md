# API de Gerenciamento de Tarefas

Este projeto é uma API para gerenciamento de listas de tarefas (To-Do List), desenvolvida para demonstrar conhecimentos em criação de APIs e persistência de dados (Banco de Dados).

## 🚀 Tecnologias
- **Python**
- **FastAPI**: Framework moderno e rápido para construção de APIs.
- **TinyDB**: Banco de Dados leve para persistência de dados em formato JSON.
- **Uvicorn**: Servidor para rodar a aplicação.

## 🛠️ Como rodar o projeto
1. Instale as dependências necessárias:
   `pip install fastapi tinydb "uvicorn[standard]"`
2. Inicie o servidor da API:
   `python -m uvicorn main:app --reload`
3. Acesse a documentação automática (Swagger) em: `http://127.0.0.1:8000/docs`

## 📂 Estrutura do Projeto
- `main.py`: Código principal da API com as rotas GET e POST.
- `banco_de_dados.json`: Arquivo onde as tarefas são salvas (nosso banco de dados).
- `requirements.txt`: Lista de bibliotecas para instalação.