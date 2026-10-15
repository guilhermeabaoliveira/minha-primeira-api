# Cadastro e consulta de tarefas

Exemplo verificado em execução local em **15/10/2026**, com dados fictícios.

## Cadastrar

Requisição para `POST /tarefas`:

```json
{
  "id": 1,
  "titulo": "Revisar a documentacao da API",
  "concluida": false
}
```

Resposta observada: **HTTP 200**.

```json
{
  "mensagem": "Tarefa salva no Banco de Dados!"
}
```

## Consultar

Resposta observada em `GET /tarefas`: **HTTP 200**.

```json
[
  {
    "id": 1,
    "titulo": "Revisar a documentacao da API",
    "concluida": false
  }
]
```

Também foi verificada a resposta **HTTP 422** ao enviar texto não numérico no campo inteiro `id`.

Ambiente: Python 3.12.14, FastAPI 0.128.2, Pydantic 2.12.5, TinyDB 4.9.0 e Uvicorn 0.40.0. A verificação cobre cadastro, consulta e esse caso de validação; não é uma suíte automatizada do projeto.

[Executar localmente](../README.md#preparação-e-execução) · [Rotas e campos](../README.md#rotas) · [Código](../main.py)
