# Próximos passos — processo e método

O que falta no **como trabalhamos**: processos, método e estrutura do repositório. O que
falta em conteúdo vive na fila do [next-steps da raiz](../next-steps.md). Lista só de
próximos passos — item concluído sai da lista; o histórico vive no git.

- **Formalizar `meta/metodologia.md`** — o loop, o método do elo pendente `[[nome]]`, os
  níveis de confiança e a direção em aberto de agentes na pesquisa. Adiados dentro dele:
  como identificar o que precisa de link; critérios mais inteligentes de confiança. Insumo: a
  escada conceito → argumento → tese → síntese, em
  `fontes/documentos/2026-06-26-epso-paradigm-sobras.raw.md#mapa-do-sistema`.
- **Processo de registro de conversas** — o gêmeo do
  [processo de transcrições](processo-transcricoes.md) para
  `fontes/conversas/`: como acionar, o que o assistente pergunta, como nomeia. Questão
  aberta: a conversa sai na voz recomposta (ideia reescrita em 1ª pessoa) ou colada ao que
  o incorporador digitou. Prova de conceito: `fontes/conversas/2026-07-07-…`. Até lá, o
  passo 3 do [encerramento](processo-encerramento.md) é lembrete, não fluxo fechado. Regra
  já decidida: conversa registrada não recebe fala de outro dia — ideia nova vira conversa
  nova, com a data do dia; a antiga só muda se tiver informação errada, retirando a parte
  errada e referenciando a conversa nova. Até o processo nascer, as seções de conversa seguem a
  diretriz de seção das transcrições: uma seção, uma ideia, nome que diz a ideia
  ([processo](processo-transcricoes.md#passar-a-limpo-a-camada-limpa)). Insumo sem regra ainda: síntese
  do agente endossada pelo incorporador entrou marcada como "síntese do agente"
  (`fontes/conversas/2026-09-30-precisar-de-menos.md#compromisso-com-pessoas-nao-com-coisas`).
- **Biblioteca de referências** — guardar livros, artigos e textos de outras pessoas como
  base e referência, citando o autor. Em aberto: onde mora, como se cita e se o texto de outro
  autor entra no acervo sozinho ou só ao lado de fala do incorporador
  (`fontes/conversas/2026-10-03-ideia-nao-tem-dono.md#uma-biblioteca-de-referencias`).
  Direção, Estimado (média): `fontes/` deixa de ser só a voz do incorporador — passa a ser o
  material-fonte, com a voz dada pela subpasta; a referência de autor (ideias e conceitos de
  alguém, duradouros, usados por vários blocos, com trecho e autoria preservados) vai para
  `fontes/referencias/`, candidata a alvo do `[[nome]]`. A pesquisa operacional (como algo
  funciona, perecível, usada por um bloco) fica no bloco que a usa, com fonte e data em cada
  afirmação e data de revisão — primeiro caso: [linkedin.md](../instituicao/comunicacao/linkedin.md).
  A regra completa nasce com o primeiro livro ou artigo.
- **Semente guarda a ideia, não só o motivo** — o campo `sementes`
  ([cobertura](processo-transcricoes.md#cobertura)) registra por que a seção ficou sem casa.
  Para um argumento novo reencontrar o que foi dito antes, serviria um resumo da ideia numa
  linha, com o tema. Sem urgência: custa processamento por seção.
- **Semente parcial na cobertura** — semente declarada em seção já encaixada (ou por ideia em
  documento bruto) fica nos metadados, mas não aparece na lista de sementes: o
  [cobertura.py](cobertura.py) dá precedência ao encaixe. Ajuste: listar também essas
  sementes, marcadas como parciais. Casos: o resto de homo evolutis e as palavras soltas da
  lista de valores, no grupo do WhatsApp; as fases do comportamento da sociedade, no readme do
  livro.
- **Mapa do documento institucional × tipos de sessão** — o
  [mapa](estrutura/mapa-documento-institucional.md) sobe o processo de sessão para o nível EPSO;
  `fontes/conversas/2026-09-27-a-construtora-e-o-epso.md#tipos-de-sessao` diz que os tipos de
  sessão eram o modo de trabalhar da construtora (hoje na entrada dela, em
  `instituicao/iniciativas/`). Conferir se o mapa pede ajuste.
- **Colagem de conversa de chat** — o registro de documento bruto não prevê a conversa de grupo
  colada em partes: a colagem arrasta mensagens de outras pessoas para dentro das do
  incorporador, o "ler mais" do WhatsApp corta mensagem longa, parte vem sem carimbo de data e
  hora, e só o lado dele chega, sem as mensagens a que responde. Em aberto: se a mensagem de
  terceiro sai ou fica anonimizada como contexto; se o bruto pode ser uma seleção; como
  datar o que veio sem carimbo. Também em aberto, a pensar com mais calma: o que fazer com
  menção a figura pública, sobretudo acusação a pessoa nomeada — hoje saiu por decisão do
  incorporador, para não distrair da ideia, e a regra de anonimização não cobre o caso.
  Insumo: a `nota` de `fontes/documentos/2026-10-08-eleicao-no-whatsapp.raw.md`.
- **O comum sobe para `fontes/`** — com os três tipos à vista (transcrições, conversas e
  documentos), o que for comum (preservação, voz, rastreabilidade) sobe para um processo da
  mãe.
- **"Em aberto" dos arquivos de conteúdo → [elaborar](../elaborar.md)** — o conteúdo guarda o
  mínimo em aberto; as provocações ao incorporador vivem em `elaborar.md`. Já vale para
  `linguagem`, `ecocidades` e `inteligencia-potencializada`; falta aplicar em `precisao`,
  `quem-sou-eu`, `ancora` e `vetor`.
