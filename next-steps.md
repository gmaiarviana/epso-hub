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

1. **Encaixe de 2026-09-22 ([PR #23](https://github.com/gmaiarviana/epso-hub/pull/23))** —
   feito sobre os caminhos antigos (`pensamento/estudos/`); adaptar à estrutura em blocos
   antes do merge.
2. **Migração, sessão 2 — Academia.** `leituras` → `estudo/academia/leituras-entrada.md` e
   `leituras-tese.md`; `mapeamento-academico` → `estudo/academia/mapeamento.md`.
3. **Migração, sessão 3 — mop-up e aposentadoria.** Parciais menores; inventário
   ([meta/estrutura/migracao-epso-paradigm.md](meta/estrutura/migracao-epso-paradigm.md)) todo
   `[x]`; então aposentar e deletar o `epso_paradigm`.
4. **Núcleo do EPSO** — propósito, valores, postura (do `epso_paradigm`, do Documento
   Institucional e da página "Base de pensamento" do site,
   https://www.erapraserobvio.com.br/quem-somos/base-de-pensamento, com o método de 4 etapas
   de `/plataforma`). A postura epistemológica compara-se antes com
   `filosofia/hipoteses/precisao.md`, que já tem a raiz "a realidade excede a verdade".
5. **Iniciativas** — construtora (institucional: princípios construtivos, acervo técnico,
   operacional) e EcoCondomínio (concepção e plano de execução), migrados do Drive. Registrar
   também as ferramentas livres já publicadas no site (Taquígrafo, Camadas da Linguagem).

## 3. Encaixar

- **Transcrição 2026-09-23** (`fontes/transcricoes/2026-09-23-producao-de-conteudo-eixos-portais-e-tematicas.md`)
  — destinos prováveis: eixos, chamados e temáticas na linha editorial da comunicação;
  portais da plataforma nas iniciativas; `#portal-linguagem` funde com
  `2026-06-26-…#abstrair-as-palavras`; `#eixo-mercado` e `#plataforma-e-autoridade` em
  `contexto/`.
- **Transcrição 2026-09-24** (`fontes/transcricoes/2026-09-24-atencao-corpo-linguagem-e-camadas.md`)
  — destinos prováveis: atenção e corpo em `filosofia/cosmovisao/quem-sou-eu.md`; linguagem
  como tecnologia da informação e camadas de sentido em `filosofia/hipoteses/`.
- **Conversa 2026-07-07** (`fontes/conversas/`) — duas ideias: na migração, reaproveitar as
  ponderações e não o resultado; a iniciativa quatro como camada filosófica (o paper-agent é
  um produto dentro dela; modelo de conceitos, não de tokens).

O PR #23 já encaixa parte das falas de 23/9 e 24/9 sobre linguagem; ao entrar, estes itens
se ajustam.

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
