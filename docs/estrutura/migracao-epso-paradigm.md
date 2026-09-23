# Migração do epso_paradigm

Inventário vivo da migração do antigo repositório `epso_paradigm` para o epso-hub. As sessões da
migração estão na fila do [next-steps da raiz](../../next-steps.md). O `epso_paradigm`
segue vivo como fonte e só é **aposentado e deletado quando todo objeto necessário estiver migrado**
— este doc é o critério de "quando".

A destilação segue a [curadoria do acervo](curadoria.md): cada arquivo do paradigm é uma **caixa**;
abre-se objeto a objeto e decide-se **inserir · fundir · evoluir · decompor**, com **dedup por
âncora** (comparar por significado, não por palavra). Item migrado marca-se `[x]` com o destino real;
o histórico fino vive no git.

## Estado da fonte

O `epso_paradigm` está 100% sincronizado com `origin/main` (`git@github.com:gmaiarviana/epso_paradigm.git`)
— o conteúdo bruto sobrevive no GitHub mesmo após deletar a pasta local. As transcrições de 2026-06-26,
fonte dos conceitos, já vivem em `fontes/transcricoes/`. O que **não** está migrado é o trabalho *destilado*:
a camada crítica `problemas-abertos` e o legwork acadêmico.

## Inventário — 19 arquivos

Coberto = substância já vive no hub. Parcial = ideia central migrada, pontas cortadas. Faltando =
não existe como pensamento processado no hub.

### Universo 1 — jornada

- [x] `foco-academico.md` → **coberto**: `academia/foco.md`, `academia/jornada.md`, `pensamento/cosmovisao/a-tese.md`.
- [ ] `frentes/leituras.md` → **faltando** · destino `academia/leituras-entrada.md` + `leituras-tese.md` (nomeados, vazios) · **inserir**.
- [ ] `frentes/mapeamento-academico.md` → **faltando** · destino `academia/mapeamento.md` (nomeado, vazio) · **inserir**.
- [ ] `frentes/posicionamento.md` → **parcial** · destino `academia/jornada.md` · **evoluir** (recuperar "forças que você traz" + item "virar pitch").
- [ ] `painel-de-controle.md` → **parcial** · destino next-steps das frentes · **fundir** (backlog "sinais ainda por registrar").

### Universo 2 — conceitos

- [ ] `conceitos/atencao.md` → **parcial** · destino `cosmovisao/a-tese.md` · **evoluir** (atenção como único locus de controle).
- [ ] `conceitos/observador.md` → **parcial** · destino `cosmovisao/a-tese.md` · **evoluir** (testemunha determinística — significado difere do "observador situado" já no hub; cuidar na fusão).
- [ ] `conceitos/evolucao-com-intencao.md` → **faltando** · destino triagem `estudos/` ↔ `cosmovisao/` · **inserir**.
- [ ] `conceitos/fluir.md` → **faltando** · destino triagem `estudos/` ↔ `cosmovisao/` · **inserir**.
- [ ] `conceitos/pulsar-fractal.md` → **faltando** · destino triagem `estudos/` ↔ `cosmovisao/` · **inserir** (cosmologia onda/pulso/mandala).

### Universo 2 — problemas abertos

Camada crítica. Os seis problemas epistemológicos eram galhos de um só argumento — "a realidade
excede a verdade; as leituras são mais ou menos precisas" — e foram respondidos pelo incorporador
na sessão 1 (2026-09-23). Viraram um arquivo só, em vez de seis.

- [x] `problemas-abertos/criterio-de-falsidade.md` → **fundido** em `estudos/precisao.md` (a intenção separa a leitura parcial da distorção; avaliar a intenção de fora fica em aberto).
- [x] `problemas-abertos/regua-de-critica.md` → **fundido** em `estudos/precisao.md` (a régua são os eixos de precisão; a medição é uma página do livro).
- [x] `problemas-abertos/tradicao-epistemologica.md` → **fundido** em `estudos/precisao.md#em-aberto` (Popper: referência, não prisão).
- [x] `problemas-abertos/paradigma-auto-imunizante.md` → **fundido** em `estudos/precisao.md` (comunicar na camada que o outro alcança).
- [x] `problemas-abertos/ponte-fisica-quantica.md` → **fundido** em `estudos/precisao.md#em-aberto` (paradigma a elaborar; cuidado com o homônimo "observador").
- [x] `problemas-abertos/no-da-medicao.md` → **fundido** em `estudos/precisao.md` (a medição acompanha, não fundamenta). Destino mudou de `ancora.md` para `precisao.md`.
- [x] `problemas-abertos/mestrado-pernas-proprias.md` → **evoluído** em `academia/jornada.md`.

### Universo 2 — sínteses

- [ ] `sinteses/nucleo-da-tese.md` → **parcial** · destino `cosmovisao/a-tese.md`, `estudos/vetor.md` · **evoluir**. A consequência da medição e Paulo Freire já entraram em `estudos/precisao.md` (2026-09-23). Falta: o choque de vetores como sinal de algo não dito (princípio de leitura) e as "sete camadas" de uma meditação anterior (cruzamento dos dois eixos da identidade).

### Aposentado

- [x] `mapa-do-sistema.md` → **não migra**: a ontologia (3 compartimentos; conceitos→argumentos→teses→sínteses) foi substituída pela estrutura própria do hub ([niveis.md](niveis.md), [criterios.md](criterios.md)). Função coberta, forma abandonada por decisão.

## Plano em 3 sessões

Uma frente por sessão, maior perda primeiro.

1. **Pensamento** (estudos + cosmovisão) — a camada `problemas-abertos` + triagem dos conceitos entre
   assentado (`cosmovisao/`) e hipótese em aberto (`estudos/`). Maior perda, mais cara de reconstruir.
2. **Academia** (campo) — `leituras` → `leituras-entrada.md`/`leituras-tese.md`; `mapeamento-academico` → `mapeamento.md`.
3. **Mop-up + aposentadoria** — parciais menores (`posicionamento`, `painel-de-controle`) nos next-steps;
   conferir o inventário todo `[x]`; então retirar e deletar o `epso_paradigm`.

## Critério de deleção

O `epso_paradigm` só é deletado quando **todo item deste inventário estiver `[x]`** (migrado ou
aposentado por decisão registrada). Até lá, ele permanece como fonte de leitura.

## Evolução do planejamento

- **2026-09-22** — inventário criado a partir da varredura de cobertura dos 19 arquivos. Diagnóstico:
  1 coberto, 7 parciais, 11 faltando; a camada `problemas-abertos` (6/7) e o legwork acadêmico não
  foram carregados no "primeiro corte" da migração. Plano de 3 sessões definido.
- **2026-09-23** — sessão 1, parte 1: a camada `problemas-abertos` migrada (6 fundidos em
  `estudos/precisao.md`, 1 evoluído em `academia/jornada.md`). A raiz "a realidade excede a
  verdade" ganhou dono em `precisao.md`. Próximo: os cinco conceitos.
