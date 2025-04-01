# Configuração

Este guia explica como configurar e personalizar o projeto após a instalação inicial.

## Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configurações sensíveis e específicas do ambiente. O arquivo `.env` deve ser configurado com base no exemplo fornecido em `env_files/.env.example`.

### Variáveis Importantes

```bash
# Configurações do Django
DJANGO_SECRET_KEY=sua_chave_secreta_aqui
DJANGO_DEBUG=True  # Mude para False em produção
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Configurações de Banco de Dados
DB_NAME=seu_banco_de_dados
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

## Configuração do Django

### Configurações Básicas

As principais configurações do Django estão localizadas em `src/core/settings.py`. Aqui estão algumas configurações importantes:

```python
# Configurações de Segurança
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

# Configuração de Banco de Dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Configuração de Idioma e Fuso Horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

### Configuração de Arquivos Estáticos

O projeto utiliza o Vite para gerenciar os arquivos estáticos do frontend. As configurações estão em:

```python
# Configurações de Arquivos Estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

## Configuração do Frontend

### Vite

O arquivo `vite.config.mjs` contém as configurações do Vite para o frontend:

```javascript
export default defineConfig({
  plugins: [
    // Plugins configurados
  ],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    emptyOutDir: true
  }
})
```

## Boas Práticas

1. **Segurança**:
   - Nunca comite arquivos `.env` no repositório
   - Mantenha o `DEBUG=False` em produção
   - Use variáveis de ambiente para configurações sensíveis

2. **Performance**:
   - Configure corretamente o cache
   - Otimize as configurações de banco de dados
   - Use CDN para arquivos estáticos em produção

3. **Desenvolvimento**:
   - Mantenha diferentes configurações para desenvolvimento e produção
   - Use ferramentas de linting e formatação
   - Configure corretamente o CORS e CSP

## Próximos Passos

Após configurar o projeto, você pode prosseguir para o guia de [Implantação](deployment.md) para aprender como colocar o projeto em produção.