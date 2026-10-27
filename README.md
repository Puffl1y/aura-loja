
# AURA — Loja Virtual de Roupas

## Descrição

AURA é uma vitrine virtual demonstrativa de roupas,
desenvolvida com Python, HTML e CSS.

O Python gera a página HTML com base em uma lista
de produtos. O NGINX, executado via Docker, disponibiliza
os arquivos estáticos pelo protocolo HTTP.

## Tecnologias

- Python
- HTML5
- CSS3
- Docker
- Docker Compose
- NGINX

## Estrutura do projeto

aura-loja/
├── docker-compose.yml
├── gerar_site.py
├── README.md
└── site/
    ├── index.html
    └── style.css

## Requisitos

- Python 3 instalado
- Docker Desktop instalado e em execução

## Como executar

### 1. Gerar a página HTML

Na raiz do projeto, execute:

python gerar_site.py

No Windows, também pode ser utilizado:

py gerar_site.py

### 2. Iniciar o servidor

docker compose up -d

### 3. Acessar a loja

Abra no navegador:

http://localhost:8080

### 4. Verificar o servidor

docker compose ps

Para testar a resposta HTTP:

curl -I http://localhost:8080

### 5. Encerrar o servidor

docker compose down

## Observações

A aplicação é uma vitrine estática.
Os links de produtos e a sacola não realizam compras.

O NGINX entrega os arquivos gerados previamente.
Ele não executa o código Python a cada requisição.

As imagens e fontes externas dependem de conexão
com a internet.
