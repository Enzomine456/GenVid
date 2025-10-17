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
├── README.md           # Este arquivo
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

## Endpoints da API

- `POST /api/register` - Registrar um novo usuário
- `POST /api/login` - Fazer login e obter token JWT
- `POST /api/upload-image` - Upload de imagem de referência (requer autenticação)
- `POST /api/generate-video` - Gerar vídeo a partir de prompt e imagens (requer autenticação)
- `GET /api/suggested-prompts` - Obter sugestões de prompts
- `GET /api/user/api-keys` - Obter chaves de API do usuário (requer autenticação)
- `POST /api/user/generate-api-key` - Gerar nova chave de API (requer autenticação)

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