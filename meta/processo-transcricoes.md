# Processo — Registro de transcrições

Documento carregado quando o fluxo de transcrição é acionado. Descreve como uma fala vira arquivo bruto rastreável em `fontes/transcricoes/` e, dali, chega à área de trabalho.

Três etapas, cada uma com seu verbo:

1. **Registrar** — gravar o bruto, intocado.
2. **Passar a limpo** — tornar a transcrição legível: a camada limpa, com seções e correções validadas.
3. **Encaixar** — levar o conteúdo à área de trabalho (acervo e pastas de ação prática). A transcrição é uma caixa; o verbo e a analogia do quebra-cabeça vivem na [curadoria](estrutura/curadoria.md#caixa).

## Gatilho

O usuário cola a transcrição bruta no chat; colar já é o pedido de registro. Se não vierem junto, perguntar numa só pergunta a data de gravação de cada áudio e a sua duração. A data nomeia o arquivo; a duração alimenta a localização de termos no degrau "reouvir".

Texto colado sem pontuação, em bloco corrido, com marcas de fala ("né", repetições, palavras deformadas) é transcrição, mesmo sem aviso. Na dúvida, perguntar antes de analisar o conteúdo.

Colagem longa pode chegar truncada: o chat corta mensagens acima de ~50 mil caracteres, sem aviso. Conferir o último marcador de tempo de cada transcrição contra a duração; se ficar muito aquém, pedir a colagem de novo antes de gravar.

## Registro do bruto

Gera a camada bruta — a transcrição automática intocada.

- Preservar o conteúdo falado na íntegra — nada é alterado, resumido, corrigido ou reordenado.
- Adicionar no topo um bloco de metadados YAML: `data`, `sessao`, `tipo: transcricao-bruta`, `titulo`, `fonte-audio` (referência ao áudio, que não é versionado).
- Nomear o arquivo `AAAA-MM-DD-titulo.raw.md`, dentro de `fontes/transcricoes/raw/`.
- Não seccionar o bruto — a estrutura por assunto vive na camada limpa.
- **Vídeo publicado** (YouTube, com legenda automática): título, data de publicação e duração saem da página do vídeo, sem perguntar ao incorporador. A data de publicação nomeia o arquivo, e a `nota` declara que não é a de gravação. `fonte-audio` é o link do vídeo.
- **Vários áudios de um mesmo bloco** vão para um arquivo só, na **ordem de gravação**. Um bloco é a unidade de pensamento que o incorporador grava em sequência; pode atravessar mais de um dia. Nesse caso, o arquivo leva a data do primeiro dia e a `nota` registra a data de cada áudio. Vale a ordem de gravação, independente da ordem em que foram colados no chat, que não é confiável. Conferir os rótulos ("áudio 1", "áudio 2") contra as emendas do conteúdo (a frase cortada no fim de um e retomada no começo do outro); se rótulo e conteúdo divergirem, perguntar ao incorporador antes de gravar. Marcar cada fronteira com `<!-- áudio N -->` e registrar a ordem adotada e o que a confirma num campo `nota` dos metadados.
- **Mais de uma transcrição automática do mesmo áudio** (ferramentas diferentes) vão para o mesmo arquivo, cada uma intocada e marcada por `<!-- transcrição: ferramenta -->`. A `nota` registra a ferramenta de cada versão e para que cada uma serve (ex.: uma mais fiel à fala, outra com marcadores de tempo para localizar trechos no áudio). Ao passar a limpo, uma versão resolve as ambiguidades da outra antes de se subir a escada de correções.

## Passar a limpo: a camada limpa

Cópia de trabalho derivada do bruto **sob validação do incorporador**, onde ambiguidades e erros de transcrição de áudio são resolvidos preservando a ideia original. É **opcional**: o bruto sozinho já cumpre o dever de preservação. Nasce ao encaixar a transcrição, **ou antes disso** quando se quer a versão legível do pensamento — pode ser gerada em lote, adiantada. Não se gera para toda transcrição por obrigação.

- Nomear `AAAA-MM-DD-titulo.md`, na raiz de `fontes/transcricoes/` (mesmo nome do bruto, sem o `.raw`).
- Metadados YAML: `data`, `sessao`, `tipo: transcricao-limpa`, `titulo`, `fonte-bruta` (caminho do `.raw.md`), `fonte-audio`.
- Dividir em seções, `## nome-da-secao` imediatamente antes do trecho — é aqui que a estrutura e as âncoras de rastreabilidade vivem. **Uma seção, uma ideia:** a seção com duas ideias se encaixa pela metade sem que nada acuse a perda (ver [Cobertura](#cobertura)). O teste: se partes da seção iriam para destinos diferentes, são duas ideias. O nome diz a ideia, não o assunto: `#a-mente-sugere-a-atencao-escolhe`, não `#mente`; `#vida-como-respiracao`, não `#energia`.
- Resolver as correções e apresentá-las ao incorporador **agrupadas por tipo, para validação em lote** — nunca uma a uma. Itens do lote não contestados na resposta contam como validados; só os contestados voltam para uma nova rodada. Formato: tabela com o trecho do bruto, a proposta, o motivo e a localização (áudio e minuto); reconstruções maiores — quando se reescreve mais que uma palavra — vão num grupo à parte. Os tipos:
  - **Correção óbvia de fala** — gagueira, falso começo, repetição. Sem risco de sentido; aplica-se direto.
  - **Truncamento** — pensamento ou palavra cortada. Propõe-se a reconstrução; na dúvida, marca-se `[...]`.
  - **Escolha de palavra que muda o sentido** — resolver por uma escada, do mais barato ao mais caro. Nunca levar ao incorporador uma pergunta crua ("o que você quis dizer?"): ele decide com o contexto na mão, não de cabeça.
    1. **Contexto imediato** — as frases antes e depois costumam decidir. Um garble logo após ele listar "corpo e mente" quase certo é "corpo"; "papai não é resistir" depois de "nosso papel é fluir" é "o papel".
    2. **Corpus** — termos recorrentes e termos-assinatura em outras transcrições (ver [aprendizados-transcricao.md](aprendizados-transcricao.md)).
    3. **Incorporador** — o que sobrar vai a ele **já com a proposta e o contexto que a justifica**, para confirmar. Pergunta ao incorporador não entra na tabela do lote: vai num bloco à parte, depois das tabelas, numerada, e cada uma com o trecho ampliado (as frases antes e depois), as leituras possíveis em linguagem simples, o que cada leitura muda na ideia e a recomendação. A validação por silêncio vale só para as tabelas: um "ok" genérico não responde a pergunta do bloco, que o agente retoma até ter resposta.
    4. **Reouvir** — para os poucos termos que nem o contexto nem o incorporador resolvem de cabeça. Cada um vai com a **localização**: áudio, posição estimada (% das palavras do áudio e minuto aproximado, pela duração do áudio quando conhecida — ver ritmo de fala em [aprendizados-transcricao.md](aprendizados-transcricao.md)) e a palavra exata do bruto, que o incorporador busca na transcrição do celular para navegar até o trecho. A lista vai em ordem cronológica, com a **prioridade** marcada: os trechos em que a escuta muda uma ideia (uma tese, a ligação entre dois argumentos) vêm destacados; os de detalhe de fala, que a proposta ou o `[...]` já resolvem, ficam como opcionais. Viável para poucos termos por sessão; dezenas de buscas tornam o degrau inviável — por isso os degraus anteriores precisam resolver a maior parte.
    5. **`[inaudível]`** — só o que não se resolve em nenhum dos anteriores. Nunca chute.
- Antes de propor, consultar [aprendizados-transcricao.md](aprendizados-transcricao.md) — padrões recorrentes de erro e termos-assinatura a preservar, que aceleram a validação. Registrar ali o que a sessão ensinar.
- Ao final, listar as seções criadas com a primeira linha de cada, para o incorporador conferir os cortes.

### Documento escrito

Um documento bruto de `fontes/documentos/` também ganha camada limpa quando reúne ideias demais para contar por arquivo: o primeiro encaixe o daria como citado e esconderia o resto na [cobertura](#cobertura). Valem as regras acima, com estas diferenças:

- O limpo fica ao lado do bruto, com o mesmo nome sem o `.raw` e metadados `tipo: documento-limpo` e `fonte-bruta`, sem `fonte-audio`.
- Não há escada de escuta: as correções são de digitação, acentuação, abreviação de chat (por extenso, mantido o registro falado, como "pra") e grafia de nome próprio. A correção mecânica — acento e maiúscula num original escrito sem eles, abreviação por extenso, sigla, nome próprio — se aplica direto, como a correção óbvia de fala, e o agente resolve pelo contexto a que muda a palavra ("esta/está", "pais/país"). Vai à tabela do lote só o que troca ou acrescenta palavra, ou o que o contexto não resolve.
- O que o bruto repete — rascunho reescrito — fica no limpo só na última versão; trecho de uma versão anterior que a última perdeu fica também. Linha de sistema e marca de formatação (separadores de post) saem.
- Documento datado por trecho (notas, chat) leva a data de origem em itálico logo abaixo do título da seção. Mensagens de uma mesma ideia se juntam numa seção, cada trecho com sua data; mensagem que só nomeia um tema, autor ou referência, sem afirmar nada, vai para uma seção de tópicos soltos do período.
- Documento grande passa a limpo em lotes, cada um validado antes do próximo.
- Trecho sem ideia afirmada — lista técnica, índice, logística — pode ter a dispensa proposta já ao passar a limpo, lote a lote; o incorporador decide. Ideia que parece repetida ou sem casa não se decide aqui: fica para o encaixe, que olha o acervo.

## Entrada no roadmap

Transcrição registrada sem camada limpa entra no tier **1. Passar a limpo** do [next-steps da raiz](../next-steps.md), para não ficar esquecida em `fontes/`. Passada a limpo, o que falta encaixar aparece na [cobertura](#cobertura); a transcrição só entra no tier **Encaixar** se houver nota a guardar (ver [roadmap](roadmap.md#fontes-na-fila)). A posição dentro do tier é decisão do incorporador; na falta dela, o item vai para o fim, sem furar itens já ordenados.

## Rastreabilidade

Conteúdo encaixado que deriva de uma transcrição referencia a fonte no formato `arquivo#secao`: o caminho do arquivo **limpo** seguido do nome da seção de origem — é a camada limpa que carrega as seções. O limpo aponta para o bruto (`fonte-bruta`) e para o áudio (`fonte-audio`), preservando a cadeia até a verdade última.

Exemplo, apontando para uma seção real já existente na pasta:

```
fontes/transcricoes/2026-06-26-modelos-eficientes-abstrair-palavras-e-economia-sustentavel.md#abstrair-as-palavras
```

## Encaixe

Encaixar uma transcrição significa levar o conteúdo para o lugar certo da área de trabalho, de forma organizada e rastreável. O foco está em organizar bem o conteúdo no seu destino, mais do que em movê-lo.

Passos do encaixe:

- Ler a fonte inteira antes de propor o plano: a entrada da fila é resumo e não substitui a fonte.
- Passar a limpo a transcrição, se ainda não foi — é da camada limpa que se encaixa.
- Identificar de que assunto o trecho trata.
- Localizar o nível e o destino do assunto, usando [meta/estrutura/niveis.md](estrutura/niveis.md) e [meta/estrutura/criterios.md](estrutura/criterios.md).
- Ler o conteúdo que já existe no destino com atenção.
- Fonte escrita há anos, cujo argumento não está claro: antes de redigir, o agente reformula o argumento em uma frase e pede ao incorporador que corrija. Se ele não lembrar o que quis dizer, o agente faz perguntas concretas (o que é X na prática, um exemplo); a fala nova vai para a conversa registrada da sessão, e é dela, ao lado da fonte antiga, que se encaixa. Juntar as frases da fonte sem o argumento produz texto sem argumento.
- Buscar o caminho da fonte no acervo inteiro: o que ela já deu em outro destino se cita ali, não se repete. A cobertura conta documento bruto por arquivo e não mostra o que já foi encaixado dele.
- Decidir entre inserção, atualização ou reorganização.
- Propor a mudança cirúrgica, com a referência de volta no formato `arquivo#secao`.
- O que o agente escreve além da fala — ligação, síntese, reformulação — amadurece com o acervo. O que pode mudar o sentido do que o incorporador disse — por exemplo, a costura que afirma uma igualdade ou uma causa que ele não fez ("é o mesmo que…", "por isso…") —, e toda decisão grande, vai a ele na conversa antes do commit, com a fala original ao lado; tirar a costura sem confirmar não basta: o texto do vizinho que dava contexto sai junto e a ideia fica travada; a revisão do PR é leitura geral, não conferência minuciosa. Quando o incorporador traz uma nuance nova na conversa, o agente devolve primeiro o que entendeu, em palavras simples e sem redação final; o texto vem depois que ele confirma o entendimento. Fonte: `fontes/conversas/2026-10-03-ideia-nao-tem-dono.md#o-texto-amadurece`, `#grandes-decisoes-vem-no-chat`; `fontes/conversas/2026-10-03-ajudar-sem-mudar-o-sentido.md#o-agente-ajuda-a-consolidar`, `#sem-regra-rigida`, `#confirmar-o-que-pode-mudar-o-sentido`.
- Fechar trecho a trecho: antes de encerrar, toda seção da transcrição foi encaixada, virou provocação em [elaborar](../elaborar.md) (pede reflexão nova do incorporador), foi dispensada, virou semente ou continua pendente na [cobertura](#cobertura), com nota no tier Encaixar do [next-steps da raiz](../next-steps.md) quando houver destino ou ressalva a guardar. Só então o item de encaixe sai da fila.
- Encaixe parcial de uma seção: a mesma mudança que encaixa uma ideia registra na fila as que ficaram, nomeadas ([roadmap](roadmap.md#fontes-na-fila)).
- Conferir ideia a ideia, não só seção a seção: uma seção citada pode ter perdido ideias na síntese. Antes de declarar o encaixe pronto, reler cada seção e procurar cada ideia no destino; o que se perdeu volta ao texto, vira provocação ou ganha destino na fila. A conferência vai para o incorporador como tabela de cobertura (seção → onde ficou).

Nem tudo se elabora no encaixe. O que pede reflexão nova do incorporador não se resolve na hora: vira provocação em [elaborar](../elaborar.md), e o arquivo de conteúdo guarda o mínimo em aberto — no máximo um ponteiro para lá.

Abordagem em camadas:

- O encaixe acontece de forma incremental, uma frente por vez.
- A primeira frente encaixada serve como prova de conceito, para observar a forma real do conteúdo encaixado antes de aplicar às demais.
- A mecânica de reconciliar conteúdo novo com o já existente (identificar o que é novo, o que repete e o que complementa) segue a curadoria do acervo — inserir, fundir, evoluir ou decompor, com dedup por âncora. Ver [meta/estrutura/curadoria.md](estrutura/curadoria.md). Uma transcrição é uma caixa; o registro aqui é o caso particular desse fluxo geral.

Em aberto:

- A ordem de encaixe das frentes.
- A migração do conteúdo maduro que hoje vive no Google Drive.
- O momento de rodar o encaixe em lote ou de forma assíncrona.

## Cobertura

[fontes/cobertura.md](../fontes/cobertura.md), gerado por `python meta/cobertura.py`, mostra, por fonte — transcrições, conversas e documentos —, o estado geral e as seções ainda não concluídas. Os estados:

- **encaixada** — citada no acervo (ou em `meta/`, ou no [elaborar](../elaborar.md)); uma seção pode servir a mais de um arquivo. Não aparece nas pendências; onde mora se acha buscando a âncora;
- **pendente** — ainda não encaixada, dispensada nem semente. Aparece com o tier quando a fila a cita (Foco, Encaixar); a seção encaixada em parte, com o resto numa nota da fila, também aparece assim;
- **dispensada** — não agrega valor ao repositório: sem ideia (abertura de fala, logística, índice). Ideia que já mora no acervo não se dispensa: cita-se a fonte no destino. Definitiva: não se revisita;
- **semente** — ideia que pode agregar valor, ainda sem casa — imatura, ou de um tema que o acervo não trata. Sai das pendências e vai à lista de sementes, no fim da cobertura, para ser revisitada quando nascer uma casa ou o contexto mudar: um argumento novo pode se ligar ao que foi dito antes, quando ainda não estava maduro. Não é depósito para zerar a cobertura: só se decide no encaixe, com o acervo à vista.

Fonte: `fontes/conversas/2026-10-01-semente-e-dispensa.md#dispenso-o-que-nao-agrega-valor`, `#semente-o-que-ainda-nao-estava-maduro`.

As duas moram nos metadados da própria fonte, com o motivo, sem tocar no conteúdo. Conversa (`fontes/conversas/`), que não tem bloco de metadados, ganha um bloco só com esses campos quando precisar:

```yaml
dispensadas:
  primeira-tentativa: abertura da fala, sem ideia
sementes:
  justica-x-liberdade: pergunta sobre sociedade; sem hipótese de sociedade hoje
```

Documento bruto, contado por arquivo, usa `dispensada: motivo` ou `semente: motivo`. Só o incorporador dispensa ou declara semente.

Para elaborar um tema, o agente lê as fontes à procura do que fala dele e consulta a cobertura para saber o que já está no acervo e o que ainda está só na fonte — esse segundo grupo fortalece o encaixe.
