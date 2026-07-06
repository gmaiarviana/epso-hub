# CLAUDE.md

Guia de trabalho do repositório epso-hub. Descreve o que este repositório é e como se trabalha nele.

## O que é o EPSO

O EPSO é um projeto de contribuição organizado por uma tese: trazer clareza para contribuir com a transformação da sociedade. O repositório se equilibra em dois lados: pensamento (fundamentar, dar clareza) e prática (fazer, provar na realidade). Os dois lados têm o mesmo peso e se alimentam.

## Idioma

Português, sempre.

## Organização e anti-redundância

Cada informação mora em um lugar só. Referências apontam para o dono da informação.

- **nucleo/** — propósito, valores e postura epistemológica do EPSO. É a régua herdada por todas as frentes. Toda frente aponta para cá em vez de repetir valores.
- **pensamento/cosmovisao/** — obra filosófica assentada, futura tese e livro.
- **pensamento/estudos/** — hipóteses em aberto e recortes pesquisáveis.
- **pratica/** — frentes concretas. A construtora entra aqui em migração futura, herdando identidade e método do topo e guardando o que é técnico-construtivo dela.
- **academia/** — alavanca a serviço do EPSO.
- **transcricoes/** — fonte bruta, datada, preservada sem alteração.

O mapa detalhado de cada frente entra no momento em que ela for migrada. Hoje o repositório está em migração inicial: núcleo, cosmovisão, estudos, prática e academia nascem como pastas e recebem conteúdo em sessões seguintes.

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

Cada sessão de planejamento termina com um prompt de edição pronto para o Claude Code e a atualização do next-steps.md da frente trabalhada.
