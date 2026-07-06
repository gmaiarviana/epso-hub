# Próximos passos

O que falta na migração para o epso-hub. Lista só de próximos passos — item concluído sai da lista; o histórico vive no git.

## Migração em andamento

O repositório nasce nesta sessão com esqueleto, README e CLAUDE. O conteúdo migra em sessões seguintes, uma frente por sessão.

Sessões planejadas:
- Núcleo — propósito, valores, postura epistemológica (do antigo epso_paradigm e do Documento Institucional).
- Cosmovisão e estudos — triagem do conteúdo filosófico entre o assentado (cosmovisao/) e as hipóteses em aberto (estudos/).
- Academia — estratégia de entrada acadêmica.
- Construtora — institucional (princípios construtivos, acervo técnico, operacional), migrado do Drive.
- EcoCondomínio — concepção e plano de execução, migrados do Drive.

## Onde paramos — cosmovisão + academia

Sessões de Cosmovisão e Academia iniciadas. Estado:

- **Feito:** criado `pensamento/cosmovisao/a-tese.md` — a tese como bifurcação, com dois centros candidatos (A: "extrair o quê / reunir tradições"; B: "quem sou eu"). Esboço aprovado.
- **Bloqueador (decisão do incorporador, offline):** escolher o centro da tese em `a-tese.md` (A, B ou outro). Destrava tudo abaixo.
- **Depois do centro:** construir a narrativa da tese em volta dele; as peças hoje soltas (identidade em camadas, une-e-supera, papel da tecnologia, aplicação prática) encontram lugar.
- **Academia (espera o centro):** `academia/foco.md` = o que estudar → passos táticos; depois `mapeamento`, `leituras`, `next-steps` e o README re-escopado ("meio, não fim").
- **A formalizar (independe do centro):** `docs/metodologia.md` — o loop (transcrição → destilação → refinamento), o método do elo pendente, níveis de confiança e a direção em aberto de agentes na pesquisa. Sub-itens adiados: como o sistema ajuda a identificar quais ideias precisam de link; critérios mais inteligentes de confiança.
- **Registrar em `CLAUDE.md`** as convenções decididas nesta sessão: sem frontmatter YAML (uso de Obsidian abortado); `[[nome]]` mantido como ponteiro simples ao dono da ideia, e um elo sem alvo é lacuna registrada, não erro.

## Fonte durante a migração

O repositório epso_paradigm segue vivo como fonte enquanto a migração acontece. Ele é aposentado e deletado quando todo o conteúdo necessário estiver migrado.

## Decisões adiadas

- Formato do roadmap e do estado por frente — definido pelos requisitos do motor de workflow, que mora em repositório próprio em construção.
- Arquitetura de marca (EPSO como marca-mãe, construtora como submarca) — decidida quando a construtora migrar.
- Posição da visão dos produtos de software dentro de pratica/ — decidida quando o primeiro produto migrar.
