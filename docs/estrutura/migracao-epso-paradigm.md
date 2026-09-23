# Migração do epso_paradigm

Inventário vivo da migração do antigo repositório `epso_paradigm` para o epso-hub. As sessões da
migração estão na fila do [next-steps da raiz](../../next-steps.md). O `epso_paradigm`
segue vivo como fonte e só é **aposentado e deletado quando todo objeto necessário estiver migrado**
— este doc é o critério de "quando".

O encaixe segue a [curadoria do acervo](curadoria.md): cada arquivo do paradigm é uma **caixa**;
abre-se objeto a objeto e decide-se **inserir · fundir · evoluir · decompor**, com **dedup por
âncora** (comparar por significado, não por palavra). Item migrado marca-se `[x]` com o destino real;
o histórico fino vive no git.

## Estado da fonte

O `epso_paradigm` está 100% sincronizado com `origin/main` (`git@github.com:gmaiarviana/epso_paradigm.git`)
— o conteúdo bruto sobrevive no GitHub mesmo após deletar a pasta local. As transcrições de 2026-06-26,
fonte dos conceitos, já vivem em `fontes/transcricoes/`. O que **não** está migrado é o trabalho *encaixado*:
a camada crítica `problemas-abertos` e o legwork acadêmico.

## Inventário — 19 arquivos

Coberto = substância já vive no hub. Parcial = ideia central migrada, pontas cortadas. Faltando =
não existe como pensamento encaixado no hub.

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

Camada crítica — a maior perda. Nenhum destes existe no hub; destino natural `pensamento/estudos/`.

- [ ] `problemas-abertos/criterio-de-falsidade.md` → **faltando** · **inserir**.
- [ ] `problemas-abertos/regua-de-critica.md` → **faltando** · **inserir** (que régua substitui a crítica materialista).
- [ ] `problemas-abertos/tradicao-epistemologica.md` → **faltando** · **inserir** (Popper / qual escola te julga).
- [ ] `problemas-abertos/paradigma-auto-imunizante.md` → **faltando** · **inserir**.
- [ ] `problemas-abertos/ponte-fisica-quantica.md` → **faltando** · **inserir** (alerta contra a ponte com o observador quântico).
- [ ] `problemas-abertos/no-da-medicao.md` → **faltando** · destino `estudos/ancora.md` · **evoluir** (consequência: medição relativa perde poder de provar).
- [ ] `problemas-abertos/mestrado-pernas-proprias.md` → **parcial** · destino `academia/jornada.md` · **evoluir** (recuperar o corte "defensável por quem nunca ouviu a filosofia").

### Universo 2 — sínteses

- [ ] `sinteses/nucleo-da-tese.md` → **parcial** · destino `cosmovisao/a-tese.md`, `estudos/ancora.md`, `estudos/vetor.md` · **evoluir** (recuperar a consequência da medição e Paulo Freire como base reconhecida).

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
