# Próximos passos

A fila de **conteúdo** entre frentes, em ordem. Os passos internos de cada frente vivem em
`<frente>/next-steps.md`; o que falta em processo e método vive em
[docs/next-steps.md](docs/next-steps.md). Diretrizes de ordem no [CLAUDE.md](CLAUDE.md#encerramento-de-sessão).
Lista só de próximos passos — item concluído sai da lista; o histórico vive no git.

## 1. Fontes

Cada fonte avança por registrar → passar a limpo → encaixar. Registrar e passar a limpo não
dependem da estrutura e seguem a qualquer momento; **os encaixes esperam a reestruturação
(seção 2)**, para não mover o conteúdo duas vezes.

- **Transcrição 2026-09-22** (`fontes/transcricoes/2026-09-22-regeneracao-lastro-e-eco-cidades.md`)
  — passada a limpo; falta encaixar. Começa por linguagem em camadas + semiótica (fundir com
  `2026-06-26-…#abstrair-as-palavras`), área estruturada em `estudos/precisao.md` e
  `cosmovisao/quem-sou-eu.md`. As seções de carreira (lastro, mestrado) vão para o bloco de
  contexto.
- **Transcrição 2026-09-23** (`fontes/transcricoes/2026-09-23-producao-de-conteudo-eixos-portais-e-tematicas.md`)
  — passada a limpo; falta encaixar. Destinos prováveis: eixos, chamados e temáticas na linha
  editorial da comunicação; portais da plataforma nas iniciativas da instituição;
  `#portal-linguagem` funde com `2026-06-26-…#abstrair-as-palavras`;
  `#plataforma-e-autoridade` com o bloco de contexto.
- **Conversa 2026-07-07** (`fontes/conversas/`) — falta encaixar duas ideias: na migração,
  reaproveitar as ponderações e não o resultado; a iniciativa quatro como camada filosófica
  (o paper-agent é um produto dentro dela; modelo de conceitos, não de tokens).
- **Transcrição 2026-09-24** (`fontes/transcricoes/2026-09-24-atencao-corpo-linguagem-e-camadas.md`)
  — passada a limpo; falta encaixar. Destinos prováveis: atenção e corpo em
  `pensamento/cosmovisao/quem-sou-eu.md`; linguagem como tecnologia da informação e camadas
  de sentido em `pensamento/estudos/precisao.md`, fundindo com
  `2026-06-26-…#abstrair-as-palavras`.

Transcrições no formato antigo migram para as três camadas sob demanda, ao serem
encaixadas — não entram na fila por conta própria.

## 2. Reestruturação em blocos

O repositório guarda duas coisas: **a pessoa** (o incorporador) e **a instituição** (o EPSO,
Era Pra Ser Óbvio — a institucionalização das ideias e práticas, que pode andar sem a pessoa).
Estrutura-alvo:

```
fontes/        entrada: áudios, conversas (fica como está)
meta/          o repositório, os processos, o agente
— a pessoa —
filosofia/     cosmovisao/, hipoteses/ (ex-pensamento/estudos: âncora, vetor, precisão)
estudo/        academia/, leituras, experimentos de aprendizado
contexto/      trajetória, carreira, empresa atual, lastro, o momento
— a instituição —
instituicao/   nucleo/, iniciativas/ (construtora, ferramentas livres, plataforma),
               comunicacao/, financiamento/
```

Fronteiras decididas:

- **Estudo × filosofia/instituição** — estudo cuida da logística de aprender (o que ler, onde
  estudar, que experimento roda); o que se aprende é encaixado em filosofia ou na instituição.
- **Experimentos** — de produto ou solução, na instituição; de aprendizado, em estudo.
- **Núcleo** — é da instituição. A filosofia pessoal fica em `filosofia/`; o núcleo deriva
  dela e se sustenta sozinho.
- **Comunicação** — é do incorporador, mas nasce fundida ao EPSO; mora na instituição até
  as vozes se separarem.

Uma etapa por PR, em ordem de esforço. Cada etapa move com `git mv`, corrige as referências
e só termina quando a busca pelos caminhos antigos volta vazia.

1. **`estudo/`** — `academia/` entra como sub-bloco. Pequeno.
2. **`meta/`** — `docs/`, `processo-transcricoes.md`, `aprendizados-transcricao.md` e o
   índice de processos. `CLAUDE.md` e `README.md` ficam na raiz. Médio (muitas referências).
3. **`filosofia/`** — `pensamento/` muda; `estudos/` vira `hipoteses/`. Médio.
4. **`instituicao/`** — `nucleo/`, `pratica/`, `comunicacao/`, `funding/` entram. Médio.
5. **`contexto/`** — nasce; recebe a parte de carreira de `academia/jornada.md`. Médio
   (é conteúdo: pede leitura e decisão do incorporador).

## 3. Conteúdo

1. **Migração, sessão 2 — Academia.** `leituras` → `leituras-entrada.md`/`leituras-tese.md`;
   `mapeamento-academico` → `mapeamento.md`.
2. **Migração, sessão 3 — mop-up e aposentadoria.** Parciais menores; inventário todo `[x]`;
   então aposentar e deletar o `epso_paradigm`.
3. **Núcleo do EPSO** — propósito, valores, postura (do `epso_paradigm`, do Documento
   Institucional e da página "Base de pensamento" do site,
   https://www.erapraserobvio.com.br/quem-somos/base-de-pensamento, com o método de 4 etapas
   de `/plataforma`). A postura epistemológica compara-se antes com
   `pensamento/estudos/precisao.md`, que já tem a raiz "a realidade excede a verdade".
4. **Cosmovisão — a discussão aberta** identidade × paradigma da informação
   (`pensamento/cosmovisao/a-tese.md`). Destrava o recorte acadêmico (`academia/foco.md`).
5. **Prática** — construtora (institucional: princípios construtivos, acervo técnico,
   operacional) e EcoCondomínio (concepção e plano de execução), migrados do Drive. Registrar
   também as ferramentas livres já publicadas no site (Taquígrafo, Camadas da Linguagem).
6. **Funding** — parâmetros de interesse e maturidade; primeiro recorte de varredura (ver
   `funding/next-steps.md`).

## Decisões adiadas

- Nome do repositório — `epso-hub` guarda a pessoa e o EPSO. Renomear custa (GitHub,
  caminhos locais, worktrees, memória do agente); decidir depois da reestruturação.
- Voz da comunicação — pessoa e EPSO fundidos no começo; reorganizar quando surgir opinião
  que não seja pelo EPSO.
- Arquitetura de marca (EPSO como marca-mãe, construtora como submarca) — decidida quando a
  construtora migrar.
- Posição da visão dos produtos de software dentro das iniciativas — decidida quando o
  primeiro produto migrar.
