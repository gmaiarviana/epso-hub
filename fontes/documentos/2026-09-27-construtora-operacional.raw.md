---
data: 2026-09-27
tipo: documento-bruto
titulo: Construtora — Operacional (Habilitação, Custos e Equipe, Marca, Roadmap, Infraestrutura)
idioma: português
fonte-original: documento "Construtora - Operacional" do Google Drive do incorporador, fora do repositório
nota: >-
  Colado no chat pelo incorporador em 2026-09-27, aba por aba. Escrito em
  sessões com Claude e validado pelo incorporador; data original desconhecida,
  anterior ao repositório. A formatação se perdeu em parte na colagem (a tabela
  de fases do roadmap chegou achatada, uma célula por linha); o texto está como
  chegou, sem correção. Os títulos `##` separam as abas e foram acrescentados
  na colagem; a aba de infraestrutura já veio em Markdown e mantém os próprios
  títulos, rebaixados um nível.
---

## Aba: Habilitação e Estrutura

Habilitação e Estrutura
A EPSO (CNPJ 58.272.456/0001-90, CNAE 7319003 — marketing direto) já existe e atende a fase de experimentação.
Para incorporação imobiliária: CNPJ separado (provavelmente SPE com patrimônio de afetação). Abertura apenas quando uma ação concreta exigir (contrato de terreno, captação formal, registro de incorporação). Validar com advogado e contador.
A definir: tipo societário da construtora, CNAE, regime tributário, relação jurídica entre EPSO e construtora/SPE.

## Aba: Custos e Equipe

Custos e Equipe
Custos fixos da EPSO (já existentes)
A levantar: quanto a EPSO custa por mês hoje (contabilidade, domínio, ferramentas). Serve como baseline.
Fase de experimentação
Orçamento da F1: ver Construtora - Operacional, Aba: Roadmap, tabela de fases. Custo provável abaixo do orçamento: domínio já existe, landing page e identidade visual básica feitas internamente. O orçamento funciona mais como reserva do que plano de gasto. 
Equipe por fase
A definir. Estrutura de referência a construir conforme as fases do projeto avançam. Premissa: o mais enxuto possível, freelancer/PJ pontual, escalar só quando houver demanda concreta.
Remuneração do incorporador
Custo do projeto, absorvido a partir do momento em que o incorporador se dedica integralmente. O fluxo de caixa do projeto (EcoCondomínio - Plano de Execução, Aba: Fluxo de Caixa) identifica o ponto saudável para esse gatilho, considerando necessidade de presença e capacidade financeira do projeto.

## Aba: Marca e Posicionamento

Marca e Posicionamento
Arquitetura
EPSO — marca guarda-chuva. Visão, comunidade, conhecimento aberto.
Construtora [nome em aberto] — braço de execução. Marca própria, vive dentro do EPSO.
Projetos — cada projeto pode ter identidade própria, vinculada à construtora.
Presença digital
Domínio: erapraserobvio.com.br (já existe). Construtora começa como seção dentro do site do EPSO. Domínio próprio quando/se fizer sentido.
Itens a desenvolver
Nome da construtora
Posicionamento e linguagem
Identidade visual básica (feita pelo incorporador inicialmente)
Tom de voz
Narrativa EPSO ↔ construtora
Canais e presença
Tudo em aberto. Será desenvolvido quando houver decisão de seguir e clareza suficiente.

## Aba: Roadmap

Roadmap da Construtora
Fases nomeadas
Fase
Nome
Descrição
Custo estimado
F0 — Concepção
Concepção
Produto, viabilidade, documentação. Onde estamos agora.
Tempo
F1 — Experimentação
Experimentação
Marca básica, landing page, presença orgânica, conexão com pessoas. Ainda usando EPSO como PJ.
Até R$ 5k (provavelmente menos)
F2 — Busca de terreno
Busca de terreno 
Busca, avaliação, due diligence. 
Deslocamentos, análises 
F3 — Adaptação 
Adaptação 
Concepção refinada para o terreno específico. Números reais. Material para investidor. 
Tempo + eventuais consultorias 
F4 — Capitalização
Capitalização
Levantar capital (investidor, banco, parceiros). Pode começar em paralelo com F3 se o material estiver pronto.
Tempo + jurídico
F5 — Formalização
Formalização
Abertura de CNPJ da construtora/SPE, contratos, compra de terreno.
Jurídico, contador, terreno
F6 — Projetos
Projetos técnicos
Arquitetônico, estrutural, licenciamento.
~R$ 200k (ref. central — ver EcoCondomínio - Concepção, Aba: Especificações Técnicas, §12) 
F7 — Vendas
Comercialização
Venda das unidades.
Marketing do projeto
F8 — Obra
Construção
Infraestrutura e unidades.
Custo do projeto

Notas:
F0 e F1 podem se sobrepor.
F2 só começa com concepção madura (M1–M4 em boa confiança).
F3 e F4 podem se sobrepor parcialmente.
F5 é gatilho para compromissos financeiros formais.
Remuneração integral do incorporador: a definir em qual fase entra. Recomendação será derivada do fluxo de caixa.

## Aba: Infraestrutura e Ferramentas

### Infraestrutura e Ferramentas

Recursos necessários para operar a empresa. Cada item tem ciclo de vida próprio (necessidade → pesquisa → gatilho → aquisição). Custos de aquisição (CAPEX) são amortizados ao longo da vida útil. Custos recorrentes (OPEX) entram como custo fixo mensal.

O custo total desta aba é rateado pelos projetos como rubrica "custos operacionais da empresa" na composição de custos por unidade.

---

#### Hardware atual

**Dell Inspiron 16 Plus 7640**
- Intel Core Ultra 7 155H, 32GB DDR5, RTX 4060 8GB, SSD 1TB
- Uso: trabalho interativo (CAD, modelagem, desenvolvimento, reuniões)
- Limitação para inferência local: 32GB RAM + 8GB VRAM comporta modelos de 7B–13B na GPU. Modelos maiores exigem offload para RAM (lento).
- Upgrade possível: RAM para 64GB (~R$ 500). Desbloqueia modelos de 20–30B com qualidade útil.

#### Itens planejados

##### Servidor de inferência local

- **Necessidade:** operar múltiplos agentes de IA em segundo plano,   servindo projetos e empresas diferentes via fila de inferência. Referência de arquitetura: paper_agent/docs/process/workflow/vision.md.
- **Estado atual:** agentes operam via APIs (Claude, DeepSeek). Funcional para validação de fluxos. Custo por token limita escala.
- **O que se quer:** máquina dedicada, silenciosa, 24/7, com memória suficiente para modelos de 70B+ parâmetros. Candidatos: Mac Studio Ultra 192GB (~R$ 52–65k), servidor Linux com GPU dedicada (a pesquisar).
- **Gatilho de aquisição:** entrada de capital (F4). Pesquisa e decisão podem antecipar — compra só com dinheiro disponível.
- **Custo estimado:** R$ 52.000–68.000. Amortização: 4–5 anos (~R$ 1.000–1.400/mês).
- **Nível de confiança:** Estimado (baixa confiança). Mercado muda rápido; modelos e hardware de outubro/2026 podem alterar a decisão.
- **Tensão a resolver:** notebook atual serve para trabalho interativo (CAD, modelagem). Servidor de inferência é headless, 24/7. São perfis diferentes — a decisão é entre Mac Studio (melhor para inferência, limitado para software de construção) e Linux/GPU (mais flexível, mais complexo de operar). Decisão madura quando a demanda real de software de construção estiver clara.

##### Upgrade de RAM — notebook atual

- **Necessidade:** ampliar capacidade de inferência local no hardware existente enquanto servidor dedicado não existe.
- **O que se quer:** 2×32GB DDR5 5600MT/s (64GB total).
- **Gatilho:** quando fluxo de agentes locais estiver validado com APIs e o modelo de 20–30B for o próximo passo.
- **Custo estimado:** R$ 400–600.
- **Nível de confiança:** Estimado (média confiança).

##### Software de construção e engenharia

- **Necessidade:** CAD, modelagem estrutural, orçamento de obras. Essencial a partir de F6 (projetos técnicos).
- **Estado atual:** em aberto. Levantar opções e custos quando relevante.
- **Gatilho:** F6 ou contratação de projetista que defina a stack.
- **Custo estimado:** a levantar.
- **Nota:** integração com MCP para assistência de IA é desejável. Viabilidade depende do software escolhido e da maturidade dos
  conectores MCP disponíveis.

---

#### Custos operacionais recorrentes (OPEX mensal)

| Item | Faixa (R$/mês) | Nota |
|---|---|---|
| Contabilidade | 500–800 | Estimativa para MEI/SPE simples |
| Claude (assinatura) | ~100 | Refinamento estratégico |
| APIs complementares | 50–100 | DeepSeek, outros — fase de validação |
| Domínio + hosting | ~50 | erapraserobvio.com.br |
| Eletricidade (servidor 24/7) | ~100 | Só após aquisição do servidor |
| Software de construção | a levantar | Só a partir de F6 |
| **Total estimado** | **~800–1.200** | **Sem servidor e sem software de construção** |

Nota: após aquisição do servidor e software, total sobe para ~R$ 2.000–3.500/mês.

---

#### Rateio para projetos

Custo total projetado para duração do EcoCondomínio (~30 meses):

- Fase pré-capital (~12 meses, OPEX leve): ~R$ 10–15k
- Fase pós-capital (~18 meses, OPEX completo + amortização): ~R$ 55–80k
- **Total: ~R$ 65–95k. Referência central: R$ 80k.**

Rateio por unidade vendida (19 un.): ~R$ 3.400–5.000. **Ref: R$ 4.200.**

Nível de confiança: Estimado (baixa confiança).
