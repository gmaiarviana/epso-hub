# Sessões Claude em paralelo

Trabalhar com **várias sessões Claude Code ao mesmo tempo** neste repositório é normal.
Este documento registra o risco que isso cria no git e como evitá-lo. Complementa a seção
"Fluxo git" do [CLAUDE.md](../CLAUDE.md).

## O risco: working copy compartilhado

Duas ou mais sessões abertas no **mesmo diretório** do repositório compartilham um único
`.git`, um único HEAD e uma única working tree. Não há isolamento por sessão: `checkout`,
`switch` ou `commit` de uma troca o estado sob os pés da outra.

**Sintoma:** o commit de uma sessão cai na branch da outra; uma branch recém-criada fica
vazia enquanto o commit aparece noutra; commits de sessões diferentes se intercalam numa
linha só. No `git reflog` surgem `checkout: moving from X to Y` e `commit:` que você não fez.

## Prevenção: um worktree por sessão

Cada sessão paralela deve ter seu **próprio working copy isolado**. A forma leve é um
`git worktree` — HEAD e working tree próprios, com os objetos do `.git` compartilhados (não
duplica histórico nem clona de novo):

```bash
git worktree add ../epso-hub-<sessao> <branch>   # ex.: ../epso-hub-transcricoes docs/transcricoes-...
# ...trabalha lá dentro...
git worktree remove ../epso-hub-<sessao>          # ao terminar
```

Checkout numa worktree não afeta a outra. Alternativa mais pesada: clones separados.

**Regra para o executor:** ao criar branch nova, não usar `git switch`/`checkout` no
diretório principal — isso troca o HEAD de qualquer outra sessão aberta ali. Criar a branch
já num worktree próprio:

```bash
git worktree add ../epso-hub-<branch> -b <branch> origin/main
```

e trabalhar dentro dele até o PR.

Sessão Claude Code na nuvem já roda num container isolado, com clone próprio: ali o
worktree é dispensável, e trabalha-se direto na branch designada pela sessão.

## Se já colidiu

Sem quebrar a sessão ativa alheia:

- **Não** faça `rebase`/`checkout` na branch de outra sessão enquanto ela está ativa — isso
  muda a working tree dela e derruba o trabalho em curso.
- **Ancore o próprio commit** na branch certa com um update de ref puro:
  `git branch -f <minha-branch> <sha>`. Isso **não toca working tree nem HEAD**, então a
  outra sessão segue intocada.
- **A limpeza da branch alheia** (tirar o commit intruso) é da sessão dona dela. Se a branch
  ainda não foi pushada: `git rebase --onto main <sha-intruso> <branch>`. Se já foi pushada,
  o mesmo rebase seguido de `git push --force-with-lease` — sempre numa branch de feature,
  **nunca no `main`** (que é protegido; ver "Fluxo git" no CLAUDE.md).
- Se as duas branches carregam o mesmo commit (mesmo SHA), o merge **deduplica por SHA**: quando
  uma PR mergear, a outra não reintroduz o commit. Não há perda — só ruído visual nas PRs até lá.
