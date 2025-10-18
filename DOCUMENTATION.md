# Documentação GenVid

## Visão Geral

GenVid é uma aplicação web baseada em Python que gera vídeos animados a partir de prompts de texto e imagens de referência fornecidos pelos usuários. O sistema inclui um sistema completo de autenticação, gerenciamento de chaves de API, sugestões de prompts, armazenamento em banco de dados e capacidade de download de vídeos.

## Arquitetura do Sistema

```
GenVid/
├── app.py              # Aplicação principal Flask
├── models.py           # Modelos de banco de dados
├── requirements.txt    # Dependências do projeto
├── .env                # Variáveis de ambiente
├── Procfile            # Configuração para Glitch
├── README.md           # Documentação principal
├── DOCUMENTATION.md    # Documentação técnica detalhada
├── templates/
│   └── index.html      # Interface do usuário
├── static/
│   └── styles.css      # Estilos personalizados
├── uploads/            # Diretório para imagens de referência
└── videos/             # Diretório para vídeos gerados
```

## Componentes Principais

### 1. Aplicação Flask (app.py)

O núcleo da aplicação é construído com o framework Flask e inclui:

- Sistema de autenticação JWT
- Rotas da API para registro, login e geração de vídeos
- Upload e gerenciamento de imagens de referência
- Geração de vídeos usando MoviePy (sem dependência da OpenAI)
- Gerenciamento de banco de dados
- Serviço para download de vídeos
- Geração e gerenciamento de chaves de API

**Rotas da API:**
- `POST /api/register` - Registrar novo usuário
- `POST /api/login` - Autenticar usuário
- `POST /api/upload-image` - Upload de imagem de referência
- `POST /api/generate-video` - Gerar vídeo a partir de prompt e imagens
- `GET /api/suggested-prompts` - Obter sugestões de prompts
- `GET /api/user/api-keys` - Obter chaves de API do usuário
- `POST /api/user/generate-api-key` - Gerar nova chave de API

### 2. Modelos de Banco de Dados (models.py)

Três modelos principais são definidos:

- **User**: Armazena informações de usuários registrados
- **APIKey**: Gerencia chaves de API para autenticação
- **VideoRequest**: Registra solicitações de geração de vídeo, incluindo referências a imagens

### 3. Interface do Usuário (templates/index.html)

Interface web responsiva construída com Bootstrap que inclui:

- Formulários de registro e login
- Área para entrada de prompts
- Seção de upload de imagens de referência
- Visualização de prévias de imagens
- Seção de sugestões de prompts
- Visualização de vídeos gerados
- Botão de download para vídeos
- Gerenciamento de chaves de API
- **Tema branco e azul bebê para uma experiência visual agradável**

## Funcionalidades

### Autenticação e Autorização

O sistema utiliza autenticação JWT para proteger as rotas da API. Após o registro, os usuários recebem uma chave de API que pode ser usada para autenticação em solicitações diretas à API.

### Upload de Imagens de Referência

Os usuários podem enviar imagens que servem como referência para a geração de vídeos:

- Suporte para múltiplas imagens
- Visualização de prévias das imagens enviadas
- Armazenamento seguro das imagens
- Integração com o processo de geração de vídeo

### Geração de Vídeos

O processo de geração de vídeos envolve:

1. Receber um prompt de texto do usuário
2. Receber imagens de referência (opcional)
3. Utilizar a biblioteca MoviePy para criar um vídeo animado
4. Armazenar os metadados no banco de dados
5. Disponibilizar o vídeo para visualização e download

### Sugestões de Prompts

O sistema oferece uma lista de prompts pré-definidos para inspirar os usuários e demonstrar as capacidades do sistema.

### Download de Vídeos

Os usuários podem baixar os vídeos gerados diretamente através da interface web.

### Gerenciamento de Chaves de API

Os usuários podem visualizar e gerenciar suas chaves de API através da interface web:

- Visualização de todas as chaves de API associadas à conta
- Geração de novas chaves de API
- Cada chave é única e pode ser usada para autenticação em APIs externas

### Interface com Tema Branco e Azul Bebê

A interface do GenVid utiliza uma paleta de cores suave com tons de branco e azul bebê, proporcionando:

- Experiência visual agradável e confortável
- Contraste adequado para melhor leitura
- Design moderno e limpo
- Cores suaves que reduzem a fadiga visual

## Implantação no Glitch

### Configuração Inicial

1. Criar um novo projeto no Glitch
2. Fazer upload de todos os arquivos do projeto
3. Configurar as variáveis de ambiente:
   - `SECRET_KEY`: Chave secreta para segurança da aplicação

### Variáveis de Ambiente

```
SECRET_KEY=chave-secreta-aqui
DATABASE_URL=sqlite:///genvid.db
```

### Processo de Implantação

O Glitch automaticamente:
1. Instala as dependências listadas em `requirements.txt`
2. Inicia a aplicação usando o comando especificado no `Procfile`
3. Fornece uma URL pública para acessar a aplicação

## Como Implantar no Fly.io

Para implantar o GenVid no Fly.io, siga estas etapas:

### 1. Instalar o Fly.io CLI

Primeiro, instale o Fly.io CLI seguindo as instruções em [https://fly.io/docs/getting-started/installing-flyctl/](https://fly.io/docs/getting-started/installing-flyctl/)

### 2. Fazer Login

Faça login na sua conta Fly.io:

```bash
flyctl auth login
```

### 3. Configurar o App

Navegue até o diretório do projeto e crie um novo app:

```bash
flyctl launch
```

Siga as instruções:
- Escolha um nome para seu app
- Selecione uma região
- Não implante ainda quando perguntado

### 4. Configurar Variáveis de Ambiente

Configure a chave secreta para a aplicação:

```bash
flyctl secrets set SECRET_KEY="sua-chave-secreta-segura-aqui"
```

### 5. Implantar

Implante a aplicação:

```bash
flyctl deploy
```

### 6. Acessar

Abra a aplicação no navegador:

```bash
flyctl open
```

### Configurações Adicionais

O arquivo `fly.toml` já está configurado com:
- Dockerfile para construção da imagem
- Porta 8080 para o serviço HTTP
- Configurações de auto scaling

Se precisar de um banco de dados persistente, considere usar o Fly.io PostgreSQL:

```bash
flyctl postgres create
```

E então conectar à sua aplicação:

```bash
flyctl postgres attach NOME_DO_SEU_BANCO_DE_DADOS
```

## Desenvolvimento Local

### Requisitos

- Python 3.7+
- Pip (gerenciador de pacotes Python)

### Instalação

1. Clonar o repositório
2. Criar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Configuração

1. Copiar `.env.example` para `.env`
2. Configurar as variáveis de ambiente:
   - `SECRET_KEY`: Chave secreta para segurança

### Execução

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## Segurança

### Práticas Implementadas

- Autenticação JWT para proteção de rotas
- Validação de entrada em todas as rotas da API
- Uso de variáveis de ambiente para chaves secretas
- Proteção contra solicitações malformadas
- Limitação de tamanho de upload de arquivos

### Considerações para Produção

- As senhas devem ser criptografadas antes de serem armazenadas
- Implementar limites de taxa para prevenir abuso da API
- Utilizar um banco de dados mais robusto (PostgreSQL, MySQL) em vez de SQLite
- Adicionar validação e sanitização mais rigorosa de entrada
- Implementar armazenamento em nuvem para imagens e vídeos

## Extensibilidade

### Adições Futuras

1. **Geração Avançada de Vídeos**: Melhorar a qualidade dos vídeos gerados com animações mais complexas
2. **Processamento de Imagens**: Usar imagens de referência para influenciar o estilo do vídeo
3. **Personalização de Estilo**: Permitir que os usuários escolham estilos visuais
4. **Biblioteca de Vídeos**: Permitir que os usuários salvem e compartilhem vídeos gerados
5. **Integração com Redes Sociais**: Compartilhamento direto em plataformas sociais
6. **Modelos de Vídeos**: Modelos pré-definidos para diferentes tipos de conteúdo

## Solução de Problemas

### Problemas Comuns

1. **Erros de Dependências**: Verifique se todas as dependências foram instaladas corretamente
2. **Problemas de Banco de Dados**: Certifique-se de que o arquivo de banco de dados tem permissões de leitura/escrita
3. **Erros de Autenticação**: Verifique se o token JWT está sendo enviado corretamente
4. **Falhas na Geração de Vídeos**: Verifique se os diretórios `videos/` e `uploads/` têm permissões de escrita
5. **Erros de Upload**: Verifique o tamanho e formato das imagens

### Logs e Depuração

A aplicação registra informações importantes no console. Para depuração adicional, defina `debug=True` no arquivo [app.py](file:///C:/Users/Enzo/Documents/GenVid/app.py).

## Contribuição

1. Fork do repositório
2. Criar branch para nova funcionalidade (`git checkout -b feature/nova-funcionalidade`)
3. Commit das alterações (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para o branch (`git push origin feature/nova-funcionalidade`)
5. Criar novo Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](file:///C:/Users/Enzo/Documents/GenVid/LICENSE.md) para detalhes.