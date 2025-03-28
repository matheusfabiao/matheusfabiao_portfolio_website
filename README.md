# Portfólio Website

Este projeto é um website que serve como uma vitrine para o meu trabalho, habilidades e experiências. Aqui, você encontrará informações sobre mim, projetos que desenvolvi, tecnologias que domino e formas de entrar em contato.

## 🚀 Tecnologias

### Backend
- Python 3.12+
- Django 5.1+
- PostgreSQL

### Frontend
- Vite (Bundler)
- Tailwind CSS v4
- DaisyUI
- Node.js

## 📋 Pré-requisitos

- Python 3.12 ou superior
- PostgreSQL
- UV (Gerenciador de pacotes Python)
- Node.js 18+ e npm

## 🔧 Instalação

1. Clone o repositório

2. Instale o UV (caso ainda não tenha):
   ```bash
   python -m pip install uv
   ```

3. Crie um ambiente virtual e instale as dependências:
   ```bash
   uv venv
   ```

4. Ative o ambiente virtual:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```

5. Instale as dependências do Python:
   ```bash
   uv pip install .
   ```

6. Instale as dependências do Node.js:
   ```bash
   npm install
7. Copie o arquivo de exemplo de variáveis de ambiente:
   ```bash
   cp env_files/.env.example env_files/.env
   ```
8. Configure as variáveis de ambiente no arquivo `.env`
9. Execute as migrações:
   ```bash
   task migrate
   ```

## 🏃‍♂️ Executando o projeto

1. Inicie o servidor de desenvolvimento do Django:
   ```bash
   task run
   ```

2. Em outro terminal, inicie o servidor de desenvolvimento do Vite:
   ```bash
   npm run dev
   ```

O projeto estará disponível em `http://localhost:8000` e o servidor de desenvolvimento do Vite em `http://localhost:5173`

## 🧪 Testes

```bash
task test
```

## 📦 Estrutura do Projeto

```
.
├── env_files/          # Arquivos de configuração de ambiente
├── src/                # Código fonte do projeto
│   ├── core/           # Configurações principais do Django
│   ├── portfolio/      # Aplicação principal
│   │   ├── migrations/ # Migrações do banco de dados
│   │   ├── models.py   # Modelos de dados
│   │   ├── views.py    # Views da aplicação
│   │   └── urls.py     # Configuração de URLs
│   ├── static/         # Arquivos estáticos
│   │   ├── css/        # Estilos CSS
│   │   └── js/         # Scripts JavaScript
│   └── templates/      # Templates HTML
│       └── portfolio/  # Templates da aplicação principal
├── node_modules/       # Dependências do Node.js (não versionado)
├── package.json        # Dependências e scripts do Node.js
├── package-lock.json   # Lock de dependências do Node.js
├── pyproject.toml      # Configuração do projeto Python
├── vite.config.mjs     # Configuração do Vite
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Este arquivo
```

## 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.