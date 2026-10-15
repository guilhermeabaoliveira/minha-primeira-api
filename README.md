# Task Management API

A Python API for creating and listing tasks, built with FastAPI and TinyDB. Records are stored in a local JSON file.

[English](#endpoints) · [Português](#api-de-gerenciamento-de-tarefas)

## Endpoints

| Method | Path | Behavior | Success response |
| --- | --- | --- | --- |
| `GET` | `/` | Returns a fixed status message | HTTP 200, `{"status": "API e Banco de Dados operantes!"}` |
| `GET` | `/tarefas` | Lists all stored tasks | HTTP 200, JSON list |
| `POST` | `/tarefas` | Validates and stores a task | HTTP 200, `{"mensagem": "Tarefa salva no Banco de Dados!"}` |

The root endpoint returns a message; it does not perform a database health check.

### Task fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | Integer | Yes | Identifier supplied by the client |
| `titulo` | String | Yes | Task title |
| `concluida` | Boolean | No | Completion state; defaults to `false` |

Example request body for `POST /tarefas`:

```json
{
  "id": 1,
  "titulo": "Estudar Python",
  "concluida": false
}
```

The API does not generate identifiers or enforce their uniqueness. Repeating the request inserts another record. POST returns a confirmation message rather than the stored task.

## Setup and execution

Requirements: Python with `venv` and `pip`. Dependency versions are not pinned in `requirements.txt`.

From the repository root:

```bash
python -m venv .venv
```

Activate the environment using the command for your shell:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies and start the development server:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Open the [interactive API documentation](http://127.0.0.1:8000/docs) to send requests, or [list tasks](http://127.0.0.1:8000/tarefas) in the browser. Stop the server with `Ctrl+C`.

## Storage and files

| File | Purpose |
| --- | --- |
| `main.py` | Application, task model, and three routes |
| `banco_de_dados.json` | Local TinyDB storage |
| `requirements.txt` | FastAPI, TinyDB, and Uvicorn dependencies |

TinyDB opens `banco_de_dados.json` relative to the process working directory. Start the server from the repository root to use the file in this repository. POST requests modify this file; GET requests list its stored records.

## Limitations

- Creation and listing are available; there are no update or deletion endpoints.
- There is no authentication, authorization, or per-user task separation.
- The model validates field types, but does not require a nonempty title or a positive, unique identifier.
- Storage errors have no application-specific handling.
- No automated test suite is included.
- `--reload` is intended for local development; production deployment is not configured here.

---

# API de Gerenciamento de Tarefas

API em Python para cadastrar e listar tarefas, com FastAPI e persistência local em JSON usando TinyDB.

## Rotas

| Método | Caminho | Comportamento | Resposta de sucesso |
| --- | --- | --- | --- |
| `GET` | `/` | Retorna uma mensagem fixa de status | HTTP 200, `{"status": "API e Banco de Dados operantes!"}` |
| `GET` | `/tarefas` | Lista os registros armazenados | HTTP 200, lista JSON |
| `POST` | `/tarefas` | Valida e armazena uma tarefa | HTTP 200, `{"mensagem": "Tarefa salva no Banco de Dados!"}` |

A rota inicial retorna uma mensagem e não executa uma verificação de integridade do banco.

### Dados da tarefa

| Campo | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `id` | Inteiro | Sim | Identificador informado pelo cliente |
| `titulo` | Texto | Sim | Título da tarefa |
| `concluida` | Booleano | Não | Estado de conclusão; padrão `false` |

O exemplo JSON em [Task fields](#task-fields) pode ser enviado a `POST /tarefas`. O sistema não gera identificadores nem impede repetições de `id`. Repetir o cadastro insere outro registro. A resposta confirma a gravação, sem devolver a tarefa cadastrada.

## Preparação e execução

É necessário Python com `venv` e `pip`. Crie e ative o ambiente virtual com os comandos de [Setup and execution](#setup-and-execution). Na raiz do repositório:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Abra a [documentação interativa](http://127.0.0.1:8000/docs) para enviar requisições ou a [listagem de tarefas](http://127.0.0.1:8000/tarefas). Use `Ctrl+C` para encerrar o servidor.

## Persistência e limites

`main.py` contém a aplicação, o modelo e as três rotas. `requirements.txt` lista as dependências, sem versões fixadas. O arquivo `banco_de_dados.json` guarda os registros.

O caminho do banco depende do diretório de execução: inicie o servidor pela raiz do repositório para usar esse arquivo. Os cadastros alteram seu conteúdo e a consulta retorna os registros salvos.

A API oferece cadastro e listagem, sem edição, exclusão, autenticação ou separação de tarefas por usuário. Os tipos dos campos são validados, mas não há regras de título não vazio ou identificador positivo e único. Falhas de armazenamento não recebem tratamento específico. O projeto não inclui testes automatizados nem configuração de implantação em produção; `--reload` serve ao desenvolvimento local.
