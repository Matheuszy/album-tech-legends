# Alura Album — Copa do Mundo Tech

Um álbum de figurinhas interativo e digital dedicado às maiores personalidades da tecnologia mundial e brasileira. Desenvolvido durante a **Imersão Julho 2026 da Alura**, o projeto combina um frontend animado com virada de páginas e integração a uma API backend para exibir as figurinhas coletadas.

---

## Objetivo

Criar uma experiência imersiva de álbum de figurinhas no navegador, celebrando pioneiros e ícones da tecnologia em categorias como IA, Python, Bancos de Dados, Sistemas Operacionais e Devs do Brasil. O álbum consome uma API REST (FastAPI) para buscar e exibir dinamicamente as figurinhas já "coladas" pelo usuário.

---

## Funcionalidades

### Álbum interativo com virada de páginas
O álbum utiliza a biblioteca [StPageFlip](https://github.com/Nodlik/StPageFlip) para simular um livro físico com animação de virada de páginas. É possível navegar arrastando as páginas com o mouse ou o dedo (touch), ou usando os botões de seta e as teclas `←` `→` do teclado.

### Som de virada de página
A cada virada, um som realista de papel é sintetizado em tempo real via **Web Audio API** — sem nenhum arquivo de áudio externo. O som pode ser silenciado a qualquer momento pelo botão no canto superior direito.

### Integração com API backend
Ao carregar o álbum, o frontend consulta o endpoint `GET /figurinhas` de uma API local (FastAPI, porta 8000). As figurinhas retornadas são inseridas nos slots correspondentes com uma animação suave de "colar". Slots sem figurinha permanecem com borda tracejada e o número visível.

### Categorias do álbum
O álbum conta com **30 slots** distribuídos em 6 páginas temáticas:

| Categoria | Slots | Destaques |
|---|---|---|
| IA | #01–#05 | Alan Turing, Sam Altman, Geoffrey Hinton |
| Python | #06–#10 | Guido van Rossum, Tim Peters, Wes McKinney |
| Banco de Dados | #11–#15 | Edgar F. Codd, Michael Widenius, Salvatore Sanfilippo |
| Sistemas Operacionais | #16–#20 | Linus Torvalds, Dennis Ritchie, Steve Jobs |
| Devs do Brasil Vol. 1 | #21–#25 | Paulo Silveira, Gustavo Guanabara, Maurício Aniche |
| Devs do Brasil Vol. 2 | #26–#30 | Guilherme Lima, Rafaela Ballerini, e **você** (#30) |

### Slots especiais
Cada página possui um **slot especial** (ocupa duas colunas) para uma figura de destaque da categoria.

### Design responsivo
O layout adapta-se a diferentes tamanhos de tela. Em dispositivos móveis, o álbum exibe uma página por vez e oculta elementos decorativos para melhor aproveitamento do espaço.

### Capa animada
A capa conta com efeito **glitch** no título, mini-cards flutuantes com animação e uma esfera 3D giratória com brilho pulsante, tudo feito em CSS puro.

---

## Estrutura do Projeto

```
├── index.html   # Estrutura do álbum e todas as páginas/slots
├── style.css    # Estilos, animações e responsividade
└── app.js       # Lógica de inicialização, navegação, som e integração com a API
```

O backend (FastAPI) é desenvolvido separadamente como parte da imersão e deve ser iniciado com:

```bash
cd backend/dia-3
uvicorn main:app --reload
```

---

## Como Executar

1. Inicie o servidor backend na porta `8000`.
2. Abra o `index.html` diretamente no navegador **ou** sirva os arquivos via qualquer servidor HTTP simples.
3. Navegue pelo álbum usando as setas, as teclas do teclado ou arrastando as páginas.

> Sem o backend rodando, o álbum ainda funciona normalmente — os slots simplesmente aparecem vazios, prontos para receber as figurinhas.

---

## Tecnologias Utilizadas

- **HTML5 / CSS3 / JavaScript** (Vanilla)
- [StPageFlip v2.0.7](https://github.com/Nodlik/StPageFlip) — animação de livro
- **Web Audio API** — síntese de som de papel
- **FastAPI** (backend, porta 8000) — fornece os dados das figurinhas
- **Google Fonts** — Inter e Outfit

---

*Imersão Julho 2026 — Alura*
