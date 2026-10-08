# LinkedIn

Como o feed do LinkedIn distribui conteúdo: o mecanismo do canal em que a comunicação começa
([canal](linha-editorial.md#canal)). Serve de base para a estratégia; as decisões de estratégia
moram na [linha editorial](linha-editorial.md).

Pesquisa de 2026-10-08. O LinkedIn não publica o peso de cada sinal: número exato de peso é
sempre estimativa externa. Cada afirmação leva o nível de confiança e a fonte com data. "Lido por
resumo" marca a fonte consultada por trechos e resumos de terceiros, sem acesso ao texto
integral. A seção [O que vale em 2026](#o-que-vale-em-2026) se revisa em 2027.

## Fontes

Oficiais e técnicas:

- LinkedIn Engineering, [Understanding feed dwell time](https://engineering.linkedin.com/blog/2020/understanding-feed-dwell-time) — 2020-05-12.
- Anúncio de menos isca de engajamento e enquetes, por [Search Engine Land](https://searchengineland.com/linkedin-feed-less-polls-engagement-bait-384986) — 2023.
- [An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking](https://arxiv.org/abs/2602.12354) (Feed SR), artigo da equipe do LinkedIn, CIKM '26 — 2026-02. Lido por resumo.
- LinkedIn Engineering, *Engineering the next generation of LinkedIn's Feed* — 2026-03-12. Lido por resumo ([saysomething](https://www.saysomething.app/blog/linkedin-feed-ai-engineering-2026)).
- LinkedIn News, [How LinkedIn Is Improving the Feed](https://news.linkedin.com/2026/ImprovingTheFeed), e [Social Media Today](https://www.socialmediatoday.com/news/linkedin-outlines-more-measures-to-combat-engagement-pods/812290/) sobre comentários automatizados — 2026. Lidos por resumo.

Estudos com dados:

- Richard van der Blom, [Algorithm Insights 2026](https://richardvanderblom.com/) — cerca de 1,3 milhão de posts. Pago; lido por resumo ([podcast](https://podcast.creatorscience.com/richard-van-der-blom-2/), [revisão crítica da Fast Growth](https://fast-growth.fr/en/white-paper/linkedin-algorithm-2026/)).
- Buffer, [frequência](https://buffer.com/resources/how-often-to-post-on-linkedin/) — mais de 2 milhões de posts, 2026.
- Ordinal, [links](https://www.tryordinal.com/blog/linkedin-link-penalty-study) (cerca de 900 mil posts) e [hashtags](https://www.tryordinal.com/blog/linkedin-hashtags) (270 mil posts) — 2025–2026.
- Metricool, [tendências 2026](https://metricool.com/linkedin-trends/) — cerca de 670 mil posts.

## Como a distribuição funciona

Princípios que valem há anos e tendem a continuar valendo.

- **Duas etapas.** A recuperação escolhe quais posts entram como candidatos para cada pessoa; a
  ordenação os ordena pela chance prevista de interação. Igual em 2020 e em 2026.
  **Nível:** Estimado (alta).
- **Tempo de leitura conta; rolar rápido conta contra.** Desde 2020 o LinkedIn modela o *skip*
  (ver o post por pouco tempo) como resultado negativo e reduz a pontuação na proporção dessa
  chance. O limite em segundos nunca foi publicado. **Nível:** Estimado (alta) — mecanismo;
  Em aberto — qualquer número.
- **Isca de engajamento é rebaixada.** Desde 2023, perde alcance o post que pede curtida,
  reação ou comentário com o fim exclusivo de ganhar alcance. Pedir um argumento de verdade fica
  fora disso; um pedido de "passar adiante" repetido como fórmula fica na zona cinza.
  **Nível:** Estimado (alta) — a regra; Estimado (média) — onde passa a linha.
- **A interação aparece para a rede de quem interage.** Quem comenta ou reage leva o post ao
  feed das próprias conexões ("fulano comentou"). **Nível:** Estimado (média).
- **Interação relevante vale mais que volume.** Comentário automatizado e grupos de troca de
  engajamento (pods) são detectados e perdem distribuição. **Nível:** Estimado (alta).
- **Conta pessoal rende mais que página de empresa** — engajamento de 2,6% contra 1,74%
  (Metricool). **Nível:** Estimado (alta).

## O que vale em 2026

Mudanças recentes que tendem a mudar de novo. Revisar em 2027.

- **O ranking lê o post junto com o perfil do autor e o histórico de quem lê** — um modelo de
  linguagem e de sequência (blog de engenharia, 2026-03-12). O Feed SR relata +2,10% de tempo
  gasto no feed. Na prática, título e histórico do perfil precisam combinar com o tema dos posts.
  **Nível:** Estimado (alta) — o modelo; Estimado (média) — a consequência para o perfil.
- **A distribuição passou da rede de conexões para o interesse pelo tema.** O LinkedIn diz que
  mostra posts "da sua rede ou de profissionais que você ainda não conhece". Constância de tema
  ajuda a ser encontrado fora da rede. **Nível:** Estimado (alta) — a direção. Os números de van
  der Blom (conexões de 70% para 10%, interesse de 5% para 50%, de 2024 a 2026): Estimado
  (baixa).
- **O alcance caiu.** As medições divergem: queda de 50% a 60% para criadores ativos (van der
  Blom); impressões −10% e engajamento +13,8% (Metricool). **Nível:** Estimado (média).
- **Repressão a automação e pods**, desde fevereiro e março de 2026: o comentário automatizado
  sai de "Mais relevantes" e fica restrito às conexões diretas de quem comentou.
  **Nível:** Estimado (alta).
- **Salvamentos e envios aparecem nas métricas** desde o fim de 2025. **Nível:** Estimado
  (média).

## Sinais

Não há peso oficial. O Feed SR agrupa curtida, comentário e compartilhamento num único objetivo e
trata o tempo longo de leitura como objetivo à parte (lido por resumo). **Nível:** Estimado
(média).

Ordem mais citada nos estudos: salvamento ≈ envio por mensagem > comentário com conteúdo >
repost com comentário > repost simples > curtida.

- Salvamento ≈ 5 curtidas ≈ 2 comentários (AuthoredUp, de 600 mil a 1 milhão de posts).
  **Nível:** Estimado (baixa).
- Repost com comentário contra repost simples: os dados se contradizem. **Nível:** Em aberto.
- Envio por mensagem: tratado como sinal forte por uns, sem impacto por outro. **Nível:**
  Estimado (baixa).
- O clique em "ver mais" como sinal próprio não aparece em documento oficial. **Nível:**
  Estimado (baixa).

## Formato

- **"Ver mais"** — o LinkedIn não publica o corte. Medições de terceiros: cerca de 140
  caracteres no celular e 210 no desktop; quebra de linha consome espaço, e o corte varia com
  aparelho e versão. Limite total do post: 3.000 caracteres. **Nível:** Estimado (média) — o
  corte; Decidido — o limite total.
- **Post curto** — um post que aparece inteiro não gera clique de expansão e tende a gerar menos
  tempo de leitura. Nenhum dado isola o efeito; a estimativa é desvantagem leve, compensada
  quando o texto faz a pessoa parar e reler. **Nível:** Estimado (baixa).
- **Hashtags** — Ordinal: +46% de taxa de engajamento e −66% de impressões (correlação).
  Neutras ou levemente negativas para alcance; mais de 10 prejudica. **Nível:** Estimado
  (média).
- **Marcar pessoas** — ajuda quando a pessoa marcada responde (LigoSocial: +35% de engajamento
  com uma marcação). Marcar quem não tem relação com o post é desaconselhado, sem dado sólido de
  penalidade. **Nível:** Estimado (baixa).
- **Link externo** — −18,8% de alcance mediano (van der Blom); −26,5% (Ordinal), quase neutro
  em perfil pessoal. O LinkedIn nunca confirmou a penalidade. **Nível:** Estimado (média) — que
  algum efeito existe.

## Ritmo e horário

- **Frequência** — o maior salto está entre 1 e de 2 a 5 posts por semana, sem teto nem punição
  por postar muito (Buffer); engajamento estável de 1 a 6 posts por semana (Ordinal). Intervalo
  irregular não mostra penalidade. **Nível:** Estimado (média).
- **Volta depois de parar** — depois de mais de um mês sem postar, os 4 ou 5 primeiros posts
  teriam cerca de 30% menos alcance (van der Blom). **Nível:** Estimado (baixa).
- **Primeiras horas** — o post começa num público de teste, e a interação inicial pesa. Cerca de
  50% das impressões chegam em 48 horas e cerca de 40% das interações no primeiro dia, em perfil
  pessoal (Metricool). Responder comentários ajuda: cada resposta reabre a conversa.
  **Nível:** Estimado (média).
- **Como uma conta esquenta** — dando ao modelo histórico: o perfil e as interações dizem de que
  tema a pessoa é, e gente desse tema reagindo confirma. Comentar com substância nos posts de
  outras pessoas do tema é o caminho mais citado e expõe o nome fora da rede. **Nível:**
  Estimado (média).
- **Horário no Brasil** — sem estudo específico do público brasileiro. Consenso das ferramentas
  em horário de Brasília: terça a quinta, das 8h às 10h, com janela secundária no almoço; fim de
  semana fraco. O Buffer de 2026 aponta o fim da tarde. O melhor horário é o que as métricas da
  própria conta mostrarem. **Nível:** Estimado (baixa).

## Mitos

| O que circula | O que os dados mostram |
|---|---|
| Comentário vale 15 curtidas | Sem fonte primária rastreável; o Feed SR agrupa as interações ativas. |
| Existe uma *golden hour* oficial de 60 minutos | O LinkedIn nunca definiu; o começo pesa, mas metade das impressões chega em até 48 horas. |
| O limite de *skip* é 3 segundos | O valor nunca foi publicado. |
| Esperar 18 horas entre posts, ou há punição | Recomendação de um estudo de 2.000 posts (van der Blom, 2023); sem penalidade oficial. |
| Link no post é punido por regra | Efeito observado e variável; quase neutro em perfil pessoal num dos estudos. |
| Mais hashtags, mais alcance | Os dados mostram menos impressões. |
| Pods e automação aceleram a conta | Desde 2026 são detectados e ficam restritos à rede direta. |
