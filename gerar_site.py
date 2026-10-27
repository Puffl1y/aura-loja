
from html import escape
from pathlib import Path

# Caminho da pasta onde os arquivos HTML e CSS ficam armazenados.
PASTA_SITE = Path(__file__).parent / "site"

# Lista de produtos da loja virtual.
produtos = [
    {
        "nome": "Camisa Linho Natural",
        "categoria": "Feminino · Camisas",
        "preco": 149.90,
        "cor": "Areia",
        "imagem": "https://images.unsplash.com/photo-1598554747436-c9293d6a588f?auto=format&fit=crop&w=900&q=85",
        "selo": "MAIS VENDIDO"
    },
    {
        "nome": "Tricot Essencial",
        "categoria": "Feminino · Tricots",
        "preco": 189.90,
        "cor": "Creme",
        "imagem": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?auto=format&fit=crop&w=900&q=85",
        "selo": "NOVO"
    },
    {
        "nome": "Jaqueta Urbana",
        "categoria": "Masculino · Jaquetas",
        "preco": 279.90,
        "cor": "Oliva",
        "imagem": "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=900&q=85",
        "selo": ""
    },
    {
        "nome": "Calça Reta",
        "categoria": "Feminino · Calças",
        "preco": 219.90,
        "cor": "Preto",
        "imagem": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=900&q=85",
        "selo": ""
    }
]


def formatar_preco(valor):
    """Converte o preço para o formato monetário brasileiro."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def criar_cartao(produto):
    """Gera o HTML de um cartão de produto."""

    nome = escape(produto["nome"])
    categoria = escape(produto["categoria"])
    cor = escape(produto["cor"])
    imagem = escape(produto["imagem"], quote=True)
    preco = formatar_preco(produto["preco"])

    selo = ""

    if produto["selo"]:
        selo = f'<span class="selo">{escape(produto["selo"])}</span>'

    cartao = f"""
    <article class="produto">
        <div class="produto-foto">
            {selo}
            <img
                src="{imagem}"
                alt="{nome}"
                loading="lazy"
            >
        </div>

        <p class="categoria">{categoria}</p>
        <h3>{nome}</h3>
        <p class="cor">Cor: {cor}</p>
        <p class="preco">{preco}</p>

        <a class="comprar" href="#aviso">
            Ver detalhes
        </a>
    </article>
    """

    return cartao


def gerar_pagina():
    """Gera a página HTML completa da loja."""

    cartoes = "\n".join(
        criar_cartao(produto)
        for produto in produtos
    )

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta
        name="description"
        content="AURA: moda contemporânea, peças essenciais e estilo atemporal."
    >

    <title>AURA | Vista o seu momento</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="faixa">
        FRETE GRÁTIS NAS COMPRAS ACIMA DE R$ 299 · COLEÇÃO NOVA
    </div>

    <header class="cabecalho">
        <a class="marca" href="#inicio">AURA<span>.</span></a>

        <nav aria-label="Menu principal">
            <a href="#novidades">Novidades</a>
            <a href="#colecao">Roupas</a>
            <a href="#sobre">Nossa essência</a>
        </nav>

        <a class="sacola" href="#colecao">
            SUA SACOLA <span>♡</span>
        </a>
    </header>

    <main>

        <section class="hero" id="inicio">
            <div class="hero-texto">
                <p class="eyebrow">COLEÇÃO / 2026</p>

                <h1>
                    Vista o seu<br>
                    <em>próprio momento.</em>
                </h1>

                <p>
                    Peças atemporais, texturas naturais e escolhas
                    feitas para acompanhar você em todos os dias.
                </p>

                <a class="botao-escuro" href="#colecao">
                    EXPLORAR COLEÇÃO <span>↗</span>
                </a>
            </div>

            <div
                class="hero-imagem"
                role="img"
                aria-label="Editorial de moda em tons neutros"
            >
                <div class="hero-legenda">
                    <span>01 / ESSENCIAIS</span>
                    <span>MENOS, MAS MELHOR.</span>
                </div>
            </div>
        </section>

        <section class="beneficios">
            <div><span>✳</span> DESIGN ATEMPORAL</div>
            <div><span>◇</span> ESCOLHAS CONSCIENTES</div>
            <div><span>↗</span> FEITO PARA DURAR</div>
        </section>

        <section class="colecao" id="colecao">

            <div class="secao-topo" id="novidades">
                <div>
                    <p class="eyebrow">SELEÇÃO AURA</p>
                    <h2>Favoritos da estação<span>.</span></h2>
                </div>

                <p>
                    Uma curadoria de peças versáteis para<br>
                    combinar do seu jeito.
                </p>
            </div>

            <div class="grade">
                {cartoes}
            </div>

            <p class="aviso" id="aviso">
                Vitrine demonstrativa para projeto acadêmico.
                Os links e a sacola não realizam compras reais.
            </p>

        </section>

        <section class="manifesto" id="sobre">
            <p class="eyebrow">NOSSA ESSÊNCIA</p>

            <h2>
                Estilo não precisa<br>
                de exageros<span>.</span>
            </h2>

            <p>
                AURA celebra o vestir com intenção: formas simples,
                tons que conversam e peças que fazem sentido
                no seu guarda-roupa.
            </p>

            <a href="#inicio" class="link-seta">
                VOLTAR AO TOPO ↑
            </a>
        </section>

    </main>

    <footer>
        <a class="marca" href="#inicio">AURA<span>.</span></a>

        <p>Projeto acadêmico · Python + HTML + CSS + NGINX</p>

        <p>© 2026 AURA</p>
    </footer>

</body>
</html>
"""

    # Cria a pasta site caso ela ainda não exista.
    PASTA_SITE.mkdir(parents=True, exist_ok=True)

    # Salva o arquivo HTML com codificação UTF-8.
    arquivo_html = PASTA_SITE / "index.html"

    arquivo_html.write_text(html, encoding="utf-8")

    print("Página da loja gerada com sucesso!")
    print(f"Arquivo criado: {arquivo_html}")


if __name__ == "__main__":
    gerar_pagina()
