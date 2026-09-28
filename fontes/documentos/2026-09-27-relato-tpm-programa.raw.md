---
data: 2026-09-27
tipo: documento-bruto
titulo: Impressões como TPM num programa de cliente
idioma: português
genero: relatório
corpus: escrita do incorporador
ia: não confirmado
escrito-em: 2024-10-21
anonimizado: >-
  Documento interno sobre um cliente, com anonimização pesada. Pessoas
  trocadas por [pessoa 1] a [pessoa 11] e [outros TPMs]; cliente, programa,
  tribos e times trocados por [cliente], [programa], [tribo], [outra tribo],
  [time A], [time B] e [time C]; a empresa do incorporador, outra consultoria,
  uma área interna e o gentílico dos colaboradores trocados por [empresa],
  [outra consultoria], [área interna] e [colaboradores].
nota: >-
  Parte do corpus de textos escritos pelo incorporador, a maioria sem uso de
  IA, colado no chat em 2026-09-27 e quebrado por documento. Conteúdo
  preservado na íntegra, sem correção; a única alteração é a anonimização,
  marcada entre colchetes. O original identificado fica fora do repositório.
  O título H1 é do registro, não do original. A formatação se perdeu na
  colagem e foi reconstruída em Markdown sem alterar o texto: subtítulos
  viraram títulos e enumerações viraram listas.
---

# Impressões como TPM num programa de cliente

Impressões como TPM em [programa] 

21/10/2024

Oi [pessoa 1], 

venho compartilhar um pouco sobre o que aprendi relacionado ao papel de Technical Program Manager depois de quatro semanas. Como atuo com a [cliente] desde julho/2022 e desde então tenho contato direto com TPMs, entendo que posso também trazer percepções que sejam aplicáveis para a [cliente] excedem particularidades do [programa].

## Expectativas para o TPM na [cliente]

- Promover visibilidade de informações para que o programa consiga ter previsibilidade se as entregas serão entregues no prazo desejado
- Anunciar riscos para os stakeholder com antecedência
- Ponto focal para comunicar aos stakeholders sobre atualizações, mudanças e entregas
- Ponto focal para receber atualizações de outros stakeholders sobre decisões, expectativas e prazos
- Garantir que os impedimentos possuam um plano de mitigação 
- Reunir os envolvidos para elaboração e alinhamento sobre um plano de mitigação
- Ser o ponto focal para permitir que os times atuem sem bloqueios, ou seja, apoiar o Product Owner e Scrum Master em escalar assuntos para outros stakeholders
- Favorecer que a ferramenta de acompanhamento (como Jira ou AzureDevOps) reflita ao máximo a realidade, para favorecer maior transparência e assim permitir que decisões de sejam tomadas considerando os dados levantados

Sob o ponto de vista de rotina e dinâmica, o papel não exige um profundo conhecimento técnico, porém necessita uma capacidade de organização, visão de negócio, comunicação, resolução de problemas. O TPM possui o apoio de Architects, Engineering Managers, Tech Leads para tomar as decisões.

O único ponto de atenção que trago é que, nesse modelo de expectativa, existe o risco do TPM ficar muito focado na gestão do backlog, no preenchimento de relatórios e na manutenção de uma burocracia. No meu entendimento, um TPM resolutivo deve ser capaz de tomar decisões após se aprofundar nos problemas e obter aconselhamento dos stakeholders parceiros. Um TPM não-resolutivo sempre delega a tomada de decisões para os stakeholders parceiros.

O papel de TPM pode causar confusão em relação a outros papéis como PdM (Product Manager) e PO (Product Owner). Na [cliente], a expectativa é que o TPM seja o responsável por conciliar as expectativas de negócio com a capacidade tecnológica, ou seja, alinhar os discursos de Produto com Engenharia. Intermedia a discussão entre o Engineering Manager, Architects, Product Managers, Release Engineers, Product Owners. Tal intermediação ocorre sem o envolvimento dos membros do time, sem aprofundamento nos requisitos do escopo. Discussões sobre o escopo, ficam sob a responsabilidade de POs e PdMs.

Para esclarecer, compartilho meu entendimento sobre as expectativas da [cliente] sobre esses papéis:

- Product Manager -> responsável por definir a estratégia dos produtos, indicando o benefício que tais iniciativas podem trazer ao programa
- Solution Architect -> Responsável por orientar as decisões tecnológicas dos produtos do programa
- Engineering Manager -> responsável por viabilizar que as decisões tecnológicas sejam implementada
- Product Owner -> tem a função de garantir que os tickets/itens estão escritos com critérios de aceitação e orientar na priorização das atividades. Quando o produto tem escopo técnico, demanda que o PO tenha um background e perfil técnico.
- Scrum Master -> poderia ser chamado de Squad Lead, pois tem a responsabilidade de liderar o time, acompanhar o dia-a-dia, atualizar a ferramenta de gestão.
- Tech Lead -> responsável por orientar o time na implementação do código.

## Contexto em [programa]

Basicamente, [programa] se refere ao novo aplicativo que centralizará ao usuário todas as configurações de seus dispositivos [cliente]. O programa [programa] funciona a 2 anos e está considerado como atrasado. O prazo para o lançamento oficial global é Abril/2025 para Apple/Android e Julho/25 para Windows. Como um movimento para atender o prazo, muitas pessoas foram alocadas nesse projeto nos últimos meses (chegando a quase 200 pessoas envolvidas), o que levou a uma reorganização dos squads. Muitas pessoas que eu tenho interação chegaram no projeto nos últimos 3 meses.

No meu ponto de vista, o [programa] se propõe a resolver um problema que não requer inovações ou soluções inexistentes no mercado. 

## Detalhes sobre minha experiência até o momento

Comecei no dia 23/09. Estou assumindo a posição que era de [pessoa 2], que está indo atuar como Release Train Engineer da [outra tribo]

[pessoa 3] é a líder de todos os TPMs (total de 5 atualmente, com uma 1 vaga possivelmente em aberto). 

Na mesma semana que eu cheguei, também iniciou um TPM da [outra consultoria], assumindo 2 times da mesma tribo que eu - seríamos pares responsáveis por todos os times da tribo. Porém ele teve um problema na contratação pela [outra consultoria] e foi desligado. Soube através dele por conversa fora dos canais da [cliente].

Conforme descrito nessa tabela, são 6 tribos. Estou na [tribo]. [time A], [time B] e [time C]. O time de [time B] não tem ninguém do [empresa], mas os outros 2 possuem. 

[pessoa 4] é a RTE e líder da [tribo], então ela faz acompanhamento sobre as entregas

PI Planning a cada duas sprints

Meus principais stakeholders são os líderes dos 3 times: 

- [pessoa 4] (RTE do [tribo])
- [pessoa 5] (Eng Manager de [time B] e [time C])
- [pessoa 6] (Eng Manager de [time A])
- [pessoa 7] (Product Manager dos 3 times)
- [pessoa 8] (Squad Lead do [time B])
- [pessoa 9] (Squad Lead do [time A])
- [pessoa 10] (PO de [time C])
- [pessoa 11] (Tech Lead do [time C])

Além desses líderes, estou em constante contato com os outros TPMs dos outros squads ([outros TPMs]) para fazer alinhamentos, planejamentos e discutir dependências.

## Expectativas sobre mim em [programa]

- Garantir que a PI Planning ocorra bem
  - Riscos que impeçam as entregas sejam identificadas
  - Atividades sejam refinadas e expectativas estejam claras
  - Dependências entre times sejam identificadas e alinhadas
  - Garantir que os objetivos para a PI estejam definidos
- Conduzir a resolução de problemas
  - Garantir que atividades bloqueadas tenham um plano adequado
  - Reunir as pessoas necessárias para que um problema seja resolvido
  - Conciliar para que os impasses cheguem em um acordo
- Comunicar para os stakeholders sobre as atualizações e mudanças
  - Trazer transparência e garantir que todos estejam na mesma página sobre as decisões tomadas
  - Enviar um relatório semanal para [pessoa 3] e [pessoa 4]
    - dar visibilidade sobre o andamento das atividades e se existe algum risco que impeça que as entregas sejam implementadas no prazo esperado
    - explicar se preciso 
- Promover a organização do Jira
  - Garantindo que todos os bugs sejam discutidos e priorizados
  - Garantindo que os possuam os campos importantes preenchidos e atualizados 
  - Rastrear itens que estejam precisando de suporte para serem desbloqueados ou finalizados
  - Acompanhar dashboards de monitoramento dos issues e progresso dos times

## Problemas identificados no [programa]

A maior dificuldade enfrentada pelo programa de [programa] não é excepcionalmente técnico, ou seja, não são as dificuldades tecnológicas que estão causando gargalos nas entregas do programa.

Pelo que acompanhei em reuniões, o time de Design se queixa de que o produto implementado até o momento não consegue acompanhar o que foi projetado, acumulando débito técnico. O projeto não foi lançado e acumula refatorações e ainda apresenta a necessidade de que algumas arquiteturas sejam refeitas.

Na minha percepção, o que tem causado atrito e ineficiência se deve a:

- A maneira que o programa tem se subdividido favorece a ter múltiplos pontos de comunicação;
- Falta de coordenação sobre as solicitações somado a múltiplos pontos de contato leva a ter muita informação acontecendo ao mesmo tempo. A maneira que o projeto se defende a isso é gerando processos burocráticos para garantir alinhamento antes de subir implementação em produção;
- Falta de clareza nos objetivos táticos, levando a ter múltiplas solicitações consideradas como urgentes ou prioritárias
- Regras de negócios são criadas às vezes pelos Architects, às vezes pelo Product Manager - mas perde-se muito tempo para chegar numa decisão final

## Sugestão de solução para esse tipo de problema 

Bom, o programa de [programa] está evoluindo e está continuamente melhorando. Sob determinado ponto de vista, podemos achar que não tem nada a ser feito, pois pouco a pouco, as coisas estão se ajustando. Mas eu acho que vale a pena mencionar que vejo oportunidade para o [empresa] fazer a diferença nesse tipo de situação - que não ocorre apenas com [programa], mas é muito comum em empresas que passam por transformação digital.

Não é algo simples, não podemos resolver sozinhos mas podemos influenciar o cliente, podemos transformar nossa mentalidade como instituição para antecipar situações semelhantes, podemos agir em pequenas ações e podemos fazer sugestões propositivas que podem abrir portas. Se tivermos a mentalidade certa, podemos aplicar isso tanto em projetos atuais como nos preparar para considerar essa abordagem na elaboração de novos contratos. Ou seja, entendo que vale muito a pena incluir o [área interna] nesse tipo de discussão.

A questão é entender que times orientados a componentes tendem a:

- Represar conhecimento, criando silos de informações em que cada time se torna especialista apenas em seu componente
- Promover que as implementações foquem apenas nos aspectos técnicos sem considerar os aspectos de negócio ou de experiência
- Criar uma rotina ineficiente em que os defeitos e problemas sejam identificados em etapas avançadas do processo de release 
- Deixar os funcionários alienados ao produto final, fazendo apenas uma etapa da ‘esteira de produção’

Por outro lado, times orientados a Produto tendem a:

- Entregar produtos mais rápido pois necessitam de menos times intermediários
- Entender a jornada de usuário e avaliar se o produto está realmente entregando valor
- Gerar transparência na elaboração de regras de negócio, pois elas iniciam sempre pela experiência do usuário
- Aproximar o time de engenharia do usuário final
- Diminuir a necessidade de burocracia ou grandes protocolos para garantir alinhamentos entre times, pois os times se tornam empoderados para atuar de ponta-a-ponta

Tenho plena clareza que o programa tem prazos apertados e muitos outros assuntos demandando muita atenção, tornando difícil imaginar que iremos ter mudanças significativas antes das grandes entregas. Mas entendo que - caso queiramos encantar o cliente, mostrar que estamos acompanhando, entendendo e identificando oportunidades de melhoria de longo prazo - algumas ações podem ser feitas. Sendo elas:

- Aprofundar o nosso entendimento no negócio do [programa]
- Levantar dados que evidenciem os problemas e gargalos
- Exercitar desenhar uma solução de organização ideal
- Quebrar a solução ideal desenhada em pequenas etapas
- Organizar uma proposta de teste envolvendo os [colaboradores] e causando o mínimo de disrupção possível no ponto de vista de gestão do programa (ou seja, propor uma solução que não faça diferença pra eles mas que faça muita diferença pra gente)
- Apresentar nossa solução e fazer a proposta de teste com prazos, escopo e estrutura definida

Tenho ciência que, na maioria das vezes, o cliente já indica onde precisa de nossa assistência quando discutimos os contratos - o que dificulta discutir sobre a estrutura de trabalho e abordagem de execução. Mas se não tivermos em mente que existe uma limitação, vamos ficar sempre dependentes das variáveis do ambiente, sempre repetindo os processos existentes e nunca empoderados para entregar com eficiência e qualidade.
 
Por outro lado, as soluções organizacionais que mencionei já são plenamente utilizadas nas empresas mais modernas e são recomendadas nas literaturas mais atualizadas.
