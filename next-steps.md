# Próximos passos

O que falta na migração para o epso-hub, no nível EPSO. Cada frente tem o seu próprio next-steps em `<frente>/next-steps.md`. Lista só de próximos passos — item concluído sai da lista; o histórico vive no git.

## Migração em andamento

O repositório nasce nesta sessão com esqueleto, README e CLAUDE. O conteúdo migra em sessões seguintes, uma frente por sessão.

Sessões planejadas:
- Núcleo — propósito, valores, postura epistemológica (do antigo epso_paradigm e do Documento Institucional).
- Cosmovisão e estudos — triagem do conteúdo filosófico entre o assentado (cosmovisao/) e as hipóteses em aberto (estudos/).
- Academia — estratégia de entrada acadêmica.
- Construtora — institucional (princípios construtivos, acervo técnico, operacional), migrado do Drive.
- EcoCondomínio — concepção e plano de execução, migrados do Drive.

## Frentes em curso

- **Cosmovisão:** centro da tese escolhido — a identidade ("quem sou eu"). Falta construir a narrativa em torno dele e resolver a discussão aberta identidade × paradigma da informação (ver `pensamento/cosmovisao/a-tese.md`).
- **Academia:** ver `academia/next-steps.md`.
- **Funding (nova frente):** scouting de financiamento das iniciativas — ver `funding/next-steps.md`.
- **Transcrições:** modelo de três camadas (bruto em `raw/` · limpo na raiz · áudio não versionado) introduzido e testado na menor transcrição (`2026-06-26-modelos-eficientes…`). Falta migrar retroativamente os demais brutos do formato antigo — sob demanda, ao destilar cada um.
- **Fontes (nova frente de metodologia):** consolidar a camada de dados-fonte — `fontes/` nasce como mãe de `destilados/`; a migração de `transcricoes/` para baixo dela e o processo de encerramento de chat ficam para sessão dedicada. Ver `fontes/next-steps.md`.
- **EPSO:** formalizar `docs/metodologia.md` (loop, método do elo pendente, níveis de confiança, direção em aberto de agentes na pesquisa; adiados: como identificar o que precisa de link, critérios mais inteligentes de confiança).

## Fonte durante a migração

O repositório epso_paradigm segue vivo como fonte enquanto a migração acontece. Ele é aposentado e deletado quando todo o conteúdo necessário estiver migrado.

## Decisões adiadas

- Formato do roadmap e do estado por frente — definido pelos requisitos do motor de workflow, que mora em repositório próprio em construção.
- Arquitetura de marca (EPSO como marca-mãe, construtora como submarca) — decidida quando a construtora migrar.
- Posição da visão dos produtos de software dentro de pratica/ — decidida quando o primeiro produto migrar.
