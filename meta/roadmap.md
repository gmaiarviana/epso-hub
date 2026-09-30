# Roadmap

As regras dos arquivos `next-steps.md`: onde cada pendência mora, em que ordem a fila anda e
como se atualiza. Os `next-steps.md` são a aplicação destas regras — não as repetem.

## Onde cada pendência mora

Processual e pontual não se misturam:

- **`meta/next-steps.md`** — o que falta em **processo e método** (como trabalhamos). É onde
  cai proposta de retrospectiva adiada.
- **`next-steps.md` da raiz** — a **fila entre blocos**, em tiers. Não acumula os passos
  internos dos blocos.
- **`<bloco>/next-steps.md`** (ex.: `estudo/next-steps.md`) — os passos internos de cada bloco.
  Um por bloco de primeiro nível; sub-blocos viram seções dentro dele.

## A fila da raiz: seis tiers

Nesta ordem:

1. **Passar a limpo** — transcrições sem camada limpa. Todo áudio passa por registrar →
   passar a limpo → encaixar ([processo](processo-transcricoes.md)).
2. **Foco** — um ou mais objetivos declarados pelo incorporador, cada um numa frase seguida da
   lista, em ordem, do que o destrava. Sobe para cá o que vier de qualquer outro tier e sai do
   tier de origem; de uma fonte que sobe só em parte, o resto fica onde estava. O agente propõe
   a ordem; o incorporador decide. Alcançado o foco, o que sobrou volta ao tier de origem.
   Ao fechar um item, o que ficou de fora de uma fonte continua pendente na cobertura, e a nota
   que valha guardar volta ao Encaixar (ver [Fontes na fila](#fontes-na-fila)); o que fica só
   na fonte, sem ser pendência, é dispensado ou declarado latente nos metadados dela.
3. **Trabalhos em aberto** — refatoração e migração em curso. Mudança estrutural grande
   (mover pastas, renomear blocos) entra aqui antes de começar, quebrada em etapas por esforço,
   uma por PR, as de baixo custo primeiro.
4. **Encaixar** — notas sobre o encaixe de fontes: destino já decidido, fusão a checar,
   ressalva. O destino da nota não fecha a porta a um arquivo novo
   ([curadoria](estrutura/curadoria.md#curar-as-decisões)). O que falta encaixar não mora aqui, mora na cobertura (ver
   [Fontes na fila](#fontes-na-fila)).
5. **Backlog** — ações definidas e ainda não iniciadas, que não são melhoria do que já existe.
6. **Melhorias** — ajustes no que já existe que mexem em mais de um bloco. Melhoria que
   mexe num bloco só fica no next-steps dele; melhoria de processo ou método, em
   `meta/next-steps.md`.

Cada item de Foco diz a ação: o que se faz, com qual fonte e em qual arquivo de destino.

Rotinas de criação de conteúdo ficam fora da fila ativa até o incorporador retomá-las.

## Fontes na fila

O que falta encaixar está em [fontes/cobertura.md](../fontes/cobertura.md), gerado por
[cobertura.py](cobertura.py): toda seção de toda fonte aparece pendente até ser encaixada,
dispensada ou declarada latente, então nenhuma se perde por falta de registro na fila
([processo](processo-transcricoes.md#cobertura)).

A fila guarda o que a cobertura não sabe: a prioridade (Foco) e as notas (Encaixar). Uma fonte
só entra no Encaixar quando há nota que não se reconstrói em segundos. A exceção é o encaixe
parcial de uma seção: a cobertura a vê como encaixada, então a nota do que ficou de fora é
obrigatória.

Item de fila fala de seção pela âncora (`#secao`) — nunca por intervalo ("de `#a` a `#b`"),
"o resto" ou "conferir o que falta"; quando vão todas, diz "arquivo inteiro". Documento bruto,
sem seções, entra pelas ideias, nomeadas uma a uma.

Fonte de origem mista — a fala do incorporador junto de texto de terceiros, como a crítica
de uma IA — tem a voz marcada no item: a ideia que não é do incorporador leva
`(voz do guia)` ou o nome de quem fala. O encaixe dela vira provocação no
[elaborar](../elaborar.md), não texto na voz do incorporador.

## Como se atualiza

- Cada sessão de planejamento termina com um prompt de edição pronto para o Claude Code e a
  atualização do `next-steps.md` do(s) bloco(s) trabalhado(s).
- Ao encerrar, atualiza-se o next-steps do(s) bloco(s) tocado(s); a fila da raiz muda quando
  entra, sai ou muda de tier/ordem um item; `meta/next-steps.md` muda quando a sessão deixa
  pendência de processo.
- Quando a sessão muda um critério de onde algo mora, revisam-se os destinos da fila que
  dependem dele — o destino regride de nível como qualquer informação cuja dependência mudou.
- Antes de acrescentar um item ou regra: se se reconstrói em segundos quando for preciso, ou
  se o caso não vai se repetir, não se registra. Na dúvida, oferece-se em uma linha em vez de
  aplicar.
- O `next-steps.md` lista só o que falta. Item concluído sai da lista — não é riscado nem
  arquivado; o histórico vive no git. Tier ou seção sem itens não aparece.
