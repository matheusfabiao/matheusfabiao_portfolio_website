# Portfólio Website

Este projeto é um website que serve como uma vitrine para o meu trabalho, habilidades e experiências. Aqui, você encontrará informações sobre mim, projetos que desenvolvi, tecnologias que domino e formas de entrar em contato.

## 🚀 Tecnologias

- Python 3.12+
- Django 5.1+
- PostgreSQL

## 📋 Pré-requisitos

- Python 3.12 ou superior
- PostgreSQL
- UV (Gerenciador de pacotes Python)

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

5. Instale as dependências do projeto:
   ```bash
   uv pip install .
5. Copie o arquivo de exemplo de variáveis de ambiente:
   ```bash
   cp env_files/.env.example env_files/.env
   ```
6. Configure as variáveis de ambiente no arquivo `.env`
7. Execute as migrações:
   ```bash
   task migrate
   ```

## 🏃‍♂️ Executando o projeto

```bash
task run
```

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
│   ├── static/         # Arquivos estáticos
│   └── templates/      # Templates HTML
├── pyproject.toml      # Configuração do projeto e dependências
└── README.md          # Este arquivo
```

## 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.