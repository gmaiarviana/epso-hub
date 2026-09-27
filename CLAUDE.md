# CLAUDE.md

Guia de trabalho do repositório epso-hub. Descreve o que este repositório é e como se trabalha nele.

## O que é o EPSO

O EPSO é um projeto de contribuição organizado por uma tese: trazer clareza para contribuir com a transformação da sociedade.

Descrição completa e mapa de pastas: [README.md](README.md) — a fonte. Não duplicar aqui.

## Idioma

Português, sempre.

## Formato dos arquivos

Arquivos de conhecimento em Markdown puro, sem frontmatter YAML — o título é o `# H1`. (Transcrições e documentos brutos em `fontes/documentos/` são exceção: mantêm o bloco de metadados descrito em [meta/processo-transcricoes.md](meta/processo-transcricoes.md).)

Referências ao dono de uma ideia usam a notação `[[nome]]`. Um `[[nome]]` cujo alvo ainda não existe não é erro — é uma lacuna registrada, um pensamento a mapear. O método de trabalho com esses elos pendentes fica em `meta/metodologia.md` (a formalizar).

## Organização e anti-redundância

Cada informação mora em um lugar só. Referências apontam para o dono da informação. O repositório guarda o estado atual: não conta como era antes nem o caminho até a decisão — a genealogia vive no git. Fica o que ajuda a agir: o sintoma ou mecanismo que faz reconhecer um problema, dados medidos que calibram uma regra e decisões que um critério exige registradas. Sai o relato: quem fez o quê, quando, como era antes. O mapa de pastas é do [README.md](README.md) — consultar lá, não repetir aqui.

O repositório se organiza em blocos por assunto; as fronteiras entre eles estão em [criterios.md](meta/estrutura/criterios.md). O mapa detalhado de cada frente entra no momento em que ela for migrada.

Os níveis de abrangência do conteúdo e os critérios de onde cada coisa mora estão em [meta/estrutura/](meta/estrutura/): [niveis.md](meta/estrutura/niveis.md) descreve os três níveis, [criterios.md](meta/estrutura/criterios.md) decide o destino e [mapa-documento-institucional.md](meta/estrutura/mapa-documento-institucional.md) traz um exemplo aplicado.

A estrutura do repositório está em evolução contínua; os critérios de organização são hipóteses de trabalho, revisáveis quando um novo conteúdo os desafiar.

## Régua de preservação de transcrições

Uma transcrição vive em três camadas, cada uma com sua régua:

- **Áudio-fonte** — a fala real, verdade última. Não versionado no repositório (referenciado por metadado `fonte-audio`).
- **Bruto** — a transcrição automática intocada, em `fontes/transcricoes/raw/…​.raw.md`. O conteúdo falado é preservado na íntegra: nada é alterado, resumido, corrigido ou reordenado. A única adição permitida ao bruto é um bloco de metadados. Não recebe seções — a estrutura vive na camada limpa.
- **Limpo** — cópia de trabalho em `fontes/transcricoes/…​.md`, derivada do bruto **sob validação do incorporador**. Resolve ambiguidades e erros de transcrição de áudio preservando a ideia original; nunca sobrescreve o bruto. Carrega os metadados, as seções `## nome` e as âncoras de rastreabilidade. O que não se resolve com segurança é marcado, não chutado: `[inaudível]` para trecho que não se recupera nem do texto nem da escuta pontual — o incorporador reouve só os poucos termos que sobram da escada de correções, localizados por áudio e posição; o resto aguarda re-transcrição futura com ferramenta melhor —, `[...]` para fragmento de fala abandonado. Marcar a incerteza é decisão validada, não pendência; é o ganho da camada sobre o bruto, que registra a falsa certeza com a mesma confiança do resto.

A camada limpa é **opcional** — o bruto sozinho já cumpre o dever de preservação. Nasce ao encaixar a transcrição na área de trabalho, ou antes disso quando se quer a versão legível do pensamento (pode ser gerada em lote). Não se gera para toda transcrição por obrigação.

Detalhe do fluxo em [meta/processo-transcricoes.md](meta/processo-transcricoes.md).

## Rastreabilidade

Quando um conteúdo encaixado deriva de uma transcrição, ele referencia a fonte no formato `arquivo#secao`: o caminho do arquivo **limpo** seguido do nome da seção de origem — é a camada limpa que carrega as seções e desambigua a fala. O limpo, por sua vez, aponta para o bruto (`fonte-bruta`) e para o áudio (`fonte-audio`). Assim toda afirmação encaixada aponta de volta para o trecho falado que a originou, com a cadeia até a verdade última preservada.

Conteúdo vindo de um repositório aposentado cita `<repositório>:<caminho>` (ex.: `epso_paradigm:universo-2-conteudo/sinteses/nucleo-da-tese.md`); o repositório segue consultável no GitHub.

## Índice de processos

Cada processo específico tem seu próprio documento, carregado quando o fluxo é acionado.

- Registro de transcrições → [meta/processo-transcricoes.md](meta/processo-transcricoes.md)
- Sessões Claude em paralelo (higiene de working copy) → [meta/sessoes-paralelas.md](meta/sessoes-paralelas.md)
- Encerramento de sessão ("vamos encerrar") → [meta/processo-encerramento.md](meta/processo-encerramento.md)
- Roadmap (regras dos next-steps) → [meta/roadmap.md](meta/roadmap.md)

## Postura

Pesquisar, analisar, estimar e apontar riscos. As decisões são do incorporador. Sinalizar premissas assumidas. Dizer "não sei" quando for o caso.

## Retomada de contexto

O incorporador não guarda de memória o que registrou em sessões anteriores. Ao retomar uma frente ou item da fila, o agente abre com um briefing antes de propor ação: onde a frente está, o que já foi dito sobre o tema (uma linha por objeto, com link para a fonte) e quais decisões a sessão vai pedir. Não assumir que o incorporador lembra do conteúdo de arquivos ou transcrições.

O briefing fala simples: cada ponto com um exemplo concreto e, quando for o caso, a pergunta que o incorporador precisa responder. Jargão técnico ou acadêmico só entra explicado.

## Níveis de confiança

Cada informação carrega um nível: Em aberto, Estimado (baixa), Estimado (média), Estimado (alta), Decidido. Uma informação regride de nível quando uma dependência dela muda.

## Como se trabalha: planejador e executor

O trabalho acontece em dois papéis.

- **Planejador** (Claude em conversa): discute, pesquisa, analisa, aponta riscos e produz o prompt de edição — arquivo alvo, mudança exata, trecho a inserir ou alterar.
- **Executor** (Claude Code): recebe o prompt e edita o arquivo direto no repositório.

O incorporador revisa entre os dois papéis, mantendo clareza do que muda antes de autorizar.

## Encerramento de sessão

Acionado pela frase **"vamos encerrar"**, o encerramento roda o ritual completo descrito em [meta/processo-encerramento.md](meta/processo-encerramento.md): (1) **retrospectiva de processo** — reler a sessão e checar se algum processo definido precisa evoluir; (2) atualizar next-steps e limpar o que ficou obsoleto; (3) lembrar de registrar ideias da conversa em `fontes/conversas/`, se houver; (4) finalizar no git. As mecânicas de next-steps ficam em [meta/roadmap.md](meta/roadmap.md).

## Fluxo git

O `main` tem branch protection: push direto é bloqueado, inclusive para admin. Toda mudança entra por branch → commit → push da branch → PR → merge pela interface. Commit local é livre; `git push origin main` falha por design.

Staging é sempre intencional: adicionar arquivos por caminho explícito, um a um. Nunca `git add .`, `git add -A` ou `git add -u` — evita arrastar mudança fora do escopo (outra frente, artefato, edição concorrente) para dentro do commit.

Branch nova nasce num worktree próprio, não por `switch` no diretório compartilhado — ver [meta/sessoes-paralelas.md](meta/sessoes-paralelas.md).

Antes de ler o repositório para planejar, confirmar que a base está no `origin/main` atual. O estado do git que chega no início da sessão é uma foto local, sem `fetch`; o hook de início de sessão ([.claude/settings.json](.claude/settings.json)) faz o `fetch` e avisa quantos commits o working copy está atrás. Se estiver atrás, atualizar — ou abrir worktree novo de `origin/main` — antes de ler.
