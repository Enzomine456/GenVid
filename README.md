# GenVid - Gerador de Vídeos Animados por IA

GenVid é uma aplicação web que utiliza inteligência artificial para gerar vídeos animados a partir de prompts de texto fornecidos pelos usuários. O sistema inclui autenticação por chave de API, sugestões de prompts, armazenamento em banco de dados e suporte para imagens de referência.

## Funcionalidades

- Registro e login de usuários
- Sistema de autenticação por chave de API
- Geração de vídeos animados a partir de prompts de texto (sem dependência da OpenAI)
- Upload e uso de imagens de referência
- Sugestões de prompts para inspirar os usuários
- Armazenamento de histórico de solicitações de vídeo
- Interface web responsiva com tema branco e azul bebê
- Download de vídeos gerados
- Geração de múltiplas chaves de API por usuário

## Tecnologias Utilizadas

- Python 3
- Flask (Framework web)
- SQLAlchemy (ORM para banco de dados)
- MoviePy (para geração de vídeos)
- Pillow (para processamento de imagens)
- HTML/CSS/JavaScript (Frontend)
- Bootstrap 5 (Framework CSS)

## Estrutura do Projeto

```
genvid/
├── app.py              # Aplicação principal Flask
├── models.py           # Modelos de banco de dados
├── requirements.txt    # Dependências do projeto
├── .env                # Variáveis de ambiente
├── Procfile            # Configuração para Glitch
├── Dockerfile          # Configuração para Docker/Fly.io
├── fly.toml            # Configuração para Fly.io
├── vercel.json         # Configuração para Vercel
├── api.py              # Ponto de entrada para Vercel
├── README.md           # Este arquivo
├── DEPLOY_FLY_IO.md    # Guia de deploy para Fly.io
├── DEPLOY_VERCEL.md    # Guia de deploy para Vercel
├── VERCEL_DEPLOY.md    # Instruções rápidas para Vercel
├── fly_launch_fix.py   # Script para corrigir problemas de deploy no Fly.io
├── deploy_windows.bat  # Script de ajuda para deploy no Windows
├── templates/
│   └── index.html      # Página principal
├── static/
│   └── styles.css      # Estilos personalizados
├── uploads/            # Diretório para imagens de referência
└── videos/             # Diretório para vídeos gerados
```

## Como Executar Localmente

1. Clone o repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente no arquivo `.env`:
   - `SECRET_KEY`: Uma chave secreta para segurança
   - `DATABASE_URL`: URL do banco de dados (padrão é SQLite)
4. Execute a aplicação:
   ```
   python app.py
   ```

## Como Implantar no Glitch

1. Crie um novo projeto no Glitch
2. Faça upload dos arquivos do projeto
3. Adicione as variáveis de ambiente nas configurações do projeto:
   - `SECRET_KEY`
4. O Glitch irá automaticamente instalar as dependências e iniciar a aplicação

## Como Implantar no Fly.io

Siga as instruções detalhadas no guia [DEPLOY_FLY_IO.md](file:///C:/Users/Enzo/Documents/GenVid/DEPLOY_FLY_IO.md) para implantar a aplicação no Fly.io.

## Como Implantar no Vercel

Siga as instruções detalhadas no guia [DEPLOY_VERCEL.md](file:///C:/Users/Enzo/Documents/GenVid/DEPLOY_VERCEL.md) ou o guia rápido em [VERCEL_DEPLOY.md](file:///C:/Users/Enzo/Documents/GenVid/VERCEL_DEPLOY.md) para implantar a aplicação no Vercel.

### Instruções para Usuários Windows

Para usuários Windows, siga estas etapas específicas:

1. Instale o Fly.io CLI:
   ```
   winget install flyctl
   ```
   
2. Feche e reabra o prompt de comando para atualizar o PATH

3. Verifique a instalação:
   ```
   flyctl version
   ```

4. Use o script de ajuda para Windows:
   ```
   deploy_windows.bat
   ```

### Instruções Gerais para Fly.io

Resumo rápido:
1. Instale o [Fly.io CLI](https://fly.io/docs/getting-started/installing-flyctl/)
2. Faça login na sua conta Fly.io:
   ```
   flyctl auth login
   ```
3. Crie um novo app no Fly.io:
   ```
   flyctl launch
   ```
4. Configure as variáveis de ambiente:
   ```
   flyctl secrets set SECRET_KEY="sua-chave-secreta-aqui"
   ```
5. Implante a aplicação:
   ```
   flyctl deploy
   ```
6. Acesse sua aplicação:
   ```
   flyctl open
   ```

## Endpoints da API

- `POST /api/register` - Registrar um novo usuário
- `POST /api/login` - Fazer login e obter token JWT
- `POST /api/upload-image` - Upload de imagem de referência (requer autenticação)
- `POST /api/generate-video` - Gerar vídeo a partir de prompt e imagens (requer autenticação)
- `GET /api/suggested-prompts` - Obter sugestões de prompts
- `GET /api/user/api-keys` - Obter chaves de API do usuário (requer autenticação)
- `POST /api/user/generate-api-key` - Gerar nova chave de API (requer autenticação)
- `GET /health` - Verificação de saúde da aplicação

## Geração de Vídeos

O GenVid gera vídeos de forma independente, sem depender da API da OpenAI. A geração é feita usando a biblioteca MoviePy, que cria vídeos animados com base nos prompts fornecidos pelos usuários. Os usuários também podem enviar imagens de referência que influenciam o processo de geração.

## Gerenciamento de Chaves de API

Cada usuário pode gerar e gerenciar múltiplas chaves de API para acessar os serviços da GenVid. As chaves podem ser usadas para autenticação em solicitações diretas à API.

## Interface com Tema Branco e Azul Bebê

A interface do GenVid utiliza uma paleta de cores suave com tons de branco e azul bebê, proporcionando uma experiência visual agradável e confortável para os usuários.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto é licenciado sob a licença MIT.