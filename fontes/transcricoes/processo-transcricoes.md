# Processo — Registro de transcrições

Documento carregado quando o fluxo de transcrição é acionado. Descreve como uma fala vira arquivo bruto rastreável em `fontes/transcricoes/` e, dali, chega à área de trabalho.

Três etapas, cada uma com seu verbo:

1. **Registrar** — gravar o bruto, intocado.
2. **Passar a limpo** — tornar a transcrição legível: a camada limpa, com seções e correções validadas.
3. **Encaixar** — levar o conteúdo à área de trabalho (acervo e pastas de ação prática). A transcrição é uma caixa; o verbo e a analogia do quebra-cabeça vivem na [curadoria](../../docs/estrutura/curadoria.md#caixa).

## Gatilho

O usuário cola a transcrição bruta no chat e pede para registrar.

## Registro do bruto

Gera a camada bruta — a transcrição automática intocada.

- Preservar o conteúdo falado na íntegra — nada é alterado, resumido, corrigido ou reordenado.
- Adicionar no topo um bloco de metadados YAML: `data`, `sessao`, `tipo: transcricao-bruta`, `titulo`, `fonte-audio` (referência ao áudio, que não é versionado).
- Nomear o arquivo `AAAA-MM-DD-titulo.raw.md`, dentro de `fontes/transcricoes/raw/`.
- Não seccionar o bruto — a estrutura por assunto vive na camada limpa.
- **Vários áudios numa sessão** vão para um arquivo só, na **ordem de gravação** — não na ordem em que foram colados no chat, que já veio invertida mais de uma vez. Conferir os rótulos ("áudio 1", "áudio 2") contra as emendas do conteúdo (a frase cortada no fim de um e retomada no começo do outro); se rótulo e conteúdo divergirem, perguntar ao incorporador antes de gravar. Marcar cada fronteira com `<!-- áudio N -->` e registrar a ordem adotada e o que a confirma num campo `nota` dos metadados.

## Passar a limpo: a camada limpa

Cópia de trabalho derivada do bruto **sob validação do incorporador**, onde ambiguidades e erros de transcrição de áudio são resolvidos preservando a ideia original. É **opcional**: o bruto sozinho já cumpre o dever de preservação. Nasce ao encaixar a transcrição, **ou antes disso** quando se quer a versão legível do pensamento — pode ser gerada em lote, adiantada. Não se gera para toda transcrição por obrigação.

- Nomear `AAAA-MM-DD-titulo.md`, na raiz de `fontes/transcricoes/` (mesmo nome do bruto, sem o `.raw`).
- Metadados YAML: `data`, `sessao`, `tipo: transcricao-limpa`, `titulo`, `fonte-bruta` (caminho do `.raw.md`), `fonte-audio`.
- Dividir em seções nomeadas por assunto, `## nome-da-secao` imediatamente antes do trecho — é aqui que a estrutura e as âncoras de rastreabilidade vivem.
- Resolver as correções e apresentá-las ao incorporador **agrupadas por tipo, para validação em lote** — nunca uma a uma. Itens do lote não contestados na resposta contam como validados; só os contestados voltam para uma nova rodada. Os tipos:
  - **Correção óbvia de fala** — gagueira, falso começo, repetição. Sem risco de sentido; aplica-se direto.
  - **Truncamento** — pensamento ou palavra cortada. Propõe-se a reconstrução; na dúvida, marca-se `[...]`.
  - **Escolha de palavra que muda o sentido** — resolver por uma escada, do mais barato ao mais caro. Nunca levar ao incorporador uma pergunta crua ("o que você quis dizer?"): ele decide com o contexto na mão, não de cabeça.
    1. **Contexto imediato** — as frases antes e depois costumam decidir. Um garble logo após ele listar "corpo e mente" quase certo é "corpo"; "papai não é resistir" depois de "nosso papel é fluir" é "o papel".
    2. **Corpus** — termos recorrentes e termos-assinatura em outras transcrições (ver [aprendizados-transcricao.md](aprendizados-transcricao.md)).
    3. **Incorporador** — o que sobrar vai a ele **já com a proposta e o contexto que a justifica**, para confirmar.
    4. **`[inaudível]`** — só o que não se resolve em nenhum dos anteriores. Nunca chute.
- Antes de propor, consultar [aprendizados-transcricao.md](aprendizados-transcricao.md) — padrões recorrentes de erro e termos-assinatura a preservar, que aceleram a validação. Registrar ali o que a sessão ensinar.
- Ao final, listar as seções criadas com a primeira linha de cada, para o incorporador conferir os cortes.

## Entrada no roadmap

Toda transcrição registrada entra na seção **Fontes** do [next-steps da raiz](../../next-steps.md#1-fontes) — a primeira da fila —, com a etapa que falta ("passada a limpo; falta encaixar"), para não ficar esquecida em `fontes/`. Entra ao fim do registro — depois da camada limpa, quando ela é gerada na mesma sessão. A posição dentro da seção é decisão do incorporador; na falta dela, o item vai para o fim, sem furar itens já ordenados. A seção concentra toda fonte em trânsito, qualquer que seja a frente de destino; o item sai de lá quando o encaixe termina.

## Rastreabilidade

Conteúdo encaixado que deriva de uma transcrição referencia a fonte no formato `arquivo#secao`: o caminho do arquivo **limpo** seguido do nome da seção de origem — é a camada limpa que carrega as seções. O limpo aponta para o bruto (`fonte-bruta`) e para o áudio (`fonte-audio`), preservando a cadeia até a verdade última.

Exemplo, apontando para uma seção real já existente na pasta:

```
fontes/transcricoes/2026-06-26-modelos-eficientes-abstrair-palavras-e-economia-sustentavel.md#abstrair-as-palavras
```

## Encaixe

Encaixar uma transcrição significa levar o conteúdo para o lugar certo da área de trabalho, de forma organizada e rastreável. O foco está em organizar bem o conteúdo no seu destino, mais do que em movê-lo.

Passos do encaixe:

- Passar a limpo a transcrição, se ainda não foi — é da camada limpa que se encaixa.
- Identificar de que assunto o trecho trata.
- Localizar o nível e o destino do assunto, usando [docs/estrutura/niveis.md](../../docs/estrutura/niveis.md) e [docs/estrutura/criterios.md](../../docs/estrutura/criterios.md).
- Ler o conteúdo que já existe no destino com atenção.
- Decidir entre inserção, atualização ou reorganização.
- Propor a mudança cirúrgica, com a referência de volta no formato `arquivo#secao`.

Abordagem em camadas:

- O encaixe acontece de forma incremental, uma frente por vez.
- A primeira frente encaixada serve como prova de conceito, para observar a forma real do conteúdo encaixado antes de aplicar às demais.
- A mecânica de reconciliar conteúdo novo com o já existente (identificar o que é novo, o que repete e o que complementa) segue a curadoria do acervo — inserir, fundir, evoluir ou decompor, com dedup por âncora. Ver [docs/estrutura/curadoria.md](../../docs/estrutura/curadoria.md). Uma transcrição é uma caixa; o registro aqui é o caso particular desse fluxo geral.

Em aberto:

- A ordem de encaixe das frentes.
- A migração do conteúdo maduro que hoje vive no Google Drive.
- O momento de rodar o encaixe em lote ou de forma assíncrona.
