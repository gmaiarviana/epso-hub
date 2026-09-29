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
   Ao fechar um item, o que ficou de fora volta nomeado por seção (ver
   [Fontes na fila](#fontes-na-fila)); o que fica só na fonte, sem ser pendência, é dispensado
   nos metadados dela.
3. **Trabalhos em aberto** — refatoração e migração em curso. Mudança estrutural grande
   (mover pastas, renomear blocos) entra aqui antes de começar, quebrada em etapas por esforço,
   uma por PR, as de baixo custo primeiro.
4. **Encaixar** — fontes prontas para encaixe: transcrições passadas a limpo; conversas e
   documentos, que já nascem legíveis.
5. **Backlog** — ações definidas e ainda não iniciadas, que não são melhoria do que já existe.
6. **Melhorias** — ajustes no que já existe que mexem em mais de um bloco. Melhoria que
   mexe num bloco só fica no next-steps dele; melhoria de processo ou método, em
   `meta/next-steps.md`.

Cada item de Foco diz a ação: o que se faz, com qual fonte e em qual arquivo de destino.

Rotinas de criação de conteúdo ficam fora da fila ativa até o incorporador retomá-las.

## Fontes na fila

O encaixe de uma fonte pode ser parcial; o registro do que falta, não. A entrada de uma fonte
na fila nomeia cada seção pela âncora (`#secao`) — nunca por intervalo ("de `#a` a `#b`"), "o
resto", "parte já encaixada" ou "conferir o que falta". Quando todas as seções vão juntas, o
item diz "arquivo inteiro". Documento bruto, sem seções, entra pelas ideias, nomeadas uma a uma.

Sintoma que a regra previne: a seção que some da fila atrás de uma forma vaga sem ter chegado
ao acervo — ninguém a procura, porque a fila diz que está coberta.

O estado de cada seção — encaixada, na fila, dispensada ou sem dono — está em
[fontes/cobertura.md](../fontes/cobertura.md), gerado por [cobertura.py](cobertura.py). A
fila guarda a decisão (prioridade e destino); a cobertura mostra o que falta. Seção sem dono
é alarme: entra na fila ou é dispensada ([processo](processo-transcricoes.md#cobertura)).

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
