# CLAUDE.md

Guia de trabalho do repositório epso-hub. Descreve o que este repositório é e como se trabalha nele.

## O que é o EPSO

O EPSO é um projeto de contribuição organizado por uma tese: trazer clareza para contribuir com a transformação da sociedade.

Descrição completa e mapa de pastas: [README.md](README.md) — a fonte. Não duplicar aqui.

## Idioma

Português, sempre.

## Formato dos arquivos

Arquivos de conhecimento em Markdown puro, sem frontmatter YAML — o título é o `# H1`. (Transcrições são exceção: mantêm o bloco de metadados descrito em [transcricoes/PROCESSO.md](transcricoes/PROCESSO.md).)

Referências ao dono de uma ideia usam a notação `[[nome]]`. Um `[[nome]]` cujo alvo ainda não existe não é erro — é uma lacuna registrada, um pensamento a mapear. O método de trabalho com esses elos pendentes fica em `docs/metodologia.md` (a formalizar).

## Organização e anti-redundância

Cada informação mora em um lugar só. Referências apontam para o dono da informação. O mapa de pastas é do [README.md](README.md) — consultar lá, não repetir aqui.

Hoje o repositório está em migração inicial: núcleo, cosmovisão, estudos, prática e academia nascem como pastas e recebem conteúdo em sessões seguintes. O mapa detalhado de cada frente entra no momento em que ela for migrada.

Os níveis de abrangência do conteúdo e os critérios de onde cada coisa mora estão em [docs/estrutura/](docs/estrutura/): [niveis.md](docs/estrutura/niveis.md) descreve os três níveis, [criterios.md](docs/estrutura/criterios.md) decide o destino e [mapa-documento-institucional.md](docs/estrutura/mapa-documento-institucional.md) traz um exemplo aplicado.

A estrutura do repositório está em evolução contínua; os critérios de organização são hipóteses de trabalho, revisáveis quando um novo conteúdo os desafiar.

## Régua de preservação de transcrições

Transcrições brutas têm o conteúdo falado preservado na íntegra — nada é alterado, resumido, corrigido ou reordenado. As únicas adições permitidas ao bruto são metadados e marcadores de seção.

## Rastreabilidade

Quando um conteúdo processado deriva de uma transcrição, ele referencia a fonte no formato `arquivo#secao`: o caminho do arquivo bruto seguido do nome da seção de origem. Assim toda afirmação destilada aponta de volta para o trecho falado que a originou.

## Índice de processos

Cada processo específico tem seu próprio documento, carregado quando o fluxo é acionado.

- Registro de transcrições → [transcricoes/PROCESSO.md](transcricoes/PROCESSO.md)

## Postura

Pesquisar, analisar, estimar e apontar riscos. As decisões são do incorporador. Sinalizar premissas assumidas. Dizer "não sei" quando for o caso.

## Níveis de confiança

Cada informação carrega um nível: Em aberto, Estimado (baixa), Estimado (média), Estimado (alta), Decidido. Uma informação regride de nível quando uma dependência dela muda.

## Como se trabalha: planejador e executor

O trabalho acontece em dois papéis.

- **Planejador** (Claude em conversa): discute, pesquisa, analisa, aponta riscos e produz o prompt de edição — arquivo alvo, mudança exata, trecho a inserir ou alterar.
- **Executor** (Claude Code): recebe o prompt e edita o arquivo direto no repositório.

O incorporador revisa entre os dois papéis, mantendo clareza do que muda antes de autorizar.

## Encerramento de sessão

Cada sessão de planejamento termina com um prompt de edição pronto para o Claude Code e a atualização do `next-steps.md` da(s) frente(s) trabalhada(s).

Cada frente tem o seu próprio `next-steps.md`, em `<frente>/next-steps.md` (ex.: `academia/next-steps.md`). O `next-steps.md` da raiz é de nível EPSO: rastreia a migração entre frentes e aponta para o de cada uma — não acumula os passos internos delas. Ao encerrar, atualiza-se o next-steps da(s) frente(s) tocada(s); o da raiz só muda quando o estado entre frentes muda.

O `next-steps.md` lista só o que falta. Item concluído sai da lista — não é riscado nem arquivado; o histórico vive no git. Regra provisória, até o motor de workflow definir o formato final do roadmap (ver `next-steps.md`, Decisões adiadas).
