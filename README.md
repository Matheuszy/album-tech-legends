# Alura Album — Copa do Mundo Tech

Um álbum de figurinhas interativo e digital dedicado às maiores personalidades da tecnologia mundial e brasileira. Desenvolvido durante a **Imersão Julho 2026 — Arquitetura Web com IA da Alura**, o projeto combina um frontend animado com virada de páginas e integração a uma API backend para exibir as figurinhas coletadas.

---

## Objetivo

Criar uma experiência imersiva de álbum de figurinhas no navegador, celebrando pioneiros e ícones da tecnologia em categorias como IA, Python, Bancos de Dados, Sistemas Operacionais e Devs do Brasil. O álbum consome uma API REST (FastAPI) para buscar e exibir dinamicamente as figurinhas já "coladas".

---

## Funcionalidades

### Álbum interativo com virada de páginas
Utiliza a biblioteca [StPageFlip](https://github.com/Nodlik/StPageFlip) para simular um livro físico com animação de virada. Navegue arrastando as páginas com mouse ou toque, usando os botões de seta ou as teclas `←` `→`.

### Figurinhas carregadas dinamicamente da API
O backend lê a pasta `figurinhas/` automaticamente — basta adicionar uma imagem seguindo o padrão `NN-nome.jpg` e ela aparece no álbum sem nenhuma alteração no código.

### Efeito holográfico em figurinhas raras
Os slots especiais (#03, #08, #13, #18, #23, #28) recebem um efeito TCG ao ser preenchidos:
- Tilt 3D que segue o cursor do mouse
- Reflexo holográfico interativo com gradiente arco-íris
- Partículas de glitter que se movem com o mouse
- Borda com rotação de cor (hue-rotate) animada
- Badge dourado **✦ RARO**

### Compartilhar álbum
Botão de compartilhar captura o álbum atual como imagem PNG em alta resolução (2x) usando `html2canvas` e faz o download automaticamente.

### Som de virada de página
Som de papel sintetizado em tempo real via **Web Audio API** — sem arquivo de áudio externo. Pode ser silenciado pelo botão no canto superior direito.

### Tema da Seleção Brasileira
Paleta de cores inspirada na seleção: verde `#009C3B`, amarelo/ouro `#FFDF00` e azul da bandeira `#002776`.

### Design responsivo
Adapta-se a diferentes tamanhos de tela. Em mobile, exibe uma página por vez.

### Capa animada
Efeito **glitch** no título, mini-cards flutuantes e esfera 3D giratória com brilho pulsante — tudo em CSS puro.

---

## Categorias do Álbum

| Categoria | Slots | Destaques |
|---|---|---|
| IA | #01–#05 | Alan Turing, Sam Altman, Geoffrey Hinton |
| Python | #06–#10 | Guido van Rossum, Tim Peters, Wes McKinney |
| Banco de Dados | #11–#15 | Edgar F. Codd, Michael Widenius, Salvatore Sanfilippo |
| Sistemas Operacionais | #16–#20 | Linus Torvalds, Dennis Ritchie, Steve Jobs |
| Devs do Brasil Vol. 1 | #21–#25 | Paulo Silveira, Gustavo Guanabara, Maurício Aniche |
| Devs do Brasil Vol. 2 | #26–#30 | Guilherme Lima, Rafaela Ballerini, e **você** (#30) |

---

## Estrutura do Projeto

```
├── front-end/
│   ├── index.html   # Estrutura do álbum e todas as páginas/slots
│   ├── style.css    # Estilos, animações e responsividade
│   └── app.js       # Lógica de navegação, som, efeito raro e compartilhar
├── back-end/
│   ├── main.py      # API FastAPI com serving de imagens estáticas
│   └── figurinhas/  # Pasta com as imagens (padrão: 01-nome.jpg)
└── README.md
```

---

## Como Executar

**Terminal 1 — backend**
```bash
cd back-end
uvicorn main:app --reload
```

**Terminal 2 — frontend**
```bash
cd front-end
python -m http.server 3000
```

Acesse **`http://localhost:3000`** no navegador.

> Sem o backend rodando, o álbum abre normalmente com os slots vazios.

### Adicionando figurinhas
Coloque imagens na pasta `back-end/figurinhas/` seguindo o padrão:
```
01-alan-turing.jpg
21-paulo-silveira.jpeg
```
O número determina em qual slot a figurinha aparece. Sem necessidade de alterar código.

---

## Tecnologias Utilizadas

- **HTML5 / CSS3 / JavaScript** (Vanilla)
- [StPageFlip v2.0.7](https://github.com/Nodlik/StPageFlip) — animação de livro
- [html2canvas v1.4.1](https://html2canvas.hertzen.com/) — captura de tela para compartilhar
- **Web Audio API** — síntese de som de papel
- **FastAPI + Uvicorn** — backend Python com serving de imagens estáticas
- **Google Fonts** — Inter e Outfit

---

## Próximos Passos (ideias)

- [ ] Sistema de troca de figurinhas entre usuários
- [ ] Autenticação com login e álbum por usuário (Spring Boot / FastAPI)
- [ ] Barra de progresso de conclusão do álbum
- [ ] Banco de dados para persistir a coleção

### Sistema de Troca — como funcionaria

A funcionalidade de troca exige backend com estado. Em tese, o fluxo seria:

**Com Python (FastAPI + SQLite/PostgreSQL)**
```python
# Modelo de troca
class Troca(BaseModel):
    de_usuario: int
    para_usuario: int
    figurinha_oferecida: int
    figurinha_desejada: int
    status: str  # "pendente", "aceita", "recusada"

@app.post("/trocas")
def propor_troca(troca: Troca, db: Session = Depends(get_db)):
    nova_troca = TrocaDB(**troca.dict(), status="pendente")
    db.add(nova_troca)
    db.commit()
    return nova_troca

@app.patch("/trocas/{id}/aceitar")
def aceitar_troca(id: int, db: Session = Depends(get_db)):
    troca = db.query(TrocaDB).filter(TrocaDB.id == id).first()
    # Transfere as figurinhas entre os usuários
    # Atualiza status para "aceita"
    ...
```

**Com Java (Spring Boot + JPA)**
```java
@Entity
public class Troca {
    @Id @GeneratedValue
    private Long id;
    private Long deUsuario;
    private Long paraUsuario;
    private Integer figurinhaOferecida;
    private Integer figurinhaDesejada;
    private StatusTroca status;
}

@RestController
@RequestMapping("/trocas")
public class TrocaController {

    @PostMapping
    public Troca propor(@RequestBody Troca troca) {
        troca.setStatus(StatusTroca.PENDENTE);
        return trocaRepository.save(troca);
    }

    @PatchMapping("/{id}/aceitar")
    @Transactional
    public Troca aceitar(@PathVariable Long id) {
        Troca troca = trocaRepository.findById(id).orElseThrow();
        // Transfere figurinhas entre coleções
        // Atualiza status
        troca.setStatus(StatusTroca.ACEITA);
        return trocaRepository.save(troca);
    }
}
```

O Spring Boot seria a escolha mais robusta para esse cenário por ter Spring Security para autenticação, JPA para os relacionamentos entre `Usuario`, `Figurinha` e `Troca`, e suporte a transações para garantir que a troca só acontece se os dois lados tiverem as figurinhas.

---

*Imersão Julho 2026 — Arquitetura Web com IA — Alura*
