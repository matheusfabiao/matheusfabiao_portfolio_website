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
- HTMX
- AlpineJS
- Node.js

### Documentação
- MkDocs
- Material for MkDocs

## 📋 Pré-requisitos

- Python 3.12 ou superior
- PostgreSQL
- UV (Gerenciador de pacotes Python)
- Node.js 18+ e npm

## 🔧 Instalação

1. Clone o repositório
   ```bash
   git clone https://github.com/matheusfabiao/matheusfabiao_portfolio_website.git
   cd matheusfabiao_portfolio_website
   ```

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
   ```

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

3. Para acessar a documentação, execute:
   ```bash
   mkdocs serve
   ```

O projeto estará disponível em:
- Aplicação: `http://localhost:8000`
- Assets (Vite): `http://localhost:5173`

## 🧪 Testes

O projeto utiliza pytest para testes automatizados. Os testes estão organizados na pasta `src/portfolio/tests/` e são divididos em:

- `conftest.py`: Configurações e fixtures compartilhadas
  - Configurações globais do pytest
  - Fixtures reutilizáveis
  - Helpers para testes

- `test_models.py`: Testes para os modelos de dados
  - Validação de campos
  - Criação e atualização de registros
  - Comportamentos específicos dos modelos

- `test_views.py`: Testes para as views da aplicação
  - Rotas e endpoints
  - Respostas HTTP
  - Renderização de templates

Para executar os testes:
```bash
task test
```
- Documentação: `http://localhost:8000/docs`

## 🧪 Testes

```bash
task test
```

## 📦 Estrutura do Projeto

```
.
├── docs/                        # Documentação do projeto
│   ├── assets/                  # Recursos da documentação
│   ├── getting_started/         # Guias de início rápido
│   └── stylesheets/             # Estilos personalizados da documentação
├── env_files/                   # Arquivos de configuração de ambiente
├── src/                         # Código fonte do projeto
│   ├── core/                    # Configurações principais do Django
│   │   ├── settings.py          # Configurações do projeto
│   │   ├── urls.py              # URLs principais
│   │   └── wsgi.py              # Configuração WSGI
│   ├── portfolio/               # Aplicação principal
│   │   ├── migrations/          # Migrações do banco de dados
│   │   ├── models.py            # Modelos de dados
│   │   ├── views.py             # Views da aplicação
│   │   ├── urls.py              # Configuração de URLs
│   │   └── tests/               # Testes automatizados
│   │       ├── conftest.py      # Configurações e fixtures de teste
│   │       ├── test_models.py   # Testes dos modelos
│   │       └── test_views.py    # Testes das views
│   ├── static/                  # Arquivos estáticos
│   │   ├── css/                 # Estilos CSS e componentes
│   │   ├── js/                  # Scripts JavaScript
│   │   └── img/                 # Imagens e recursos visuais
│   └── templates/               # Templates HTML
│       ├── components/          # Componentes reutilizáveis
│       └── portfolio/           # Templates específicos
├── mkdocs.yml                   # Configuração da documentação
├── package.json                 # Dependências do frontend
├── pyproject.toml               # Dependências do Python
├── vite.config.mjs              # Configuração do Vite
└── uv.lock                      # Lock file do gerenciador de pacotes Python
```

## 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.