# Instalação

Este guia fornecerá instruções detalhadas para configurar o ambiente de desenvolvimento e instalar todas as dependências necessárias para executar o projeto.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em seu sistema:

- Python 3.8 ou superior
- Node.js 18 ou superior
- Git

## Passos para Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/matheusfabiao/matheusfabiao_portfolio_website.git
cd matheusfabiao_portfolio_website
```

### 2. Instale o UV

O UV é um instalador e gerenciador de pacotes Python rápido, escrito em Rust. Para instalá-lo, execute:

```bash
python -m pip install uv
```

### 3. Configure o Ambiente Python

```bash
# Crie um ambiente virtual usando UV
uv venv

# Ative o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux/MacOS:
source .venv/bin/activate

# Instale as dependências Python usando UV
uv pip install .
```

### 4. Instale as Dependências Node.js

```bash
# Instale as dependências do projeto
npm install
```

### 5. Configure as Variáveis de Ambiente

1. Copie o arquivo de exemplo de variáveis de ambiente:
```bash
cp env_files/.env.example env_files/.env
```

2. Abra o arquivo `env_files/.env` em um editor de texto e configure as variáveis de acordo com seu ambiente.

### 6. Execute as Migrações

```bash
task migrate
```

## Verificando a Instalação

Para verificar se tudo foi instalado corretamente, você pode iniciar o servidor de desenvolvimento:

1. Inicie o servidor Django:
```bash
task run
```

2. Em outro terminal, inicie o servidor Vite:
```bash
npm run dev
```

Se tudo estiver configurado corretamente, você poderá acessar o projeto em `http://localhost:8000`.

## Solução de Problemas

Se você encontrar algum problema durante a instalação, verifique:

1. Se todas as dependências estão instaladas corretamente
2. Se o ambiente virtual está ativado
3. Se as variáveis de ambiente estão configuradas corretamente
4. Se todas as portas necessárias estão disponíveis