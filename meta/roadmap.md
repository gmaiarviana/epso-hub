# Roadmap

As regras dos arquivos `next-steps.md`: onde cada pendência mora, em que ordem a fila anda e
como se atualiza. Os `next-steps.md` são a aplicação destas regras — não as repetem.

Regra provisória, até o motor de workflow definir o formato final do roadmap (ver
[next-steps.md](next-steps.md)).

## Onde cada pendência mora

Processual e pontual não se misturam:

- **`meta/next-steps.md`** — o que falta em **processo e método** (como trabalhamos). É onde
  cai proposta de retrospectiva adiada.
- **`next-steps.md` da raiz** — a **fila entre blocos**, em tiers. Não acumula os passos
  internos dos blocos.
- **`<bloco>/next-steps.md`** (ex.: `estudo/next-steps.md`) — os passos internos de cada bloco.
  Um por bloco de primeiro nível; sub-blocos viram seções dentro dele.

## A fila da raiz: quatro tiers

Nesta ordem:

1. **Passar a limpo** — transcrições sem camada limpa. Todo áudio passa por registrar →
   passar a limpo → encaixar ([processo](processo-transcricoes.md)).
2. **Trabalhos em aberto** — refatoração e migração em curso.
3. **Encaixar** — fontes já passadas a limpo que ainda não foram encaixadas.
4. **Melhorias** — só as que cruzam blocos. A exclusiva de um bloco vai para o next-steps
   dele; a de método, para `meta/next-steps.md`.

Rotinas de criação de conteúdo ficam fora da fila ativa até o incorporador retomá-las.

## Como se atualiza

- Cada sessão de planejamento termina com um prompt de edição pronto para o Claude Code e a
  atualização do `next-steps.md` do(s) bloco(s) trabalhado(s).
- Ao encerrar, atualiza-se o next-steps do(s) bloco(s) tocado(s); a fila da raiz muda quando
  entra, sai ou muda de tier/ordem um item; `meta/next-steps.md` muda quando a sessão deixa
  pendência de processo.
- O `next-steps.md` lista só o que falta. Item concluído sai da lista — não é riscado nem
  arquivado; o histórico vive no git.
