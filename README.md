# 📚 Book CRUD API

API RESTful para gerenciamento de livros com operações CRUD completas usando FastAPI e MongoDB.

## 🚀 Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **MongoDB** - Banco de dados NoSQL
- **Motor** - Driver assíncrono para MongoDB
- **Docker** & **Docker Compose** - Containerização

## 📦 Atributos do Livro

| Campo | Tipo | Descrição |
|-------|------|-----------|
| title | string | Título do livro (1-200 caracteres) |
| author | string | Nome do autor (1-100 caracteres) |
| year | integer | Ano de publicação (1450-2024) |
| genre | string | Gênero literário (1-50 caracteres) |

## 🐳 Executando com Docker

### Pré-requisitos
- Docker
- Docker Compose

### Passos

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/book-crud.git
cd book-crud
