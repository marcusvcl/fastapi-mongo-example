# API Simples com FastAPI + MongoDB

Exemplo de uma API REST básica utilizando **FastAPI** integrado com **MongoDB**, demonstrando operações CRUD fundamentais.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

## ✨ Funcionalidades

- Operações CRUD básicas
- Integração com MongoDB usando o driver assíncrono Motor
- Configuração por variáveis de ambiente
- Validação de dados com Pydantic
- Documentação automática da API (Swagger/ReDoc)

## 🚀 Primeiros Passos

### Pré-requisitos

- Python 3.9+
- Instância do MongoDB (local ou em nuvem)
- Gerenciador de pacotes pip

### Instalação

1. **Criar e ativar ambiente virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/MacOS
   .\.venv\Scripts\activate   # Windows
   ```

2. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar ambiente**  
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   MONGODB_URI=mongodb://localhost:27017
   DATABASE_NAME=fastapi_demo
   ```

### Executando o Servidor

Inicie o servidor de desenvolvimento com um dos comandos:

```bash
uvicorn app.main:app --reload
```

ou 

```bash
fastapi dev app/main.py
```

A API estará disponível em `http://localhost:8000`

## 📚 Documentação da API

Acesse a documentação interativa:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔧 Configuração

Modifique estas variáveis no arquivo `.env` conforme necessário:
- `MONGODB_URI`: String de conexão do MongoDB
- `DATABASE_NAME`: Nome do banco de dados

### ⚠️ Importante
- Certifique-se que seu servidor MongoDB está rodando antes de iniciar a API
- A versão do Python deve ser compatível com o FastAPI 0.68+
