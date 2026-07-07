# Processo — Registro de transcrições

Documento carregado quando o fluxo de transcrição é acionado. Descreve como uma fala vira arquivo bruto rastreável em `transcricoes/`.

## Gatilho

O usuário cola a transcrição bruta no chat e pede para registrar.

## Registro

- Preservar o conteúdo falado na íntegra — nada é alterado, resumido, corrigido ou reordenado.
- Adicionar no topo um bloco de metadados YAML com os campos: `data`, `sessao`, `tipo`, `titulo`.
- Dividir o conteúdo em seções nomeadas por assunto, cada uma marcada com `## nome-da-secao` imediatamente antes do trecho que pertence a ela.
- Nomear o arquivo no formato `AAAA-MM-DD-titulo.md`, dentro de `transcricoes/`.
- Ao final, listar as seções criadas com a primeira linha de cada, para o usuário conferir os cortes.

## Rastreabilidade

Conteúdo processado que deriva de uma transcrição referencia a fonte no formato `arquivo#secao`: o caminho do arquivo bruto seguido do nome da seção de origem.

Exemplo, apontando para uma seção real já existente na pasta:

```
transcricoes/2026-07-06-quatro-iniciativas.md#iniciativa-2-ferramentas
```

## Processamento

Processar uma transcrição significa levar o conteúdo bruto para o lugar certo do repositório, de forma organizada e rastreável. O foco está em organizar bem o conteúdo no seu destino, mais do que em movê-lo.

Passos de processamento:

- Identificar de que assunto o trecho trata.
- Localizar o nível e o destino do assunto, usando [docs/estrutura/niveis.md](../docs/estrutura/niveis.md) e [docs/estrutura/criterios.md](../docs/estrutura/criterios.md).
- Ler o conteúdo que já existe no destino com atenção.
- Decidir entre inserção, atualização ou reorganização.
- Propor a mudança cirúrgica, com a referência de volta no formato `arquivo#secao`.

Abordagem em camadas:

- O processamento acontece de forma incremental, uma frente por vez.
- A primeira frente processada serve como prova de conceito, para observar a forma real do conteúdo destilado antes de aplicar às demais.
- A mecânica de reconciliar conteúdo novo com o já existente (identificar o que é novo, o que repete e o que complementa) segue a curadoria do acervo — inserir, fundir, evoluir ou decompor, com dedup por âncora. Ver ../docs/estrutura/curadoria.md. Uma transcrição é uma caixa; o registro aqui é o caso particular desse fluxo geral.

Em aberto:

- A ordem de processamento das frentes.
- A migração do conteúdo maduro que hoje vive no Google Drive.
- O momento de rodar o processamento em lote ou de forma assíncrona.
