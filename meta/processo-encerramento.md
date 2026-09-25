# Processo de encerramento de sessão

Como uma sessão de trabalho fecha. Acionado pela frase **"vamos encerrar"**.

O encerramento tem quatro passos, em ordem. O primeiro — a retrospectiva — é o
coração deste processo: é o que garante que os processos definidos evoluem em
vez de estagnar. Os passos 2 e 3 já viviam no repositório e são referenciados,
não reescritos aqui.

## 1. Retrospectiva de processo

Reler a conversa da sessão e perguntar: **tem algo no nosso jeito de trabalhar
que deveria mudar?** O alvo é o *como* (o processo), não o *quê* (o conteúdo —
esse é o passo 3).

O princípio de fundo: muito do que se faz numa sessão é pontual e não se repete
— isso **não** vira processo, e inventar regra para trabalho de-uma-vez é um
erro a evitar. A retrospectiva existe para o outro caso: o trabalho que passou
por um **processo já definido**, onde a prática pode ter revelado que a regra
precisa mudar.

### Passos

1. **Reler a sessão inteira** — do início ao fim, não só o último trecho.

2. **Separar em duas pilhas** o que a sessão tocou:
   - **Pontual / não-repetível** — decisão de conteúdo, escolha única, análise
     específica. Não gera processo. Seguir em frente.
   - **Passou por processo definido** — tocou uma regra ou fluxo declarado. A
     superfície de varredura é o conjunto de processos que o [CLAUDE.md](../CLAUDE.md)
     declara (fluxo git, transcrições, critérios de `meta/estrutura/`, planejador
     e executor, formato de arquivos, rastreabilidade, níveis de confiança,
     formato de next-steps, notação `[[nome]]`) mais os documentos do seu
     "Índice de processos". Não manter uma lista duplicada aqui — ela apodrece;
     o CLAUDE.md é a fonte.

3. **Para cada processo tocado, rodar quatro perguntas-diagnóstico:**
   - **Atrito** — algo no processo atrapalhou, foi mais lento ou mais confuso do
     que precisava?
   - **Exceção** — precisei fazer diferente do que o processo manda? Uma regra
     foi dobrada em silêncio?
   - **Lacuna** — apareceu uma situação que o processo simplesmente não cobria?
   - **Melhoria emergente** — surgiu na prática um jeito melhor que valeria
     virar regra?

4. **Filtrar sinal de ruído.** Só vira proposta o que é estrutural ou recorrente.
   Atrito de-uma-vez, ou preso àquele conteúdo específico, fica de fora — não se
   reescreve um processo para caber uma sessão. Um bom teste: *"isso vai
   acontecer de novo em sessões futuras?"* Se não, é ruído.

5. **Sinal extra a observar:** um trabalho que estava na pilha "pontual" mas
   apareceu pela segunda ou terceira vez é candidato a **virar** processo novo.
   A retrospectiva não só evolui processos existentes — ela também detecta
   quando um processo deveria nascer.

### Saída

- **Se há proposta:** apresentar como sugestão, no formato do repositório —
  recomendação direta, o porquê (1–3 razões), o trade-off principal. Apontar o
  **documento exato** e a **mudança exata**, no formato de prompt de edição
  pronto para o executor (Claude Code). **A decisão é do incorporador** — a
  retrospectiva propõe, não aplica. Nada é editado sem autorização.

- **Se nada precisa mudar:** dizer isso de forma explícita — *"nada a evoluir
  nos processos nesta sessão"* — e, em uma linha, por quê. Não fabricar melhoria
  para preencher o passo. Uma retrospectiva vazia é um resultado válido.

A evolução dos processos vive no **git dos próprios documentos** — não se mantém
um log separado de retrospectivas. Consistente com o princípio do repositório:
o histórico vive no git.

## 2. Atualizar next-steps e limpar

Conferir o que a sessão tornou obsoleto: itens de next-steps concluídos, trechos que mudaram
de dono (deixam um link no lugar do conteúdo) e arquivos que um critério registrado manda
aposentar. Fontes (`fontes/`) nunca se limpam: a caixa se preserva.

Atualizar o `next-steps.md` da(s) frente(s) trabalhada(s), a fila da raiz se um
item entre frentes mudou, e `meta/next-steps.md` se ficou pendência de processo. As
mecânicas (processual separado de pontual, item concluído sai da lista) estão no
[CLAUDE.md § Encerramento de sessão](../CLAUDE.md) — não duplicar aqui.

## 3. Registrar ideias da conversa, se a sessão gerou acervo

Se a conversa produziu ideias que são material de acervo (pensamento do
incorporador que vale preservar como fonte), lembrar de registrá-las em
`fontes/conversas/`. O processo formal desse registro — como acionar, o que o
assistente pergunta, como nomeia, em que voz sai — ainda está **a formalizar**
(ver [next-steps.md](next-steps.md)). Até lá, este passo é um lembrete, não um
fluxo fechado: sinalizar ao incorporador que há ideia a registrar e capturar sob
sua validação.

## 4. Finalizar no git

Commit e PR são o **último** passo do encerramento — abertos ao dizer "vamos
encerrar", **depois** da retrospectiva, para que qualquer edição de processo que
ela produza entre no mesmo PR. Isso troca "PR quando o trabalho fica pronto" por
"PR quando a sessão fecha", mantendo o ritual auto-consistente: a retrospectiva
sempre tem onde cair. Mecânica de branch → commit → PR: ver
[CLAUDE.md § Fluxo git](../CLAUDE.md).

**Ressalva:** trabalho grande ou independente pode abrir PR antes de encerrar,
quando faz sentido pôr em revisão logo. Nesse caso o encerramento não reabre
nada — só roda a retrospectiva, e um achado que edite processo vira commit
adicional no PR já aberto (ou um PR próprio, se for de outro escopo).
