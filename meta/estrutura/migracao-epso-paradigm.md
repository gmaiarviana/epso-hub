# Migração do epso_paradigm

Inventário vivo da migração do repositório `epso_paradigm` para o epso-hub. As sessões da
migração estão na fila do [next-steps da raiz](../../next-steps.md). O `epso_paradigm`
segue vivo como fonte até o fim da migração — este doc é o critério de "quando".

O critério de "o quê": guarda-se o que é **válido e valioso**; o que se reconstrói com a
provocação e o contexto certos pode ficar para trás. Migrado, o conteúdo passa a morar no hub e
não cita a origem.

O encaixe segue a [curadoria do acervo](curadoria.md): cada arquivo do paradigm é uma **caixa**;
abre-se objeto a objeto e decide-se **inserir · fundir · evoluir · decompor**, com **dedup por
âncora** (comparar por significado, não por palavra). Item migrado marca-se `[x]` com o destino real;
o histórico fino vive no git.

## Estado da fonte

O `epso_paradigm` está 100% sincronizado com `origin/main` (`git@github.com:gmaiarviana/epso_paradigm.git`).
As transcrições de 2026-06-26, fonte dos conceitos, já vivem em `fontes/transcricoes/`. Falta rever
os três parciais abaixo.

## Inventário — 19 arquivos

Coberto = substância já vive no hub. Parcial = ideia central migrada, pontas cortadas. Faltando =
não existe como pensamento encaixado no hub.

### Universo 1 — jornada

- [x] `foco-academico.md` → **coberto**: `estudo/academia/foco.md`, `estudo/academia/jornada.md`, `filosofia/cosmovisao/a-tese.md`.
- [x] `frentes/leituras.md` e `frentes/mapeamento-academico.md` → **migrados pelas ponderações** (conversa `fontes/conversas/2026-09-27-as-duas-teses-e-a-migracao.md`): o mestrado como estudo de uma tese vizinha em `estudo/academia/jornada.md`; medir se duas palavras apontam para a mesma ideia em `estudo/academia/foco.md`; o modelo científico, Boaventura e os nomes acadêmicos em `hipoteses/precisao.md`; a separação das duas teses no next-steps da raiz. O resto — a aula de epistemologia, as frentes A/B, instituições, orientadores, termos de busca — se reconstrói com varredura; as frentes voltam pela provocação "teses vizinhas" do [elaborar](../../elaborar.md#academia).
- [ ] `frentes/posicionamento.md` → **parcial** · destino `estudo/academia/jornada.md` · **evoluir** (recuperar "forças que você traz" + item "virar pitch").
- [ ] `painel-de-controle.md` → **parcial** · destino next-steps das frentes · **fundir** (backlog "sinais ainda por registrar").

### Universo 2 — conceitos

Os cinco conceitos são uma corrente só — a resposta a "quem sou eu?" — e moram num arquivo
em `cosmovisao/`.

- [x] `conceitos/atencao.md` → **evoluído** em `cosmovisao/quem-sou-eu.md#sou-minha-atenção`.
- [x] `conceitos/observador.md` → **evoluído** em `cosmovisao/quem-sou-eu.md#sou-o-observador`. A testemunha e o "observador situado" são o mesmo conceito: não se controla o filme, mas o assento, a companhia e a mentalidade mudam a experiência.
- [x] `conceitos/evolucao-com-intencao.md` → **inserido** em `cosmovisao/quem-sou-eu.md#evoluir-com-intenção`.
- [x] `conceitos/fluir.md` → **inserido** em `cosmovisao/quem-sou-eu.md#fluir`.
- [x] `conceitos/pulsar-fractal.md` → **inserido** em `cosmovisao/quem-sou-eu.md#tudo-pulsa`.

### Universo 2 — problemas abertos

Camada crítica. Os seis problemas epistemológicos são galhos de um só argumento — "a realidade
excede a verdade; as leituras são mais ou menos precisas" — respondidos pelo incorporador e
reunidos num arquivo só.

- [x] `problemas-abertos/criterio-de-falsidade.md` → **fundido** em `hipoteses/precisao.md` (a intenção separa a leitura parcial da distorção; avaliar a intenção de fora fica em aberto).
- [x] `problemas-abertos/regua-de-critica.md` → **fundido** em `hipoteses/precisao.md` (a régua são os eixos de precisão; a medição é uma página do livro).
- [x] `problemas-abertos/tradicao-epistemologica.md` → **fundido** em `hipoteses/precisao.md#em-aberto` (Popper: referência, não prisão).
- [x] `problemas-abertos/paradigma-auto-imunizante.md` → **fundido** em `hipoteses/precisao.md` (a resposta) e `hipoteses/linguagem.md` (comunicar na camada que o outro alcança).
- [x] `problemas-abertos/ponte-fisica-quantica.md` → **fundido** em `hipoteses/precisao.md#em-aberto` (paradigma a elaborar; cuidado com o homônimo "observador").
- [x] `problemas-abertos/no-da-medicao.md` → **fundido** em `hipoteses/precisao.md` (a medição acompanha, não fundamenta).
- [x] `problemas-abertos/mestrado-pernas-proprias.md` → **evoluído** em `estudo/academia/jornada.md`.

### Universo 2 — sínteses

- [ ] `sinteses/nucleo-da-tese.md` → **parcial** · destino `cosmovisao/a-tese.md`, `hipoteses/vetor.md` · **evoluir**. A consequência da medição está em `hipoteses/precisao.md`; Paulo Freire, em `hipoteses/linguagem.md`. Falta: o choque de vetores como sinal de algo não dito (princípio de leitura) e as "sete camadas" de uma meditação anterior (cruzamento dos dois eixos da identidade).

### Aposentado

- [x] `mapa-do-sistema.md` → **não migra**: a ontologia (3 compartimentos; conceitos→argumentos→teses→sínteses) tem a função coberta pela estrutura própria do hub ([niveis.md](niveis.md), [criterios.md](criterios.md)); a forma não migra, por decisão.

## Critério de deleção

Em duas etapas, na fila do [next-steps da raiz](../../next-steps.md): primeiro a **poda** — remover
do `epso_paradigm` os arquivos `[x]`; depois, em chat novo, o **olhar novo** sobre o que sobrou.
Com todo item `[x]` (migrado ou deixado para trás por decisão), deletam-se o `epso_paradigm`,
este inventário e os itens da fila.
