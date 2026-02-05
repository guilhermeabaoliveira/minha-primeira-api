# Task Management API

This project is a task management API (To-Do List) developed to demonstrate backend development skills and data persistence.

## 🚀 Technologies
- **Python**
- **FastAPI**: Modern and fast framework for building APIs.
- **TinyDB**: Lightweight database for JSON data persistence.
- **Uvicorn**: Server to run the application.

## 🛠️ How to run the project
1. Install the necessary dependencies:
   `pip install fastapi tinydb "uvicorn[standard]"`
2. Start the API server:
   `python -m uvicorn main:app --reload`
3. Access the automatic documentation (Swagger) at: `http://127.0.0.1:8000/docs`

## 📂 Project Structure
- `main.py`: Main API code with GET and POST routes.
- `banco_de_dados.json`: File where tasks are saved (our database).
- `requirements.txt`: List of libraries for installation.

---

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
