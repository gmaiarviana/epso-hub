# Próximos passos

A fila entre blocos. Regras (tiers, o que mora onde, como se atualiza) em
[meta/roadmap.md](meta/roadmap.md).

## 1. Passar a limpo

Todas com o bruto seccionado na raiz de `fontes/transcricoes/`: passar a limpo leva o bruto
para `raw/` e cria a cópia limpa. As já encaixadas são citadas por
`arquivo#secao` — se uma seção mudar de nome, as citações acompanham.

- **2026-07-06 "Estratégia profissional"** — primeiro: é a fonte principal de `contexto/`.
- **2026-07-06 "Quatro iniciativas"**
- **2026-07-07 "Camada filosófica e a jornada acadêmica"** — já encaixada (tese, jornada, trajetória).
- **2026-06-26 "A tese — mudança de paradigma"** — já encaixada (tese, precisão).
- **2026-06-26 "Equilíbrio matéria-ideias e a tese de vida"**
- **2026-06-26 "Mestrado, doutorado e contribuição à sociedade"** — já encaixada (quem sou eu).

## 2. Trabalhos em aberto

1. **Migração, sessão 2 — Academia.** `leituras` → `estudo/academia/leituras-entrada.md` e
   `leituras-tese.md`; `mapeamento-academico` → `estudo/academia/mapeamento.md`.
2. **Migração, sessão 3 — mop-up e aposentadoria.** Parciais menores; inventário
   ([meta/estrutura/migracao-epso-paradigm.md](meta/estrutura/migracao-epso-paradigm.md)) todo
   `[x]`; então aposentar e deletar o `epso_paradigm`.
3. **Núcleo do EPSO** — propósito, valores, postura (do `epso_paradigm`, do Documento
   Institucional e da página "Base de pensamento" do site,
   https://www.erapraserobvio.com.br/quem-somos/base-de-pensamento, com o método de 4 etapas
   de `/plataforma`). A postura epistemológica compara-se antes com
   `filosofia/hipoteses/precisao.md`, que já tem a raiz "a realidade excede a verdade".
4. **Iniciativas** — construtora (institucional: princípios construtivos, acervo técnico,
   operacional) e EcoCondomínio (concepção e plano de execução), migrados do Drive. Registrar
   também as ferramentas livres já publicadas no site (Taquígrafo, Camadas da Linguagem).

## 3. Encaixar

- **Transcrição 2026-09-23** (`fontes/transcricoes/2026-09-23-producao-de-conteudo-eixos-portais-e-tematicas.md`)
  — destinos prováveis: eixos, chamados e temáticas na linha editorial da comunicação;
  portais da plataforma nas iniciativas; `#eixo-mercado` e `#plataforma-e-autoridade` em
  `contexto/`. `#portal-linguagem` já está em `filosofia/hipoteses/linguagem.md`.
- **Transcrição 2026-09-24** (`fontes/transcricoes/2026-09-24-atencao-corpo-linguagem-e-camadas.md`)
  — de `#sem-controle` a `#sem-manual-de-instrucoes`, em `filosofia/cosmovisao/quem-sou-eu.md`;
  `#regua-coletiva` parece o eixo de universalidade de `filosofia/hipoteses/precisao.md` —
  checar fusão. De `#feitos-para-aprender` ao fim já está em `filosofia/hipoteses/linguagem.md`.
- **Conversa 2026-07-07** (`fontes/conversas/`) — duas ideias: na migração, reaproveitar as
  ponderações e não o resultado; a iniciativa quatro como camada filosófica (o paper-agent é
  um produto dentro dela).
- **Transcrição 2026-09-22, seções sem encaixe** (`fontes/transcricoes/2026-09-22-regeneracao-lastro-e-eco-cidades.md`):
  - `#fora-do-paradigma-mecanicista` (valores: regeneração, coletividade, colaboração,
    combate à desigualdade) → `instituicao/nucleo/`, junto com o item Núcleo do tier 2.
  - `#instituicoes-do-novo-paradigma` (instituições do novo paradigma e renda) e
    `#novas-instituicoes-e-rotina-autonoma` (rotina autônoma, cuidado de si junto com entrega
    de valor) → `contexto/trajetoria.md`.
  - `#empreender-em-construcao-sustentavel` → `instituicao/iniciativas/`, junto com a
    construtora.
  - `#lastro-conteudo-e-academia` (LinkedIn; pilares de autoridade → índice de temas →
    calendário) → `instituicao/comunicacao/`, junto com a transcrição 2026-09-23.

- **Narrativa de carreira, excerto v8** (`fontes/documentos/2026-09-26-career-narrative-v8-excerto.raw.md`,
  em inglês) — o repositório é o dono destas partes; o documento externo, complementar,
  guarda o detalhe de carreira e passa a derivar daqui:
  - `## 1. Purpose` e `## 2. Values` → `instituicao/nucleo/`, junto com o item Núcleo do tier 2.
  - Parágrafo do EPSO em `## 3. Career Vision` ("dois braços": ferramentas e catálogo; ideias
    entre culturas) → `instituicao/iniciativas/`. Diverge do README (construtora, ferramentas,
    plataforma): vira provocação em [elaborar](elaborar.md).
  - Pesquisa em IA eficiente (`## 3`) → checar fusão com `filosofia/hipoteses/inteligencia-potencializada.md`
    e `estudo/academia/foco.md`.
  - Resto de `## 3` (autoridade de decisão, três autonomias, gestor generalista, áreas de
    impacto) → `contexto/trajetoria.md`, junto com a transcrição "Estratégia profissional".
  - Princípios (1)–(4) do Pillar 5 (método de trabalho com IA) → destino a decidir no encaixe:
    `meta/` ou hipótese.

## 4. Melhorias

- **Cosmovisão — a discussão aberta** identidade × paradigma da informação
  (`filosofia/cosmovisao/a-tese.md`). Destrava o recorte acadêmico (`estudo/academia/foco.md`).

## Decisões adiadas

- Incorporador × EPSO — são uma coisa só. Quando se separarem (por exemplo, opinião que
  não seja pelo EPSO), revisitar a voz da comunicação, o bloco de contexto, os nomes de pasta
  e o nome do repositório.
- Arquitetura de marca (EPSO como marca-mãe, construtora como submarca) — decidida quando a
  construtora migrar.
- Posição da visão dos produtos de software dentro das iniciativas — decidida quando o
  primeiro produto migrar.
- Carreira num lugar só — hoje dividida entre o repositório (público) e o documento externo
  da narrativa (privado, complementar). Revisitar quando houver solução para conteúdo privado.
