![logo do projeto](assets/Logo%20Verde.png){ width="200" .logo }

# Bem-vindo à Documentação

Este é o portal de documentação do meu portfólio website, uma plataforma que serve como vitrine para meu trabalho, habilidades e experiências profissionais. Aqui você encontrará toda a documentação técnica necessária para entender, instalar e contribuir com o projeto.

## Visão Geral

O projeto foi desenvolvido com foco em performance, usabilidade e manutenibilidade, utilizando tecnologias modernas tanto no backend quanto no frontend.

### Stack Tecnológico

#### Backend
- **Python 3.12+**: Linguagem de programação principal
- **Django 5.1+**: Framework web robusto e escalável
- **PostgreSQL**: Sistema de gerenciamento de banco de dados

#### Frontend
- **Vite**: Bundler moderno e eficiente
- **Tailwind CSS v4**: Framework CSS utilitário
- **DaisyUI**: Biblioteca de componentes para Tailwind
- **HTMX**: Biblioteca para interações dinâmicas
- **AlpineJS**: Framework JavaScript minimalista

#### Documentação
- **MkDocs**: Gerador de documentação
- **Material for MkDocs**: Tema moderno e responsivo

## Recursos Principais

- Interface moderna e responsiva
- Seção de projetos com demonstrações interativas
- Blog técnico integrado
- Área de contato e redes sociais
- Documentação completa e atualizada

## Começando

Para começar a utilizar ou contribuir com o projeto, recomendamos seguir nossa [guia de instalação](getting-started/installation.md) que contém todas as instruções necessárias para configurar o ambiente de desenvolvimento.

## Estrutura do Projeto

```
.
├── docs/                  # Documentação do projeto
│   ├── assets/           # Recursos da documentação
│   ├── getting_started/  # Guias de início rápido
│   └── stylesheets/      # Estilos personalizados da documentação
├── env_files/            # Arquivos de configuração de ambiente
├── src/                  # Código fonte do projeto
│   ├── core/             # Configurações principais do Django
│   │   ├── settings.py   # Configurações do projeto
│   │   ├── urls.py       # URLs principais
│   │   └── wsgi.py       # Configuração WSGI
│   ├── portfolio/        # Aplicação principal
│   │   ├── migrations/   # Migrações do banco de dados
│   │   ├── models.py     # Modelos de dados
│   │   ├── views.py      # Views da aplicação
│   │   └── urls.py       # Configuração de URLs
│   ├── static/           # Arquivos estáticos
│   │   ├── css/          # Estilos CSS e componentes
│   │   ├── js/           # Scripts JavaScript
│   │   └── img/          # Imagens e recursos visuais
│   └── templates/        # Templates HTML
│       ├── components/   # Componentes reutilizáveis
│       └── portfolio/    # Templates específicos
├── mkdocs.yml            # Configuração da documentação
├── package.json          # Dependências do frontend
├── pyproject.toml        # Dependências do Python
├── vite.config.mjs       # Configuração do Vite
└── uv.lock               # Lock file do gerenciador de pacotes Python
```

## Contribuindo

Contribuições são sempre bem-vindas! Se você encontrou um bug ou tem uma sugestão de melhoria, por favor, abra uma issue no nosso repositório GitHub.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://github.com/matheusfabiao/matheusfabiao_portfolio_website/blob/main/LICENSE) para mais detalhes.