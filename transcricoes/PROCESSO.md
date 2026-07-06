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

## Processamento — a definir

A etapa de destilar o bruto nas frentes (pensamento, prática, academia) ainda será descrita aqui, depois de ser executada pela primeira vez. Só então o passo a passo real fica registrado, em vez de um processo inventado antes do primeiro uso.
