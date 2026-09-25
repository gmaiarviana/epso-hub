# Critérios de onde o conteúdo mora

Estes critérios são hipóteses de trabalho, revisáveis quando um novo conteúdo os desafiar. A maioria do conteúdo cai no primeiro caso e dispensa deliberação.

Os níveis a que estes critérios se referem estão descritos em [niveis.md](niveis.md).

## Os blocos: a pessoa e a instituição

O repositório guarda duas coisas: **a pessoa** (o incorporador) e **a instituição** (o EPSO,
que pode andar sem a pessoa). O mapa de pastas é do [README](../../README.md). Fronteiras entre
os blocos:

- **Estudo × filosofia/instituição** — estudo cuida da logística de aprender (o que ler, onde
  estudar, que experimento roda); o que se aprende é encaixado em filosofia ou na instituição.
- **Experimentos** — de produto ou solução, na instituição; de aprendizado, em estudo.
- **Núcleo** — é da instituição. A filosofia pessoal fica em `filosofia/`; o núcleo deriva
  dela e se sustenta sozinho.
- **Comunicação** — é do incorporador, mas nasce fundida ao EPSO; mora na instituição até
  as vozes se separarem.
- **Contexto** — onde a pessoa está (carreira, empresa atual, lastro, momento). O que é
  logística de estudo fica em estudo; o contexto dá o porquê.

## Caso 1 — nasce num nível e fica

Conteúdo que pertence claramente a um nível permanece nele. Exemplos: princípios construtivos, estrutura operacional e acervo técnico ficam no nível iniciativa.

## Caso 2 — camadas de generalidade (herança)

Quando uma ideia existe em versão geral e versão especializada, a versão geral mora no nível mais alto e o nível de baixo a referencia, acrescentando o que é próprio dele. Exemplo: o propósito mora em `instituicao/nucleo/` (nível EPSO); a construtora referencia o propósito e acrescenta a identidade dela como construtora.

## Caso 3 — documento que mistura funções (partição por função)

Quando um documento reúne assuntos de funções diferentes, cada função vai para o nível onde governa. Exemplo: a metodologia se divide entre processo de sessão (nível EPSO) e modelagem financeira (nível iniciativa).
